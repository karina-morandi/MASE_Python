import pandas as pd
from tabulate import tabulate

def main():
        data = {'Name': ['Seán', 'Aoife', 'Oisín', 'Siobhan', 'Aoibheann', 'Odhrán'],
                'Age': [25, 30, 16, 25, 44, 32],
                'Location': ['Galway City', 'Kinvara', 'Cliften', 'Athenry', 'Inis More', 'Connemara']}
        df = pd.DataFrame(data)
        df['Location'] = df['Location'].str.replace('a', '@')
        print(tabulate(df, headers='keys', tablefmt='pretty'))

if __name__=='__main__':
    main()


