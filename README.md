# PandasDataTypes
cleaning data using Pandas

(be sure you have Fork'd and then Clone'd this repo)

- Clear out all the Cell output.
- Step through notebook.
- Create a new python file (sc2.py), that has all the correct and needed steps to transform df[] to that same as the output of df_2[] that gets produced by ./salescleanup.py
  - You will be copying lines from the notebook, and pasting them into the py file.
  - Make sure to only copy the lines that transform the dataframe, not the working attempts at trying to get a single transform step right.
  - when you `python3 ./sc2.py` you should get the same kind of output as this
  - when you achieve the output correctly, `git push` your changes everything to your forked copy.
  
```
(base) Aeneid:notebooks kristofer$ python3 ./salescleanup.py
   Customer Number     Customer Name      2016       2017  Percent Growth  Jan Units  Month  Day  Year Active Start_Date
0            10002  Quest Industries  125000.0   162500.0            0.30      500.0      1   10  2015   True 2015-01-10
1           552278    Smith Plumbing  920000.0  1012000.0            0.10      700.0      6   15  2014   True 2014-06-15
2            23477   ACME Industrial   50000.0    62500.0            0.25      125.0      3   29  2016   True 2016-03-29
3            24900        Brekke LTD  350000.0   490000.0            0.04       75.0     10   27  2015   True 2015-10-27
4           651029         Harbor Co   15000.0    12750.0           -0.15        NaN      2    2  2014  False 2014-02-02
```


#### NB:

If you get the 
```
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate
```
error, perform these steps...

```
# in shell/terminal
$  pip3 install certifi
$  /Applications/Python\ 3.8/Install\ Certificates.command
```

(if your Python3 is 3.8. You might have 3.7, change that in the line above.