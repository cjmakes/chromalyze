{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
        with pkgs; {
          devShells.default = mkShell {
            buildInputs = [ (python311Packages.opencv4.override { enableGtk2 = true; }) ];
          };
        }
    );
}

# This is also possible using an override
# {
# 	description = "A very basic flake";
# 
# 	inputs = {
# 		nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
# 	};
# 
# 	outputs = { self, nixpkgs }: 
#  let
# 	system = "x86_64-linux";
# 	pkgs = import nixpkgs {
# 		inherit system;
# 		overlays = [
# 		(final: prev: {
# 			python311 = prev.python311.override {
# 				packageOverrides = pyfinal: pyprev: {
# 					opencv4 = pyprev.opencv4.override {
# 					 enableGtk2 = true; 
# 					};
# 				};
# 			};
# 		})
# 		];
# 	};
# 	in
# 	{
# 		devShells.x86_64-linux.default = pkgs.mkShell {
# 			buildInputs = [ pkgs.python311Packages.opencv4 ];
# 		};
# 	};
# }
