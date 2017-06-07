import pandas as pd
import numpy as np

def gender(val):
    m = 0
    f = 0
    if val == 'M':
        m = 1
    elif val == 'F':
        f = 1
    return m, f

# df.FND_AM_BIN.unique()
# array([13,  5, 11,  7,  1,  0,  6,  3, 12,  2, 14,  9,  4, 10,  8])
def getResult(val, labelList):
    temp = []
    for label in labelList:
        if str(val) == str(label):
            temp.append(1)
        else:
            temp.append(0)
    return tuple(temp)

def fnd(val):
    labelList = [13,  5, 11,  7,  1,  0,  6,  3, 12,  2, 14,  9,  4, 10,  8]
    return getResult(val, labelList)

def apr(val):
    labelList = [4, 1, 7, 6, 3, 0, 5, 8, 2]
    return getResult(val, labelList)

def age(val):
    labelList = [5, 1, 0, 2, 4, 3]
    return getResult(val, labelList)

def make(val):
    labelList = ['JEEP', 'DODGE', 'RAM', 'CHRYSLER', 'SUBARU', 'FORD', 'THIS IS',
       'CHEVROLET', 'MITSUBISHI', 'PONTIAC', 'OLDSMOBILE', 'BUICK',
       'CADILLAC', 'SATURN', 'GMC', 'ISUZU', 'HARLEY', 'HONDA', 'LINCOLN',
       'MERCURY', 'NISSAN', 'TOYOTA', 'VOLKSWAGEN', 'MAZDA', 'ACURA',
       'SUZUKI', 'LEXUS', 'FIAT', 'KIA', 'SCION', 'MERCEDES', 'BMW',
       'HUMMER', 'INFINITI', 'HYUNDAI', 'VOLVO', 'JAGUAR', 'LAND ROVER',
       'LOTUS', 'AUDI', 'SMART', 'MINI', 'PORSCHE', 'SAAB', 'MASERATI',
       'GAP', 'ALFA ROMEO', 'GENESIS']
    return getResult(val, labelList)

def year(val):
    labelList = [14, 15, 16, 17, 12, 13,  4,  8,  7,  9,  6,  5,  3, 10, 11,  2, 20,
       90, 98,  0,  1, 99, 97, 95, 93, 89, 96, 94, 91, 92]
    return getResult(val, labelList)

def pl(val):
    labelList = ['P', 'L']
    return getResult(val, labelList)
# Index([u'Unnamed: 0', u'VIN', u'EWT', u'SRV', u'MNT', u'TLP', u'RHT', u'PNTP',
#        u'ETCH', u'DENT', u'FND_AM', u'APR', u'AGE', u'GENDER', u'ZIP', u'MAKE',
#        u'MODEL', u'YEAR', u'MILAGE', u'PURCHASE_LEASE', u'LOAN_TERM',
#        u'DLR_ZIP3', u'CUST_ZIP3', u'FND_AM_BIN', u'APR_BIN', u'AGE_BIN'],
#       dtype='object')

if __name__ == '__main__':
    # read origin csvs
    df = pd.read_csv('poc_ml_data_v3_.csv')
    # generate new DataFrame with keep feature
    newDf = df[['VIN', 'EWT', 'SRV', 'MNT', 'TLP', 'RHT', 'PNTP', 'ETCH', 'DENT']]

    # for GENDER
    len(df.GENDER.unique())
    newDf['MALE'], newDf['FEMALE'] = zip(*df['GENDER'].map(gender))
    # for FND_AM_BIN
    len(df.FND_AM_BIN.unique())
    tempDf = pd.DataFrame(data = np.array(zip(*df['FND_AM_BIN'].map(fnd))).T, columns = ['FND_AM_BIN_' + str(val) for val in df.FND_AM_BIN.unique()])
    newDf[tempDf.columns] = tempDf
    # for APR_BIN
    len(df.APR_BIN.unique())
    tempDf = pd.DataFrame(data = np.array(zip(*df['APR_BIN'].map(apr))).T, columns = ['APR_BIN_' + str(val) for val in df.APR_BIN.unique()])
    newDf[tempDf.columns] = tempDf
    # for AGE_BIN
    len(df.AGE_BIN.unique())
    tempDf = pd.DataFrame(data = np.array(zip(*df['AGE_BIN'].map(age))).T, columns = ['AGE_BIN_' + str(val) for val in df.AGE_BIN.unique()])
    newDf[tempDf.columns] = tempDf
    # for MAKE
    len(df.MAKE.unique())
    tempDf = pd.DataFrame(data = np.array(zip(*df['MAKE'].map(make))).T, columns = ['MAKE_' + str(val) for val in df.MAKE.unique()])
    newDf[tempDf.columns] = tempDf
    # for YEAR
    len(df.YEAR.unique())
    tempDf = pd.DataFrame(data = np.array(zip(*df['YEAR'].map(year))).T, columns = ['YEAR_' + str(val) for val in df.YEAR.unique()])
    newDf[tempDf.columns] = tempDf
    # for PURCHASE_LEASE
    len(df.PURCHASE_LEASE.unique())
    tempDf = pd.DataFrame(data = np.array(zip(*df['PURCHASE_LEASE'].map(pl))).T, columns = ['PURCHASE_LEASE_' + str(val) for val in df.PURCHASE_LEASE.unique()])
    newDf[tempDf.columns] = tempDf
    # ignore
    # for model
    len(df.MODEL.unique())
    len(df.LOAN_TERM.unique())
    len(df.DLR_ZIP3.unique())
    len(df.CUST_ZIP3.unique())

    newDf.to_csv('output.csv')
    len(newDf.columns)
    newDf.describe()
