import requests
import os
import uuid
from dotenv import load_dotenv
from flask import render_template


def tts(text):
    sound_dir = "./sounds"
    for f in os.listdir(sound_dir):
        if f.endswith(".wav"):
          os.remove(os.path.join(sound_dir, f))

    load_dotenv()
    apikey = os.getenv('TTS_API_KEY')
    voice = 'sophie'
    speed = 'slow'
    # text = 'Bonjour, ceci est Python qui parle.'
    url = f'https://api.narakeet.com/text-to-speech/m4a?voice={voice}&speed={speed}'
    options = {
        'headers': {
            'Accept': 'application/octet-stream',
            'Content-Type': 'text/plain',
            'x-api-key': apikey,
        },
        'data': text.encode('utf8')
    }

    unique_id = str(uuid.uuid4())
    filename = f"./sounds/output_{unique_id}.wav"
    try:
        with open(filename, 'wb') as f:
            f.write(requests.post(url, **options).content)
    except Exception as e:
        return render_template("error.html",e=e)    

    return filename
