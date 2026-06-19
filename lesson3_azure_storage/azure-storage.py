import os
import mimetypes
from datetime import datetime, timedelta, timezone
from azure.storage.blob import BlobServiceClient, ContentSettings, generate_blob_sas, BlobSasPermissions
from dotenv import load_dotenv

load_dotenv()

account_key = os.getenv('AZURE_STORAGE_KEY')
account_url = os.getenv('ACCOUNT_URL')
container_name = 'my-site'


def upload_file(file_path:str, blob_name:str):
    try:
       client = BlobServiceClient(account_url,account_key)
       
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

def download_file(blob_name: str, download_path:str, version_id:str=None):
    client = BlobServiceClient(account_url, account_key)
    container_client = None
    if version_id is None:
        container_client = client.get_blob_client(container=container_name, blob=blob_name)  
    else: container_client = client.get_blob_client(container=container_name, blob=blob_name, version_id=version_id)
    
    with open(download_path, 'wb') as file:
        download_stream = container_client.download_blob()
        file.write(download_stream.readall())

def list_of_versions(blob_name:str):
    client = BlobServiceClient(account_url, account_key)
    container_client = client.get_container_client(container_name)
    
    blobs = container_client.list_blobs(blob_name, include="versions")
    for blob in blobs:
        print("Version-ID: ", blob.version_id)
        print("Is current version: ", blob.is_current_version)
        print("Modified date: ", blob.last_modified)
        print('\n')

def restore_blob_version(blob_name:str, version_id:str):
    client = BlobServiceClient(account_url, account_key)
    
    target_blob = client.get_blob_client(container=container_name, blob=blob_name)
    print("target blob url: ", target_blob.url)
    source = client.get_blob_client(container=container_name, blob=blob_name, version_id=version_id)
    print("source blob url: ", source.url)
    target_blob.start_copy_from_url(source.url)

def get_sas_url(blob_name:str):
    client = BlobServiceClient(account_url, account_key)
    container_client = client.get_blob_client(container_name,blob_name)
    
    sas_token = generate_blob_sas(
        account_name=client.account_name,
        container_name=container_name,
        blob_name=blob_name,
        account_key=account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.now(timezone.utc) + timedelta(minutes=30)
    )
    
    return f"{container_client.url}?{sas_token}"

# list_of_versions("azure-storage.py")

# url = upload_file('C:\\Users\\dsgnrr\\Desktop\\pv_412_411_azure\\azure-storage.py', 'code.py')
# print(url)

# download_file('azure-storage.py','C:\\Users\\dsgnrr\\Desktop\\pv_412_411_azure\\code-old.py', version_id='2026-06-15T15:16:47.1209006Z')

# restore_blob_version("azure-storage.py", '2026-06-15T15:16:47.1209006Z')

print(get_sas_url('code.py'))
