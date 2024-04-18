from second_torch import Line
import torch

load_model_1 = Line()

load_model_1.load_state_dict(torch.load(f=str("models/model_1.pth")))

print(load_model_1.state_dict())

