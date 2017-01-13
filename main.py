import tweepy, time, sys, WikiScraper, FactGenerator

CONSUMER_KEY = 'EvDZPTkU4zBpPSSL038mcFVTn'
CONSUMER_SECRET = 'W3xjLHAxRVkKR5YmEpDO9y6MxCZAT901lsF7MjmOMryPxEKqQw'
ACCESS_KEY = '817595515332272129-WWRCfLrCgnq2Ir8LUVmypvfrtUfJfQu'
ACCESS_SECRET = '89QjN1MuAkepiytZ5qhvJpQE88HI5VektSDnmxBFHdlcM'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
 
for i in range(6):
	line = FactGenerator.create_fact()
	print('*'*20)
	print('Tweeting:')
	print(line)
	api.update_status(line)
	time.sleep(600)