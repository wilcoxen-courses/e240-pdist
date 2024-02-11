"""
demo.py
Spring 2022 PJW

Demonstrate additional important features of Pandas.
"""

import pandas as pd

#
#  Read county population data being careful to keep FIPS codes
#  for both the state and county as strings
#

fips = { 'state':str, 'county':str }
county = pd.read_csv('county_pop.csv',dtype=fips)

#
#  Set the index to the state and county (a two level MultiIndex), 
#  and then rename the population column to make it easier to read.
#

county = county.set_index(['state','county', 'NAME'])
county = county.rename(columns={'B01001_001E':'pop'})

#%%
#
#  Divide the counties into deciles based on their populations
#

dec = pd.qcut( county['pop'], 10, labels=range(1,11) )
print( dec )

#
#  Add the decile into the dataframe as a new column
#

county['dec'] = dec

#%%
#
#  Sort the counties by population
#

county = county.sort_values('pop')

#
#  Use the .xs() method (short for cross-section) to select and 
#  print the counties for state 04, which is Arizona 
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

#
#  Print Arizona's information
#

print( county.xs('04',level='state') )

#
#  Check that each state's counties add up to 100%

grouped = county.groupby('state')

check = grouped['percent'].sum()
print( check )

#%%
#
#  Demonstrate more features of groupby. First, trim the counties down to just 
#  a couple of states for readability. We'll talk more about the .query() 
#  method later in the semester.
#

trimmed = county.query("state =='04' or state == '36'")

#
#  Now group the counties by state and iterate through the groups to show 
#  their structure. Not usually needed.
#

group_by_state = trimmed.groupby('state')

for t,g in group_by_state:
    print(f'\nGroup for type {t}:\n')
    print(g)
    
#%%
#
#  Some quick aggregations, return one row per group
#

print( '\nMedian county population:' )
pop_med = group_by_state['pop'].median()
print( pop_med )

print( '\n25th percentile county population:' )
pop_25th = group_by_state['pop'].quantile(0.25)
print( pop_25th )

#%%
#
#  Some descriptive methods
#

print( '\nRows in each group:' )
num_rows = group_by_state.size()
print( num_rows )

print( '\nPopulation statistics by group:' )
inc_stats = group_by_state['pop'].describe()
print( inc_stats )

print( '\nUpper and lower population quartiles by group:')
print( inc_stats[['25%','75%']])

#%%
#
#  Selecting subsets of the records in each group. The dataframe was sorted 
#  by population so the first and last rows of each group will be that group's
#  smallest and largest populations.
#

print( '\nFirst rows in each group:')
first2 = group_by_state.head(2)
print( first2 )

print( '\nLast rows in each group:')
last2 = group_by_state.tail(2)
print( last2 )

#%%
#
#  The following could be used to find the largest populations if the 
#  data were not already sorted. Returned largest to smallest within
#  each group.
#

print( '\nChoosing rows with largest 2 populations in each group:')
largest = group_by_state['pop'].nlargest(2)
print( largest )

#%%
#
#  Producing information about ungrouped data. These all return objects
#  having the same index as the original data (i.e., 5 rows here with 
#  index columns 'id' and 'type'.
#

print( '\nGroup numbers for raw data:')
groups = group_by_state.ngroup()
print( groups )

print( '\nSequence within group:')
seqnum = group_by_state.cumcount()
print( seqnum )

print( '\nCumulative population within group:')
cumulative_inc = group_by_state['pop'].cumsum()
print( cumulative_inc )

print( '\nRank within group:')
rank_age = group_by_state['pop'].rank()
print( rank_age )

