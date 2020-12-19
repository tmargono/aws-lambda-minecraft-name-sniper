import urllib3, time

def lambda_handler(event, context):
    https = urllib3.PoolManager()
    wantedName = event.get('name')
    token = event.get('token')
    delay = event.get('delay')
    
    #Delay for specified seconds because Cloudwatch rule smallest increment of time is minutes
    time.sleep(delay)
    
    #API Request, change name
    r = https.request('PUT', f'https://api.minecraftservices.com/minecraft/profile/name/{wantedName}', fields={'Authorization': f'Bearer {token}'})
    
    #Print Status Code 
    print(r.status)
    
    #Print Result
    print(r.data.decode('utf-8'))
