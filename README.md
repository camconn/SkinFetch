#SkinFetch

SkinFetch is a Python program for downloading the skins of Minecraft users.
I made SkinFetch just as a small project for fun. It helped me learn some basic
stuff about Python3 and PyQt.

##Dependencies
- A version of Python 3
    - urllib3
    - PyQt4 (required only for gui)
- An internet connection

All of these packages should be installed on average Ubuntu installation, if for
some reason you don't have one of these packages, run: 

`sudo apt-get install python3-qt4 python3 python3-urllib3`

If you prefer pip, run the below instead of the above:

`sudo pip3 install urllib3 pyqt4` 


##Running 
Downloaded skins will be placed into a 'skins' folder in the current working
directory. The program will accept as many skins as you feed it.

To run SkinFetch with an (un)fancy GUI: `./fetchGUI.py` 
To run SkinFetch from command line, `./fetch.py user1 [user2 ... userN]`


An example of typical command-line usage:
```./fetch.py Notch jeb_ carlmanneh```

##License
Copyright (c) 2014 Cameron Conn 

The program is released under the GNU Public License version 3 or any later
version.

A copy of the license may be found in the COPYING file.
