import os
import mimetypes

from azure.storage.blob import BlobServiceClient, ContentSettings
from dotenv import load_dotenv

load_dotenv()

account_key = os.getenv('AZURE_STORAGE_KEY')
account_url = os.getenv('ACCOUNT_URL')
container_name = 'my-site'


def upload_file(file_path:str, blob_name:str):
    try:
       client = BlobServiceClient('',account_key)
       
       container_client = client.get_blob_client(container=container_name, blob=blob_name)
       """
       text/plain
       text/html
       application/json
       application/
       
       """
       
       mime = mimetypes.guess_type(file_path)
       print(mime)
       content_options = ContentSettings(content_type=mime or "application/octet-stream")
       
       with open(file_path, 'rb') as data:
           container_client.upload_blob(data, overwrite=True, content_settings=content_options)
        
       return container_client.url;
           

    except Exception as ex:
        print("Error uploading file: ", ex)
        
url = upload_file('LOCAL_FILE_PATH', 'STORAGE_FILE_PATH')
print(url)