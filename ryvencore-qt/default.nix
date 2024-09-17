{ 
  lib,
  python, pysidePkg,
  additionalPythonPackages ? [ ],
}:
let
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
  get-version = s: builtins.head (builtins.match ".*version[[:space:]*]=[[:space:]*]([[:digit:]|\.]*).*" s);
  version = get-version (builtins.readFile ./setup.cfg);
  src = with lib.fileset;
    toSource {
      root = ./.;
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
  ryvencore-qt = python.pkgs.buildPythonPackage rec {
    pname = "ryvencore_qt";
    inherit version src;
    # build dependencies
    buildInputs = with python.pkgs; [ 
      setuptools wheel
    ];
    # runtime dependencies
    propagatedBuildInputs = with python.pkgs; [
      pysidePkg
      qtpy
      ryvencore
    ] ++ additionalPythonPackages;
    doCheck = false;
    meta = {
      homepage = "https://ryven.org";
      descriptions = "TODO";
    };
  };
in
ryvencore-qt
