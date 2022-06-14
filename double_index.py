#Define the function to accept two parameters,
#one for the list and another for the index of the value
#we are going to double
#Test if the index is invalid. If its invalid then return the original list
#If the list is valid then get all values up to the index and store it as a new list
#Append the value at the index times 2 to the new list
#Add the rest of the list from the index onto the new list
#Return the new list

#Write your function here
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
