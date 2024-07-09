import torch
from torch import nn
import matplotlib.pyplot as plt
from pathlib import Path


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

print(device)

class Line(nn.Module):
    def __init__(self):
        super().__init__()
        self.line_layer = nn.Linear(in_features=1,
                              out_features=1)

    def forward(self, x):
        return self.line_layer(x)


weight = 2
bias = 0.2


start = 0
end = 1
step = 0.02


X = torch.arange(start, end, step).unsqueeze(dim=1) # without unsqueeze, errors will pop up
y = weight * X + bias


train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]


model_1 = Line()
model_1 = model_1.to(device)
loss_fn_1 = nn.L1Loss()
optimizer_1 = torch.optim.SGD(params=model_1.parameters(), lr=0.001)


torch.manual_seed(42)

# to cuda
X_train = X_train.to(device)
y_train = y_train.to(device)
X_test = X_test.to(device)
y_test = y_test.to(device)

def plot_predictions(train_data=X_train,
                     train_labels=y_train,
                     test_data=X_test,
                     test_labels=y_test,
                     predictions=None):
    """
    Plots training data, test data and compares predictions.
    """
    plt.figure(figsize=(10, 7))

    # Plot training data in blue
    plt.scatter(train_data, train_labels, c="b", s=4, label="Training data")

    # Plot test data in green
    plt.scatter(test_data, test_labels, c="g", s=4, label="Testing data")

    if predictions is not None:
        # Plot the predictions in red (predictions were made on the test data)
        plt.scatter(test_data, predictions, c="r", s=4, label="Predictions")

    # Show the legend
    plt.legend(prop={"size": 14})
    plt.show()



epoch = 25000

for i in range(epoch):
    model_1.train()

    y_prediction = model_1(X_train) # 1

    loss = loss_fn_1(y_prediction, y_train) # 2

    optimizer_1.zero_grad() # 3

    loss.backward() # 4

    optimizer_1.step() # 5

    model_1.eval()
    with torch.inference_mode(): # 6
        y_prediction = model_1(X_test)
        loss_test = loss_fn_1(y_prediction, y_test) # 10
        if i % 1000 == 0:
            print(f"epoch: {i} LossTest: {loss_test.item()}, Loss: {loss}") # 11

with torch.inference_mode():
    predictions = model_1(X_test)

print(predictions.cpu())

plot_predictions(
    predictions=predictions.cpu(),
    train_data=X_train.cpu(),
    train_labels=y_train.cpu(),
    test_data=X_test.cpu(),
    test_labels=y_test.cpu())

print(model_1.state_dict())

# Directory for model
MODEL_PATH_1 = Path("models")
MODEL_PATH_1.mkdir(parents=True, exist_ok=True)

# model(state dict) to directory
NAME_1 = "model_1.pth"
SAVE_PATH_1 = MODEL_PATH_1 / NAME_1

torch.save(obj=model_1.state_dict(),
           f=str(SAVE_PATH_1)) # f= is where saved


print(torch.cuda.is_available(), torch.cuda.get_device_name(torch.cuda.current_device()))



