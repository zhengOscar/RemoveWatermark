

import requests
 

def get_redirected_url(sub):
    response = requests.get(sub, allow_redirects=True)
    return response.url