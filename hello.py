print("Viv")
print(1/3)
print(2**3)
print(10 % 3)
print(6//7)
print(10//3)


###max returns the largest number in the iterable and min returns the smallest value
names =["kim","donata","derrick","easter","parankimalil"]

# finds the minimum length of a name in names
min(names, key=lambda n:len(n))
print(names)


# find the longest name itself
max(names, key=lambda n:len(n))
print(names)

songs = [
	{"title": "rudimental", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "otile", "playcount": 99},
	{"title": "diamond", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) 
print(songs)
# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title']
print(songs)



#lass SpecialList:
 
    #def __init__(self, data):
       # self.__data = data
 
    #def __len__(self):  
        ##return 50


#l1 = SpecialList([1,40,30,100,30,1,2,3,4])
#l2 = SpecialList([1,3,4,5]) 

#print(len(l1)) 
#print(len(l2)) 
