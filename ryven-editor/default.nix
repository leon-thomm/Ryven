{
  lib,
  python, pysidePkg,
  ryvencore-qt,
  additionalPythonPackages ? [],
}:
let
  get-version = s: builtins.head (
    builtins.match ".*version[[:space:]*]=[[:space:]*]([[:digit:]|\.]*).*" s
  );
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
          ./ryven
        ]);
    }
  ;
  ryven = python.pkgs.buildPythonPackage rec {
    pname = "ryven";
    inherit version src;
    # build dependencies
    buildInputs = with python.pkgs; [ 
      setuptools wheel
    ];
    # runtime dependencies
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
      license = lib.licenses.mit;
    };
  };
in
ryven
