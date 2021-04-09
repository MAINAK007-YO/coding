from gtts import gTTS
from playsound import playsound
def play_audio(play_audio):
    playsound(play_audio)
def convert_to_audio(text):
    my_audio=gTTS(text)
    my_audio.save('hello.mp3')
    play_audio('hello.mp3')

convert_to_audio("hey mainak now this is the time to take a physical exercise break. prepare yourself for the beast mode!! unstopable!!!")