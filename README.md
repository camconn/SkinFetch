#SkinFetch

SkinFetch is a Python program for downloading the skins of Minecraft users.

##Dependencies
- A version of Python 3
    - The [requests](http://docs.python-requests.org/en/latest/) library
- An internet connection

All of these packages should be installed on average Ubuntu installation, if for
some reason you don't have one of these packages, run: 

`sudo pip3 install requests`

##Running 
Downloaded skins will be placed into a 'skins' folder in the current working
directory. The program will accept as many skins as you feed it.

To run SkinFetch from command line, `./fetch.py user1 [user2 ... userN]`


An example of typical command-line usage:
```./fetch.py Notch jeb_ carlmanneh```

##License
Copyright (c) 2015 Cameron Conn 

The program is released under the GNU Public License version 3 or any later
version.

A copy of the license may be found in the COPYING file.
