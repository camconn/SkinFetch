#!/usr/bin/env python3

# SkinFetch: Download a player's Minecraft Skin
# Copyright (c) 2013 Cameron Conn

# Begin License ===============================================================
# This file is part of SkinFetch.

# SkinFetch is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# SkinFetch is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with SkinFetch.  If not, see <http://www.gnu.org/licenses/>.
# End License =================================================================

import sys
from urllib import request
from os import path, mkdir, getcwd


def skin_fetch(username):
    """
    Fetch a player's skin

    username -- The username of skin to fetch
    """

    # Check to see if directory 'skins' exists, if not, make it
    if not path.isdir('skins'):
        mkdir('skins')
        print('"skins" folder not found, creating one')

    # Figure out name of file to fetch, and where to save it
    fileName = ''.join([username, '.png'])
    filePath = path.join(getcwd(), 'skins', fileName)  # Save to skins folder

    print('\nFetching skin for {}...'.format(username))

    # Actually download the skin
    skin_url = 'http://s3.amazonaws.com/MinecraftSkins/{}'.format(fileName)
    skin = request.urlopen(skin_url)
    with open(filePath, 'wb') as f:
        f.write(skin.read())

    print('Skin for {0} saved in {1}'.format(username, filePath))


# For running skinfetch from the command line
if __name__ == "__main__":
    # If no arguments passed, display error and exit
    if len(sys.argv) == 1:
        print('Error: No arguments passed')
        sys.exit()

    for name in sys.argv[1:]:
        username = name.strip()  # Remove whitespace just in case

        try:
            skin_fetch(username)
        except Exception as e:
            print('Failed to fetch skin for {0}\n{1}'.format(username, e))
