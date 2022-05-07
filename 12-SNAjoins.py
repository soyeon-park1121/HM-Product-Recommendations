import pandas as pd

articles = pd.read_csv('articles.csv')
customers = pd.read_csv('customers.csv')
transactions = pd.read_csv('transactions_train.csv')

full_data = transactions.merge(customers,on = 'customer_id', how = 'left')
full_data = full_data.merge(articles, on= 'article_id',how = 'left')

full_data.to_csv('joined_data.csv')