import speech_recognition as sr
from googletrans import Translator
from google_speech import Speech

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
     text = r.recognize_google(audio, language="ru-RU")
except sr.UnknownValueError:
    print("Робот не расслышал фразу")
except sr.RequestError as e:
    print("Ошибка сервиса; {0}".format(e))

print(text)

translator = Translator()

result = translator.translate(text, src = "ru", dest = "zh-cn")

print(result.text)

lang = "zh-cn"
speech = Speech(result.text, lang)
speech.play()
