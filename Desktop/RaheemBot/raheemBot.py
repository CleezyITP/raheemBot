from twython import Twython

import pprint

APP_KEY='9g5PqPBY0gK8HIJuYAh8bSA85'
APP_SECRET='3Kywza8xk4MAMatT9J1A28lvY0re7jKbOqO4lKYETWKwFcvVIK'
OAUTH_TOKEN='2900707964-ie2XOwxn4QHGQyXi85rvKdhTFCIdNsjHZaerHN9'
OAUTH_TOKEN_SECRET='bWmnDNWieNAtwFaY0QEKx70aomueJ7r6pU8NEMcgHRHrB'

twitter= Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
loveTweets=twitter.search(q='#love')
loveStatuses=loveTweets['statuses']

hateTweets=twitter.search(q='#hate')
hateStatuses=hateTweets['statuses']

# pprint.pprint(loveStatuses[0])
# pprint.pprint(hateStatuses[0])
# print(len(loveStatuses))
# print(len(hateStatuses))

#pythonfolder



for hateStatus in hateStatuses:
	tweet_id= hateStatus['id']
	pprint.pprint(tweet_id)

	text = hateStatus['text']
	user = hateStatus['user']['screen_name']

	print tweet_id, text, user

	twitter.update_status(status=text
		# , in_reply_to_status_id=user
		)

#	if str()