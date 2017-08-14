import pandas as pd
import numpy as np
import os
import operator
accList = []
decList = []
fileNames = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(".csv") and '20' not in file:
            df = pd.read_csv(file)
            featureDict = df[df.columns.tolist()].mean().to_dict()
            featureAcc = sorted(featureDict.items(), key=operator.itemgetter(1))[:20]
            featureDec = sorted(featureDict.items(), key=operator.itemgetter(1), reverse=True)[:20]
            accList.append(featureAcc)
            decList.append(featureDec)
            with open(file[:-4] + '_feature.txt', 'w') as f:
                fileNames.append(file[:-4])
                f.write('bottom 20\n')
                f.write("\n".join([str(items[0]) + ": " + str(items[1]) for items in featureAcc[:20]]))
                f.write('\n\n\n')
                f.write('top 20\n')
                f.write("\n".join([str(items[0]) + ": " + str(items[1]) for items in featureDec[:20]]))


accList = [dict(item) for item in accList]
decList = [dict(item) for item in decList]

accDf = pd.DataFrame().from_dict(accList)
accDf['product'] = fileNames
cols = accDf.columns.tolist()
cols = cols[-1:] + cols[:-1]
accDf = accDf[cols]
accDf.transpose().to_csv('bottom20.csv', index=True)

decDf = pd.DataFrame().from_dict(decList)
decDf['product'] = fileNames
cols = decDf.columns.tolist()
cols = cols[-1:] + cols[:-1]
decDf = decDf[cols]
decDf.transpose().to_csv('top20.csv', index=True)
