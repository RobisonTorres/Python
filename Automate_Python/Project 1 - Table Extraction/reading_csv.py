import pandas as pd
import camelot
print('Automate with Python – Full Course for Beginners')
print('Project #1 Table Extraction - Extract Tables from Websites')

# reading 1 csv file from the website
df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')
# rename columns
df_premier21.rename(columns={'Date':'date',
                             'HomeTeam':'home_team',
                             'AwayTeam':'away_team',
                             'FTHG': 'home_goals',
                             'FTAG': 'away_goals'}, inplace=True)
print(df_premier21)

# reading web page
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
# Showing the top five
print(simpsons[1].head())

# reading pdf file
tables = camelot.read_pdf('foo.pdf', pages='1', flavor='lattice')
tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')  # To export the first table (only) to csv file
print(tables[0].df)  # To show as dataframe
