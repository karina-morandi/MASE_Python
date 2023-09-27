import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import time

def main():
    pd.options.display.float_format = '{:.2f}'.format
    print("Pandas Lab")
    local_file = 'https://davmase.z6.web.core.windows.net/data/sales.csv'
    start = time.time()
    sales = pd.read_csv(local_file)
    end = time.time()
    print('Time taken to load data: {0:.5f} seconds'.format((end-start)))

    print(sales.info(verbose=True, memory_usage='deep', show_counts=True))

if __name__ == '__main__':
    main()