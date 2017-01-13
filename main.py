import tweepy, time, sys, WikiScraper, FactGenerator, keys

api = keys.api

for i in range(6):
	try:
		line = FactGenerator.create_fact()
		print('*'*20)
		print(time.strftime("%D %H:%M%PM"))
		print('Tweeting:')
		print(line)
		api.update_status(line)
		time.sleep(900)
	except:
		print("Bad UTF-8 and ASCII encoding")