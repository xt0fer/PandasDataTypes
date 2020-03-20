import pandas as pd
import numpy as np

def convert_currency(val):
    """
    $125,000.00 -> 125000.00
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)

def convert_percent(val):
    """
    Convert the percentage string to an actual floating point percent
    """
    new_val = val.replace('%', '')
    return float(new_val) / 100

df_2 = pd.read_csv("https://github.com/chris1610/pbpython/blob/master/data/sales_data_types.csv?raw=True", 
                   dtype={'Customer Number':'int'},
                   converters={'2016':convert_currency,
                               '2017': convert_currency,
                               'Percent Growth': convert_percent,
                               'Jan Units': lambda x: pd.to_numeric(x, errors='coerce'),
                               'Active': lambda x: np.where(x == "Y", True, False)
                              })

df_2["Start_Date"] = pd.to_datetime(df_2[['Month', 'Day', 'Year']])

print(df_2)

# Should output something like:

# (base) Aeneid:notebooks kristofer$ python3 ./salescleanup.py
#    Customer Number     Customer Name      2016       2017  Percent Growth  Jan Units  Month  Day  Year Active Start_Date
# 0            10002  Quest Industries  125000.0   162500.0            0.30      500.0      1   10  2015   True 2015-01-10
# 1           552278    Smith Plumbing  920000.0  1012000.0            0.10      700.0      6   15  2014   True 2014-06-15
# 2            23477   ACME Industrial   50000.0    62500.0            0.25      125.0      3   29  2016   True 2016-03-29
# 3            24900        Brekke LTD  350000.0   490000.0            0.04       75.0     10   27  2015   True 2015-10-27
# 4           651029         Harbor Co   15000.0    12750.0           -0.15        NaN      2    2  2014  False 2014-02-02
