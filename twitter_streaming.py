from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2596736233-IzFD20PyKkprVnsa1G5eQ2dcoxrHpXivj6jfa6z"
access_token_secret = "C1pB7GdE8xTfS6WgJIKcipMdGu2gsseKOzxKW4skcXt4g"
consumer_key = "3Ci8ZN0XiDLYF3pAB0QnQj6jc"
consumer_secret = "wUNAYHHUFXxFVhtfqhmV1HRuOqmcu4CaiOr6sWiILNM6tDN2EF"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['MSG', 'Warrior Lion Heart'])
