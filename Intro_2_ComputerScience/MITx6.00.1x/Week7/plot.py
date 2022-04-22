import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

#first trial
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)

#second trial
plt.figure('lin')
plt.clf()
plt.title('Linear')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.title('Quadratic')
plt.ylabel('quadratic function')
plt.plot(mySamples, myQuadratic)
plt.figure('cube')
plt.clf()
plt.title('Cubic')
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.clf()
plt.title('Exponential')
plt.plot(mySamples, myExponential)