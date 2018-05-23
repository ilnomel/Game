import random

"""
1.
function called min3
take 3 numbers as parameters and return the smallest value
if more than one number tied for smallest, still return the smallest number
us a proper if/elif/else chain
"""

#def min3 (num1, num2, num3):
    #if num1 < num3 and num3:
        #return num1
    #if num3 < num1 and num2:
        #return num3
    #if num2 < num1 and num3:
        #return num2
    #if num1 == num2 == num3 or num1 == num2 or num1 == num3:
        #return num1
    #if num2 == num3:
        #return num2
    
#print(min3(4, 7, 5))
#print(min3(4, 5, 5))
#print(min3(4, 4, 4))
#print(min3(-2, -6, -100))
#print(min3("Z", "B", "A"))

"""
2.
function called box
will output boxes given a height and width
"""

#def box(height, width):
    #for row in range(height):
        #for column in range(width):
            #print("*", end=" ")
        #print()

#box(7,5)  # Print a box 7 high, 5 across
#print()   # Blank line
#box(3,2)  # Print a box 3 high, 2 across
#print()   # Blank line
#box(3,10) # Print a box 3 high, 10 across

"""
3.
function called find
will take a list of numbers, my_list, along with on other number, key
have it search the list for the value contained in key
each time function finds the key value, print the array position of the key
"""

#def find(my_list, key):
    #for i in range(len(my_list)):
        #if my_list[i] == key:
            #print("Found %d at position %d" %(key, i))
            
#my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
#find(my_list, 12)
#find(my_list, 91)
#find(my_list, 80)

"""
4.
- function called create_list
- takes in a list size and returns a list of random numbers from 1-6

- function called count_list
- takes in a list and a number
- the function return the number of times the specified number appears in the list

- funciton called average_list
- returns the average of the list passed into it
"""

def create_list(list_size):
    random_list = []
    for i in range(list_size):
        random_list.append(random.randrange(1,7))
    return random_list

#my_list = create_list(5)
#print(my_list)

def count_list(the_list, number):
    counting = 0
    for i in range(len(the_list)):
        if the_list[i] == number:
            counting += 1
    return counting

#count = count_list([1,2,3,3,3,4,2,1],3)
#print(count)

def average_list(the_list):
    sum = 0
    avg_cal = 0
    for i in range(len(the_list)):
        sum += the_list[i]
    avg_cal = sum/len(the_list)
    return avg_cal

#avg = average_list([1,2,3])
#print(avg)

def main():
    my_list = create_list(10000)
    for i in range(1,7):
        count = count_list(my_list, i)
        print("the number of %d is %d" %(i, count))
    print("the average is %d" %(average_list(my_list)))
    
if __name__ == "__main__":
    main()