import pandas as pd
import numpy as np

if __name__ == '__main__':
    # read origin csvs
    df = pd.read_csv('poc_ml_data_v3.csv')
    # remove null in DLR_ZIP3
    # df[['DLR_ZIP3']] = df[['DLR_ZIP3']].apply(pd.to_numeric)
    df[['DLR_ZIP3']] = df[['DLR_ZIP3']].astype(str)
    df = df[df.DLR_ZIP3 != '(nu']

    # new dlrZip2
    df['DLR_ZIP2'] = df['DLR_ZIP3'].astype(str).str[:2]

    # loanTermBins
    loanTermBinRange = [0, 0.5, 12, 24, 36, 48, 60, 100]
    loanTermBinLabels = range(len(loanTermBinRange) - 1)
    df['LOAN_TERM_BIN'] = pd.cut(df['LOAN_TERM'], loanTermBinRange, include_lowest=True, labels=loanTermBinLabels)
    # df['LOAN_TERM_BIN'] = pd.cut(df['LOAN_TERM'], loanTermBinRange, include_lowest=True)

    # RECENT_YEAR
    df['RECENT_YEAR'] = df['YEAR'].astype(str)
    df.loc[(df.RECENT_YEAR.astype(int) > 17) | (df.RECENT_YEAR.astype(int) < 10) , 'RECENT_YEAR'] = np.nan

    # generate new DataFrame with keep feature
    newDf = df[['VIN', 'EWT', 'SRV', 'MNT', 'TLP', 'RHT', 'PNTP', 'ETCH', 'DENT']]


    # print df.columns
    temp = pd.get_dummies(df[['MILAGE_BIN', 'AGE_BIN', 'APR_BIN', 'FND_AM_BIN', 'DLR_ZIP2', 'PURCHASE_LEASE', 'GENDER', 'MAKE', 'MODEL', 'LOAN_TERM_BIN', 'RECENT_YEAR']])

    newDf = pd.concat([newDf, temp], axis=1)



    # print newDf.columns
    newDf.to_csv('converted.csv', index=False)
