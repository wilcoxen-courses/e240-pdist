#! /bin/python3
#  Spring 2020 (PJW)

import pandas as pd

incomes = pd.read_csv('state-data.csv',index_col='name')
geocodes = pd.read_csv('state-geocodes.csv',index_col='Name')

#%%

incomes['reg'] = geocodes['Region']
incomes['div'] = geocodes['Division']
incomes['fips'] = geocodes['State FIPS']

grouped = incomes.groupby(['reg','div']) 

grouped_pop = grouped['pop']

totals = grouped_pop.sum()/1e6

print(totals.round(1))

#%%

print( totals.index )

print( '\nRegion: Northeast')
print( totals[1] )

print( '\nDivision: New England')
print( totals[:,1] )
