"""
Pandas Udemy;
Oussama Rjab
series
"""

import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d= {'a':10,'b':20,'c':30} #dictinary

pd.Series(data=my_data)
"""
0	10
1	20
2	30
dtype: int64
"""
pd.Series(data=my_data,index=labels)
#pd.Series(my_data,labels)
"""
a	10
b	20
c	30
dtype: int64
"""
pd.Series(d)
"""
a	10
b	20
c	30
dtype: int64
"""

ser1=pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])
"""
USA		1
Germany	2
USSR	3
Japan	4
dtype: int64
"""

ser2=pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
"""
USA		1
Germany	2
Italy	5
Japan	4
dtype: int64
"""

ser1['USA']
"""
1
"""

ser3=pd.Series(data=labels)

ser1+ser2
"""
Germany		4.0
Italy		NaN
Japan		8.0
USA			2.0
USSR		NaN
dtype: float64
"""