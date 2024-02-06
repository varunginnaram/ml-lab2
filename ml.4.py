def onehotencode(data):
    unique_values = list(set(data))
    encoding_dict = {value: index for index, value in enumerate(unique_values)}
    encoded_data = []
    for val in data:
        encoding = [0] * len(unique_values)
        encoding[encoding_dict[val]] = 1
        encoded_data.append(encoding)
    return encoded_data, encoding_dict

# Get user input for categorical data
user_input = input("Enter categorical values: ")



categorical_data=user_input.split()
# Apply one-hot encoding
encoded_data, encoding_dict = onehotencode(categorical_data)

print("Original Data:", categorical_data)
print("One-Hot Encoded Data:")
for data_point in encoded_data:
    print(data_point)

print("\nEncoding Dictionary:")
for key, value in encoding_dict.items():
    print(f"{key}: {value}")