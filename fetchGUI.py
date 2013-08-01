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

# This program serves as a simple frontend for fetch.py
# Any command line arguments given are thrown away.

import sys
from PyQt4 import QtGui, uic
from urllib import error
from fetch import skin_fetch


class FetchWindow(QtGui.QMainWindow):

    def __init__(self):
        super(FetchWindow, self).__init__()
        self.initUI()

    def initUI(self):
        """
        Load UI and setup PyQt signals
        """
        # Load UI from file
        uic.loadUi('design.ui', self)

        self.fetchBtn.clicked.connect(self.getSkin)
        self.show()

    def getSkin(self):
        """
        Call the fetch method to retrieve the skin.
        """

        username = self.fetchLine.text()

        # Try not to crash when we encounter an error
        try:
            skin_fetch(username)
            self.statusBar().showMessage('Skin {} fetched!'.format(username))
        except error.HTTPError as e:
            if e.code == 403:
                self.errorDialog("""Sorry, but I couldn't find the skin
                                    for {}. (Hint: Usernames are CaSe
                                    SeNsItIvE)""".format(username))
            else:
                self.errorDialog('HTTP error: {}'.format(e.cause))
        except:
            self.errorDialog('An unknown error happened: {}'.format(e))

    def errorDialog(self, message):
        """
        Display an Error Dialog to the user

        message -- The message to display with the error dialog
        """
        dialog = QtGui.QErrorMessage(self)
        dialog.showMessage(message)

# Actually run the program
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    fetch = FetchWindow()
    sys.exit(app.exec_())
