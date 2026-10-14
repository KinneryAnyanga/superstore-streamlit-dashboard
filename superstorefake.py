'''
# Load the data
df = pd.read_csv('Superstore.csv',  encoding='latin1')
# Display the data
st.subheader('Superstore Data')
st.dataframe(df.head())
# Category selection
categories = df['Category'].unique()
selected_category = st.selectbox('Choose a Category', categories)
#   Filter the data
filtered_df = df[df['Category']== selected_category]
# Calculate metrics 
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_quantity = filtered_df['Quantity'].sum()
# Display the metrics
col1, col2, col3 = st.columns(3)
col1.metric('Total Sales', f'${total_sales:,.2f}')
col2.metric('Total Profit', f'${total_profit:,.2f}')
col1.metric('Quantity Sold', total_quantity)
# Sales by date
st.subheader('Sales Over Time')
sales_by_date =  filtered_df.groupby('Order Date')['Sales'].sum()
st.line_chart(sales_by_date)
'''