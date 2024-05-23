# This sets up a basic deveopment environment using Nix shells.
# It assumes it is running on a Linux machine with X server running.
# Other than that, it should be fairly portable.

/* Notes

    * installing Qt: pip installing PySide2 or PySide6 won't work out 
      of the box, because they expect a bunch of system libraries to be 
      available. You can either:
        * pip package + manual dependency resolution
            * PySide6: didn't get to work yet
            * PySide2:
                * include library dependencies in buildInputs:
                    qt5.full
                    stdenv.cc.cc.lib
                    glibc glib libGL zlib bzip2 openssl libpng libjpeg
                    ffmpeg libxkbcommon fontconfig freetype zstd dbus
                    xorg.libXrender xorg.libxcb xorg.libX11 xorg.libXext 
                    xorg.libXcursor xorg.xhost
                * extend paths in shellHook:
                    $ export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${pkgs.lib.makeLibraryPath buildInputs}"
                    $ export PYTHONPATH=$PYTHONPATH:$VENV/${pkgs.python3.sitePackages}/
                * then pip install PySide2
        * using nixpks provided wrappers
            * PySide6:
                * include in buildInputs:
                    python310Packages.pyside6
                * use --system-site-packages with virtualenv so PySide6 
                  is available in the virtual environment
            * PySide2: similar to PySide6
    * on Linux, with X server running, you might need to allow connections 
      to the X server; on the host machine, run:
        $ nix-shell -p xorg.xhost
        $ xhost +

*/

{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell rec {
    buildInputs = with pkgs; [
        # stuff
        git man which

        # python
        python310
        python310Packages.pip
        python310Packages.virtualenvwrapper
        # python310Packages.pyside6

        # for PySide2, uncomment:
        qt5.full
        stdenv.cc.cc.lib
        glibc glib libGL zlib bzip2 openssl libpng libjpeg
        ffmpeg libxkbcommon fontconfig freetype zstd dbus
        xorg.libXrender xorg.libxcb xorg.libX11 xorg.libXext 
        xorg.libXcursor xorg.xhost
    ];

    shellHook = ''
        SOURCE_DATE_EPOCH=$(date +%s)
        export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${pkgs.lib.makeLibraryPath buildInputs}"

        # setup Python venv
        export TMPDIR=/tmp  && export VENV=$(mktemp -d)
        virtualenv --system-site-packages $VENV
        source $VENV/bin/activate
    '';
}
