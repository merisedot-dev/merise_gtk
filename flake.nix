{
  description = "MeriseDot frontend toolchain";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
    # adding our own custom dependency
    merise_dot.url = "github:merisedot-dev/merise_dot";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      merise_dot,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        # default build
        packages.default = pkgs.callPackage ./default.nix { inherit merise_dot; };

        # devShells from fellow lazy devs
        devShells.default = pkgs.mkShell {
          name = "merise_gtk";
          inputsFrom = [ self.packages.${system}.default ];
          packages =
            with pkgs.python3Packages;
            with pkgs;
            [
              venvShellHook
              bumpver
              behave # testing utility
              mkdocs # documentation building tool
            ];
          postVenvCreation = "pip install -e .";
          venvDir = ".venv";
          src = null;
        };
      }
    );
}
