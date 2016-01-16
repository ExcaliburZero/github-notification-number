### BEGIN LICENSE
# The MIT License (MIT)
#
# Copyright (C) 2016 Christopher Wells <cwellsny@nycap.rr.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
### END LICENSE
"""This is a script which returns the number of GitHub notifications that the
user has."""

import os
import sys
import urllib.request


def get_api_token():
    """Returns the GitHub api token that the user has set at
    GH_NOTIFICATION_TOKEN

    :returns str: The GitHub api token.
    """

    # Get the API access token
    api_token = os.environ.get("GH_NOTIFICATION_TOKEN")

    # Make sure that the token exists
    if api_token is None:
        print("No token set at GH_NOTIFICATION_TOKEN")
        sys.exit(1)

    # Return the token
    return api_token


def get_notifications(api_token):
    """Returns the user's GitHub notifications in JSON format.

    :param str api_token: The user's api access token.
    :returns str: The user's notifications in JSON format.
    """

    # Get the notification info from GitHub
    response = urllib.request.urlopen("https://api.github.com/notifications?access_token=" + api_token)
    notifications = response.read()

    # Return the notifications
    return notifications


def main():
    """Return the number of notifications the user has on GitHub to standard
    output."""

    # Get the API access token
    api_token = get_api_token()

    # Print out the notifications
    notifications = get_notifications(api_token)
    print(notifications)

# Run the main method of the script
if __name__ == '__main__':
    main()
