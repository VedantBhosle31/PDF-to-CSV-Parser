from PyPDF2 import PdfReader
import numpy as np
import pandas as pd

reader = PdfReader("liq nitrus oxide.pdf")
page = reader.pages[0]
page1=page.extract_text()
print(page1.split(sep="ft3)\n")[-1])

data=""
for i in reader.pages:
        data=data+i.extract_text().split(sep="ft3)\n")[-1]+"\n"

print("Data in Text fromat\n",data)

test=data[:-1].split("\n")

nums=[[float(i) for i in test[j].split()] for j in range(len(test))]

for i in range(len(nums)):
    if len(nums[i])<12:
        # print(nums[i])
        nums[i]= nums[i] + [None]*(12-len(nums[i]))
        # print(nums[i])

dataset=[[i[:3]] +[i[3:6]]+[i[6:9]]+[i[9:12]] for i in nums]

dataset=dataset[:-1]

dataset.sort()
df=pd.DataFrame(dataset)
df=df.dropna()
df.to_csv('codeGenerated.csv')