from pathlib import Path

# Import data
input_data = Path('/Kodprojekt/adventofcode/adventofcode2020/input_data')
input_file = input_data / 'adventofcode_input_9.txt'
f = open(input_file, 'r')
content = f.readlines()

# Create list
input_data = []
for line in content:
    input_data.append(int(line))

#number_to_find = 127
number_to_find = 1639024365

# An efficient program  
# to print subarray 
# with sum as given sum  
  
# Returns true if the  
# there is a subarray  
# of arr[] with sum 
# equal to 'sum'  
# otherwise returns  
# false. Also, prints  
# the result. 
def subArraySum(arr, n, sum): 
      
    # Initialize curr_sum as 
    # value of first element 
    # and starting point as 0  
    curr_sum = arr[0] 
    start = 0
  
    # Add elements one by  
    # one to curr_sum and  
    # if the curr_sum exceeds  
    # the sum, then remove  
    # starting element  
    i = 1
    while i <= n: 
          
        # If curr_sum exceeds 
        # the sum, then remove 
        # the starting elements 
        while curr_sum > sum and start < i-1: 
          
            curr_sum = curr_sum - arr[start] 
            start += 1
              
        # If curr_sum becomes 
        # equal to sum, then 
        # return true 
        if curr_sum == sum: 
            print ("Sum found between indexes") 
            print ("% d and % d"%(start, i-1)) 
            print('Encryption weekness: ', max(arr[start:i-1]) + min(arr[start:i-1]))
            return 1
  
        # Add this element  
        # to curr_sum 
        if i < n: 
            curr_sum = curr_sum + arr[i] 
        i += 1
        #print(curr_sum)
  
    # If we reach here,  
    # then no subarray 
    print ("No subarray found") 
    return 0
  
# Driver program 
#arr = [15, 2, 4, 8, 9, 5, 10, 23] 
n = len(input_data) 
sum = number_to_find
  
subArraySum(input_data, n, sum) 