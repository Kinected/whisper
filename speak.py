from pydub import AudioSegment
from pydub.playback import play
import io
import os

# file_path = os.path.join(os.getcwd(), "speech.mp3")

file_path = "E:/Kinected/whisper/speech.mp3"

if file_path is None:
    print("Le fichier audio est introuvable.")
    exit(1)

# Chargez le fichier audio
audio_segment = AudioSegment.from_mp3(file_path)

# Lisez le fichier audio
play(audio_segment)