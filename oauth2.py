import requests

class oauth(object):
    #To Dsicord
    api_endpoint = 'https://discord.com/api/v6'
    discord_access_token = 'https://discord.com/api/v6/oauth2/token'
    
    
    #Remove or Add your scopes depending on what you set 
    scope = "identify email guilds
    
    # The application information.
    # The applications client_id e.g.'123456789101112131'. client_secret e.g. 'pxS3D8EB6M9zWBUNFpJmge9NcBX95bDK'
    client_id = ''
    client_secret = ''    
    
    # "Redirects" set the redirect URI. e.g. 'http://127.0.0.1:5000/discord/login' 
    redirect_uri = ''
    
    @staticmethod
    def exchange_code(code):
        data = {
            'client_id': oauth.client_id,
            'client_secret': oauth.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': oauth.redirect_uri,
            'scope': oauth.scope
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        exchange_code_requests = requests.post('%s/oauth2/token' % oauth.api_endpoint, data = data, headers = headers)
        exchange_code_requests.raise_for_status()
        return exchange_code_requests.json()
    
        
    @staticmethod
    def get_user_data(access_token):
        uri_user = f"{oauth.api_endpoint}/users/@me"
        uri_guild = f"{oauth.api_endpoint}/users/@me/guilds"

        headers = {
            "Authorization": 'Bearer {}'.format(access_token)
        }

        data_object_user = requests.get(url = uri_user, headers = headers)
        
        # You Need the 'identify email guilds' scopes for this to work:
        data_object_guild = requests.get(url = uri_guild, headers = headers)
        
        class data():
            user = data_object_user
            guild = data_object_guild
            
        # Check to see if your getting json, if not add '.json' to the end.    
        return data

    #If you have a refresh token, pass it here and get new a new token
    @staticmethod
    def refresh_token(refresh_token):
        token_uri = "{oauth.api_endpoint}/oauth2/token"
        
        data = {
            'client_id': oauth.client_id,
            'client_secret': oauth.client_secret,
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'redirect_uri': oauth.redirect_uri,
            'scope': 'identify email guilds'
        }
        
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        refreshed_info = requests.post(token_uri, data = data, headers = headers)
        refreshed_info.raise_for_status()
        
        return refreshed_info.json()

