from recommender import JMA_Product_Recommender
import pandas as pd
import json

if __name__ == "__main__":
    modelPath = 'data/'
    dataPath = 'data/poc_ml_data_.csv'
    # build the recommender
    RECOMMENDER = JMA_Product_Recommender(modelPath, dataPath)

    # add the testing data
    df = pd.read_csv(dataPath)
    y = df[['EWT','SRV','MNT','TLP','RHT','PNTP','ETCH','DENT']]
    x = df.drop(['EWT','SRV','MNT','TLP','RHT','PNTP','ETCH','DENT'], axis=1)

    count = 0
    for index, row in x.iterrows():
        # get predict
        top3 = json.loads(RECOMMENDER.recommend(json.dumps(row.to_dict()), numTop=3))
        # get real
        real = y.iloc[index].to_dict()
        # compare
        for key in top3:
            if real[key] != 0:
                count += 1
        if index % 100 == 0 and index != 0:
            print 'index: %s, accuracy is %s' %(index, float(count)/(index * 3 + 3))

    print 'accuracy is %s' %(float(count)/(len(x) * 3))
