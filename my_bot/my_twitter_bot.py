import tweepy
import time
 
print("aj")

CONSUMER_KEY='z7CyRlAxkh9LdsGZpEzdSokwt'
CONSUMER_SECRET='Fi0laHSfmkc7GIHQUQxKivawnPdcZRjw73DlmxwSxDkveXtgcC'
ACCESS_KEY='1247316086183297027-fanJnmEUFynZJxRkj762D4KrFcY1di' 
ACCESS_SECRET='wflTzu8N9hPGr2RAKxWV3afmnOdbDE0TF14X2mXtPHSnE'



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth) 
FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return 

def reply_to_tweets():
    print("working")
    last_seen_id=retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id,tweet_mode='extended')
    # 1247329708452216836
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id=mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if "#helloworld" in mention.full_text.lower():
            print ("found")
            print("respo nding back")
            api.update_status("@" +  mention.user.screen_name + " it is a beautifull world", mention.id)
            
while True:
    reply_to_tweets()
    time.sleep(15)
    break
    
