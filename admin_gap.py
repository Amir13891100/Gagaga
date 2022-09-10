from rubpy import Rubika
import asyncio

async def checkAd(text : str) -> bool:
	links : list = ['@' , 'post' , 'join' , 'rubika.ir/','http://','https://','.ir','.com','.org','.net','me']
	for link in links:
		if link in text.lower():
			return 1

async def deleteMessage(bot , group_guid : str , message_id : str , user_guid : str) -> dict:
	while 1:
		try:
			group_admins : list = [i['member_guid'] for i in await bot.getGroupAdmins(group_guid)]
			if user_guid in group_admins:
				break
			else:
				await bot.deleteMessages(group_guid , [message_id])
				break
		except:
			continue

async def lookGroup(bot , group_guid : str, message_id : str , user_guid : str) -> dict:
	while 1:
		try:
			group_admins : list = [i['member_guid'] for i in await bot.getGroupAdmins(group_guid)]
			if user_guid in group_admins:
				await bot.setMembersAccess(group_guid , [])
				await bot.sendMessage(group_guid , "**گروه قفل شد.**" , message_id = message_id)
				break
		except:
			continue

async def openGroup(bot , group_guid : str, message_id : str , user_guid : str) -> dict:
	while 1:
		try:
			group_admins : list = [i['member_guid'] for i in await bot.getGroupAdmins(group_guid)]
			if user_guid in group_admins:
				await bot.setMembersAccess(group_guid , ['SendMessages'])
				await bot.sendMessage(group_guid , "**گروه باز شد.**" , message_id = message_id)
				break
		except:
			continue

async def get_robot(bot , group_guid : str , message_id : str , user_guid : str) -> dict:
	while 1:
		try:
			username : dict = await bot.getUserInfo(user_guid)
			username : str = username['user']['first_name']
			await bot.sendMessage(group_guid , f"بفـــرما **{username}** عزیـــزم 😊🌹" , message_id = message_id)
			break
		except:
			continue

bot = Rubika("hnljwjxzuzbsfkcluzdwibnvgiqtrnxj")
group_guid : str = ("g0BVJoi06260895c103168675b325467")
answered : list = []
try:
	open('answered.txt' , 'r').read()
except FileNotFoundError:
	open('answered.txt' , 'w+').write('CreatedByShayan...')

async def main():
	while 1:
		try:
			last_message_id : str = await bot.getGroupLastMessageId(group_guid)
			messages : list = await bot.getMessagesInterval(group_guid , last_message_id)
			for msg in messages:
				if msg['type'] == 'Text' and not msg['message_id'] in open('answered.txt' , 'r').read():
					text : str = msg['text']
					if await checkAd(text):
						await deleteMessage(bot , group_guid , msg['message_id'] , msg['author_object_guid'])

					elif text == 'قفل گروه':
						await lookGroup(bot , group_guid , msg['message_id'] , msg['author_object_guid'])

					elif text == 'بازکردن گروه' or text == 'باز کردن گروه':
						await openGroup(bot , group_guid , msg['message_id'] , msg['author_object_guid'])

					elif text == 'ربات' or text == 'بات':
						await get_robot(bot , group_guid , msg['message_id'] , msg['author_object_guid'])

					elif 'forwarded_from' in msg.keys():
						await deleteMessage(bot , group_guid , msg['message_id'] , msg['author_object_guid'])

					open('answered.txt' , 'a+').write('\n' + msg['message_id'])
		except:
			...

loop = asyncio.new_event_loop()
asyncio.run(main())
asyncio.set_event_loop(loop)
from rubika.client import Bot

#شناسه اکانت
bot = Bot("hnljwjxzuzbsfkcluzdwibnvgiqtrnxj")
#......
#شناسه گروه
target = "g0Be5VF07c80ba9dc22b2e195e235456"
#......


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

		while(1):
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
						print("links pak shodand")
					else:pass
				else:
					if "forwarded_from" in pay.keys() and bot.getMessagesInfo(target, [pay.get("message_id")])[0]["forwarded_from"]["type_from"] == "Channel" and not pay.get("author_object_guid") in admins:
						bot.deleteMessages(target, [pay.get("message_id")])
						print("forwards pak shodand")
					else:pass
			except:pass
			answer.append(pay['message_id'])
		else:pass
	except:pass