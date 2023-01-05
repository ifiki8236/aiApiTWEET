import tweepy
import time

client_key = '8rcak09Aqc9SFiurv69k8D1rA'
client_secret = '8MINcHVXndueeXRcVHRykqdcI1RVfLwX4A5iydklMaTJSACHkW'
access_token = '1594705005264633857-tLbLjeoYxYh9SNAUPWJnrdqVDoH1c1'
access_token_secret = 'ofJYfnPXEJXnTWna24X1D66L921B7LvKSSh7wWY5CPIo5'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(client_key, client_secret, access_token,
                     access_token_secret)
api = tweepy.API(auth)

# Tweet every 1 minute
while True:
  api.update_status("This is another tweet to test my API once again.")
  time.sleep(600)  # Sleep for 1 minute
  print(auth)
