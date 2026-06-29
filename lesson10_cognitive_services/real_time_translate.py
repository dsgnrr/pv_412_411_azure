import azure.cognitiveservices.speech as speechsdk
import utils as u

(AZURE_URL, AZURE_KEY, AZURE_REGION) = u.get_creds()

speech_config = speechsdk.translation.SpeechTranslationConfig(
    subscription=AZURE_KEY,
    region=AZURE_REGION,
)

speech_config.add_target_language("en-US")
speech_config.speech_recognition_language = 'uk-UA'

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
recognizer = speechsdk.translation.TranslationRecognizer(
    translation_config=speech_config,
    audio_config=audio_config
)

result = recognizer.recognize_once()

print("Translation", result)