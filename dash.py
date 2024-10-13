
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Page setup
st.set_page_config(page_title="Lively Trade and Shipping Dashboard", layout="wide")

# Load dataset (assuming the dataset is stored as CSV)
data = pd.read_csv("PythonProject_input.csv")

# Set up the dashboard title and description
st.title("Trade and Shipping Data Dashboard")
st.markdown("### A lively, in-depth exploration of import/export data, shipping methods, and key metrics.")

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
st.write("This pie chart gives an overview of the trade balance, showing the proportion of imports and exports in the dataset.")

# 2. Sunburst Chart: Imports and Exports by Shipping Method and Country
st.header("2. Sunburst Chart: Imports/Exports by Shipping Method and Country")
sunburst_fig = px.sunburst(data, path=['Import_Export', 'Shipping_Method', 'Country'], values='Value', color='Shipping_Method')
st.plotly_chart(sunburst_fig)
st.write("The sunburst chart gives a hierarchical view of imports and exports by shipping method and country, providing a comprehensive look at trade flows.")

# 3. Box Plot: Quantity, Value, and Weight
st.header("3. Box Plot: Quantity, Value, and Weight")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=data[['Quantity', 'Value', 'Weight']], ax=ax3, palette="Set3")
ax3.set_title("Box Plot of Quantity, Value, and Weight")
st.pyplot(fig3)
st.write("This box plot shows the distribution of key metrics (Quantity, Value, and Weight) and highlights the presence of any outliers.")

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
st.write("The histograms display right-skewed distributions for Quantity and Value, showing that most transactions occur at lower values.")

# 5. Pie Chart: Distribution of Shipping Methods
st.header("5. Pie Chart: Shipping Method Distribution")
shipping_method_counts = data['Shipping_Method'].value_counts()

fig5, ax6 = plt.subplots()
ax6.pie(shipping_method_counts, labels=shipping_method_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
ax6.axis('equal')
st.pyplot(fig5)
st.write("This pie chart visualizes the distribution of different shipping methods, showing that sea shipping dominates the dataset.")

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
st.write("This line plot shows fluctuations in total quantity over time, helping to identify seasonal patterns in trade activity.")

# 7. Correlation Heatmap: Quantity, Value, and Weight
st.header("7. Correlation Heatmap: Quantity, Value, and Weight")
corr_matrix = data[['Quantity', 'Value', 'Weight']].corr()

fig7, ax8 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='Blues', ax=ax8, linewidths=0.5)
ax8.set_title("Correlation Heatmap of Quantity, Value, and Weight")
st.pyplot(fig7)
st.write("This heatmap reveals the relationships between Quantity, Value, and Weight, showing a strong positive correlation between Quantity and Value.")

# 8. Line Plot: Monthly Value Over Time
st.header("8. Monthly Value Over Time")
monthly_value_data = data.groupby('Month')['Value'].sum()

fig8, ax9 = plt.subplots(figsize=(12, 6))
monthly_value_data.plot(kind='line', color='dodgerblue', ax=ax9, marker='o')
ax9.set_title("Monthly Total Value Over Time")
ax9.set_xlabel("Month")
ax9.set_ylabel("Total Value")
st.pyplot(fig8)
st.write("This line plot shows the total trade value each month, helping to track the flow of monetary value over time.")

# 9. Box Plot: Value by Import/Export
st.header("9. Box Plot: Value by Import/Export")
fig9, ax10 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Import_Export', y='Value', data=data, ax=ax10, palette="coolwarm")
ax10.set_title("Box Plot of Value by Import/Export")
ax10.set_xlabel("Import/Export")
ax10.set_ylabel("Value")
st.pyplot(fig9)
st.write("This box plot highlights how the value of imports tends to be higher than that of exports, particularly showing outliers in the import data.")

# 10. Violin Plot: Quantity by Shipping Method
st.header("10. Violin Plot: Quantity by Shipping Method")
fig10, ax11 = plt.subplots(figsize=(10, 6))
sns.violinplot(x='Shipping_Method', y='Quantity', data=data, ax=ax11, palette="muted")
ax11.set_title("Violin Plot of Quantity by Shipping Method")
st.pyplot(fig10)
st.write("The violin plot shows the distribution of Quantity for each Shipping Method, highlighting how Sea shipping handles larger quantities overall.")

# 11. Histogram: Distribution of Weight
st.header("11. Distribution of Weight")
fig11, ax12 = plt.subplots(figsize=(10, 6))
ax12.hist(data['Weight'], bins=20, color='lightgreen', edgecolor='black')
ax12.set_title("Distribution of Weight")
ax12.set_xlabel("Weight")
ax12.set_ylabel("Frequency")
st.pyplot(fig11)
st.write("The histogram displays the distribution of Weight, showing that most goods fall within a lower weight range, with a few high-weight outliers.")

# 12. Scatter Plot: Relationship between Value and Weight
st.header("12. Scatter Plot: Value vs Weight")
fig12, ax13 = plt.subplots()
sns.scatterplot(x='Weight', y='Value', data=data, ax=ax13, hue='Import_Export', palette="coolwarm", s=100)
ax13.set_title("Scatter Plot of Value vs Weight")
ax13.set_xlabel("Weight")
ax13.set_ylabel("Value")
st.pyplot(fig12)
st.write("The scatter plot shows the relationship between Weight and Value. Heavier items tend to have higher values, especially in imports.")

# Conclusion
st.subheader("Conclusion")
st.write("""
This dashboard offers a visually rich and dynamic exploration of trade data, with various graphs providing insights into key metrics like quantity, value, and weight.
The inclusion of multiple chart types such as sunburst, violin, and correlation heatmaps helps uncover patterns in imports, exports, shipping methods, and more.
""")
