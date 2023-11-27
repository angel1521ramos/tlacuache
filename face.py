# import requests module
import requests

# Making a get request
response = requests.get('https://www.facebook.com/permalink.php?story_fbid=122105530226123078&id=61553692342844&ref=embed_post')

# print response
print(response)

# print json content
print(response.json())
