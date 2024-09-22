# # str_lst = list('MUSURMONOVABDULAZIZBOTIROVICH')
# # str_lst.sort()
# # str_lst = ''.join(str_lst)
# # print(str_lst)


# # Selection sort in Python
# # time complexity O(n*n)
# #sorting by finding min_index
# def selectionSort(array, size):
    
#     for ind in range(size):
#         min_index = ind
 
#         for j in range(ind + 1, size):
            
#             if array[j] < array[min_index]:
#                 min_index = j
        
#         (array[ind], array[min_index]) = (array[min_index], array[ind])
 

# arr = [5, 8, 3, 1, 5, 9, 7, 9, 2 ]
# size = len(arr)
# selectionSort(arr, size)

# print('Saralangan massive Abilov Abdulaziz tomonidan ')
# print(arr)
# Check if the input is a natural number
# Ask the user to enter a natural number

# user_input = input("Enter a natural number: ")


#     # Initialize a list to count the occurrences of each digit (0-9)
# digit_count = [0] * 10
    
#     # Iterate over each digit in the input
# for digit in user_input:
#         # Convert the digit from string to integer
#     digit_index = int(digit)
#         # Increment the count for this digit
#     digit_count[digit_index] += 1
    
#     # Print the count of each digit
#     for i in range(10):
#         if digit_count[i] > 0:
#             print(f"{i} occurs {digit_count[i]} times")
# else:
#     print("Please enter a valid natural number.")
#################################################
# user_input = input("Enter a natural number: ")
# for i in  user_input : 
#     count0 = 0
#     count1 = 0
#     count2 = 0
#     count3 = 0
#     count4 = 0
#     count5 = 0
#     count6 = 0
#     count7 = 0
#     count8 = 0
#     count9 = 0
#     if i==0:
#         count0=+1
#     if i==1:
#         count1=+1
#     if i==2:
#         count2=+1
#     if i==3:
#         count3=+1
#     if i==4:
#         count4=+1
#     if i==5:
#         count5=+1
#     if i==6:
#         count6=+1
#     if i==7:
#         count7=+1
#     if i==8:
#         count8=+1
#     if i==9:
#         count9=+1
# if count0 > 0:
#     print("0" , count0 )

################################3
# for n in range(1, 1001):
#     count = 0
#     for i in range(1, n + 1):
#         if n%i == 0:
#             count+= 1
#     if count==5:
#         print(n)

# for a in range(1,10):
#     for b in range(1,10):
#         c=a*b
#         t = f'{a} \"kara"'
#         text = f'{a}x{b}={c}'
        
#         print(text)

# a = input("n-->")
# count = 0
# lis = []
# for i in a:
#     lis.append(i)
#     if i in lis:
#         count=+1
#         print(i, count)

# # Prompt the user to enter a natural number
# user_input = input("Enter a natural number: ")

# # Initialize counters for each digit
# count0 = count1 = count2 = count3 = count4 = count5 = count6 = count7 = count8 = count9 = 0

# # Iterate over each digit in the input and count occurrences
# for digit in user_input:
#     if digit == '0':
#         count0 += 1
#     elif digit == '1':
#         count1 += 1
#     elif digit == '2':
#         count2 += 1
#     elif digit == '3':
#         count3 += 1
#     elif digit == '4':
#         count4 += 1
#     elif digit == '5':
#         count5 += 1
#     elif digit == '6':
#         count6 += 1
#     elif digit == '7':
#         count7 += 1
#     elif digit == '8':
#         count8 += 1
#     elif digit == '9':
#         count9 += 1

# # Print the count of each digit if it occurs
# if count0 > 0:
#     print(f"0 occurs {count0} times")
# if count1 > 0:
#     print(f"1 occurs {count1} times")
# if count2 > 0:
#     print(f"2 occurs {count2} times")
# if count3 > 0:
#     print(f"3 occurs {count3} times")
# if count4 > 0:
#     print(f"4 occurs {count4} times")
# if count5 > 0:
#     print(f"5 occurs {count5} times")
# if count6 > 0:
#     print(f"6 occurs {count6} times")
# if count7 > 0:
#     print(f"7 occurs {count7} times")
# if count8 > 0:
#     print(f"8 occurs {count8} times")
# if count9 > 0:
#     print(f"9 occurs {count9} times")




    

           
                
                
           
        
    
    
        
      
       


