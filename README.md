### Tutorial Used
https://thepythoncode.com/article/make-a-chess-game-using-pygame-in-python#google_vignette

### Getting setup
I used pyenv ([tutorial for mac here](https://medium.com/marvelous-mlops/the-rightway-to-install-python-on-a-mac-f3146d9d9a32))
to get my python environment setup.

Once you have python just run
`pip intall pygame`

### Building Game
To compile the game into a single executable for the platform you are developing on, you'll
first need to install [pyinstaller](https://www.google.com/search?client=safari&rls=en&q=pyinstaller&ie=UTF-8&oe=UTF-8)

`pip install pyinstaller`

Once pyinstaller is installed, to build the executable run:

`pyinstaller --add-data "data/imgs/*.png:./data/imgs" main.py -F`

If we break this down, the first flag `--add-data "[relative-path-to-images]:[executable-path-to-images]"`
will specify what images pyinstaller will copy to the executable. We copy this to the same path in the executable preceded
by a "." (signifies relative directory of main.py) to ensure that our code will be able to find our images in the same
directory when run by the executable.

The `*` in "data/imgs/*.png" tells pyinstaller to copy all .png files in the data/imgs directory.

Finally, the -F flag tells pyinstaller to build the app into a single executable. Without this flag, by default
pyinstaller will produce a one folder bundle, instead of a single file bundle executable.

#### Specific versions
- Python: 3.12.2
- pygame: 2.5.2
- however pretty sure any python >= 3.8 is fine (min version for pyinstaller), and whatever latest pygame you get should be fine too

