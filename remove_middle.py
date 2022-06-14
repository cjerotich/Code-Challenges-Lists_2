#Define the function to accept three parameters:
#the list, the starting index, and the ending index
#Get all elements before the starting index
#Get all elements after the ending index
#Combine the two partial lists into the result
#Return the result

#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
