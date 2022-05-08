import model

h = model.Linear()

x = [19,300,430,770,1200]
y = [2885,15642,24222,38497,59909]

size = len(x)

for epoch in range(500):
    for b in range(size):
        prediction = h.forward(x[b])
        loss = h.MSE(prediction, y[b])
        h.backward()
        h.zero_grad()
    if (epoch % 10) == 0:
        print("epoch{0}:{1}".format(epoch, h.h_0))
h.summary()
