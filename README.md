# Twitter Replies Collector 🎥
This project is meant to help individuals collect replies to a specific tweet

## Motivation 🤔
It can be hard for PAs to scroll through the replies to a Twitter post of an influential person to gather specific information 
... but what if we can automate that process? 🤔

## Disclaimers 🚨

-   This is purely for fun purposes.
-   **At the moment**, this repository won't perform any form of Named Entity Recognition(NER) nor sentiment analysis of the replies. It will just return the replies

## Requirements

-   Python 3.6+
-   tweepy

## Installation 👩‍💻

1. Clone this repository

2. Run `pip3 install -r requirements.txt`

3.  
	3a **Automatic Install**: Run `python main.py` and type 'yes' to activate the setup assistant.

	3b **Manual Install**: Rename `.env.template` to `.env` and replace all values with the appropriate fields. To get Twitter API credentials(**required**), visit [The Twitter Dev Page](https://developer.twitter.com/en/products/twitter-api) TL;DR set up an app that is a "script". Copy your keys into the `.env` file.

4. Run `python main.py` (unless you chose automatic install, then the installer will automatically run main.py)

5. Enjoy 😎


If you want to see more detailed guide, please refer to the official [documentation](https://developer.twitter.com/en/docs).

## Contributing & Ways to improve 📈

In its current state, this bot does exactly what it needs to do. However, lots of improvements can be made.

- [x] Allowing users to choose a tweet to track.
- [x] Allowing users to choose the account to whose post is to be tracked.
- [x] Returning a list of replies.
- [x] Adding a command line interface.
- [ ] Performing NER on each reply to extract specific info (i.e. name of university, name of person)
- [ ] Creating better documentation.

## Developer(s) and maintainer(s).

Serkhani - https://github.com/Serkhani (Founder)