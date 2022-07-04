"""
Setup Script for PA-Assist 
    - Repurposed from Elebumm's RedditVideoMakerBot
"""

# Imports
import os
import time
from utils.console import print_markdown
from utils.console import print_step
from utils.console import print_substep
from rich.console import Console
from utils.loader import Loader
from os.path import exists
console = Console()

setup_done = exists(".setup-done-before")

if setup_done == True:
	console.log("[red]Setup was already completed! Please make sure you have to run this script again. If you have to, please delete the file .setup-done-before")
	exit()

# These lines ensure the user:
# - knows they are in setup mode
# - knows that they are about to erase any other setup files/data.

print_step("Setup Assistant")

print_markdown(
	"### You're in the setup wizard. Ensure you're supposed to be here, then type yes to continue. If you're not sure, type no to quit."
)

# This Input is used to ensure the user is sure they want to continue.
ensureSetupIsRequired = input("Are you sure you want to continue? > ").casefold()
if ensureSetupIsRequired != "yes":
	console.print("[red]Exiting...")
	time.sleep(0.5)
	exit()
else:
	# Again, let them know they are about to erase all other setup data.
	console.print("[bold red] This will overwrite your current settings. Are you sure you want to continue? [bold green]yes/no")
	overwriteSettings = input("Are you sure you want to continue? > ").casefold()
	if overwriteSettings != "yes":
		console.print("[red]Abort mission! Exiting...")
		time.sleep(0.5)
		exit()
	else:
		# Once they confirm, move on with the script.
		console.print("[bold green]Alright! Let's get started!")
		time.sleep(1)

# Oauth keys
console.log("Ensure you have the following ready to enter:")
console.log("[bold green]CONSUMER_KEY")
console.log("[bold green]CONSUMER_SECRET")
console.log("[bold green]ACCESS_TOKEN")
console.log("[bold green]ACCESS_TOKEN_SECRET")
time.sleep(0.5)
console.print("[green]If you don't have these, please follow the instructions in the README.md file to set them up.")
console.print("[green]If you do have these, type yes to continue. If you dont, go ahead and grab those quickly and come back.")
confirmUserHasCredentials = input("Are you sure you have the credentials? > ").casefold()
if confirmUserHasCredentials.lower() != "yes" or confirmUserHasCredentials.lower() != "y":
	console.print("[red]I don't understand that.")
	console.print("[red]Exiting...")
	exit()
else:
	console.print("[bold green]Alright! Let's get started!")
	time.sleep(1)

"""

Begin the setup process.

"""

console.log("Enter your credentials now.")
CONSUMER_KEY = input("CONSUMER_KEY > ")
CONSUMER_SECRET = input("CONSUMER_SECRET > ")
ACCESS_TOKEN = input("ACCESS_TOKEN > ")
ACCESS_TOKEN_SECRET = input("ACCESS_TOKEN_SECRET > ")
console.log("Attempting to save your credentials...")
loader = Loader("Saving Credentials...", "Done!").start()
time.sleep(0.5)
console.log("Removing old .env file...")
os.remove(".env")
time.sleep(0.5)
console.log("Creating new .env file...")
with open('.env', 'a') as f:
	f.write(f'CONSUMER_KEY="{CONSUMER_KEY}"\n')
	time.sleep(0.5)
	f.write(f'CONSUMER_SECRET="{CONSUMER_SECRET}"\n')
	time.sleep(0.5)
	f.write(f'ACCESS_TOKEN="{ACCESS_TOKEN}"\n')
	time.sleep(0.5)
	f.write(f'ACCESS_TOKEN_SECRET="{ACCESS_TOKEN_SECRET}"\n')
	time.sleep(0.5)

with open('.setup-done-before', 'a') as f:
	f.write("This file blocks the setup assistant from running again. Delete this file to run setup again.")

loader.stop()

console.log("[bold green]Setup Complete! Returning...")

# Post-Setup: send message and try to run main.py again.
os.system("python main.py")