__author__ = 'ruben'

import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


ckey = YOUR_CONSUMER_KEY_HERE
csecret = YOUR_CONSUMER_SECRET_HERE
atoken = YOUR_TWITTER_APP_TOKEN_HERE
asecret = YOUR_TWITTER_APP_SECRET_HERE

murcia = [-1.157420, 37.951741, -1.081202, 38.029126] #Check it out, is a very nice city!

file =  open('tweets.txt', 'a')

class listener(StreamListener):

    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        try:
            decoded = json.loads(data)
        except Exception as e:
            print e #we don't want the listener to stop
            return True

        if decoded.get('geo') is not None:
            location = decoded.get('geo').get('coordinates')
        else:
            location = '[,]'
        text = decoded['text'].replace('\n',' ')
        user = '@' + decoded.get('user').get('screen_name')
        created = decoded.get('created_at')
        tweet = '%s|%s|%s|s\n' % (user,location,created,text)

        file.write(tweet)
        print tweet
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    print 'Starting'

    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    twitterStream = Stream(auth, listener())
    twitterStream.filter(locations=murcia)