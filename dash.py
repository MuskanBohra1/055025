import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Comprehensive Trade and Shipping Dashboard", layout="wide")

# Load dataset (assuming the dataset is stored as CSV)
data = pd.read_csv("PythonProject_input.csv")

# Set up the dashboard title and description
st.title("Trade and Shipping Data Dashboard")
st.markdown("### A detailed exploration of import/export data, shipping methods, and key metrics.")

# Sidebar filters (optional)
st.sidebar.header("Filter Options")
country_list = data['Country'].unique()
selected_countries = st.sidebar.multiselect("Select Countries", country_list, default=country_list)

# Apply country filter if selected
if selected_countries:
    data = data[data['Country'].isin(selected_countries)]

# 1. Pie Chart: Distribution of Imports and Exports
st.header("1. Distribution of Imports and Exports")
import_export_counts = data['Import_Export'].value_counts()

fig1, ax1 = plt.subplots()
ax1.pie(import_export_counts, labels=import_export_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#ff9999'])
ax1.axis('equal')
st.pyplot(fig1)
st.write("This pie chart provides an overview of the trade balance by visualizing the proportion of imports and exports.")

# 2. Bar Plot: Frequency of Shipping Methods
st.header("2. Frequency of Shipping Methods")
shipping_method_counts = data['Shipping_Method'].value_counts()

fig2, ax2 = plt.subplots()
shipping_method_counts.plot(kind='bar', color='lightgreen', ax=ax2)
ax2.set_title("Frequency of Shipping Methods")
ax2.set_xlabel("Shipping Method")
ax2.set_ylabel("Count")
st.pyplot(fig2)
st.write("This bar plot shows the frequency of each shipping method. Sea shipping is the most used method, followed by Air.")

# 3. Box Plot: Quantity, Value, and Weight
st.header("3. Box Plot for Quantity, Value, and Weight")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=data[['Quantity', 'Value', 'Weight']], ax=ax3, palette="Set3")
ax3.set_title("Box Plot of Quantity, Value, and Weight")
st.pyplot(fig3)
st.write("This box plot visualizes the distribution and variability of Quantity, Value, and Weight. It highlights the presence of outliers.")

# 4. Histogram: Quantity and Value Distribution
st.header("4. Distribution of Quantity and Value")
fig4, (ax4, ax5) = plt.subplots(1, 2, figsize=(14, 6))

ax4.hist(data['Quantity'], bins=20, color='lightblue', edgecolor='black')
ax4.set_title("Distribution of Quantity")
ax4.set_xlabel('Quantity')
ax4.set_ylabel('Frequency')

ax5.hist(data['Value'], bins=20, color='salmon', edgecolor='black')
ax5.set_title("Distribution of Value")
ax5.set_xlabel('Value')
ax5.set_ylabel('Frequency')

st.pyplot(fig4)
st.write("The histograms show that both Quantity and Value have right-skewed distributions, indicating that most transactions have lower values.")

# 5. Pie Chart: Shipping Methods Distribution
st.header("5. Pie Chart: Distribution of Shipping Methods")
shipping_method_counts = data['Shipping_Method'].value_counts()

fig5, ax6 = plt.subplots()
ax6.pie(shipping_method_counts, labels=shipping_method_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
ax6.axis('equal')
st.pyplot(fig5)
st.write("This pie chart visualizes the distribution of different shipping methods used, with Sea shipping being the most common.")

# 6. Line Plot: Monthly Quantity Over Time
st.header("6. Monthly Quantity Over Time")
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
data['Month'] = data['Date'].dt.to_period('M')
monthly_data = data.groupby('Month')['Quantity'].sum()

fig6, ax7 = plt.subplots(figsize=(12, 6))
monthly_data.plot(kind='line', color='coral', ax=ax7, marker='o')
ax7.set_title("Monthly Total Quantity Over Time")
ax7.set_xlabel("Month")
ax7.set_ylabel("Total Quantity")
st.pyplot(fig6)
st.write("This line plot shows the trend of total quantity over time, giving insights into seasonal or monthly fluctuations in trade activity.")

# 7. Box Plot: Value by Import/Export
st.header("7. Box Plot: Value by Import/Export")
fig7, ax8 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Import_Export', y='Value', data=data, ax=ax8, palette="coolwarm")
ax8.set_title("Box Plot of Value by Import/Export")
ax8.set_xlabel("Import/Export")
ax8.set_ylabel("Value")
st.pyplot(fig7)
st.write("This box plot compares the value distribution for imports and exports. Imports tend to have higher values, as seen by the distribution of outliers.")

# 8. Correlation Heatmap: Quantity, Value, and Weight
st.header("8. Correlation Heatmap: Quantity, Value, and Weight")
corr_matrix = data[['Quantity', 'Value', 'Weight']].corr()

fig8, ax9 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='Blues', ax=ax9, linewidths=0.5)
ax9.set_title("Correlation Heatmap of Quantity, Value, and Weight")
st.pyplot(fig8)
st.write("The correlation heatmap indicates a positive relationship between Quantity and Value, suggesting that larger quantities tend to have higher values.")

# 9. Bar Plot: Frequency of Countries Involved in Trade
st.header("9. Frequency of Countries Involved in Trade")
country_counts = data['Country'].value_counts()

fig9, ax10 = plt.subplots(figsize=(10, 6))
country_counts.plot(kind='bar', color='lightcoral', ax=ax10)
ax10.set_title("Frequency of Countries Involved in Trade")
ax10.set_xlabel("Country")
ax10.set_ylabel("Count")
st.pyplot(fig9)
st.write("This bar plot shows the frequency of trade activities per country, highlighting which countries are most active in international trade.")

# 10. Histogram: Distribution of Weight
st.header("10. Distribution of Weight")
fig10, ax11 = plt.subplots(figsize=(10, 6))
ax11.hist(data['Weight'], bins=20, color='lightgreen', edgecolor='black')
ax11.set_title("Distribution of Weight")
ax11.set_xlabel("Weight")
ax11.set_ylabel("Frequency")
st.pyplot(fig10)
st.write("The histogram shows the distribution of weights in the dataset. Most goods fall within a lower weight range, with some outliers.")

# 11. Line Plot: Monthly Value Over Time
st.header("11. Monthly Value Over Time")
monthly_value_data = data.groupby('Month')['Value'].sum()

fig11, ax12 = plt.subplots(figsize=(12, 6))
monthly_value_data.plot(kind='line', color='dodgerblue', ax=ax12, marker='o')
ax12.set_title("Monthly Total Value Over Time")
ax12.set_xlabel("Month")
ax12.set_ylabel("Total Value")
st.pyplot(fig11)
st.write("This line plot shows the trend of total value over time, giving insights into fluctuations in trade value across months.")

# Conclusion
st.subheader("Conclusion")
st.write("""
This dashboard provides a comprehensive overview of trade and shipping data through a variety of visualizations. 
Each graph offers insights into different aspects, such as the distribution of key metrics, shipping preferences, and trends over time. 
The analysis helps uncover patterns in trade activities, shipping methods, and country-level involvement.
""")
