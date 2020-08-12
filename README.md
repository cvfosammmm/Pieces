# Pieces

Personal task manager for the GNU/Linux desktop, written in Python with Gtk.

Website: <a href="https://www.cvfosammmm.org/pieces/">https://www.cvfosammmm.org/pieces/</a>

![Screenshot](https://github.com/cvfosammmm/Pieces/raw/master/data/screenshot.png)

## Running Pieces with Gnome Builder

To run Pieces with Gnome Builder just click the "Clone.." button on the start screen, paste in the url (https://github.com/cvfosammmm/Pieces.git), click on "Clone" again, wait for it to download and hit the play button. It will build Pieces and its dependencies and then launch it.

Warning: Building Pieces this way may take some time.

## Running Pieces on Debian (probably Ubuntu, other Distributions too?)

This way is probably a bit faster and may save you some disk space. I develop Pieces on Debian and that's what I tested it with. On Debian derivatives (like Ubuntu) it should probably work the same. On distributions other than Debian and Debian derivatives it should work more or less the same. If you want to run Pieces from source on another distribution and don't know how please open an issue here on GitHub. I will then try to provide instructions for your system.

1. Run the following command to install prerequisite Debian packages:<br />
`apt-get install libgtk-3-dev python3-xdg`

2. Download und Unpack Pieces from GitHub

3. cd to Pieces folder

4. Run meson: `meson builddir`<br />
Note: Some distributions may not include systemwide installations of Python modules which aren't installed from distribution packages. In this case, you want to install Pieces in your home directory with `meson builddir --prefix=~/.local`.

5. Install Pieces with: `ninja install -C builddir`<br />
Or run it locally: `./scripts/pieces.dev`

## Getting in touch

Pieces development / discussion takes place on GitHub at [https://github.com/cvfosammmm/Pieces](https://github.com/cvfosammmm/Pieces "project url").

## License

Pieces is licensed under GPL version 3 or later. See the COPYING file for details.
