import pandas as pd
import numpy as np

dataPath = 'data/poc_ml_data_.csv'
df = pd.read_csv(dataPath)

# print df.columns.values
# print len(df.columns.values)
# print df.iloc[0]
# print df.columns.get_loc('FND_AM')
# df.ix[0]
#
# pd.get_dummies(df['GENDER'], drop_first=True)
#
# print gender


# print df[['EWT']].corrwith(df.ix[:, 10:11], axis=0,drop=True)
len(df)
print df[0:1000000].corr()



newDf = pd.get_dummies(df, drop_first=True)

print newDf[:1000000].corr()



# print df['EWT', 0:10].corr(pd.get_dummies(df['GENDER'], drop_first=True))
