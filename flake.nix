{
  description = "MeriseDot frontend toolchain";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
    # adding our own custom dependency
    meriseDot = {
      url = "github:merisedot-dev/merise_dot";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      meriseDot,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
        merise_dot = meriseDot.packages.${system}.default;
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
              libadwaita
            ];
          postVenvCreation = "pip install -e .";
          venvDir = ".venv";
          src = null;
        };
      }
    );
}
