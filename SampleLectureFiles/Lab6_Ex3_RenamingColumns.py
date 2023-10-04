import pandas as pd
from tabulate import tabulate

def main():
        data = {'who': ['Seán', 'Aoife', 'Oisín', 'Siobhan', 'Aoibheann', 'Odhrán'],
                'old': [25, 30, 16, 25, 44, 32],
                'where': ['Galway City', 'Kinvara', 'Cliften', 'Athenry', 'Inis More', 'Connemara']}
        df = pd.DataFrame(data)
        print(tabulate(df, headers='keys', tablefmt='pretty'))
        df.rename(columns={'who': 'Name', 'old' : 'Age', 'where': 'Location'}, inplace=True)
        print("After Rename:\n", tabulate(df, headers='keys', tablefmt='pretty'))

if __name__=='__main__':
    main()


