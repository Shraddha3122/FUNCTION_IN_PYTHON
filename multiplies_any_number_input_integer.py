#  Create a function that takes an integer as input and returns a function that multiplies any number by the input integer.

def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

# Example usage:
double = multiplier(2)
result = double(4)  
print(result) 

triple = multiplier(3)
result = triple(4)  
print(result)  

