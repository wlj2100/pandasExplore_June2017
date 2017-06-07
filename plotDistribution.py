import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import collections

def plotDataDict(dataDict):
    for key in dataDict:
        plt.clf()
        if len(dataDict[key]) < 20:
            od = collections.OrderedDict(sorted(dataDict[key].items()))
            f, axarr = plt.subplots(1, 2)

            axarr[0].bar(range(len(od.keys())), od.values())
            axarr[0].set_xticks(range(len(od.keys())))
            axarr[0].set_xticklabels(od.keys())
            axarr[1].pie([od[val] for val in od], labels=[val for val in od], autopct='%1.1f%%')
            axarr[1].axis('equal')
            plt.suptitle(key + ' analysis')
            # plt.savefig(key+'.png', dpi=200)
            plt.show()
        elif len(dataDict[key]) < 100:
            od = collections.OrderedDict(sorted(dataDict[key].items()))
            plt.bar(range(len(od.keys())), od.values(), 0.3)
            plt.xticks(range(len(od.keys())), od.keys(), rotation='vertical')
            plt.title(key + ' analysis')
            # plt.savefig(key+'.png', dpi=250)
            plt.show()
        else:
            print key, len(dataDict[key])
        
        

        
        # try:
        #     f, axarr = plt.subplots(1, 2)
        #     axarr[0, 0].bar(range(len(dataDict[key].keys())), dataDict[key].values(), 0.5)
        #     axarr[0, 0].set_xticks(range(len(dataDict[key].keys())))
        #     axarr[0, 0].set_xticklabels(dataDict[key].keys())
        #     axarr[0, 0].set_title('polarity')
        #     axarr[0, 1].pie([dataDict[key][val] for val in dataDict[key]], labels=[val for val in dataDict[key]], autopct='%1.1f%%')
        #     axarr[0, 1].axis('equal')
        #     plt.suptitle(key + ' analysis')
        #     plt.show()
        # except:
        #     print 'error in %s' %(key)

def write_file(data, fileName):
    with open(fileName, 'w') as outfile:
        json.dump(data, outfile)

def read_file(path):
    with open(path) as data_file:
        data = json.load(data_file)
    return data

if __name__ == "__main__":
    dataPath = 'data/poc_ml_data_.csv'
    df = pd.read_csv(dataPath)
    # [u'VIN', u'EWT', u'SRV', u'MNT', u'TLP', u'RHT', u'PNTP',
    #    u'ETCH', u'DENT', u'FND_AM', u'APR', u'AGE', u'GENDER', u'ZIP', u'MAKE',
    #    u'MODEL', u'YEAR', u'MILAGE', u'PURCHASE_LEASE', u'LOAN_TERM',
    #    u'FND_AM_BIN', u'APR_BIN', u'AGE_BIN']
    # df.iloc[0]
    # keyList = []
    # dataDict = {}
    # for i in range(10, len(df.columns)):
    #     keyList.append(df.columns[i])
    # for key in keyList:
    #     dataDict[key] = {}
    # print keyList
    # print dataDict
    # for index in range(len(df)):
    #     series = df.iloc[index]
    #     for key in keyList:
    #         if series[key] in dataDict[key]:
    #             dataDict[key][series[key]] += 1
    #         else:
    #             dataDict[key][series[key]] = 1
    #     if index % 10000 == 0:
    #         print 'process: %0.1f %%' %(float(index) * 100 / len(df))
    #     if index == len(df) - 1:
    #         print 'process: 100 %'
    # write_file(dataDict, 'dataDict.json')
    dataDict = read_file('dataDict.json')
    # print dataDict
    plotDataDict(dataDict)

    # pd.options.display.mpl_style = 'default'
    # df.boxplot()
