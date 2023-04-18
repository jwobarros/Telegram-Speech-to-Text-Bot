# Telegram Speech to Text Bot

This Telegram bot uses the `pytelegrambotapi` and `speech_recognition` libraries to convert voice messages sent to it into text.

## Setup

To use this bot, you'll need to create a Telegram bot and obtain its API token. You can follow the [official instructions](https://core.telegram.org/bots#creating-a-new-bot) to create a new bot and get its token.

Add the following env variable to run your telegram bot. `TELEGRAM_API_KEY=<your-API-token>`

Next, you'll need to install the required libraries. You can do this using pip:

```
pip install pytelegrambotapi
pip install SpeechRecognition
```

## Usage

To start the bot, simply run the `main.py` script:

```
python main.py
```

The bot will then listen for voice messages sent to it. When a voice message is received, the bot will convert it to text using the `speech_recognition` library and send the result back to the user.

## Customization

You can customize the behavior of the bot by modifying the `main.py` script. For example, you can change the message sent to users when they start the bot or customize the behavior of the `speech_recognition` library.

## Limitations

The `speech_recognition` library relies on an internet connection to use Google's speech recognition service. If you have poor internet connectivity, the bot may not be able to perform speech-to-text conversion accurately.
