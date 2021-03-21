#! /bin/python3
#  Spring 2020 (PJW)

import pandas as pd

#
#  Read county population data being careful about FIPS codes
#

fips = { 'state':str, 'county':str }
county = pd.read_csv('county_pop.csv',dtype=fips)

#
#  Set the index to the state and county, and then rename the 
#  population column to make it easier to read.
#

county = county.set_index(['state','county'])
county = county.rename({'B01001_001E':'pop'},axis='columns')

#%%
#
#  Divide the counties into deciles based on their populations
#

dec = pd.qcut( county['pop'], 10, labels=range(1,11) )
print( dec )

#
#  Add the decile into the dataframe
#

county['dec'] = dec

#%%
#
#  Sort the counties by population
#

county = county.sort_values('pop')

#
#  Use the .xs() method to select and print the counties for 
#  state 04, which is Arizona 
#

print( county.xs('04',level='state') )

#
#  Now group the counties by state and calculate each state's population. 
#  Then sort by population and print.
#

state = county.groupby('state')['pop'].sum()
state = state.sort_values()

print( state )

#
#  Calculate each county's population as a percent of its state's 
#  population. Note that this works even though county has two index 
#  levels (state and county) and state has only one (state), and on 
#  top of that, state is in a different order. Pandas automatically
#  aligns the common index level (state) and broadcasts the state 
#  populations across each state's counties.
#

county['percent'] = 100*county['pop']/state

print( county.xs('04',level='state') )

#
#  Check that each state's counties add up to 100%

check = county.groupby('state')['percent'].sum()
print( check )
