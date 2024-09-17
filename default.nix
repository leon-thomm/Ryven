let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/archive/63dacb46bf939521bdc93981b4cbb7ecb58427a0.tar.gz";
  # nixpkgs = /home/leon/projects/Nix/nixpkgs;
in
{
  pkgs ? import nixpkgs {},
  rebuildVenv ? false,
}:
let
  python = pkgs.python310;
  pysidePkgs = [python.pkgs.pyside6];
  # read the version from a setup.cfg file
  get-version = s: builtins.head (
    builtins.match ".*version[[:space:]*]=[[:space:]*]([[:digit:]|\.]*).*" s
  );
  # ryvencore Nix package, from the PyPI package
  ryvencore = python.pkgs.buildPythonPackage rec {
    pname = "ryvencore";
    version = "0.5.0";
    src = python.pkgs.fetchPypi {
      inherit pname version;
      sha256 = "sha256-/cCfy+3ELmJ0PjpCVfAyXt5H5Eq0/+FxaJVv8DvCjkI=";
    };
    buildInputs = with python.pkgs; [
      setuptools wheel
    ];
    doCheck = false;
  };
  # ryven Nix package, from ./ryvencore-qt
  ryvencore-qt = python.pkgs.buildPythonPackage rec {
    pname = "ryvencore_qt";
    version = get-version (builtins.readFile ./ryvencore-qt/setup.cfg);
    src = with pkgs.lib.fileset;
      toSource {
        root = ./ryvencore-qt;
        fileset = 
          intersection
          (gitTracked ./..)
          (unions [
            ./setup.py
            ./setup.cfg
            ./MANIFEST.in
            ./ryvencore_qt
          ]);
      }
    ;
    # build dependencies
    buildInputs = with python.pkgs; [ 
      setuptools wheel
    ];
    # runtime dependencies
    propagatedBuildInputs = with python.pkgs; [
      qtpy
      ryvencore
    ] ++ pysidePkgs;
    doCheck = false;
    meta = {
      homepage = "https://ryven.org";
      descriptions = "TODO";
    };
  };
  # ryven Nix package, from ./ryven-editor
  ryven = python.pkgs.buildPythonPackage rec {
    pname = "ryven";
    version = get-version (builtins.readFile ./ryven-editor/setup.cfg);
    src = with pkgs.lib.fileset;
      toSource {
        root = ./ryven-editor;
        fileset = 
          intersection
          (gitTracked ./..)
          (unions [
            ./setup.py
            ./setup.cfg
            ./MANIFEST.in
            ./ryven
          ]);
      }
    ;
    # build dependencies
    buildInputs = with python.pkgs; [ 
      setuptools wheel
    ];
    # runtime dependencies
    propagatedBuildInputs = with python.pkgs; [
      qtpy
      jinja2
      pygments
      textdistance
      packaging
      ryvencore-qt
    ] ++ pysidePkgs;
    doCheck = false;
    meta = {
      homepage = "https://ryven.org";
      description = "Flow-based visual scripting for Python";
      license = pkgs.lib.licenses.mit;
    };
  };
  /*
  While there are Nix packages for PySideX/PyQtX, Ryven primarily
  targets PyPI packaging, so we want to use pip by default.
  This is why we are not using the Nix packages defined in the
  respective sub-directories for the default dev shell.
  Nevertheless, Nix allows us to have tight environment control.
  * installing Qt
    `pip install PySide{2,6}` won't work out of the box, due to 
    system library depencencies. We can either:
    * manually satisfy dependencies (include them in buildInputs
      and extend paths in shellHook)
      * seems to work for PySide2, not yet for PySide6
    * use nixpks provided wrappers (pkgs.python310Packages.pysideX,
      and use --system-site-packages with virtualenv)
  * X server: on Linux with X server running you might need to
    manually allow connections to it by running
    $ nix-shell -p xorg.xhost
    $ xhost +
  */
  make-shell = {
    useNixPySide ? false,
  }: pkgs.mkShellNoCC rec {    
    packages = with pkgs; [
      git man which
      python.pkgs.pip
      python.pkgs.virtualenv
    ] ++ (
      if useNixPySide then pysidePkgs else [
        # dependencies for the PySide2 package from PyPI to work
        qt5.full stdenv.cc.cc.lib glibc glib libGL zlib bzip2 openssl libpng libjpeg ffmpeg libxkbcommon fontconfig freetype zstd dbus xorg.libXrender xorg.libxcb xorg.libX11 xorg.libXext xorg.libXcursor xorg.xhost
    ]);
    VENV_DIR = "venv-nix";
    shellHook = ''
      # set up environment variables
      SOURCE_DATE_EPOCH=$(date +%s)
      export TMPDIR=/tmp
      export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${pkgs.lib.makeLibraryPath packages}"  

      # setup Python venv (in tmp directory if VENV_DIR is not set)
      if [ "$rebuildVenv" = "true" ]; then
        rm -r $VENV_DIR
      fi
      if [ -z $VENV_DIR ]; then
        export VENV_DIR=$(mktemp -d)
      fi
      virtualenv --system-site-packages $VENV_DIR
      source $VENV_DIR/bin/activate

      # install ryven dependencies
      pushd ryven-editor
      pip install . && pip uninstall --yes ryven
      popd

      # install ryvencore-qt dependencies
      pushd ryvencore-qt
      pip install . && pip uninstall --yes ryvencore-qt
      popd

      ${if useNixPySide then "" else "pip install PySide2"}

      cat << EOF

      >>>> Ryven dev shell >>>>
      
      This shell allows to run Ryven and build the pip packages
      in a somewhat traditional manner, using pip and a Python
      virtual environment.
      This shell has activated the Python virtual environment:
        $VENV_DIR

      To e.g. build the Ryven package, run:
        cd ryven-editor
        pip install .
      or to run the Ryven editor, run:
        pip uninstall --yes ryven
        python ryven-editor/ryven/main/Ryven.py

      ${if useNixPySide then ''
        This shell uses a Nix provided PySide package.
      '' else ''
        This shell uses a PySide2 package from PyPI. several
        dependencies are included in the buildInputs to satisfy
        system library dependencies. Some might still be missing.
      ''}
      <<<<<<<<<<<<<<<<<<<<<<<<<
      
      EOF
    '';
  };
in
{
  inherit ryvencore ryvencore-qt ryven;
  pip-shell = make-shell { useNixPySide = false; };
  nix-shell = make-shell { useNixPySide = true; };
}