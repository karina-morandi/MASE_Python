import pandas as pd

def main():
    file_path = 'https://davmase.z6.web.core.windows.net/data/sales.csv'
    polls = pd.read_csv(file_path, verbose=True)
    print('Print DataFrame Info')
    print(polls.info())
    print('\nPrint Number of Unique Items')
    print(polls.nunique())
    print('\nPrint Number of Unique Items in Each Column')
    print(polls.apply(pd.unique))


if __name__ == "__main__":
    main()


