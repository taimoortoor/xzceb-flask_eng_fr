"""Initiation of translator instance and definition of translator methods"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_To_French(englishText):
    """Function for converting english text to french"""
    data = language_translator.translate(text=englishText, model_id='en-fr')
    translation = data.get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def french_To_English(frenchText):
    """Function for converting english text to french"""
    data = language_translator.translate(text=frenchText, model_id='fr-en')
    translation = data.get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
