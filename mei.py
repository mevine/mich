###using fiters...................####
users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "ariana", "tweets":["i love mum","i love dad","hellow world"]},
    {"username": "cara", "tweets":["hellow world"]},
    {"username": "ana","tweets":[]},
    {"username": "mariana","tweets":[]},
    {"username": "lariana","tweets":["i love dad","hellow world"]},
    {"username": "pariana","tweets":["i love mum","i love dad",]},
    {"username": "riana","tweets":[]}, 

    ]
########extract inactive users using filter#####  
inactive_users = list(filter(lambda u: not u['tweets'], users))  
print(inactive_users)

# extract usernames of inactive users w/ map and filter:
#map is a functions that accepts two arguments,a function and iterrable----something we iterrate like lists,dictionaries,tuples###
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))
print(usernames)    

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]
print(inactive_users2)

# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]
print(usernames2)