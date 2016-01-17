# github-notification-number
This is a script which returns the number of GitHub notifications that the user has. The script works via a GitHub api token, which it can be given either through an environment variable or through standard input, with standard input taking priority.

## Usage
Once the token environment variable has been set, as shown in the setup section, this script can be used as follows:

```
$ ./notifications.py
15
```

The script can also be run by giving the GitHub notification token to it via standard input. Note that the token given in standard input takes priority over the token set as the environment variable.

```
$ echo "YOURTOKENCODEHERE" | ./notifications.py
15
```

## Setup
Before github-notification-number can be successfully run, it must first be setup to work with your GitHub account. It works using an api access token which you can setup though GitHub.

First go to your GitHub setting page, then go under personal access tokens. Generate a new token and set it to only have the scope `notifications`, feel free to turn off all other scopes. Also give it a good descriptsion to make sure that you can remember what it is being used for.

Once you have generated the token, copy the content of the token that GitHub generates, and run it in the following command, replacing `YOURTOKENCODEHERE` with the token code.

```
export GH_NOTIFICATION_TOKEN=YOURTOKENCODEHERE
```

Once the api token has bee successfully set, github-notification-number should work correctly.

If you want to have the token environment variable be persistant across logins, add the command to your `~/.bashrc` or other bash configuration file.

### Conky
If you are using github-notification-number in conky, such as for a notification in a conky-based status bar, it needs to be run a bit differently, due to the use of the environment variable.

When you want to call the script in order to display its result, be sure to run it through bash using the `-i` and `-c` flags and echoing the environment variable into the command, as follows, but changing it to use the correct location of the script on your system. The use of the `-i` flag allows echo to access the environmental variable set in your bash configuration file. The use of the `-c` flag runs the given commands in bash.

```
bash -i -c 'echo $GH_NOTIFICATION_TOKEN | ~/.config/i3/conkybar/github-notification-number/notifications.py'
```

For instance, if you wanted to display the number of github notifications you have, refreshed at a set interval, you would use something along the lines of the following:

```
${execi 200 bash -i -c 'echo $GH_NOTIFICATION_TOKEN | ~/.config/i3/conkybar/github-notification-number/notifications.py'}
```

## License
github-notification-number is availible under the [MIT License](http://opensource.org/licenses/MIT), see `LICENSE` for more information.
