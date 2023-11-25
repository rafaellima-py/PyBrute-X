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

