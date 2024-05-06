import requests

api_cep_url = 'https://example.api.findcep.com/v1/cep/{cep}.json'
api_cep_removido_url = 'https://example.api.findcep.com/v1/cep/removido/{cep}.json'
headers = {'Referer': 'example.com'}

def validate_cep(field):
    cep = "".join(field.replace("-"," ").split())
    if cep.isdigit() and len(cep) == 8:
        return cep
    raise Exception('CEP "{field}" Format Invalid'.format(field=field))


def findcep(cep):
    cep = validate_cep(cep)
    response = requests.get(api_cep_url.format(cep=cep), headers=headers)
    if response.status_code == 404:
        response = requests.get(api_cep_removido_url.format(cep=cep), headers=headers)
    return response.json()


if __name__ == '__main__':
    print(findcep('01234000'))
    print(findcep('11680000'))
