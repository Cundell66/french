import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

load_dotenv()
API_KEY = os.getenv("DG_API_KEY")



def text2speech(text):
    SPEAK_OPTIONS = {"text": text}
    try:
        # STEP 1: Create a Deepgram client using the API key from environment variables
        deepgram = DeepgramClient(api_key=API_KEY)

        # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
        options = SpeakOptions(
            model="aura-asteria-fr",
            encoding="linear16",
            container="wav"
        )
        filename = "output.wav"

        # STEP 3: Call the save method on the speak property
        deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    text2speech("this is a test")