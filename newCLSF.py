import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import ShuffleSplit
from sklearn import linear_model
import matplotlib.pyplot as plt

def classify(X, y, clf, xGroup, yName):
    # clf = clf.fit(X, y)
    # print 'overall accuracy: ', clf.score(X, y)

    ss = ShuffleSplit(n_splits=5, test_size=0.25,random_state=0)

    acc = []
    featureImportances = []
    coefs = []
    for train, test in ss.split(X):
        # print("%s %s" % (train, test))
        # break
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
        # break
        clf.fit(X_train, y_train)
        acc.append(clf.score(X_test, y_test))
        # featureImportances.append(clf.feature_importances_)
        coefs.append(clf.coef_)
    print acc
    print 'avg acc:', np.average(acc)
    # print 'feature importance:'
    # for importance in featureImportances:
    #     print importance
    # print 'coef:'
    # for coef in coefs:
    #     print coef
    # tempList = [coef[0] for coef in coefs]
    # print np.mean(tempList, axis=0)
    print len(coefs)
    # yName = 'temp.csv'
    with open(yName+'.csv', 'w') as f:
        for item in xGroup:
            f.write(str(item) + ',')
        f.write('\n')
        for coef in coefs:
            plt.plot(coef[0])
            for item in coef[0]:
                f.write(str(item) + ',')
            f.write('\n')


    # plt.xticks(range(len(coefs[0][0])), xGroup, rotation='vertical')
    plt.title(yName)
    # plt.rc('xtick', labelsize=10)
    # plt.legend()
    # plt.show()
    plt.savefig(yName + '.png', dpi=500)

# def mul_classify(X, y_all):
#     clf_list = []
#     for i in range(y_all):
#         clf_list.append()

if __name__ == '__main__':
    # read origin csvs
    df = pd.read_csv('head.csv')
    print df.shape
    # remove null in DLR_ZIP3
    # df[['DLR_ZIP3']] = df[['DLR_ZIP3']].apply(pd.to_numeric)
    # df[['DLR_ZIP3']] = df[['DLR_ZIP3']].astype(str)
    # df = df[df.DLR_ZIP3 != '(nu']


    # colList = df.columns.tolist()
    #
    # print colList.index('MALE')
    # print colList.index('DLR_ZIP3_212')
    # print colList.index('DLR_ZIP3_29')
    # print colList[10:203]
    #
    # print colList.index('VIN')
    # print colList.index('EWT')


    # facorizedDf = df.apply(lambda x: pd.factorize(x)[0])
    facorizedDf = df
    yGroup = ['EWT','SRV','MNT','TLP','RHT','PNTP','ETCH','DENT']
    # print len(yGroup)
    y_all = [facorizedDf[columnname].tolist() for columnname in yGroup]

    xGroup = df.columns.tolist()[10:]
    # xGroup = df.columns.tolist()[10:202] + df.columns.tolist()[640:]
    # xGroup = ['FND_AM','APR','AGE','GENDER','ZIP','MAKE','MODEL','YEAR','MILAGE','PURCHASE_LEASE','LOAN_TERM','DLR_ZIP3','CUST_ZIP3','CASH_DEAL']
    x_all = np.array([np.array(facorizedDf[columnname].tolist()) for columnname in xGroup])
    X = x_all.transpose()
    y = np.array(y_all[0])
    # clf = RandomForestClassifier(n_estimators=10, n_jobs=4)
    clf = linear_model.LogisticRegression(C=1e5, n_jobs=4)
    for i in range(len(y_all)):
        print yGroup[i]
        classify(X, np.array(y_all[i]), clf, xGroup, yGroup[i])
        # break
