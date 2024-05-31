{ 
  pkgs ? import <nixpkgs> {},
  python ? pkgs.python310,
  pysidePkg ? python.pkgs.pyside2,
}:
let
  get-version = s: builtins.head (builtins.match ".*version[[:space:]*]=[[:space:]*]([[:digit:]|\.]*).*" s);
  version = get-version (builtins.readFile ./setup.cfg);

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

  sourceFiles = with pkgs.lib.fileset; intersection
    (gitTracked ./..)
    (unions [
      ./setup.py
      ./setup.cfg
      ./MANIFEST.in
      ./ryvencore_qt
    ]);

  ryvencore-qt = python.pkgs.buildPythonPackage rec {
    pname = "ryvencore_qt";
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
      ryvencore
    ];
    doCheck = false;
    meta = {
      homepage = "https://ryven.org";
      descriptions = "TODO";
    };
  };
in
ryvencore-qt
