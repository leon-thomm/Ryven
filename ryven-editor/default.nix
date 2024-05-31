{ 
  pkgs ? import <nixpkgs> {},
  python ? pkgs.python310,
  pysidePkg ? python.pkgs.pyside2,
  additionalPythonPackages ? []
}:
let
  get-version = s: builtins.head (builtins.match ".*version[[:space:]*]=[[:space:]*]([[:digit:]|\.]*).*" s);
  version = get-version (builtins.readFile ./setup.cfg);

  ryvencore-qt = pkgs.callPackage ../ryvencore-qt {
    inherit pkgs python pysidePkg;
  };

  sourceFiles = with pkgs.lib.fileset; intersection
    (gitTracked ./..)
    (unions [
      ./setup.py
      ./setup.cfg
      ./MANIFEST.in
      ./ryven
    ]);

  ryven = python.pkgs.buildPythonPackage rec {
    pname = "ryven";
    inherit version;
    src = pkgs.lib.fileset.toSource {
      root = ./.;
      fileset = sourceFiles;
    };
    buildInputs = with python.pkgs; [ 
      setuptools wheel
    ];
    propagatedBuildInputs = with python.pkgs; [
      pysidePkg
      qtpy
      jinja2
      pygments
      textdistance
      packaging
      ryvencore-qt
    ] ++ additionalPythonPackages;
    doCheck = false;
    meta = {
      homepage = "https://ryven.org";
      description = "Flow-based visual scripting for Python";
      license = pkgs.lib.licenses.mit;
    };
  };
in
ryven
