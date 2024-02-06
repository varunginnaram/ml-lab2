import numpy as np

def euclidean_distance(vector1, vector2):
    # Ensure vectors have the same dimensions
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimensions")
    
    # Calculate the Euclidean distance
    return np.sqrt(np.sum((np.array(vector1) - np.array(vector2)) ** 2))

def knn_classifier(training_data, labels, new_instance, k):
    if len(training_data) != len(labels):
        raise ValueError("Length of training data and labels must match")
    
    # Calculate distances from the new instance to all instances in the training data
    distances = [(euclidean_distance(new_instance, instance), label) for instance, label in zip(training_data, labels)]
    
    # Sort distances and get the k nearest neighbors
    distances.sort(key=lambda x: x[0])
    neighbors = distances[:k]
    
    # Count occurrences of each label in the nearest neighbors
    counts = {}
    for _, label in neighbors:
        counts[label] = counts.get(label, 0) + 1
    
    # Determine the majority label
    predicted_label = max(counts, key=counts.get)
    
    return predicted_label

# Example usage:
training_data = [[1, 2], [2, 3], [3, 4], [4, 5]]
labels = ['A', 'A', 'B', 'B']
new_instance = [3, 3]
k = 3

predicted_label = knn_classifier(training_data, labels, new_instance, k)
print("Predicted label:", predicted_label)

