import urllib.request
import urllib.parse
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
data =  {
  "input_data": {"example_key": "example_value"},
  "params": {"example_param_key": "example_param_value"}
}

body = str.encode(json.dumps(data))

url = 'https://starlight-retail.eastus.inference.ml.azure.com/score'
api_key = '2xgKaRLTNCrnDiRC6fNrdar2xZRmlLfm'  # your API key

headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)