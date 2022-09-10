print('hi ai')

from PIL import Image

image = Image.open("./Dog_Breeds.jpeg")

# The first pytorch training
import torch

five = torch.Tensor([5])
three = torch.Tensor([3])
eight = torch.Tensor([8])

from torch.nn import Linear, MSELoss

f = Linear(2, 1).cuda()
input = torch.cat([five, three]).cuda()
print(input.shape)
input = input.unsqueeze(0)
eight = eight.unsqueeze(0).cuda()
print(input.shape)
print(eight.shape)

torch.Size([2])
torch.Size([1, 2])
torch.Size([1, 1])



from torch.optim import Adam
optimizer = Adam(f.parameters(), lr=0.0004)
mse = MSELoss()


from tqdm import trange
pbar = trange(15000)
outputs = []
for i in pbar:
  output = f(input)
  loss = mse(output, eight)

  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
  pbar.set_description(f'output = {output.item()}')
  if i % 100 == 0 :
    outputs.append(output.item())


from matplotlib import pyplot as plt

plt.plot(outputs)
plt.show()