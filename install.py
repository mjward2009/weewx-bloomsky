#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
#                       Installer for Bloomsky Driver
#
# Version: 0.1.0                                        Date: 25 June 2017
#
# Revision History
#   25 June 2017         v0.1
#       - initial implementation
#

import weewx

from distutils.version import StrictVersion
from setup import ExtensionInstaller

REQUIRED_VERSION = "3.7.0"
BLOOMSKY_VERSION = "0.1.0"


def loader():
    return BloomskyInstaller()


class BloomskyInstaller(ExtensionInstaller):
    def __init__(self):
        if StrictVersion(weewx.__version__) < StrictVersion(REQUIRED_VERSION):
            msg = "%s requires weeWX %s or greater, found %s" % (''.join(('Bloomsky driver ', BLOOMSKY_VERSION)),
                                                                 REQUIRED_VERSION,
                                                                 weewx.__version__)
            raise weewx.UnsupportedFeature(msg)
        super(BloomskyInstaller, self).__init__(
            version=BLOOMSKY_VERSION,
            name='Bloomsky',
            description='weeWX driver for Bloomsky Sky1/Sky2/Storm personal weather stations.',
            author="Gary Roderick",
            author_email="gjroderick<@>gmail.com",
            files=[('bin/user', ['bin/user/bloomsky.py'])],
            config={
                'Bloomsky': {
                    'api_key': 'INSERT_API_KEY_HERE',
                    'poll_interval': 15,
                    'driver': 'user.bloomsky'
                },
                'Accumulator': {
                    'deviceID': {
                        'adder': 'noop'
                    },
                    'deviceName': {
                        'adder': 'noop'
                    },
                    'imageURL': {
                        'adder': 'noop'
                    },
                    'deviceType': {
                        'adder': 'noop'
                    },
                    'night': {
                        'adder': 'noop'
                    },
                    'imageTimestamp': {
                        'adder': 'noop'
                    }
                }
            }
        )
