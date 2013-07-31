#SkinFetch

##About
SkinFetch is a Python program for downloading the skins of minecraft users.
I made SkinFetch just as a small project for fun.

##Dependencies
- PyQt4 (required only for GUI)
- Python 3 or later
    - urllib3
- An internet connection

All of these packages should be installed on average Ubuntu installation, if for
some reason you don't have one of these packages, run:
`sudo apt-get install python-qt4 python3 python-urllib3`

##Running 
Downloaded skins will be placed into a 'skins' folder in the current working
directory.

To run SkinFetch with a fancy GUI: `./fetchGUI.py`
To run SkinFetch from command line, `./fetch.py user1 [user2 ... userN]`

Example of typical command-line usage:
`./fetch.py Notch jeb_ carlmanneh`

##License
Copyright (c) 2013 Cameron Conn

The program is released under the GNU Public License version 3 or any later
version.

A copy of the license may be found in the COPYING file.
