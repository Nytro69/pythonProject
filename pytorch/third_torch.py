import pandas as pd
import torch
from torch import nn
from matplotlib import pyplot as plt
import sklearn
from sklearn.datasets import make_circles
import math

def accuracy_fn(y_true, y_pred):
    correct = torch.eq(y_true, y_pred).sum().item() # torch.eq() calculates where two tensors are equal
    acc = (correct / len(y_pred)) * 100
    return acc

def split_data(x, y, split=0.8):
    splitx = math.trunc(split * len(x))
    splity = math.trunc(split * len(y))
    y1 = y[:splity]
    y2 = y[splity:]
    x1 = x[:splitx]
    x2 = x[splitx:]

    return x1, x2, y1, y2

def layers(input_num=1, output_num=1, layers1=10, neurons=128, func=nn.ReLU, func1=nn.Linear):
    layers = [func1(input_num, neurons)]
    for i in range(layers1 - 1):
        layers.append(func1(neurons, neurons))
        layers.append(func())

    layers.append(func1(neurons, output_num))
    return layers

device = "cuda" if torch.cuda.is_available() else "cpu"
sample_size = 1000

x, y = make_circles(
    n_samples=sample_size,
    noise=0.02,
    random_state=69
)

circle = pd.DataFrame({
    'x1': x[:, 0],
    'x2': x[:, 1],
    'label': y
})


plt.scatter(x=x[:, 0],
            y=x[:, 1],
            c=y,
            cmap=plt.cm.RdYlBu)

plt.show()

x = torch.from_numpy(x).type(torch.float) # turns np array to torch tensor
y = torch.from_numpy(y).type(torch.float) # -

x_train, x_test, y_train, y_test = split_data(x, y)

x_train = x_train.to(device)
x_test = x_test.to(device)
y_train = y_train.to(device)
y_test = y_test.to(device)

print(len(x_train), len(x_test), len(y_train), len(y_test))

"""
class Circle_option(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(in_features=2, out_features=8) # feature is size
        self.layer2 = nn.Linear(in_features=8, out_features=1) # "in" takes "out" of previous

    def forward(self):
        return self.layer2(self.layer1(x)) # output 1 to 2
"""
circle_model = nn.Sequential(
    *layers(input_num=2, output_num=1, neurons=256, layers1=10)
).to(device)

# loss function and optimizer
loss_fn = torch.nn.BCEWithLogitsLoss()

optimizer = torch.optim.Adam(params=circle_model.parameters(),
                             lr=0.001)

epoch = 100

#y_train = y_train.unsqueeze(1)  # This will reshape y_train to [800, 1]


for i in range(epoch):
    # train mode
    circle_model.train()

    # 1. forward method
    y_pred = circle_model(x_train).squeeze(1)

    # 2. calculate loss
    loss = loss_fn(y_pred, y_train)

    # 3. zero grad
    optimizer.zero_grad()

    # 4. backward method (backpropagation)
    loss.backward()

    # 5. step
    optimizer.step()

    # eval mode
    circle_model.eval()

    # do same thing on test data
    with torch.inference_mode():
        # forward pass
        y_pred = circle_model(x_test).squeeze(1) #

        # calculate loss
        test_loss = loss_fn(y_pred, y_test)

        # calculate accuracy
        if i % 10 == 0:
            print(f"epoch: {i} LossTest: {test_loss.item()}, Loss: {loss}, Acc: {accuracy_fn(y_true=y_test, y_pred=torch.round(torch.sigmoid(y_pred)))}%")
from helper_functions import plot_predictions, plot_decision_boundary

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Train")
plot_decision_boundary(circle_model, x_train, y_train)
plt.subplot(1, 2, 2)
plt.title("Test")
plot_decision_boundary(circle_model, x_test, y_test)
plt.show()