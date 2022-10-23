# Signora Bot
Signora B..blush?
<p align="center">
  <img src="./data/images/signora.png" width="350" title="angry tubby?">
</p>

## General Instructions
After cloning the repo first create a python enviroment. For that follow the following steps:<br/>
- ```python -m venv <virtual_env_name>```<br/>
This should create a folder with the corresponding name. Then activate the python environment using the following command.<br/>
- ```<virtual_env_name>\Scripts\activate.bat```(only works for Windows)<br/>
After this you can easily set up the python pakages using `pip`.<br/>
- ```python -m pip install -r requirements.txt```<br/>
Note that if you install/update any new requirements use the ` pip freeze > requirements.txt` command to update the requuirements file.<br/>
- If you want to code a new feature for this bot, create a cog or modify existing cog and add uniersal functions in utils. Finally add the cog to the main file.<br/>

For more information on virtual environments click [here](https://docs.python.org/3/tutorial/venv.html)<br/>

*Note: In `discord.py` overriding the default provided `on_message` forbids any extra commands from running. To fix this, add a bot.process_commands(message) line at the end of your `on_message`. I would recommend not to use this as commands can satisfy most of your needs*

## How it works
There are 2 main files in this repository: `main.py` and `main.yml`.
The `main.py` file contains the logic of the bot and the `main.yml` contains instructions to setup the CI pipeline for github.
The `main.yml` is based on the standard template provided by GitHub.
```
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```
The above code indicates that the set of instructions provided will trigger on every push and an accepted pull__request.
```
workflow_dispatch:
  schedule:
    - cron: '0 */6 * * *'
```
This peice of code indicates that the workflow dispatch is scheduled for every six hours.
For more information on cron visit https://crontab.guru/.
This part of code basically helps keep the bot up 24x7. The base code is under a event loop, so it doesn't terminate and Github tends to kill any processes that run for more than 6hrs, so this code retriggers the CI pipline after every six hours.
```
env: # Or as an environment variable
  BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
run: |
  echo Add other actions to build,
  echo test, and deploy your project.
  echo "$BOT_TOKEN"
  pip install discord
  pip install python-dotenv
  python main.py
```
The above code are the main set of instructions that are to be run by the bot.
First the `BOT_TOKEN`, the repo secret(provided by discord), has to be loaded as an enviroment variable so that the python program can have access to it.
The `roasts.json` is not mine. Credits to: [Nydauron](https://raw.githubusercontent.com/Nydauron/CharBot/master/roasts.json)
The artifact rater in the `rater.py` and the translations in `translations.py` are edits to the og artifact rater bot by [shrubin](https://github.com/shrubin/Genshin-Artifact-Rater), credits to him.
