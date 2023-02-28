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
N = 100 # Number of investors
initWealth = 10000 # Initial cash

def main():
    # Get price of the last day
    results = simulateInvestment(N).tolist()

    # Print mean
    print(sum(results)/N)
    print("--- %s seconds ---" % (time.time() - start_time))
    
    # Drawing Graph
    w=100
    plt.hist(results, bins=np.arange(min(results), max(results) + w, w))
    plt.show()


def simulateInvestment(inv_num: int) -> np.ndarray:
    cash = np.full(inv_num, initWealth, np.float32)
    stock = np.zeros(inv_num, np.float32)
    proc_prob = np.random.random(inv_num) # Rolled dice for procastination probability

    zero = np.zeros(inv_num, np.float32)
    # Loop through all trading days
    for _, day in df.iterrows():
        price = np.full(inv_num, float(day["Price"]), np.float32)

        # Roll dice to see if the investor is doing anything
        p = np.random.random(inv_num)
        action = (p > proc_prob)
        no_action = np.logical_not(action)

        # Calculate
        no_cash = (cash == zero)
        has_cash = np.logical_not(no_cash)
        sell_all_cash = stock * price
        buy_all_stock = cash / price

        action_cash = np.select([no_cash, has_cash], [sell_all_cash, zero])
        action_stock = np.select([no_cash, has_cash], [zero, buy_all_stock])

        cash = np.select([action, no_action], [action_cash, cash])
        stock = np.select([action, no_action], [action_stock, stock])

    return cash + stock * price

if __name__ == '__main__':
    main()