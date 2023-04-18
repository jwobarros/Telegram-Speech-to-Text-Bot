import os
import telebot
from audio import audio_to_text


# Initialize your bot using the token provided by BotFather
APY_KEY = os.getenv("PERSONAL_TELEGRAM_BOT")
bot = telebot.TeleBot(APY_KEY)


# Handler function for audio messages
@bot.message_handler(content_types=["voice"])
def handle_audio(message):
    # Download the audio file sent by the user
    file_info = bot.get_file(message.voice.file_id)
    audio_file = bot.download_file(file_info.file_path)

    # Converting speech to text
    audio_text = audio_to_text(audio_file)

    # Reply to the user based on the action.
    bot.reply_to(message, f"{audio_text}")


if __name__ == "__main__":
    # Start the bot
    bot.polling()
