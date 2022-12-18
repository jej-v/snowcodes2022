# snowcodes2022
This is my Discord Bot submission for Snowcodes 2022.

jej-mas is a general purpose bot, features a variety of fun and interactive commands to keep you and your friends hopefully entertained while maintaining the Xmas holiday spirit!

## List of Commands

![image](https://user-images.githubusercontent.com/64602039/208318957-7a0bd77a-e718-4338-b26e-6e66a9dc9f1e.png)

# List of APIs used:

1. [TheCatAPI](https://thecatapi.com/)
2. [HTTPCat](https://http.cat/)
3. [The Bored API](https://www.boredapi.com/)
4. ~[Jikan API (4.0.0)](https://docs.api.jikan.moe/)~
4. [MyAnimeList API (beta ver)](https://myanimelist.net/apiconfig/references/api/v2#section/Versioning)
5. [Inspiro Bot API](https://inspirobot.me/)
6. [AdviceSlip API](https://api.adviceslip.com/)
7. [Giphy API](https://developers.giphy.com/)

# Requirements

## Python 3.8 or higher is required.

Install Python on https://www.python.org/.

**Get all the needed modules from requirements.txt**

```bash
# Linux/macOS/Windows
$ pip install -r requirements.txt
```

## 1. Your bot's discord token

If you're having trouble finding it, or don't know how to. Follow this [tutorial](https://www.writebots.com/discord-bot-token/).

## 2. Giphy API Key 
Can be obtained from https://developers.giphy.com/

## 3. MyAnimeList API Key
Can be obtained from https://myanimelist.net/apiconfig

# Bot Setup
```bash
$ git clone https://github.com/jej-v/snowcodes2022
$ cd snowcodes2022
```
Add your Bot Token and Giphy Api Token to the `config.py` file.
```python
token = 'bot_token_here'
mal_api_key = 'mal_client_id_here'
giphy_api_key = 'giphy_api_token_here'
```
Run the bot
```bash
$ python3 main.py
```

# Troubleshooting
`ImportError: cannot import name 'commands' from 'discord.ext' (unknown location)`

`AttributeError: __aexit__` / `AttributeError: __aenter__`

Uninstall discord.py
```bash
$ python3 -m pip uninstall discord.py discord -y
```

Uninstall py-cord
```bash
$ python3 -m pip uninstall py-cord
```

Install and Update py-cord
```bash
$ python3 pip install -U py-cord 
```

Note: this repository currently uses py-cord version `2.3.2`

In case you have `pycord` installed by chance: 
```bash
$ python3 -m pip uninstall pycord
```


# Sides Notes
There are quite a few Honkai Impact 3rd references, such as the `/yatta` command and Honkai stickers from Hoyoblab set as thumbnails in some of the commands. Even the profile picture itself! Personally, I think they were a nice addition, lol.
