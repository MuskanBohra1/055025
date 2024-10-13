import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data (replace with your dataset path or loaded data)
data = pd.read_csv("C://Users//dhruv//OneDrive//Documents//python_project//PythonProject_input.csv")

# Set up the dashboard layout
st.title("Final Term Project Dashboard")
st.subheader("Analysis of Imports, Exports, and Shipping Data")

# Pie Chart: Distribution of Imports vs Exports
st.header("Distribution of Imports and Exports")
import_export_counts = data['Import_Export'].value_counts()

fig1, ax1 = plt.subplots()
ax1.pie(import_export_counts, labels=import_export_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99'])
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
st.pyplot(fig1)
st.write("The pie chart shows the percentage share of imports and exports in the dataset. We can see that both activities are almost evenly distributed, showing a balanced trade scenario.")

# Bar Plot: Frequency of Shipping Methods
st.header("Frequency of Shipping Methods")
shipping_method_counts = data['Shipping_Method'].value_counts()

fig2, ax2 = plt.subplots()
shipping_method_counts.plot(kind='bar', color='skyblue', ax=ax2)
ax2.set_title("Frequency of Shipping Methods")
ax2.set_xlabel("Shipping Method")
ax2.set_ylabel("Count")
st.pyplot(fig2)
st.write("The bar plot illustrates the distribution of different shipping methods. Sea and Air shipping are more frequently used, indicating a preference for quicker transport options.")

# Heatmap: Shipping Methods by Country
st.header("Shipping Methods Count by Country")
grouped_data = data.groupby(['Country', 'Shipping_Method']).size().unstack(fill_value=0)

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(grouped_data, annot=True, fmt='d', cmap='YlGnBu', ax=ax3)
ax3.set_title("Shipping Methods by Country")
st.pyplot(fig3)
st.write("This heatmap provides insight into the shipping preferences of different countries. Some countries, like the USA, prefer air shipping, while others utilize a mix of methods.")

# Box Plot: Quantity, Value, and Weight
st.header("Box Plot for Quantity, Value, and Weight")
fig4, ax4 = plt.subplots(figsize=(12, 6))
sns.boxplot(data=data[['Quantity', 'Value', 'Weight']], ax=ax4)
ax4.set_title("Box-Whisker Plot for Quantity, Value, and Weight")
st.pyplot(fig4)
st.write("The box plot highlights the spread and outliers in the data for quantity, value, and weight. It's evident that some extreme values exist, particularly in the Value variable.")

# Histogram: Distribution of Quantity and Value
st.header("Distribution of Quantity and Value")
fig5, (ax5, ax6) = plt.subplots(1, 2, figsize=(12, 5))

ax5.hist(data['Quantity'], bins=20, color='skyblue', edgecolor='black')
ax5.set_title("Distribution of Quantity")
ax5.set_xlabel('Quantity')
ax5.set_ylabel('Frequency')

ax6.hist(data['Value'], bins=20, color='salmon', edgecolor='black')
ax6.set_title("Distribution of Value")
ax6.set_xlabel('Value')
ax6.set_ylabel('Frequency')

st.pyplot(fig5)
st.write("Both histograms show a right-skewed distribution, especially for value. This indicates a few transactions with high values, while most of the transactions remain in lower quantity and value ranges.")

# Scatter Plot: Relationship between Weight and Value
st.header("Relationship between Weight and Value for Import/Export")
fig6, ax7 = plt.subplots()
sns.scatterplot(x='Weight', y='Value', hue='Import_Export', data=data, ax=ax7)
ax7.set_title("Scatter Plot: Weight vs. Value")
ax7.set_xlabel("Weight")
ax7.set_ylabel("Value")
st.pyplot(fig6)
st.write("The scatter plot indicates a strong correlation between weight and value, with imports generally tending towards higher weight and value categories compared to exports.")

# Conclusion
st.subheader("Conclusion")
st.write("This dashboard provides a comprehensive view of the dataset, showing key distributions and relationships. The visualizations reveal patterns in shipping methods, trade balance, and the relation between weight and value of goods.")
