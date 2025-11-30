{
  description = "MeriseDot frontend toolchain";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      ...
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        # default build
        packages.default = pkgs.callPackage ./default.nix { };

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
            ];
          postVenvCreation = "pip install -e .";
          venvDir = ".venv";
          src = null;
        };
      }
    );
}
