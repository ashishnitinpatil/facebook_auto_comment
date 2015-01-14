"""
Author - !mmorta!
Created on - 23:30 IST, Jan 14, 2015
License - BSD New/Simplified
"""

# Using the python library "facebook-sdk"
import facebook
import time
import random

# Get a permanent (60 days) access token through the Graph API Tools
# https://developers.facebook.com/tools/explorer/
# Apparently, temporary tokens (application - Graph API Explorer) didn't work,
# glad that I had an old & unused Facebook app handy
# "Get access token" -> "Extended Permissions" -> "publish_actions" -> approve

oauth_access_token = "This should be a secret"
# authentication
graph = facebook.GraphAPI(oauth_access_token)

##profile = graph.get_object("me")
##friends = graph.get_connections("me", "friends")
##print profile
# fetch the facebook thread (replace post_id with actual numeric id)
comments = graph.get_connections(id='post_id', connection_name='comments')
##print comments

# Googled for a while & was blessed with http://www.coverfire.com/files/quotes.txt
with open("quotes.txt") as quotes_file:
    quotes = [each.replace('\n', ' ').replace('\t', ' ') for each in quotes_file.read().split("\n\n")]

# Introduce a little anarchy...
for i in range(200):
    # get a random quote
    quote = random.choice(quotes)
    # burn the quote so we don't repeat (not a very good solution)
    quotes.remove(quote)
    # post the quote as a comment on the given facebook thread/status
    graph.put_object(parent_object='post_id', connection_name='comments',
                     message=quote)
    # don't abuse resources, take a chill pill
    time.sleep(random.randint(5,20))
    # log to the output window for progress
    print "Post no. " + str(i) + " - " + quote[:15] + "..."
