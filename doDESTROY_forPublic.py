import requests


def find(r):
    r = r.json()
    print '\nYour droplets and droplet names are: \n'
    droplet = 'droplet'
    divider = '----->'
    result = []
    for i in r['droplets']:
        data = i['id']
        result.append(data)        
    result1 = []
    for x in r['droplets']:
        data = x['name']
        result1.append(data)
    associated = {}
    for i in range(len(result)):
        associated[result[i]] = result1[i]
    for i in associated:
        print droplet, i, divider, associated[i]
    return associated, result1, result

def des_all(list_made, headers):
    list_ = list_made[2]    
    for i in list_[:]:        
        r = requests.delete('https://api.digitalocean.com/v2/droplets/' + str(i), headers=headers)
    if r.status_code == 204:
        print '\n.....DELETED ALL DROPLETS'
    else:
        print r.text

def des_one(list_made, headers):
    list_ = list_made[1]
    list_1 = list_made[2]
    index = range(len(list_))
    for x,y in zip(list_, index):
        print '\nType ' + str(y) + ' to destroy droplet "' + str(x) + '"'
    answer = input('--->')
    answer = str(list_1[answer])    
    r = requests.delete('https://api.digitalocean.com/v2/droplets/' + answer, headers=headers)
    if r.status_code == 204:
        print '\n.....DELETED'
    else:
        print '\n....NOP'

def main():
    api_token = 'XXX'#CHANGE 'XXX' TO YOUR DO API TOKEN, WITH NO QUOTATIONS
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_token
    }
    r = requests.get('https://api.digitalocean.com/v2/droplets', headers=headers)

    find_ = find(r)
    list_made = find_
    ask = raw_input('\nDo you want to delete all or individual droplets?\n [1] ---> all \n [2]---> individual\n')
    if ask == '1':
        des_all(list_made, headers)
    if ask == '2':
        des_one(list_made, headers)
    
    


main()
