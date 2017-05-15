import pandas as pd
import numpy as np 
import matplotlib as plt
from sklearn.preprocessing import MinMaxScaler

"""

offers = pd.read_csv('offers.csv')

sampleSubmission = pd.read_csv('sampleSubmission.csv')

testHistory = pd.read_csv('testHistory.csv')

trainHistory = pd.read_csv('trainHistory.csv')

transactions = pd.read_csv('transactions.csv')
"""
"""
# Investigation on Offers

print (offers.describe())
print (offers.shape)
print (offers.head(3))

# Investigation on testHistory
print (testHistory.describe())
print (testHistory.shape)
print (testHistory.head(3))

# Investigation on trainHistory
print (trainHistory.describe())
print (trainHistory.shape)
print (trainHistory.head(3))

#invertigations on transactions 
print (transactions .describe())
print (transactions .shape)
print (transactions .head(3))

"""
"""
#Unique offers 

offers_unique_offer = offers.offer.unique()
offers_unique_offer= np.asarray(offers_unique_offer)
np.savetxt("offers_unique_offer.csv", offers_unique_offer, delimiter= ",")

offers_unique_category = offers.category.unique()
offers_unique_category=np.asarray(offers_unique_category)
np.savetxt("offers_unique_category.csv", offers_unique_category, delimiter = ",")

offers_unique_company = offers.company.unique()
offers_unique_company = np.asarray(offers_unique_company)
np.savetxt("offers_unique_company.csv", offers_unique_company, delimiter = ",")

offers_unique_brand = offers.brand.unique()
offers_unique_brand = np.asarray(offers_unique_brand)
np.savetxt("offers_unique_brand.csv", offers_unique_brand, delimiter = ",")





#Unique trainhistory

trainHistory_unique_id = trainHistory.id.unique()
trainHistory_unique_id=np.asarray(trainHistory_unique_id)
np.savetxt("trainHistory_unique_id.csv", trainHistory_unique_id, delimiter = ",")

trainHistory_unique_chain = trainHistory.chain.unique()
trainHistory_unique_chain = np.asarray(trainHistory_unique_chain)
np.savetxt("trainHistory_unique_chain.csv", trainHistory_unique_chain,delimiter = ",")

trainHistory_unique_offer = trainHistory.offer.unique()
trainHistory_unique_offer = np.asarray(trainHistory_unique_offer)
np.savetxt("trainHistory_unique_offer.csv", trainHistory_unique_offer, delimiter = ",")

trainHistory_unique_market = trainHistory.market.unique()
trainHistory_unique_market = np.asarray(trainHistory_unique_market)
np.savetxt("trainHistory_unique_market.csv", trainHistory_unique_market, delimiter = ",")



#Unique transaction

transactions_unique_id = transactions.id.unique()
transactions_unique_id = np.asarray(transactions_unique_id)
np.savetxt("transactions_unique_id.csv", transactions_unique_id, delimiter = ",")                                    
                                    
transactions_unique_chain = transactions.chain.unique()
transactions_unique_chain = np.asarray(transactions_unique_chain)
np.savetxt("transactions_unique_chain.csv", transactions_unique_chain, delimiter = ",")


transactions_unique_dept = transactions.dept.unique()
transactions_unique_dept = np.asarray(transactions_unique_dept)
np.savetxt("transactions_unique_dept.csv", transactions_unique_dept, delimiter = ",")

transactions_unique_category = transactions.category.unique()
transactions_unique_category = np.asarray(transactions_unique_category)
np.savetxt("transactions_unique_category.csv", transactions_unique_category, delimiter = ",")

transactions_unique_company = transactions.company.unique()
transactions_unique_company = np.asarray(transactions_unique_company)
np.savetxt("transactions_unique_company.csv", transactions_unique_company, delimiter = ",")

transactions_unique_brand = transactions.brand.unique()
transactions_unique_brand = np.asarray(transactions_unique_brand)
np.savetxt("transactions_unique_brand.csv", transactions_unique_brand, delimiter = ",")
"""
"""
merge_trainhistory_transactions = pd.merge_asof(trainHistory, transactions, on = 'id', by = 'chain')
merge_trainhistory_transactions.to_csv('merge_trainhistory_transactions.csv')

merge_testHistory_transactions = pd.merge_asof(testHistory, transactions, on = 'id', by = 'chain')
merge_testHistory_transactions.to_csv('merge_testHistory_transactions.csv')
"""
"""
merge_testHistory_transactions = pd.read_csv('merge_testHistory_transactions.csv')
merge_trainhistory_transactions = pd.read_csv('merge_trainhistory_transactions.csv')

merge_trainHistory_transactions_temp = ((merge_trainhistory_transactions.purchasequantity * merge_trainhistory_transactions.purchaseamount) +(merge_trainhistory_transactions.repeattrips * merge_trainhistory_transactions.purchaseamount))
merge_trainHistory_transactions_temp.to_csv('merge_trainHistory_transactions_temp.csv')

merge_trainhistory_transactions['rating'] = merge_trainHistory_transactions_temp
merge_trainhistory_transactions.to_csv('merge_trainhistory_transactions_rating.csv')

"""

merge_trainhistory_transactions_rating = pd.read_csv('merge_trainhistory_transactions_rating.csv')

scaler = MinMaxScaler(feature_range = (0, 10))

merge_trainhistory_transactions_rating['rating'] = scaler.fit_transform(merge_trainhistory_transactions_rating['rating'])

fdf = merge_trainhistory_transactions_rating.drop(['Unnamed: 0', 'Unnamed: 0.1', 'offerdate', 'date', 'productsize', 'productmeasure', 'repeater'], axis=1, inplace=True)

merge_trainhistory_transactions_rating.to_csv('final_df.csv')


