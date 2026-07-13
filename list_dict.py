# List Operations
from itertools import count

# a = ["apple", 14, False, 23, 19]

# for i in range(len(a)):
#     print(a[i])

# for list in a:
#     print(list)

# print(a[slice(1,4)])

# print(type(list))


# numbers = [23, -7, 14, 89, -3, 42]
#
# positives = []
# negatives = []
#
# for i in numbers:
#     if i > 0:
#         positives.append(i)
#     elif i < 0:
#         negatives.append(i)
#
# print("Positive numbers:", positives)
# print("Negative numbers:", negatives)


# Real world practical example

# create = ["green", "red", "green", "yellow", "red", "green", "pink lady"]
#
# green_apple = []
#
# for x in create:
#     if x == "green":
#         green_apple.append(x)
#
# print("Green apples:", green_apple)
# print("Total Green Apples:", len(green_apple))
#
# #  [ WHAT TO KEEP |  WHERE TO LOOK  |  THE FILTER CONDITION ]
# green_apple_basket = [apple for apple in create if apple == "green"]
#
# print("Green apples in basket:", green_apple_basket)
# print("Total Green Apples in basket:", len(green_apple_basket))

# Find the Second Greatest Element
# numbers = [23, -7, 14, 89, -3, 14, 23, 42]
# unique_numbers = list(set(numbers))
# unique_numbers.sort(reverse=True)
#
# # Second way
# second_greatest_number_1 = sorted(list(set(numbers)), reverse=True)[1]
#
# second_greatest_number = unique_numbers[1]
# print("Unique Numbers:", unique_numbers)
# print("Second Greatest Number:", second_greatest_number)
# print("Second Greatest Number method_2:", second_greatest_number_1)


# Manual approach to the unique list

# manual_unique_numbers = []
# for num in numbers:
#     if num not in manual_unique_numbers:
#         manual_unique_numbers.append(num)
#
# print("Manual Unique Numbers:", manual_unique_numbers)

# Manual approach to sort the list

# data = [23, -7, 14, -3]
#
# # We loop through the list multiple times
# n = len(data)
# for i in range(n):
#     # The last i elements are already in place
#     for j in range(0, n - i - 1):
#         # Compare adjacent elements
#         if data[j] > data[j + 1]:
#             # Swap if they are in the wrong order
#             data[j], data[j + 1] = data[j + 1], data[j]
#
# print(data) # Output: [-7, -3, 14, 23]


# To learn this quickly, stop thinking about the whole code at once. Instead, focus on the
# "Swap"
#  logic and the
# "Range"
#  shrinking.
#
# ### 1. The Core Mechanic: The "Swap"
#
# Python makes swapping incredibly easy. You don't need a temporary "box" to hold a number like in other languages.
# `data[j], data[j + 1] = data[j + 1], data[j]`
# This tells Python: "Take the value on the right, put it on the left; take the value on the left, put it on the right—do it simultaneously."
#
# ---
#
# ### 2. The Step-by-Step Execution
#
# Let’s trace `data = [23, -7, 14, -3]` with `n = 4`.
#
# ####
# Pass 1 (i = 0)
#
#
# We look at all pairs to push the largest number to the end.
#
# 1.
# Compare 23 and -7:
#  23 > -7?
# Yes.
#  Swap! $\rightarrow$ `[-7, 23, 14, -3]`
# 2.
# Compare 23 and 14:
#  23 > 14?
# Yes.
#  Swap! $\rightarrow$ `[-7, 14, 23, -3]`
# 3.
# Compare 23 and -3:
#  23 > -3?
# Yes.
#  Swap! $\rightarrow$ `[-7, 14, -3, 23]`
#
# Result after Pass 1: The biggest number (23) is now correctly at the end.
#
#
# ####
# Pass 2 (i = 1)
#
#
# We only need to look at the first 3 items because 23 is already done.
#
# 1.
# Compare -7 and 14:
#  -7 > 14? No.
# 2.
# Compare 14 and -3:
#  14 > -3?
# Yes.
#  Swap! $\rightarrow$ `[-7, -3, 14, 23]`
#
# Result after Pass 2: The second biggest (14) is now in place.
#
#
# ####
# Pass 3 (i = 2)
#
#
# We only need to look at the first 2 items.
#
# 1.
# Compare -7 and -3:
#  -7 > -3? No.
#
# Result after Pass 3: The list is now fully sorted.
#
#
# ---
#
# ### 3. Why the Loops are written that way
#
#
#
# The Outer Loop (`for i in range(n)`):
#  This keeps track of how many items are "done" at the back of the list. Every time this loop runs once, we finish putting one more number in its correct final position.
#
#
# The Inner Loop (`for j in range(0, n - i - 1)`):
#
#
#  `n - 1` is used because we compare `j` with `j + 1`. If we didn't stop early, `j + 1` would go out of bounds and cause an error.
#
#  `- i` is the secret sauce. Since the largest `i` numbers are already sorted at the end, we don't need to check them again.
# This is why the inner loop gets shorter every time!
#
#
#
#
# ### The "Mental Shortcut" Summary
#
#
#
# Outer Loop:
#  "How many full passes do I need to make?" (One for each number).
#
#
# Inner Loop:
#  "How many comparisons do I need in this specific pass?" (Fewer every time, because the end of the list is already finished).
#
# Does seeing how the inner loop ignores the "finished" numbers at the end of the list help make sense of the `n - i - 1` logic?


# sorting_numbers = [23, -7, 14, 89, -3, 42]
#
# n = len(sorting_numbers)
#
# for i in range(n):
#     for j in range(0, n-i-1):
#         if sorting_numbers[j] > sorting_numbers[j+1]:
#             sorting_numbers[j], sorting_numbers[j+1] = sorting_numbers[j+1], sorting_numbers[j]
#
# print("Sorted Numbers:", sorting_numbers)

# Simple way to get the mean value
# sum_numbers = [1,2,3,4,5,6,7]
#
# total_sum = 0
# count = 0
#
# for num in sum_numbers:
#     total_sum += num
#     count += 1
#
# average = total_sum / count if count > 0 else 0
# print("Total Sum: ", total_sum)
# print("Average: ", average)
# print(average)

# Finding Maximum number
# numbers = [1,2,3,4,5,6,7,5,8,1,0,2]
#
#
# maximum = numbers[0]
#
# for num in numbers:
#     if num > maximum:
#         maximum = num
#         print(num)
#         print(maximum)
#
# print("Maximum number:", maximum)


# The Transformation
# sample_list = [10, 20, 30,10,10,10,30,20,10]
# set_list = set(sample_list)  # The messy, unique tray
#
# for ele in set_list:
#     print(ele)
#


# sorted_list = sorted(sample_list)
# print(sorted_list)

# my_set = {10, 20, 30,10,10,10,30,20,10}          # The messy, unique tray
# my_list = sorted(my_set, reverse=True)        # Putting them into an organized, indexed box
# print(my_list)              # Now we can ask for the second item!


# Programmatic way to remove duplicates

def duplicates_remover(data):
    unique_data = []
    seen = []

    for item in data:
        if item not in seen:
            unique_data.append(item)
            seen.append(item)

    return unique_data

my_list = [10, "apple", 10, "banana", "apple", 20.5, 20.5]
print(duplicates_remover(my_list))



## Dictionaries

# student = {"name": "Alice", "score": 85, "age": 40}
#
# for key in student:
#     print([key, student[key]])

# student = {"name": "Alice", "score": 85, "age": 40}
#
# # Convert the dictionary directly into a list of lists
# master_list = [(key, value) for key, value in student.items()]
#
# print(master_list)

# list flatten
# student = {"name": "Alice", "score": 85, "age": 40}
# flat_list = []
#
# for key, value in student.items():
#     flat_list.append(key)
#     flat_list.append(value)
#
# print(flat_list)

## The Pair Sum Finder
# nums = [0,1,3,5,8,9]
# target = 9
#
# def pair_sum(nums, target):
#     n = len(nums)
#     all_pairs = []
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] + nums[j] == target:
#                 all_pairs.append([i,j])
#     return all_pairs
#
# print(pair_sum(nums, target))

# tasks = ["Eat", "Sleep", "Code"]

''' The Solution: Slicing with [::2]
You can use the slice notation [start:stop:step] to create a smaller version of your list that only includes every 2nd item, and then enumerate that'''
# tasks = ["Eat", "Sleep", "Code", "Repeat", "Rest","Chill","Code","Eat","Sleep","Code"]
# for key, value in enumerate(tasks[::2]):
#     print(f"Task {key + 1} -> {value}")
#
# for i in range(0,len(tasks), 2):
#     print(f"Task {i + 1} -> {tasks[i]}")

''' This creates a generator object, it doesn't run the loop yet
my_gen = (x * 2 for x in range(5))'''

# my_gen = (x * 2 for x in range(1,5,2))
# print(list(my_gen))

# Output: <generator object <genexpr> at 0x000001E88E2FA9B0>'''

# print(list(task for task in list(set(tasks)) if task == "Code"))
# print(list(set(tasks)))

# for index , value in enumerate(tasks):
#     print(f"Task {index + 1} -> {value}")

