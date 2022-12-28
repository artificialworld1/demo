from vosk import Model, KaldiRecognizer
import pyttsx3
import pyaudio

model = Model(r"C:\\Users\\asmit\\PycharmProjects\\happy1\\vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model, 16000)
cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
a = 0

def command():

   print("")
   print("Listening...")
   print("")

   while True:

       data = stream.read(4000, exception_on_overflow=False)
       remember = open("C:\\Users\\asmit\\PycharmProjects\\happy1\\remember.txt", "r")
       if recognizer.AcceptWaveform(data):
           text = recognizer.Result()
           p = text[14:-3]
           print(remember.read() + ' said : ' + p)
           if len(p) > 0:
              return p


           else:
             pass


APRIL = pyttsx3.init('sapi5')
voice = APRIL.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_EvaM'
rate = APRIL.getProperty('rate')
APRIL.setProperty('rate', 180)
voices = APRIL.getProperty('voices')
APRIL.setProperty('voice', assistant_voice_id)


def speak(audio):
    print('APRIL: ' + audio)
    APRIL.say(audio)
    APRIL.runAndWait()







def asmit():
    while True:

        query = command()

        if "hi" in query:
            speak("hi")
        elif "hello" in query:
            speak("hello")
        else:
            speak("noo")


asmit()