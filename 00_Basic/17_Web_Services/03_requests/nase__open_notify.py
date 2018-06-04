try:
    import requests
except ImportError:
    from os import system
    system('pip install requests')
    import requests
"""
Purpose: to get the ISS pass time over a particular location on earth
    API ref: http://open-notify.org/Open-Notify-API/ISS-Pass-Times/


REST API 
    METHODS
        - GET 
        - POST
        - PUT
        - DELETE
        
"""

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"lat": 40.71, "lon": -74}

# Make a get request with the parameters.
response = requests.get("http://api.open-notify.org/iss-pass.json", 
                        params=parameters)

# Print the content of the response (the data the server returned)
print(response.content)

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print(response.content)