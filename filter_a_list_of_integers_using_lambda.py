#  Create a function that accepts a list of integers and a lambda function,
# applying the lambda to filter the list.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print("Original list of integers:")
print(nums)

print("\nEven numbers from the said list:")


even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

print("\nOdd numbers from the said list:")

odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums) 


