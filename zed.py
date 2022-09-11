from libraryArsein.Arsein import Robot_Rubika
from colorama import Fore
from time import  sleep as S
from os import system
import time
for x in range(11):
    for i in ("⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"):
        S(0.1)
        if x == 10:
            print('',end='')
            time.sleep(0.2)
            system("clear")
            break
        else:
            print(Fore.CYAN+'   LOADiNG',Fore.YELLOW+'ZeD LiNK',Fore.MAGENTA+'[',Fore.GREEN+i,Fore.MAGENTA+']',end='\r')
bot = Robot_Rubika("pqpkwjcspxjxrxpktigehwxuyqlvyrmk")
target= "g0B3rim0c23c1b00ad5dd2ec17627e1e"


answer = []

def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me"]
	for i in links:
		if i in msg:
			return True

while (1):
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		v =  bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]

		while(5):
			try:
				x = bot.getMessages(target,v)
				break
			except:continue

		for pay in x:
			try:
				if pay['type'] == 'Text' and not pay['message_id'] in answer:
					print("messages:" + "  " + pay['text'])
					if hasAds(pay.get("text")) and not pay.get("author_object_guid") in admins:
						bot.deleteMessages(target, [pay.get("message_id")])
						print("link pak shod")
					else:pass
				else:
					if "forwarded_from" in pay.keys() and bot.getMessagesInfo(target, [pay.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not pay.get("author_object_guid") in admins:
						bot.deleteMessages(target, [pay.get("message_id")])
						print("forward pak shod")
					else:pass
			except:pass
			answer.append(pay['message_id'])
		else:pass
	except:pass