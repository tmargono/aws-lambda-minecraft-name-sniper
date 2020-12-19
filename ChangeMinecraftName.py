import urllib3

def lambda_handler(event, context):
    https = urllib3.PoolManager()
    wantedName = event.get(wantedName)
    token = event.get(token)
    r = https.request('PUT', f'https://api.minecraftservices.com/minecraft/profile/name/{wantedName}', fields={'Authorization': f'Bearer {token}'})
    print(r.status)
