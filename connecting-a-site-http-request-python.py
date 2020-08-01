#site está acessível > input

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está acessível no mommento. 🌠💭')
else:
    print('O site está conectado! ⌨💻️')
    print(site.read())

    

#output     
C:\Users\Deltah\PycharmProjects\pythonteste.py\venv\Scripts\python.exe C:/Users/Deltah/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/scratch_15.py
O site está conectado! ⌨💻️

C:\Users\Deltah\PycharmProjects\pythonteste.py\venv\Scripts\python.exe C:/Users/Deltah/AppData/Roaming/JetBrains/PyCharmCE2020.1/scratches/scratch_15.py
O site está conectado! ⌨💻️
b'<all site resumed here!>'b

Process finished with exit code 0

#Banz\inGa! LuxSoftware 
#Bug Bounty API's Specialist



