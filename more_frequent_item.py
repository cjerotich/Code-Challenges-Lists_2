#Define the function to accept three parameters:
#the list, the first item, and the second item
#Count the number of times item1 shows up in our list
#Count the number of times item2 shows up in our list
#If item1 shows up more, return item1. Otherwise, return item2

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
