# Implement the factorial function using recursion.

def factorial(n): 
	
	# Checking the number
	# is 1 or 0 then
	# return 1
	# other wise return
	# factorial
	if (n==1 or n==0):
		return 1
	else:
		return (n * factorial(n - 1)) 
num = 5; 
print("number : ",num)
print("Factorial : ",factorial(num))
