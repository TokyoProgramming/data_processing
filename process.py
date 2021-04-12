
import pandas as pd
import numpy as np


# define missing value
missing_values = ["n/a", "na", "--"]

train_df = pd.read_csv('E:/python/titanic/train.csv')
market_df1 = pd.read_csv('E:/python/titanic/marketing_data.csv', na_values = missing_values)
market_df2 = pd.read_csv('E:/python/titanic/marketing_data.csv')
missing_data = pd.read_csv('E:/python/titanic/missing_data.csv', na_values = missing_values)
netflix_data = pd.read_csv('E:/python/titanic/netflix_titles.csv', na_values = missing_values)
df = pd.read_csv('E:/python/titanic/country_vaccinations.csv', na_values = missing_values)
card = pd.read_csv('E:/python/titanic/creditcard.csv', na_values = missing_values)
bank = pd.read_csv('E:/python/titanic/BankChurners.csv', na_values = missing_values)


class dataDetail:
    def __init__(self,data):
        self.data = data
        
    def structureData(self):
        data = self.data 
        head_data= data.head(8)
        describe = data.describe()
        return (head_data,describe)
    
    def missingData(self):
        
        data = self.data
        total = data.isnull().sum().sort_values(ascending = False)
        percentage1 = data.isnull().sum()/data.isnull().count()*100
        percentage2 = (round(percentage1,1)).sort_values(ascending=False)
        missing_data = pd.concat([total,percentage2], axis = 1, keys = ['Total','%'])
        return missing_data
    
    def multiTypeData(self):
        data = self.data
        colLen = len(data.columns)
        for col in range(colLen):
            try:
                res5 = data[data.columns[col]].apply(type).value_counts()
                if(len(res5) > 1):
                    print(res5)
                    print(col)
            except:
                print('error')
        
    
def call(data):
    res1 = dataDetail(data).missingData()
    res2 = dataDetail(data).structureData()
    res3 = dataDetail(data).multiTypeData()

# res1 = dataDetail(market_df1).missingData()
# res2 = dataDetail(missing_data).missingData()
# res3 = dataDetail(missing_data).multiTypeData()
# res6 = dataDetail(netflix_data).missingData()
# res7 = dataDetail(netflix_data).multiTypeData()
# res10 = dataDetail(df).missingData()
# res11 = dataDetail(card).missingData()
res12 = dataDetail(bank).missingData()
res13 = dataDetail(bank).multiTypeData()
print(res12)
print(res13)

# print(res6)

# for col in netflix_data.columns:
#     print(col)


# print(netflix_data['date_added'].head())

rowLen = len(netflix_data['director'])
dateData = netflix_data['director']
# # print(type(dateData[1]) != str)


print('---------------------------')

def array(rowLen):
    arr = list()
    for row in range(rowLen):
        check = type(dateData[row])
        if(check != str):
           arr.append(row)
            
    return arr 
        
    
print('show name')
print('---------')

director = netflix_data['director'].head()
# print(director)

print('---------')
res8 = array(rowLen)
# print(len(res8))

title_name = netflix_data['title']
country_name = netflix_data['country']
release_year = netflix_data['release_year']

for x in range(10):
    y = res8[x]
    title = title_name[y]
    country = country_name[y]
    year = release_year[y]

    # print('movie:{0} country:{1} year:{2}'.format(title, country, year))
    

print('---------------------------')




 







