import json
import FactGenerator
import keys
import tweepy
import configparser
import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
#OAuth
auth=keys.auth
twitterApi = keys.api
config = configparser.ConfigParser()
config.read('.twitter')
stream_rule = config.get('app', 'rule')
account_screen_name = config.get('app', 'account_screen_name').lower() 
account_user_id = config.get('app', 'account_user_id')


class FactRequest(StreamListener):

	def on_data(self, data):
		tweet = json.loads(data.strip())

		retweeted = tweet.get('retweeted')
		from_self = tweet.get('user',{}).get('id_str','') == account_user_id

		if retweeted is not None and not retweeted and not from_self:
			tweetId = tweet.get('id_str')
			screenName = tweet.get('user',{}).get('screen_name')
			tweetText = tweet.get('text')
			quotation1=tweetText.find('a fact about "')+14
			quotation2=(tweetText[quotation1:].find('"'))+quotation1
			if quotation1 >=14 and quotation1 < quotation2:
				topic = tweetText[quotation1:quotation2]
				print("Request topic is:", topic)
			else:
				topic = 'Bad Chat Bot'
				print('Bad Format; Request topic changed to: Bad Fact Bot')
			def chatResponser(topic):
				chatResponse = FactGenerator.create_fact(topic)
				try:
					return chatResponse
				except:
					return chatResponser(topic)
			chatResponse=chatResponser(topic)
			replyText = '@' + screenName + ' ' + chatResponse
			try:
				#check if repsonse is over 140 char
				if len(replyText) > 140:
				    replyText = replyText[0:139] + '…'
				print("*"*50)
				print('Tweet ID: ' + tweetId)
				print('From: ' + screenName)
				print("Timestamp:",time.strftime("%D %H:%M%P"))
				print('Tweet Text: ' + tweetText)
				print("*"*50)
				print('Reply Text: ' + replyText[0:139])
			except:
				print('Something went wrong with encoding print messages')
			print("*"*50)
			print("Waiting for next fact request...")

			# If rate limited, the status posts should be queued up and sent on an interval
			twitterApi.update_status(status=replyText, in_reply_to_status_id=tweetId)

if __name__ == '__main__':
    streamListener = FactRequest()
    twitterStream = Stream(auth, streamListener)
    twitterStream.userstream(_with='user')