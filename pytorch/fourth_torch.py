import torch
import torchmetrics
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.datasets import make_blobs
import torch.nn as nn
import math
from helper_functions import plot_predictions, plot_decision_boundary

def main():
    def to_dev(device="cuda:0", *args):
        return [arg.to(device) for arg in args]

    def accuracy_fn(y_true, y_pred):
        correct = torch.eq(y_true, y_pred).sum().item() # torch.eq() calculates where two tensors are equal
        acc = (correct / len(y_pred)) * 100
        return acc

    def layers(input_num=1, output_num=1, layers1=10, neurons=128, func=nn.ReLU, func1=nn.Linear):
        layers = [func1(input_num, neurons)]
        for i in range(layers1 - 1):
            layers.append(func1(neurons, neurons))
            layers.append(func())

        layers.append(func1(neurons, output_num))
        return layers

    def split_data(x, y, split=0.8):
        splitx = math.trunc(split * len(x))
        splity = math.trunc(split * len(y))
        y1 = y[:splity]
        y2 = y[splity:]
        x1 = x[:splitx]
        x2 = x[splitx:]

        return x1, x2, y1, y2

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    samples = 1000
    num_types = 4
    num_features = 2

    x_blob, y_blob = make_blobs(n_samples=samples,
                                        n_features=num_features,
                                        centers=num_types,
                                        cluster_std=0.4)

    x_blob = torch.from_numpy(x_blob).float().to(device)
    y_blob = torch.from_numpy(y_blob).long().to(device)

    x_blob_train, x_blob_test, y_blob_train, y_blob_test = split_data(x_blob,
                                                                      y_blob,
                                                                      split=0.2)

    plt.figure(figsize=(10, 7))
    plt.scatter(x_blob[:, 0].to("cpu"), x_blob[:, 1].to("cpu"), c=y_blob.to("cpu"), s=40, cmap=plt.cm.RdYlBu)
    plt.show()

    class Blob(nn.Module):
        def __init__(self, input, out, hidden):
            super().__init__()
            self.layer = nn.Sequential(
                *layers(input_num=input, output_num=out, neurons=hidden)
            )

        def forward(self, x):
            return self.layer(x)

    blob_model = Blob(input=2,
                      out=4,
                      hidden=1024).to(device)

    # Create a loss function for multi-class classification - loss function measures how wrong our model's predictions are
    loss_fn = nn.CrossEntropyLoss()

    # Create an optimizer for multi-class classification - optimizer updates our model parameters to try and reduce the loss
    optimizer = torch.optim.SGD(params=blob_model.parameters(),
                                lr=0.01)

    x_blob_train, x_blob_test, y_blob_train, y_blob_test = to_dev(device, x_blob_train, x_blob_test, y_blob_train, y_blob_test)

    epochs = 3000

    for epoch in range(epochs):
        blob_model.train()

        y_logits = blob_model(x_blob_train)
        y_pred = torch.softmax(y_logits, dim=1).argmax(dim=1)

        loss = loss_fn(y_logits, y_blob_train)
        acc = accuracy_fn(y_blob_train, y_pred)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        blob_model.eval()
        with torch.inference_mode():
            test_logits = blob_model(x_blob_test)
            test_pred = torch.softmax(test_logits, dim=1).argmax(dim=1)

            test_loss = loss_fn(test_logits, y_blob_test)
            test_acc = accuracy_fn(y_blob_test, test_pred)

            if epoch % 100 == 0:
                print(f"Epoch: {epoch}, test loss: {test_loss}, test acc: {test_acc}, loss: {loss}, acc: {acc}")


    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title("Train")
    plot_decision_boundary(blob_model, x_blob_train, y_blob_train)
    plt.show()

    accuracy = torchmetrics.Accuracy().to(device)

    accuracy(y_pred, y_blob_test)

    print(f"Accuracy: {accuracy}")

if __name__=="__main__":
    main()