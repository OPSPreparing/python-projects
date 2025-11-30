import numpy as np
import pandas as pd
# import openpyxl as op 
# a = pd.read_excel(r"C:\Users\v-navmittal\Desktop\pipelines.xlsx")
# print(a.to_string()) 
# print(type(a))
# print(a.head(5))
# a = {
#     'cars' : ["BMW", "Volvo"],
#     'passings' : [3, 2]  
# }

# df = pd.DataFrame(a)
# print(df)

b = [1,2,3]
c = pd.Series(b)
# print(c)
# print(c[0])
dates = pd.date_range("20130101", periods=6)
# print(dates)
data = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))
numdata= data.to_numpy()
print(numdata)