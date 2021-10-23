import requests

CLIENT_ID = 'yourclientid'
CLIENT_SECRET = 'yourclientsecret'

AUTH_URL = 'https://accounts.spotify.com/authorize?client_id=18e8f7f4ba1c467e9c77afbb34645234&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A8080&scope=playlist-modify-public'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()
print(auth_response_data)
# save the access token
#access_token = auth_response_data['access_token']