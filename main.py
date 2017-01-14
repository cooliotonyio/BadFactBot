import tweepy, time, sys, WikiScraper, FactGenerator, keys

api = keys.api

while True:
	try:
		line = FactGenerator.create_fact()
		print('*'*20)
		print(time.strftime("%D %H:%M%PM"))
		print('Tweeting:')
		print(line)
		api.update_status(line)
		for i in range(7):
			time.sleep(60*60*24)
			print('Days before next tweet:',7-i)
	except:
		print("Bad UTF-8 and ASCII encoding")