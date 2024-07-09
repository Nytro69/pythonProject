import torch
from torch import nn


def to_dev(device="cuda:0", *args):
    return [arg.to(device) for arg in args]
def layers(input_num=2, output_num=1, layers1=10, neurons=128, func=nn.ReLU, func1=nn.Linear):
    layers = [func1(input_num, neurons)]
    for i in range(layers1 - 1):
        layers.append(func1(neurons, neurons))
        layers.append(func())

    layers.append(func1(neurons, output_num))
    return layers

# Setup device agnostic code
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# Setup random seed
RANDOM_SEED = 42

# Create a dataset with Scikit-Learn's make_moons()
from sklearn.datasets import make_moons

s = 1000
noise = 0.1
xy = make_moons(n_samples=s, noise=noise, random_state=42)
x, y = xy
a = x[:, 0]
b = x[:, 1]


data = []
for i in range(len(a)):
    data.append([a[i], b[i], y[i]])
print(data)
# Turn data into a DataFrame
import pandas as pd
df = pd.DataFrame(data, columns=["x", "y", "result"])
print(df)

# into torch
x = torch.from_numpy(x).float().to(device)
y = torch.from_numpy(y).float().to(device)

# Visualize the data on a scatter plot
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))
plt.scatter(x[:, 0].to("cpu"), x[:, 1].to("cpu"), c=y.to("cpu"), cmap=plt.cm.RdYlBu)
plt.show()

# Split the data into train and test sets (80% train, 20% test)
from sklearn.model_selection import train_test_split

x, y = to_dev(device, x, y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

import torch
from torch import nn

# Inherit from nn.Module to make a model capable of fitting the mooon data
class MoonModelV0(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            *layers()
        )

    def forward(self, x):
        return self.layer(x)

# Instantiate the model
moon_model = MoonModelV0().to(device)

# Setup loss function
loss_fn = torch.nn.BCEWithLogitsLoss()
# Setup optimizer to optimize model's parameters
optimizer = torch.optim.Adam(params=moon_model.parameters(),
                             lr=0.1)
# What's coming out of our model?
# logits (raw outputs of model)
logits = moon_model(x_test)
print(f"Logits: {logits}")

# Prediction probabilities
pred = torch.sigmoid(logits)
print(f"Pred probs: {pred}")

# Prediction labels
labels = torch.round(torch.sigmoid(logits))
print(f"Pred labels: {labels}")

# Let's calculuate the accuracy using accuracy from TorchMetrics
from torchmetrics import Accuracy

## TODO: Uncomment this code to use the Accuracy function
acc_fn = Accuracy(task="multiclass", num_classes=2).to(device) # send accuracy function to device

## TODO: Uncomment this to set the seed

# Setup epochs
epochs = 1000

# Loop through the data
for epoch in range(epochs):
    # 1. Forward pass (logits output)
    logits = moon_model(x_train)

    # Turn logits into prediction probabilities
    pred = torch.softmax(logits, 1)


    # Turn prediction probabilities into prediction labels
    labels = torch.round(pred)


    # 2. Calculaute the loss
    loss = loss_fn(logits.squeeze(), y_train) # loss = compare model raw outputs to desired model outputs

    # Calculate the accuracy
    acc = acc_fn(labels.shape[1], y_train.int()) # the accuracy function needs to compare pred labels (not logits) with actual labels

    # 3. Zero the gradients
    optimizer.zero_grad()

    # 4. Loss backward (perform backpropagation) - https://brilliant.org/wiki/backpropagation/#:~:text=Backpropagation%2C%20short%20for%20%22backward%20propagation,to%20the%20neural%20network's%20weights.
    loss.backward()

    # 5. Step the optimizer (gradient descent) - https://towardsdatascience.com/gradient-descent-algorithm-a-deep-dive-cf04e8115f21#:~:text=Gradient%20descent%20(GD)%20is%20an,e.g.%20in%20a%20linear%20regression)
    optimizer.step()

    ### Testing
    model_0.eval()
    with torch.inference_mode():
        # 1. Forward pass (to get the logits)
        logits = moon_model(x_test)

        # Turn the test logits into prediction labels
        test_label = torch.round(torch.softmax(logits, 1))
        acc_test = acc_fn(test_label, y_test)

        # 2. Caculate the test loss/acc
        loss_test = loss_fn(logits.squeeze(), y_test)


        # Print out what's happening every 100 epochs
        if epoch % 100 == 0:
            print(f"Epoch: {epoch}, train Acc: {acc}, train loss: {loss} Test Acc: {acc_test}, Test loss: {loss_test}")
"""
# Plot the model predictions
import numpy as np


def plot_decision_boundary(model, X, y):
    # Put everything to CPU (works better with NumPy + Matplotlib)
    model.to("cpu")
    X, y = X.to("cpu"), y.to("cpu")

    # Source - https://madewithml.com/courses/foundations/neural-networks/
    # (with modifications)
    x_min, x_max = X[:, 0].min() - 0.1, X[:, 0].max() + 0.1
    y_min, y_max = X[:, 1].min() - 0.1, X[:, 1].max() + 0.1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 101),
                         np.linspace(y_min, y_max, 101))

    # Make features
    X_to_pred_on = torch.from_numpy(np.column_stack((xx.ravel(), yy.ravel()))).float()

    # Make predictions
    model.eval()
    with torch.inference_mode():
        y_logits = model(X_to_pred_on)

    # Test for multi-class or binary and adjust logits to prediction labels
    if len(torch.unique(y)) > 2:
        y_pred = torch.softmax(y_logits, dim=1).argmax(dim=1)  # mutli-class
    else:
        y_pred = torch.round(torch.sigmoid(y_logits))  # binary

    # Reshape preds and plot
    y_pred = y_pred.reshape(xx.shape).detach().numpy()
    plt.contourf(xx, yy, y_pred, cmap=plt.cm.RdYlBu, alpha=0.7)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.RdYlBu)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

# Plot decision boundaries for training and test sets

# Create a straight line tensor

# Replicate torch.tanh() and plot it


# Code for creating a spiral dataset from CS231n
import numpy as np
import matplotlib.pyplot as plt
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
N = 100 # number of points per class
D = 2 # dimensionality
K = 3 # number of classes
X = np.zeros((N*K,D)) # data matrix (each row = single example)
y = np.zeros(N*K, dtype='uint8') # class labels
for j in range(K):
  ix = range(N*j,N*(j+1))
  r = np.linspace(0.0,1,N) # radius
  t = np.linspace(j*4,(j+1)*4,N) + np.random.randn(N)*0.2 # theta
  X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
  y[ix] = j
# lets visualize the data
plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.RdYlBu)
plt.show()

# Turn data into tensors
import torch
X = torch.from_numpy(X).type(torch.float) # features as float32
y = torch.from_numpy(y).type(torch.LongTensor) # labels need to be of type long

# Create train and test splits
from sklearn.model_selection import train_test_split


# Let's calculuate the accuracy for when we fit our model

from torchmetrics import Accuracy

## TODO: uncomment the two lines below to send the accuracy function to the device
# acc_fn = Accuracy(task="multiclass", num_classes=4).to(device)
# acc_fn

# Prepare device agnostic code
# device = "cuda" if torch.cuda.is_available() else "cpu"

# Create model by subclassing nn.Module



# Instantiate model and send it to device


# Setup data to be device agnostic


# Print out first 10 untrained model outputs (forward pass)
print("Logits:")
## Your code here ##

print("Pred probs:")
## Your code here ##

print("Pred labels:")
## Your code here ##

# Setup loss function and optimizer
# loss_fn =
# optimizer =

# Build a training loop for the model

# Loop over data


## Training

# 1. Forward pass


# 2. Calculate the loss


# 3. Optimizer zero grad


# 4. Loss backward


# 5. Optimizer step


## Testing


# 1. Forward pass

# 2. Caculate loss and acc

# Print out what's happening every 100 epochs



# Plot decision boundaries for training and test sets
"""