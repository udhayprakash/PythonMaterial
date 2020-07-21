import requests
 
 
def api():
    response = requests.get('https://www.google.com/')
    return response.status_code