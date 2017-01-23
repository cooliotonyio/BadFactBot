import tweepy, time, sys, WikiScraper, FactGenerator, keys

api = keys.api

for k in range(100):
	try:
		line = FactGenerator.create_fact()
		print('*'*40)
		print('Tweet number',k+1,'of 100')
		print(time.strftime("%D %H:%M%P"))
		print('Tweeting:')
		print(line)
		api.update_status(line)
		for j in range(24):
			print(24-j,'hours left before tweet #',k+2)
			time.sleep(3600)
	except UnicodeEncodeError:
		print("Bad UTF-8 and ASCII encoding")
		print('Trying again...')