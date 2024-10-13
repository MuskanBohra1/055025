import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Comprehensive Trade and Shipping Dashboard", layout="wide")

# Load dataset (ensure to replace the file path with your actual data file path)
data = pd.read_csv("C://Users//dhruv//OneDrive//Documents//python_project//PythonProject_input.csv")

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

# 3. Heatmap: Shipping Methods by Country
st.header("3. Heatmap of Shipping Methods by Country")
grouped_data = data.groupby(['Country', 'Shipping_Method']).size().unstack(fill_value=0)

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(grouped_data, annot=True, fmt='d', cmap='coolwarm', ax=ax3, linewidths=0.5, cbar_kws={'label': 'Count'})
ax3.set_title("Shipping Methods by Country")
st.pyplot(fig3)
st.write("The heatmap shows how different countries use various shipping methods, helping to understand the logistical preferences by region.")

# 4. Box Plot: Quantity, Value, and Weight
st.header("4. Box Plot for Quantity, Value, and Weight")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=data[['Quantity', 'Value', 'Weight']], ax=ax4, palette="Set3")
ax4.set_title("Box Plot of Quantity, Value, and Weight")
st.pyplot(fig4)
st.write("This box plot visualizes the distribution and variability of Quantity, Value, and Weight. It highlights the presence of outliers.")

# 5. Histogram: Quantity and Value Distribution
st.header("5. Distribution of Quantity and Value")
fig5, (ax5, ax6) = plt.subplots(1, 2, figsize=(14, 6))

ax5.hist(data['Quantity'], bins=20, color='lightblue', edgecolor='black')
ax5.set_title("Distribution of Quantity")
ax5.set_xlabel('Quantity')
ax5.set_ylabel('Frequency')

ax6.hist(data['Value'], bins=20, color='salmon', edgecolor='black')
ax6.set_title("Distribution of Value")
ax6.set_xlabel('Value')
ax6.set_ylabel('Frequency')

st.pyplot(fig5)
st.write("The histograms show that both Quantity and Value have right-skewed distributions, indicating that most transactions have lower values.")

# 6. Scatter Plot: Weight vs Value (Import/Export)
st.header("6. Scatter Plot: Weight vs. Value (By Import/Export)")
fig6, ax7 = plt.subplots()
sns.scatterplot(x='Weight', y='Value', hue='Import_Export', data=data, ax=ax7, palette="coolwarm", s=100)
ax7.set_title("Scatter Plot of Weight vs. Value")
ax7.set_xlabel("Weight")
ax7.set_ylabel("Value")
st.pyplot(fig6)
st.write("The scatter plot shows the relationship between Weight and Value, with imports generally having higher weights and values compared to exports.")

# 7. Correlation Heatmap: Quantity, Value, and Weight
st.header("7. Correlation Heatmap: Quantity, Value, and Weight")
corr_matrix = data[['Quantity', 'Value', 'Weight']].corr()

fig7, ax8 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='Blues', ax=ax8, linewidths=0.5)
ax8.set_title("Correlation Heatmap of Quantity, Value, and Weight")
st.pyplot(fig7)
st.write("The correlation heatmap indicates a positive relationship between Quantity and Value, suggesting that larger quantities tend to have higher values.")

# 8. Pie Chart: Shipping Methods Distribution
st.header("8. Pie Chart: Distribution of Shipping Methods")
shipping_method_counts = data['Shipping_Method'].value_counts()

fig8, ax9 = plt.subplots()
ax9.pie(shipping_method_counts, labels=shipping_method_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
ax9.axis('equal')
st.pyplot(fig8)
st.write("This pie chart visualizes the distribution of different shipping methods used, with Sea shipping being the most common.")

# 9. Box Plot: Value by Import/Export
st.header("9. Box Plot: Value by Import/Export")
fig9, ax10 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Import_Export', y='Value', data=data, ax=ax10, palette="coolwarm")
ax10.set_title("Box Plot of Value by Import/Export")
ax10.set_xlabel("Import/Export")
ax10.set_ylabel("Value")
st.pyplot(fig9)
st.write("This box plot compares the value distribution for imports and exports. Imports tend to have higher values, as seen by the distribution of outliers.")

# 10. Line Plot: Monthly Quantity Over Time
st.header("10. Monthly Quantity Over Time")
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')
data['Month'] = data['Date'].dt.to_period('M')
monthly_data = data.groupby('Month')['Quantity'].sum()

fig10, ax11 = plt.subplots(figsize=(12, 6))
monthly_data.plot(kind='line', color='coral', ax=ax11, marker='o')
ax11.set_title("Monthly Total Quantity Over Time")
ax11.set_xlabel("Month")
ax11.set_ylabel("Total Quantity")
st.pyplot(fig10)
st.write("This line plot shows the trend of total quantity over time, giving insights into seasonal or monthly fluctuations in trade activity.")

# 11. Heatmap: Shipping Methods by Category
st.header("11. Heatmap: Shipping Methods by Category")
category_shipping = data.groupby(['Category', 'Shipping_Method']).size().unstack(fill_value=0)

fig11, ax12 = plt.subplots(figsize=(10, 6))
sns.heatmap(category_shipping, annot=True, fmt='d', cmap='YlGnBu', ax=ax12, linewidths=0.5)
ax12.set_title("Heatmap of Shipping Methods by Product Category")
st.pyplot(fig11)
st.write("The heatmap shows how different product categories are shipped using various methods, giving a better understanding of logistical preferences across industries.")

# Conclusion
st.subheader("Conclusion")
st.write("""
This dashboard provides an extensive overview of trade data, using a wide range of visualizations to explore shipping methods, trade balance, and relationships between key metrics like value, quantity, and weight.
Each graph provides insights into different aspects of the trade and shipping landscape, helping to uncover patterns and trends.
""")
