import json
import requests
import hashlib

request = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=d057816a07d0118ec4335d2ae94c360f85899cd7')
response = request.json()
archive = open('answer.json', "w")
json.dump(response, archive)
archive.close()
cifrado = response['cifrado']

s = ''

for c in cifrado: 
    if chr(ord(c)).isidentifier():
        if (ord(c) - response['numero_casas']) < 97:
            s += chr(ord(c) - response['numero_casas'] + 26)        
        else:
            s += chr(ord(c) - response['numero_casas'])
    else:
        s += chr(ord(c))

dados = {
    'numero_casas': response['numero_casas'],
    'token': response['token'],
    'cifrado': response['cifrado'],
    'decifrado': s,
    'resumo_criptografico': hashlib.sha1(s.encode()).hexdigest()
}

archive = open('answer.json', "w")
json.dump(dados, archive)

archive.close()

url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=d057816a07d0118ec4335d2ae94c360f85899cd7'

files = {'answer': open('answer.json', 'rb')}
r = requests.post(url, files=files)
print(r.status_code)
print('----'*10)
print(r.headers)
print('----'*10)
print(r.content)
r.text
