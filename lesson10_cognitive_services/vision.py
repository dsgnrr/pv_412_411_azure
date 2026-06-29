from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

import utils as u

(AZURE_URL, AZURE_KEY, AZURE_REGION) = u.get_creds()

client = ImageAnalysisClient(
    endpoint=AZURE_URL,
    credential=AzureKeyCredential(AZURE_KEY)
)

image_bytes = u.file_to_bytes("assets/london_metro.jpg")

result = client.analyze(
    image_data=image_bytes,
    visual_features=[
        VisualFeatures.PEOPLE,
        VisualFeatures.TAGS
    ]
)

print(result)