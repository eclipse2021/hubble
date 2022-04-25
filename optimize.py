import model

h = model.Linear()

x = [19,300,430,770,1200]
y = [0.2885,1.5642,2.4222,3.8497,5.9909]

size = len(x)

for epoch in range(500):
    for b in range(size):
        prediction = h.forward(x[b])
        loss = h.MSE(prediction, y[b])
        h.backward()
        h.zero_grad()
    print("epoch{0}:{1}".format(epoch, h.h_0))
h.summary()
