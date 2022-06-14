#Define the function to accept one parameter for our list of numbers
#Determine if the length of the list is even or odd
#If the length is even, then return the average of the middle two numbers
#If the length is odd, then return the middle number

#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum/2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
