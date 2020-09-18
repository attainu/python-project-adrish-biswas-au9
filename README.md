[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+)

# Bitcoin Alert 

##### What is Bitcoin?

> Bitcoin offers an efficient means of transferring money over the internet and is controlled by a decentralized network with a transparent set of rules, thus presenting an alternative to central bank-controlled fiat money.

##### Advantage of Bitcoin:

>     By using a cryptocurrency, users are able to exchange value digitally without third party oversight

##### Problem Faced by Users:

> The main Issue with Bitcoin is that it is "FICKLE THING" and its value changes every minute.

## BITCOIN-ALERT PROJECT:

> #### This Project consistes of a "Bitcoin-Notification Messaging Service" that can be used to send Real-Time Bitcoin Prices to target Messaging Service like Telegram,E-mail,Phone SMS and Push Notification(IFTTT App)

# Installation Guide:

> step by step series of examples and explanations about how to get your development env running :)

##### Step 1

- Either Download the Repo,Which you will find at the top right of [Repo link](https://github.com/attainu/python-project-adrish-biswas-au9/tree/dev) or clone it in your Local Machine.
  ```sh
  git clone https://github.com/attainu/python-project-adrish-biswas-au9.git
  ```

##### Step 2

- Go into the Folder containing the Project Files


##### Step 3

- Make Sure that your Machine has Python 3.6+
- Run the follwing Command
  ```python
  $ python bitcoin_notifier.py --help
  ```

##### Step 4

- Then,you will see the following options

  ```sh
--set-threshold                  sets the threshold value for the emergency sms updates
--set-interval                   sets the interval for daily updates
--set-duration                   sets the duration value for the emergency sms updates
--set-destination                sets the destination app for daily updates
--set-message-bunch              sets the number of messages to be bunched at an interval
--help                           print this help and exit
  ```

## Guide for Command Line:

> Run the below mentioned appropriate commands for the Target Applications,in the Terminal.
--set-threshold                  sets the threshold value(in rupees) for the emergency sms updates; notice we 
                                 don't provide any options to the user here; the emergency notifications will be as a sms.
--set-interval                   sets the interval(sec) for daily updates (by daily we mean email/telegram updates.)
--set-duration                   sets the duration value(sec) for the entire script/program.
--set-destination                sets the destination app(in words) for the daily updates; we provide two options     
                                 telegram or email; user can choose either one. enter 'email_update' for email or 'telegram_update' for telegram.
--set-message-bunch              sets the number of messages to be bunched between an interval.

## Target Applications:

|         Telegram          |         E-mail          |         SMS          |
## Python Packages & Libraries Used

- Request
- time
- Sys
- datetime
- locale (Formatting numbers to the Indian currency system)

## Technologies Used:

- Python 3.8.5
- HTTPS
- Webhooks
- Messaging Platforms Available:
  - Telegram
  - IFTTT App
  - E-mail
  - Android SMS

## API Reference

- [coindesk](https://api.coindesk.com)
- [IFTTT API reference](https://platform.ifttt.com/docs/api_reference)
- [floatrates](http://www.floatrates.com) For converting usd to inr
## Future Scope:

- To make this project more dynamic as in to provide an option to enter phone numbers and email ids from the 
  command line itself rather than setting those values up in the IFTTT applets.
- Expand the Messaging Platforms


## Contribute

bicoin-notifier is built on with Python 3.8.5 and IFTTT service. If you are new to this ,head over to this page
[IFTTT docs and Integration](https://platform.ifttt.com/docs)

## Credits

- https://realpython.com/python-bitcoin-ifttt/
- Stackoverflow
- RealPython