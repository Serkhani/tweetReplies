# Main
from utils.console import print_markdown
from utils.console import print_step
from utils.console import print_substep
from rich.console import Console
import time
from utils.loader import Loader
from dotenv import load_dotenv
from dotenv import load_dotenv
import os, time, shutil, argparse

def configure():
    console = Console()

    configured = True
    REQUIRED_VALUES = [
        "CONSUMER_KEY",
        "CONSUMER_SECRET",
        "ACCESS_TOKEN",
        "ACCESS_TOKEN_SECRET",
    ]


    print_markdown(
        "### Thanks for using this tool! [Feel free to contribute to this project on GitHub!]If you have any questions, feel free to reach out to me on Twitter or submit a GitHub issue."
    )

    """

    Load .env file if exists. If it doesnt exist, print a warning and launch the setup wizard.
    If there is a .env file, check if the required variables are set. If not, print a warning and launch the setup wizard.

    """

    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

    load_dotenv()

    console.log("[bold green]Checking environment variables...")
    time.sleep(1)


    if not os.path.exists(".env"):
        configured = False
        console.log("[red] Your .env file is invalid, or was never created. Standby.")

    for val in REQUIRED_VALUES:
        #print(os.getenv(val))
        if val not in os.environ or not os.getenv(val):
            console.log(f'[bold red]Missing Variable: "{val}"')
            configured = False
            console.log(
                "[red]Looks like you need to set your Twitter credentials in the .env file. Please follow the instructions in the README.md file to set them up."
            )
            time.sleep(0.5)
            console.log(
                "[red]We can also launch the easy setup wizard. type yes to launch it, or no to quit the program."
            )
            setup_ask = input("Launch setup wizard? > ")
            if setup_ask.trim().lower() == "yes" or setup_ask.trim().lower() == "y":
                console.log("[bold green]Here goes nothing! Launching setup wizard...")
                time.sleep(0.5)
                os.system("python setup.py")

            elif setup_ask.trim().lower() == "no" or setup_ask.trim().lower() == "n":
                console.print("[red]Exiting...")
                time.sleep(0.5)
                exit()
                return False
            else:
                console.print("[red]I don't understand that. Exiting...")
                time.sleep(0.5)
                exit()
                return False
    console.log("[bold green]Enviroment Variables are set! Continuing...")
    return True