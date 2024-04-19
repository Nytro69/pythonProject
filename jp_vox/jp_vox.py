import dotenv
import os
import sys
import deepl
import urllib.parse
import requests
import pathlib
import hashlib
import pygame

def speak_jp(sentance):
    dotenv.load_dotenv()

    voicevox_key = os.getenv('VOICEVOX_KEY')
    deepl_key = os.getenv("DEEPL_KEY")

    translator = deepl.Translator(deepl_key)

    result = translator.translate_text(sentance, target_lang="JA").text

    print(result)

    url = "https://deprecatedapis.tts.quest/v2/voicevox"

    settings = urllib.parse.urlencode({
        "text": result,
        "speaker": 13, # male: 13 female: 66, 20, 55, 73
        "emotion": 0,
        "pitch": 0,
        "intonationScale": 1,
        "speedScale": 1,
        "key": voicevox_key
    })

    request = requests.post(f"{url}/audio/?{settings}")
    if request.status_code == 200:

        output_filename = f"voicevox_output_{hashlib.sha256(result.encode()).hexdigest()}.wav"
        output_path = pathlib.Path(output_filename)
        with output_path.open("wb") as f:
            f.write(request.content)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(output_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass

        pygame.quit()

    else:
        sys.exit(f"bad request: {request.status_code}")

if __name__ == "__main__":
    speak_jp(input("Text: "))