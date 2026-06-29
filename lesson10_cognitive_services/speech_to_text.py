import azure.cognitiveservices.speech as speechsdk
import utils as u

(AZURE_URL, AZURE_KEY, AZURE_REGION) = u.get_creds()

speech_config = speechsdk.SpeechConfig(
    subscription=AZURE_KEY,
    region=AZURE_REGION,
    speech_recognition_language="uk-UA",
)

speech_config.speech_synthesis_language = 'en-US'

recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
result = recognizer.recognize_once()

print("text: ", result.text)