# Telegram Speech to Text Bot

This Telegram bot uses the `pytelegrambotapi` and `speech_recognition` libraries to convert voice messages sent to it into text.

## Setup

To use this bot, you'll need to create a Telegram bot and obtain its API token. You can follow the [official instructions](https://core.telegram.org/bots#creating-a-new-bot) to create a new bot and get its token.

Add the following env variable to run your telegram bot. `TELEGRAM_API_KEY=<your-API-token>`

Next, you'll need to install the required libraries. You can do this using pip:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install pytelegrambotapi
pip install SpeechRecognition
</code></div></div></pre>

## Usage

To start the bot, simply run the `main.py` script:

<pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">python main.py
</code></div></div></pre>

The bot will then listen for voice messages sent to it. When a voice message is received, the bot will convert it to text using the `speech_recognition` library and send the result back to the user.

## Customization

You can customize the behavior of the bot by modifying the `main.py` script. For example, you can change the message sent to users when they start the bot or customize the behavior of the `speech_recognition` library.

## Limitations

The `speech_recognition` library relies on an internet connection to use Google's speech recognition service. If you have poor internet connectivity, the bot may not be able to perform speech-to-text conversion accurately.
