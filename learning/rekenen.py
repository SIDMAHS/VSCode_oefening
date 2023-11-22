def perform_operations(num1, num2):
    # Addition
    addition_result = num1 + num2
    
    # Subtraction
    subtraction_result = num1 - num2
    
    # Returning a tuple with all results
    return addition_result, subtraction_result
   

# Example usage
num1 = 10
num2 = 5

result_tuple = perform_operations(num1, num2)

print(f"Addition: {result_tuple[0]}")
print(f"Subtraction: {result_tuple[1]}")

