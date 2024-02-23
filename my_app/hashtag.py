# from flask import Flask, request, jsonify
from mastodon import Mastodon, StreamListener
import mastodon
from my_app.createCommentTree import create_tree
from my_app.chatgpt import summarize_text
import asyncio

# Mastodon API configuration
instance = "https://social.cs.swarthmore.edu"
hashtag_to_track = "summarizethis"

f = open("./user_token",'r')
token = f.readlines()[0] 

# Creates an instance of the Masotodon class 
mastodon = Mastodon(
    access_token=token,
    api_base_url=instance
)

# Variable to store comment ID and content 
info = []
# Define the StreamListener class
class StreamListener(StreamListener): 
    def on_update(self, status):
        global info 
        info = []
        # Define what you want to do when a new status is received
        info.append(status.id)
        info.append(status.account['id'])
        info.append(status.created_at)
        m = Mastodon(access_token=token, api_base_url="https://social.cs.swarthmore.edu")
        # m.status_post("Request confirmed", in_reply_to_id = info[0])

        tree = create_tree(info)
        if tree: 
            content = str(asyncio.run(summarize_text(tree)))
            m.status_post("Summary: \n" + content, in_reply_to_id = info[0])

# Creates an instance of custom StreamListener 
listener = StreamListener()

# Start streaming with the custom listener
def getPosts(): 
    mastodon.stream_hashtag(hashtag_to_track, listener, local=False, run_async=True, timeout=300, reconnect_async=False, reconnect_async_wait_sec=5)
    return info 
