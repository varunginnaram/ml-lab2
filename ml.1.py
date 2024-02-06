import math

def euclidean_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimensions")
    
    squared_diff_sum = 0
    for i in range(len(vector1)):
        squared_diff_sum += (vector1[i] - vector2[i]) ** 2
    
    return math.sqrt(squared_diff_sum)

def manhattan_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimensions")
    
    abs_diff_sum = 0
    for i in range(len(vector1)):
        abs_diff_sum += abs(vector1[i] - vector2[i])
    
    return abs_diff_sum

# Example usage:
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

euclidean_dist = euclidean_distance(vector1, vector2)
manhattan_dist = manhattan_distance(vector1, vector2)

print("Euclidean Distance:", euclidean_dist)
print("Manhattan Distance:", manhattan_dist)


