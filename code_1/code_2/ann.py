import numpy as np
X = np.array([[1,0,1,0],[1,0,1,1],[0,1,0,1]])
y = np.array([[1],[1],[0]])
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def derivative_sigmoid(x):
    return x * (1 - x)
nb_epoch = 5000
learning_rate = 0.1
inputlayer_neurons = X.shape[1]
hidden_layer_neurons = 3
output_neurons = 1

# wh - weight for hidden layer
# bh - bias for hidden layer
wh = np.random.uniform(size = (inputlayer_neurons, hidden_layer_neurons))
bh = np.random.uniform(size = (1, hidden_layer_neurons))

# wout - weight for output layer
# bout - bias for output layer
wout = np.random.uniform(size = (hidden_layer_neurons, output_neurons))
bout = np.random.uniform(size = (1, output_neurons))


for i in range(nb_epoch):
    # feedforward
    hidden_layer = np.dot(X,wh)
    hidden_layer_input = hidden_layer + bh
    hidden_layer_activation = sigmoid(hidden_layer_input)
    output_layer1 = np.dot(hidden_layer_activation, wout)
    output_layer_input = output_layer1 + bout
    output = sigmoid(output_layer_input)

    # Backpropagation
    E = y - output
    slope_output_layer = derivative_sigmoid(output)
    slope_hidden_layer = derivative_sigmoid(hidden_layer_activation)

    delta_output = E * slope_output_layer
    err_hidden_layer = delta_output.dot(wout.T)

    delta_hidden_layer = err_hidden_layer * slope_hidden_layer

    wout += hidden_layer_activation.T.dot(delta_output) * learning_rate
    bout += np.sum(delta_output, axis=0, keepdims=True) * learning_rate
    wh += X.T.dot(delta_hidden_layer) * learning_rate
    bh += np.sum(delta_hidden_layer, axis=0, keepdims=True) * learning_rate

print(output)







