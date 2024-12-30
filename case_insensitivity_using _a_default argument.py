# Implement a function that accepts a list of strings and a target string and checks if the target exists in the list, with an option for case insensitivity using a default argument.


def check_Laptops():

	laptops = ['Msi', 'Lenovo', 'Hp', 'Dell']

	your_laptop = 'lenovo'

	# 'lenovo' is in lower case but it is present in the list of laptops.

	for lapy in laptops:
	
	#convert to lowercase and compare
		if your_laptop.lower() == lapy.lower():

			return True
	else:
		return False
if check_Laptops():

	print('Laptop is present')
	

# If function returns false
else:

	print('Laptop is not present')






