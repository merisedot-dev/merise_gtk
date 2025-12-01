{
  pkgs,
  stdenv,
  python3,
  python3Packages,
  fetchPypi,
  hatch,
  merise_dot, # our own custom dependency
  ...
}:

let
  merisegtk_version = "0.0.0";

  # build scripts
  hatch-build-scripts = python3Packages.buildPythonPackage rec {
    pname = "hatch-build-scripts";
    version = "0.0.4";
    format = "pyproject";

    buildInputs = [ hatch ];
    src = fetchPypi {
      inherit version;
      pname = "hatch_build_scripts";
      sha256 = "sha256-x4UgmGkH5HU48suyT95B7fwsxV9FK1Ni+64Vzk5jRPc=";
    };
  };
in
python3Packages.buildPythonApplication {
  pname = "merise_gtk";
  version = merisegtk_version;

  src = ./.;
  format = "pyproject";

  nativeBuildInputs =
    with pkgs;
    with python3Packages;
    [
      hatch
      hatch-build-scripts
      merise_dot # inner library
      pygobject3
      gtk4
    ];
}
