from operator import index
import pandas as pd
import os
#Threshhold
systolic = 180
diastolic = 120

#function to parse blood pressure and highlights if hypertensive crisis
def highlight_cells(bp):
    try:
        bp = bp.split("/")
        sys = int(bp[0])
        dia = int(bp[1])
    except:
        color = '#EBECF0'
        return 'background-color: {}'.format(color)
    
    
    color = '#FF7F7F' if sys >= systolic or dia >= diastolic else '#EBECF0'
    
    return 'background-color: {}'.format(color)

#Change out.xlsx is the read in file
df = pd.read_excel("out.xlsx", "Sheet1")
df = df.style.applymap(highlight_cells, subset='Message')
#BP_Colored is the out file
df.to_excel("BP_Colored.xlsx", index = False)
print("Completed")

