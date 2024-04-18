import torch
from torch import nn
import matplotlib.pyplot as plt
from pathlib import Path

"""
functions: 

.arange a range of numbers in a matrix
.zeros_like everything into 0
.ones_like everything into 1
.tensor(dtype=float32) creating a tensor
+-*/ per element, tensor +-*/ num
.mul = Multiplication
.matmul, .mm = Matrix Multiplication, Rules: inner dimensions must match, outer dimensions chooses the size of the resulting matrix
.add = Addition
.rand random tensor of chosen dimensions
.T changes dimensions of a matrix (x, y) -> (y, x)
.min gets smallest value of a tensor
.max gets largest value of a tensor
.mean gets average value of a tensor (no int)
.sum get sum of tensor
.argmin gets index of smallest num
.argmax gets index of largest num
.reshape allows to add and change dimensions 
.view same as .reshape but changes the input to itself (except extra dimension) y = x.view -> y = x (x changes)
.stack Concatenates a sequence of tensors along a new dimension. stack([2, 5], [4, 6]) -> [[2, 5], [4, 6]]
.squeeze removes dimensions with 1 as the shape of the dimension [[[2, 4, 4]]] -> [2, 4, 4], shape: (1, 5) -> (5)
.unsqueeze(dim=0) adds a dimension as dim= parameter ex dim=0 [2, 3] -> [[2, 3]] dim=1 [2, 3] -> [[2], [3]]
.permute from size(x) = [4, 6, 8] x.permute(num = dim ->(0, 2, 1)) -> [4, 8, 6] # changes dim 0 -> 0, 1 -> 2, 2 -> 1. also changes value in original when changed
[:, x, y], : means all elements in dimension
Unknown:


"""

print(torch.cuda.is_available(), torch.cuda.get_device_name(torch.cuda.current_device()))

torch.device('cuda:0')


seed_number = 69
torch.manual_seed(seed=seed_number)
f = torch.rand(1, 7)

seed = torch.manual_seed(seed=seed_number)
g = torch.rand(1, 7)
print(f"{f}\n{g}")

print(f == g)

print(torch.argmax(f)) # position of largest value

weight = 0.7
bias = 0.3

# Create
start = 0
end = 1
step = 0.02
X = torch.arange(start, end, step).unsqueeze(dim=1)
print("X: ", X)
y = weight * X + bias
print("y: ", y)


train_split = int(0.8 * len(X))
X_train, y_train = X[:train_split], y[:train_split]
X_test, y_test = X[train_split:], y[train_split:]



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



class Line(nn.Module):
    def __init__(self):
        super().__init__()
        self.weights = nn.Parameter(
            torch.randn(1,  #start with a random weight and try to adjust it to the ideal weight
                        requires_grad=True,
                        dtype=torch.float))

        self.bias = nn.Parameter(torch.randn(1,
                                             requires_grad=True,
                                             dtype=torch.float))

    # Forward method to define the computation in the model
    def forward(self, x: torch.Tensor) -> torch.Tensor:  # <- "x" is the input data
        return self.weights * x + self.bias  # this is the linear regression formula


model_0 = Line()

print(next(model_0.parameters()).device)

model_0.to("cuda:0")

print(next(model_0.parameters()).device)

with (torch.inference_mode()):
  y_prediction = model_0(X_test)

loss_fn_0 = nn.L1Loss()

optimizer_0 = torch.optim.SGD(params=model_0.parameters(), # parameters of target model to optimize
                            lr=0.001)

print(f"parameters: {list(model_0.parameters())}")

epoch = 250000000


for i in range(epoch):
    model_0.train()

    y_prediction = model_0(X_train)

    loss = loss_fn_0(y_prediction, y_train)

    optimizer_0.zero_grad()

    loss.backward()

    optimizer_0.step()

    model_0.eval()
    with torch.inference_mode():
        y_prediction_new = model_0(X_test)

        test_loss = loss_fn_0(y_prediction_new, y_test)
        if i % 1000 == 0:
            print(f"Epoch: {i}, test loss: {test_loss}, loss: {loss}")

print(model_0.state_dict())

with torch.inference_mode():
    y_prediction_new = model_0(X_test)

plot_predictions(predictions=y_prediction_new)


MODEL_PATH = Path("models")
MODEL_PATH.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "model_0.pth"
SAVE_PATH = MODEL_PATH / MODEL_NAME

print(SAVE_PATH)
torch.save(obj=model_0.state_dict(),
           f=str(SAVE_PATH))

load_model_0 = Line()

load_model_0.load_state_dict(torch.load(f=str(SAVE_PATH)))

load_model_0.eval()
with torch.inference_mode():
    y_prediction_new = load_model_0(X_test)

plot_predictions(predictions=y_prediction_new)



print(torch.cuda.is_available(), torch.cuda.get_device_name(torch.cuda.current_device()))