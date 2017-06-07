import pandas as pd

if __name__ == "__main__":
    predictPath = 'data/recom.csv'
    testPath = 'data/poc_ml_data_.csv'

    predictDf = pd.read_csv(predictPath)
    testDf = pd.read_csv(testPath)
    # predictDf = predictDf[['EWT','SRV','MNT','TLP','RHT','PNTP','ETCH','DENT']]
    testDf = testDf[['EWT','SRV','MNT','TLP','RHT','PNTP','ETCH','DENT','VIN']]
    testDf = testDf.loc[testDf['VIN'].isin(predictDf['VIN'])]
    print len(testDf)
    print len(predictDf)

    predictDf = predictDf.sort(['VIN'])
    testDf = testDf.sort(['VIN'])

    count = 0
    # if we know how many value need to compare
    # we do not need to sum total in loop
    # total = 0
    pickValue = 1
    total = pickValue * len(predictDf)
    for index in range(len(predictDf)):
        predictSerie = predictDf.iloc[index]
        testSerie = testDf.iloc[index]
        if predictSerie['VIN'] != testSerie['VIN']:
            print 'error: vin not match'
        count += testSerie[predictSerie['top1']]
        # count += testSerie[predictSerie['top1']] + testSerie[predictSerie['top2']] + testSerie[predictSerie['top3']]
        # print index, count
        if index % 1000 == 0:
            print 'process: %0.1f %%' %(float(index) * 100 / len(predictDf))
        if index == len(predictDf) - 1:
            print 'process: 100 %'
    # print len(predictDf)
    # for index, predictSerie in predictDf.iterrows():
    #     testSerie = testDf.iloc[index]
    #     print testSerie
    #     print predictSerie
    #     # testSerie = testDf.loc[testDf['VIN'] == predictSerie['VIN']].iloc[0]
    #     count += testSerie[predictSerie['top1']] + testSerie[predictSerie['top2']] + testSerie[predictSerie['top3']]
    #     # testSerie = testDf.iloc[int(predictSerie.iloc[0])]
    #     # temp = predictSerie[['EWT','SRV','MNT','TLP','RHT','PNTP','ETCH','DENT']]
    #     # temp = temp[temp == 1]
    #     # temp2 = testSerie[temp.index]
    #     # total += len(temp)
    #     # count += temp.dot(temp2)
    #     # print index, count
    #     if index % 1000 == 0:
    #         print 'process: %0.1f %%' %(float(index) * 100 / len(predictDf))
    #     if index == len(predictDf) - 1:
    #         print 'process: 100 %'
    #     break
    # print total
    print 'testing result: the accuracy is %s, with %s prediction' %(count / float(total), len(predictDf))
