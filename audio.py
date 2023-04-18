import speech_recognition as sr
import os, subprocess


LANG = os.getenv("LOCALE_LANG")


def remove_audio_files():
    if os.path.exists("temp/audio.ogg"):
        os.remove("temp/audio.ogg")
    if os.path.exists("temp/audio.wav"):
        os.remove("temp/audio.wav")


def audio_to_text(audio_data):
    with open("temp/audio.ogg", "wb") as file:
        file.write(audio_data)

    # Converting to WAV
    process = subprocess.run(["ffmpeg", "-i", "temp/audio.ogg", "temp/audio.wav"])
    if process.returncode != 0:
        raise Exception("Something went wrong")

    with sr.AudioFile("temp/audio.wav") as source:
        r = sr.Recognizer()
        audio = r.record(source)
        try:
            # Convert the audio file to text using Google Cloud Speech API
            # Write the heard text to a text variable
            audio_text = r.recognize_google(audio, language=LANG)
            response = audio_text
        except:
            response = "Words not recognized. Please, try again!"

    # Removing files after convertion to text
    remove_audio_files()
    return response
