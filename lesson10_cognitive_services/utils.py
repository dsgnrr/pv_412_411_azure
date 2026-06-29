from dotenv import load_dotenv
import os

load_dotenv()

def get_creds():
    AZURE_URL = os.getenv('AZURE_URL')
    AZURE_KEY = os.getenv('AZURE_KEY')
    AZURE_REGION = os.getenv('AZURE_REGION')
    
    return(AZURE_URL, AZURE_KEY, AZURE_REGION)
    

def file_to_bytes(path:str)->bytes:
    try:
        with open(path, 'rb') as file:
            file_bytes = file.read()
            return file_bytes
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print("Unepxected error: ", e)
        return None