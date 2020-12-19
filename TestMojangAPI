import urllib3

def lambda_handler(event, context):
    https = urllib3.PoolManager()
    r = https.request('GET', 'https://status.mojang.com/check')
    print(r.data.decode('utf-8'))
