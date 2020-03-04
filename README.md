# Exercise: Distributional Analysis Using Pandas

### Summary

This exercise uses Pandas to do the ETR calculation from the earlier
assignment.

### Input Data

Files **households.csv** and **quantities.csv** are the CSV files from the
previous distributional analysis. As you'll probably recall, there 
are 1000 households in the analysis and households.csv has their attributes. 
It has five columns, `id`, `type`, `inc`, `a` and `b`, and there is one row 
for each household. The second file, quantities.csv, has three columns: 
`id`, `qd1`, and `qd2` and again there is one row for each household.

### Deliverables

A script called **etr.py** that carries out the calculations described 
below.

### Instructions

1. Import pandas as pd.

1. Create a dataframe called `hh` by using `pd.read_csv()` to read
households.csv. Use the keyword `index_col='id'` to set the index 
to the `id` field for each household.

1. Create a dataframe called `q` by using `pd.read_csv()` to read
quantities.csv. Again use the keyword `index_col='id'` to set the index 
to the `id` field for each household.

1. Compute the income quintile of each household using the Pandas call 
    `pd.qcut()` and add it to the `hh` dataframe as column 'quint'. The
    first argument to `qcut()` should be the column of incomes,
    `hh['inc']`, the  second argument should be 5 to request quintiles,
    and the third should be `labels=[1,2,3,4,5]` to have the quintiles
    labeled 1-5. To avoid confusion, please note that `pd.qcut()` is a
    standalone Pandas function that is invoked like this:
    
    ```
    some_variable_here = pd.qcut(some_arguments_here)
    ```
    That is, it is *not* a method built into the series and dataframe
    objects so it is *not* invoked like this: `variable.qcut()`.
    
1. As in the earlier exercise, create a variable called `pd1` that is equal 
to 53.35 and one called `pd2` equal to 55.27. Then create a variable called 
`dp` that is equal to `pd2 - pd1`.

1. Compute the ETRs by multiplying 100 times `dp` times the `qd2` column 
of `q` divided by the `inc` column of `hh`. Note that this would work
correctly no matter what order `hh` and `q` were in because Pandas will 
use the indexes to match up the income and quantity variables. Store 
the result in the `hh` dataframe as column 'etr'.

1. Now group the data by type and quintile by creating a variable called
`grouped` that is the result of using the `groupby()` call on `hh` with
the list `['type','quint']` as its argument.

1. Create a variable called `grouped_etrs` that is equal to the 'etr'
column of `grouped`.

1. Compute the median ETR for each group by applying the `median()`
method of `grouped_etrs` and then applying the `round(2)` method to round
the ETRs to 2 digits. Store the result in a variable called `medians`.

1. Print `medians`. Be sure to look over the result to make sure it 
matches the previous results. Note that Pandas automatically omits 
repeated headings.

1. Now print a blank line and then print `medians.index`. Notice that it's 
a MultiIndex, which is really just a list of tuples where the first 
element is the type and the second is the quintile. That makes it 
possible to pull out subsets of the information, which we'll do next. 

1. Print an appropriate heading and then list the medians for type 3
by printing `medians[3]`. The `[3]` instructs Pandas to pick out all 
the elements where 3 is the first element in the index tuple.

1. Print an appropriate heading and then list the medians for the 5th 
quintile by printing `medians[:,5]`. The 5 indicates that tuples with 
5 in the quintile position should be printed, and the colon is a 
placeholder that indicates that all types (the first element in the 
tuples) should be included. 

1. Print an appropriate heading and then print the median ETR for type 3, 
quintile 5, by printing `medians[3,5]`.

1. Finally, to really show the power of the automatic alignment built 
into Pandas, print an appropriate heading and then print `medians - 
medians[:,1]`. That will show how much higher the ETR is for each quintile 
for a given type relative to the first one for that type. Pandas will 
automatically align the data to ensure that the household type matches when
doing the subtraction.

### Submitting

Once you're happy with everything and have committed all of the changes to
your local repository, please push the changes to GitHub. At that point, 
you're done: you have submitted your answer.

### Tips

+ It would be easy to add the additional aggregations from the earlier
exercise by adding a couple more `groupby()` calls to group the data by 
'type' and 'quint' separately.

+ It's probably painfully clear from the difference between this 
exercise and the previous one that Pandas is incredibly useful for 
data analytics. The key reason is that it has a lot of very, very 
common operations baked into it. The really important ones illustrated 
here are: reading the data and converting variables to numeric form;
automatically handling alignment of variables based on keys (the 
household id in this case); applying calculations to blocks of data 
without needing explicit for loops; and very easy grouping and 
aggregation. Behind the scenes it's going through exactly the same steps
you used in the earlier exercise, but with a lot less coding on your 
part.
