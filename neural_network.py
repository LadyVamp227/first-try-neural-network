import numpy as np

input_features = np.array([[1, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1],
                           [0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1],
                           [0, 0, 0, 1], [0, 0, 1, 0],[0, 0, 1, 1]])
target_output = np.array([[1, 1, 0, 0, 1, 1, 0, 0, 1]])
# Reshaping our target output into vector :
target_output = target_output.reshape(9, 1)
weights = np.array([[0.1], [0.2], [0.3], [0.4]])
bias = 0.3
# Learning Rate :
lr = 0.05
# Sigmoid function :


def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Derivative of sigmoid function :


def sigmoid_der(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Main logic for neural network :
# Running our code 10000 times :
for epoch in range(1000000):
    inputs = input_features
    # Feedforward input :
    pred_in = np.dot(inputs, weights) + bias
    # Feedforward output :
    pred_out = sigmoid(pred_in)
    # Backpropogation
    # Calculating error
    error = pred_out - target_output

    # Going with the formula :
    x = error.sum()

    # Calculating derivative :
    dcost_dpred = error
    dpred_dz = sigmoid_der(pred_out)

    # Multiplying individual derivatives :
    z_delta = dcost_dpred * dpred_dz
    # Multiplying with the 3rd individual derivative :
    inputs = input_features.T
    weights -= lr * np.dot(inputs, z_delta)  # Updating the bias weight value :
    for i in z_delta:
        bias -= lr * i
# Printing final weights:
print(weights)
print(bias)  # Taking inputs :
single_point = np.array([1, 0, 0, 1])  # 1st step :
result1 = np.dot(single_point, weights) + bias  # 2nd step :
result2 = sigmoid(result1)  # Print final result
print(result2)  # Taking inputs :
single_point = np.array([0, 0, 1, 1])  # 1st step :
result1 = np.dot(single_point, weights) + bias  # 2nd step :
result2 = sigmoid(result1)  # Print final result
print(result2)  # Taking inputs :
single_point = np.array([1, 0, 1, 0])  # 1st step :
result1 = np.dot(single_point, weights) + bias  # 2nd step :
result2 = sigmoid(result1)  # Print final result
print(result2)
