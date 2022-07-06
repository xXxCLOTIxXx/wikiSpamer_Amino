from os import system as s
from threading import Thread
try:import AminoXZ
except:s("pip install AminoXZ");import AminoXZ
try:from colored import fore
except:s("pip install colored");from colored import fore
client = AminoXZ.Client()
s("cls")
print(fore.MEDIUM_PURPLE_4, """

░██╗░░░░░░░██╗██╗██╗░░██╗██╗  ░██████╗██████╗░░█████╗░███╗░░░███╗███████╗██████╗░
░██║░░██╗░░██║██║██║░██╔╝██║  ██╔════╝██╔══██╗██╔══██╗████╗░████║██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████═╝░██║  ╚█████╗░██████╔╝███████║██╔████╔██║█████╗░░██████╔╝
░░████╔═████║░██║██╔═██╗░██║  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░╚██╗██║  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝

	Made by Xsarz (@DXsarz)
	GitHub: https://github.com/xXxCLOTIxXx
	Telegram channel: https://t.me/DxsarzUnion
	YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q

	""", fore.GREY_63)
while True:
	try:client.login(email=input("Input email>> "), password=input("Input password>> ")); print(fore.GREEN, "Successful login\n", fore.GREY_63);break
	except Exception as error:print(fore.RED, f"Fail login:\n{error}\n", fore.GREY_63)

while True:
	title = input("Input post title>> ")
	content = input("Input post text>> ")
	if title == '' or content == '':print(fore.RED, "\nPlease enter correct details\n", fore.GREY_63)
	else:break

while True:
	try:comId = client.get_from_link(input("Input community link>> "))['extensions']['community']['ndcId'];break
	except Exception as error:print(fore.RED, f"Fail:\n{error}\n", fore.GREY_63)

try:client.join_community(comId=comId)
except:print(fore.RED, f"Fail join community:\n{error}\n", fore.GREY_63)

def spam():
	while True:
		try:client.post_wiki(comId=comId, title=title, content=content); print(fore.GREEN, "\nPost created\n", fore.GREY_63)
		except:print(fore.RED, "\nFailed to create post\n", fore.GREY_63)
for _ in range(100):
	Thread(target=spam).start()