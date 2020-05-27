#any and all...
###All----returns tue if all elements in itterable are truthy or if the iterable is empty
people = ["Charle","Cain","Caren","Carregy"]
all([name[0] =='C'for name in people])



import sys
# A simple comparison of size (in Bytes)
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")


#sorted an inbuilt function that returns a new sorted list in the iterable

users = [
	{"username": "sam", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "kate", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "sly", "tweets": [], "num": 10, "color": "teal"},
	{"username": "josh", "tweets": ["cat are the best", "I'm hungry"]},
	{"username": "guinie", "tweets": []}
]
 #####To sort users by their username####
username =sorted(users,key=lambda user: user['username'])
print(username)

# Finding our most active users...
# Sort users by number of tweets, descending
tweets = sorted(users,key=lambda user: len(user["tweets"]), reverse=True)
print(tweets)


##another example###
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "rudimental", "playcount": 6},
	{"title": "ohangla", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
playcount = sorted(songs, key=lambda s: (s['playcount']),reverse=True)
print(playcount)