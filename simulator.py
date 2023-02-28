# Time the program
import time
start_time = time.time()


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from objects import Investor

# Styling the histogram
matplotlib.use('tkAgg')
plt.style.use('_mpl-gallery')

# Global dataframe
df = pd.read_csv(r'final.csv')

# Global vars
N = 1 # Number of investors
results = [] # To store final results
initWealth = 10000 # Initial cash

def main():
    # Get price of the last day
    price = df.iloc[-1]["Price"]

    # Loop through investors
    for i in range(N):
        investor = simulateInvestor()
        investor = simulateInvestment(investor)
        wealth = investor.cash + investor.stock*price
        results.append(wealth)

    # Print mean
    print(sum(results)/N)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    # Drawing Graph
    w=100
    plt.hist(results, bins=np.arange(min(results), max(results) + w, w))
    plt.show()


def simulateInvestment(investor):
    # Loop through all trading days
    for index, day in df.iterrows():
        # Roll dice to see if the investor is doing anything
        p = np.random.random(1)[0]

        # Check if the investor will make any action:
        if p > investor.prob:
            # Get price
            price = float(day["Price"])

            # If cash = 0: sell all stocks
            if investor.cash == 0:
                investor.cash = investor.stock * price
                investor.stock = 0

            # If cash not 0: buy all
            else:
                investor.stock = investor.cash / price
                investor.cash = 0

    return(investor)



def simulateInvestor():
    cash = initWealth
    stock = 0
    prob = np.random.random(1)[0] # Rold dice for procastination probability

    return(Investor(cash, stock, prob))



if __name__ == '__main__':
    main()