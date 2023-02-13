# Cianee Sumowalt
# October 27, 2022
# American Widget Company

import random

# random.seed(0) (Used for testing program)

number_of_scores = random.randint(20,30)

print ("Input ", number_of_scores, " widget scores")
num_list = input("Input widget scores separated by commas ")
num_list = num_list.split(",") #This removes the commas from the list so it can count as an integer
for idx in range(number_of_scores):
    num_list[idx] = int(num_list[idx])


def sortem(): #Sorts the functions from smallest to largest
    for index in range(0, len(num_list) - 1):
        minVal = num_list[index]
        minIndex = index
        for k in range(index + 1, len(num_list)):
            if num_list[k] < minVal:
                minVal = num_list[k]
                minIndex = k
            num_list[minIndex] = num_list[index]
            num_list[index] = minVal
    return num_list



def mode_string(num_list):
    frequency_table = [0 for i in range(11)]
    for index in range(number_of_scores):
        value = num_list[index]
        frequency_table[value] += 1
        frequency_table[num_list[index]]
    high = max(num_list)
    return high #Returns the mode, but only seems to return the largest mode if there are multiple


mode = mode_string(num_list)

def mean(num_list):
    sum = 0
    for index in num_list:
        sum += index
    mean = round(sum/ float(len(num_list)),2)
    return mean #Returns the mean of the list

mean = mean(num_list)

def median(num_list):
    if len(num_list) % 2 == 0:
        medS1 = num_list[len(num_list)//2]
        medS2 = num_list[len(num_list)//2 -1]
        median = (medS1+medS2)/2
    else:
        median = num_list[len(num_list)//2]
    return median
median = median(num_list) #Returns the median of the function depending on whether or not the list length is odd or even

print (f"The mean for {number_of_scores} values is {mean}.")
print (f"The mode(s) for {number_of_scores} is {mode}. ")
print (f"The median for {number_of_scores} values is {median}")

def std_dev(num_list,mean):
    sum = 0
    for index in num_list:
        sum += (index - mean)**2
    std = round(((sum/(len(num_list)-1))**.5),2)
    return std #Standard deviation relies on the mean for its value

std = std_dev(num_list, mean)

print (f"The standard deviation of {number_of_scores} values is {std}.")