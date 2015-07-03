#!/usr/bin/env python3

# SkinFetch: Download a player's Minecraft Skin
# Copyright (c) 2015 Cameron Conn

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
import requests
from os import path, mkdir, getcwd


def fetch_skin(username):
    """
    Fetch a player's skin

    username -- The username of skin to fetch
    """

    # Where do we save the file?
    file_name = ''.join([username, '.png'])
    file_path = path.join(getcwd(), 'skins', file_name)  # Save to skins folder

    skin_url = 'http://skins.minecraft.net/MinecraftSkins/{}'.format(file_name)
    skin = requests.get(skin_url)

    if skin.status_code == requests.codes.ok:
        with open(file_path, 'wb') as f:
            for chunk in skin.iter_content():
                f.write(chunk)
        print('Done!')
    elif skin.status_code == 404:
        print('Skin not found.')
    else:
        print('An error occurred.')


# For running skinfetch from the command line
if __name__ == "__main__":
    # If no arguments passed, display error and exit
    if len(sys.argv) == 1:
        print('Error: You must specify a skin to download!')
        sys.exit()

    # Check to see if directory 'skins' exists, if not, make it
    if not path.isdir('skins'):
        mkdir('skins')
        print('"skins" folder not found, creating one')

    for name in sys.argv[1:]:
        name = name.strip()

        print('Fetching skin for {}...'.format(name), end=' ')
        fetch_skin(name)
