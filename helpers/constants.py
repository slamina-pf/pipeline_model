from dotenv import load_dotenv
import os
load_dotenv()


API_KEY = os.getenv('API_KEY')
SECRET = os.getenv('SECRET')

TEMP_DATA_GENERAL_PATH = "./shared/temp_data" 