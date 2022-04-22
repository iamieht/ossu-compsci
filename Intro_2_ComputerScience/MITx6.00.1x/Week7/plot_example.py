import pylab as plt

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1 + mRate) + monthly]
    return base, savings

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate. terms)
        plt.plot(xvals, yvals, label = 'retire:' + str(monthly))
        plt.legend(loc = 'upper left')

def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:'+str(month)+':'+str(int(rate*100)))
        plt.legend(loc = 'upper left')

displayRetireWMonthlies([500,600,700,800,900,1000,1100], .05, 40*12)
displayRetireWRates(800, [.03, .05, .07], 40*12)