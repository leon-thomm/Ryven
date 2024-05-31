# This sets up a basic deveopment environment using Nix shells.
# It assumes it is running on a Linux machine with X server running.
# Other than that, it should be fairly portable.

/* Notes

  * installing Qt: pip installing PySide2 or PySide6 won't work out 
    of the box, because they expect a bunch of system libraries to be 
    available. You can either:
    * pip package + manual dependency resolution
      * PySide6: didn't get to work yet
      * PySide2:
        * include library dependencies in buildInputs:
            qt5.full
            stdenv.cc.cc.lib
            glibc glib libGL zlib bzip2 openssl libpng libjpeg
            ffmpeg libxkbcommon fontconfig freetype zstd dbus
            xorg.libXrender xorg.libxcb xorg.libX11 xorg.libXext 
            xorg.libXcursor xorg.xhost
        * extend paths in shellHook:
          $ export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${pkgs.lib.makeLibraryPath buildInputs}"
          $ export PYTHONPATH=$PYTHONPATH:$VENV/${pkgs.python3.sitePackages}/
        * then pip install PySide2
    * using nixpks provided wrappers
      * PySide6:
        * include in buildInputs:
            python310Packages.pyside6
        * use --system-site-packages with virtualenv so PySide6 
          is available in the virtual environment
      * PySide2: similar to PySide6
  * on Linux, with X server running, you might need to allow connections 
    to the X server; on the host machine, run:
      $ nix-shell -p xorg.xhost
      $ xhost +

*/

{ 
  pkgs ? import <nixpkgs> {},
  rebuildVenv ? false,
}:
let
  ryven = pkgs.callPackage ./ryven-editor/default.nix {
    python = pkgs.python310;
  };
in
pkgs.mkShellNoCC rec {
  packages = with pkgs; [
    # stuff
    git man which
    python310Packages.pip
    python310Packages.virtualenv
    python310Packages.pyside6
    # for manual PySide2 setup, include the following:
    # qt5.full
    # stdenv.cc.cc.lib
    # glibc glib libGL zlib bzip2 openssl libpng libjpeg
    # ffmpeg libxkbcommon fontconfig freetype zstd dbus
    # xorg.libXrender xorg.libxcb xorg.libX11 xorg.libXext 
    # xorg.libXcursor xorg.xhost
  ];
  VENV_DIR = "venv-nix";
  shellHook = ''
    # set up environment variables
    SOURCE_DATE_EPOCH=$(date +%s)
    export TMPDIR=/tmp
    export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${pkgs.lib.makeLibraryPath packages}"  

    # setup Python venv (in tmp directory if VENV_DIR is not set)
    if [ "$rebuildVenv" = "true" ]; then
      rm -rf $VENV_DIR
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
  '';
}