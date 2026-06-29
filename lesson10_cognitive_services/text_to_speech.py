import azure.cognitiveservices.speech as speechsdk
import utils as u

(AZURE_URL, AZURE_KEY, AZURE_REGION) = u.get_creds()

speech_config = speechsdk.SpeechConfig(
    subscription=AZURE_KEY,
    region=AZURE_REGION,
)

speech_config.speech_synthesis_voice_name = 'en-US-GuyNeural'

synthesier = speechsdk.SpeechSynthesizer(
    speech_config=speech_config
)

synthesier.speak_text("Performs synthesis on plain text in a blocking (synchronous) mode.")