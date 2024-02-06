def label_encode(data):
    # Find unique values in the data
    unique_values = list(set(data))
    
    # Create a dictionary to map unique values to labels
    encoding_dict = {val: i for i, val in enumerate(unique_values)}
    
    # Encode the data using the dictionary
    encoded_data = [encoding_dict[val] for val in data]
    
    return encoded_data, encoding_dict

# Get user input for categorical data 
user_input = input("Enter categorical values separated by spaces: ")

# Split the input into individual values
data = user_input.split()

# Apply label encoding to the data
encoded_data, encoding_dict = label_encode(data)

print("Original Data:", data)
print("Encoded Data:", encoded_data)

print("\nEncoding Dictionary:") 
for key, value in encoding_dict.items():
    print(f"{key}: {value}")

