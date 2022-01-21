import requests
import random
import hashlib
import base64
import json
from urllib import parse


clinicKey = "A77X26HFNT5XMJ5MMLASJKEFSGPV5YU5"
clinicId = "30516"
clinicianId = "224560"


def GetRandomString():
    emptystr1 = ""
    random32 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    randomPhrase = random.choices(random32, k = 32)
    str1 = emptystr1.join(randomPhrase)
    return str1

randomString = GetRandomString()

print(randomString)

def GetEncryptedClinicId(randomString, clinicKey):
    phrasePlusClinckey = str.encode(randomString+clinicKey)
    hash = hashlib.sha512(phrasePlusClinckey).digest()
    base64String = base64.b64encode(hash)
    base64String = base64String.decode('UTF-8')
    if base64String[-2:] == "==":
        base64String = base64String.rstrip(base64String[-2])
    encryptedclinicid = randomString + base64String
    return encryptedclinicid


def GetEncryptedUserID(randomString,clinicianId,clinicKey):
    phrasePlusClinckey = str.encode(clinicianId+randomString[:22]+clinicKey)
    hash = hashlib.sha512(phrasePlusClinckey).digest()
    base64String = base64.b64encode(hash)
    base64String = base64String.decode('UTF-8')
    if base64String[-2:] == "==":
        encryptedclinicianid = base64String.rstrip(base64String[-2])
    return encryptedclinicianid



encryptedClinicId = GetEncryptedClinicId(randomString, clinicKey)
encryptedClinicianId = GetEncryptedUserID(randomString, clinicianId, clinicKey)

authCrdentials = base64.b64encode(str.encode(clinicId + ":" + encryptedClinicId))
authCrdentials = authCrdentials.decode('UTF-8')

url = 'https://my.staging.dosespot.com/webapi/token'
headers = {
           'Content-Type': 'application/x-www-form-urlencoded',
           'Authorization': 'Basic ' + authCrdentials,
           }

#URL encode the encrypted userID
encryptedClinicianId = parse.quote(encryptedClinicianId)

payload = 'grant_type=password&Username=' + clinicianId + '&Password=' + encryptedClinicianId

#makes the request to generate an access token
rawToken = requests.post(url, headers=headers, data=payload, timeout=5)
#Places the full bearer token in the token variable

#token = json.loads(rawToken.text)['access_token']
token = rawToken.json()
token = token["access_token"]

