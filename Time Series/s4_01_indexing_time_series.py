import pandas as pd

sales_data = pd.read_csv('../sample_data/04 Time Series/sales_data.csv', parse_dates=True, index_col='InvoiceDate')


# Print sales_data DataFrame to check it's working
#print(sales_data.head())
#print(sales_data)
#print(sales_data['Description'])

#print(sales_data.info())


# Use .loc accessor
morning_sale = sales_data.loc['2010-12-01 08:25:00':'2010-12-01 08:30:00']
print(morning_sale)
