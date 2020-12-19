import pandas as pd
import plotly.graph_objects as go

dataframe = pd.read_csv("Datagraphsdata.csv")


'''
#Groupby code (groups the attempts by the level): 
print(dataframe.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    y= dataframe.groupby("level")["attempt"].mean() ,
    x= ["Level 1","Level 2","Level 3","Level 4"]
))

fig.show()
'''


'''
#Groupby code (Groups the attempts by the student id(horizontal orientation))
print(dataframe.groupby("student_id")["attempt"].mean())

fig = go.Figure(go.Bar(
    x= dataframe.groupby("student_id")["attempt"].mean() ,
    y= ["TRL_123","TRL_987","TRL_abc","TRL_imb","TRL_mda" ,"TRL_mno","TRL_rst","TRL_xsl","TRL_xyz","TRL_zet","TRL_zny"],
    orientation = 'h'
))

fig.show()
'''
'''
#Groupby code (Groups the attempts by level from the data of ONE student)
TRL1 = (dataframe.loc[dataframe['student_id'] == "TRL_xsl"])
print(TRL1.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    y= TRL1.groupby("level")["attempt"].mean() ,
    x= ["Level 1","Level 2","Level 3","Level 4"]
))

fig.show()
'''