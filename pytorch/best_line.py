import torch
from torch import nn
import matplotlib.pyplot as plt
from pathlib import Path

torch.device('cuda:0')


class Line(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))
        self.bias = nn.Parameter(torch.randn(1, requires_grad=True, dtype=torch.float))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.weights * x + self.bias

def plot_predictions(train_data, train_labels, test_data, test_labels, predictions=None):
    plt.figure(figsize=(10, 7))
    plt.scatter(train_data, train_labels, c='b', s=4, label='Training data')
    plt.scatter(test_data, test_labels, c='g', s=4, label='Testing data')
    if predictions is not None:
        plt.scatter(test_data, predictions, c='r', s=4, label='Predictions')
    plt.legend(prop={'size': 14})
    plt.show()

X = torch.tensor([5, 19, 34, 53, 22, 41, 60, 15, 60, 49], dtype=torch.float) # dataset
y = torch.tensor([19, 31, 22, 13, 25, 18, 8, 32, 10, 15], dtype=torch.float)

train_split = int(0.9 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]

model = Line()
loss_fn = nn.L1Loss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

for epoch in range(250000):
    model.train()
    y_pred = model(X_train)
    loss = loss_fn(y_pred, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 1000 == 0:
        model.eval()
        with torch.no_grad():
            y_pred_test = model(X_test)
            test_loss = loss_fn(y_pred_test, y_test)
            print(f'Epoch: {epoch}, Train loss: {loss.item()}, Test loss: {test_loss.item()}')

MODEL_PATH = Path('models')
MODEL_PATH.mkdir(parents=True, exist_ok=True)
MODEL_NAME = 'model.pth'
torch.save(model.state_dict(), MODEL_PATH / MODEL_NAME)

loaded_model = Line()
loaded_model.load_state_dict(torch.load(MODEL_PATH / MODEL_NAME))
loaded_model.eval()

with torch.no_grad():
    y_pred_test = loaded_model(X_test)
print(model.state_dict())
plot_predictions(X_train, y_train, X_test, y_test, y_pred_test)