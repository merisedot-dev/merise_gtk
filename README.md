# MeriseGTK

A GUI for [MeriseDot], meant both as a PoC and a default usable interface to edit your databases.

## Installation

As of now, not that many methods are implemented for installation, but they can be added if needed. Please refer to the contribution guidelines if you wish to add your own.

### Nix

If you wish to use [Nix] for installation, please run the following command in your shell :

```shell
nix profile add github:merisedot-dev/merise_gtk
```

Alternatively, you can use the following set of commands :

```shell
git clone https://github.com/merisedot-dev/merise_gtk
cd merise_gtk
nix profile add .
```

## Usage

[MeriseDot]: https://github.com/merisedot-dev/merise_dot
[Nix]: https://nixos.org
