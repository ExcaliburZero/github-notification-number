# github-notification-number
This is a script which returns the number of GitHub notifications that the user has.

## Usage
This script can be used as follows:

```
$ python notifications.py
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

## License
github-notification-number is availible under the [MIT License](http://opensource.org/licenses/MIT), see `LICENSE` for more information.
