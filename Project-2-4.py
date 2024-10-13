import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the dashboard title
st.title("Trade and Shipping Data Dashboard")
st.subheader("Visualizing Imports, Exports, and Shipping Methods")

# Load the dataset
data = pd.read_csv("C://Users//dhruv//OneDrive//Documents//python_project//PythonProject_input.csv")

# Pie Chart: Distribution of Imports and Exports
st.header("Distribution of Imports and Exports")
import_export_counts = data['Import_Export'].value_counts()

fig1, ax1 = plt.subplots()
ax1.pie(import_export_counts, labels=import_export_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#ff9999'])
ax1.axis('equal')
st.pyplot(fig1)
st.write("This pie chart shows the share of imports and exports in the dataset, revealing a balanced distribution of trade activities.")

# Bar Plot: Shipping Method Frequencies
st.header("Shipping Methods Frequency")
shipping_method_counts = data['Shipping_Method'].value_counts()

fig2, ax2 = plt.subplots()
shipping_method_counts.plot(kind='bar', color='lightgreen', ax=ax2)
ax2.set_title("Frequency of Shipping Methods")
ax2.set_xlabel("Shipping Method")
ax2.set_ylabel("Count")
st.pyplot(fig2)
st.write("The bar plot highlights that Sea shipping is the most used method, followed by Air and Land.")

# Heatmap: Shipping Methods by Country
st.header("Shipping Methods Count by Country")
grouped_data = data.groupby(['Country', 'Shipping_Method']).size().unstack(fill_value=0)

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(grouped_data, annot=True, fmt='d', cmap='YlGnBu', ax=ax3)
ax3.set_title("Shipping Methods by Country")
st.pyplot(fig3)
st.write("The heatmap showcases how countries prefer different shipping methods, with some relying heavily on air transport while others favor sea.")

# Box Plot: Quantity, Value, and Weight
st.header("Box Plot for Quantity, Value, and Weight")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=data[['Quantity', 'Value', 'Weight']], ax=ax4)
ax4.set_title("Box Plot for Quantity, Value, and Weight")
st.pyplot(fig4)
st.write("The box plot reveals the distribution and presence of outliers, particularly in the Value and Weight variables.")

# Histogram: Quantity and Value Distribution
st.header("Quantity and Value Distribution")
fig5, (ax5, ax6) = plt.subplots(1, 2, figsize=(12, 6))

ax5.hist(data['Quantity'], bins=20, color='lightblue', edgecolor='black')
ax5.set_title("Quantity Distribution")
ax5.set_xlabel("Quantity")
ax5.set_ylabel("Frequency")

ax6.hist(data['Value'], bins=20, color='salmon', edgecolor='black')
ax6.set_title("Value Distribution")
ax6.set_xlabel("Value")
ax6.set_ylabel("Frequency")

st.pyplot(fig5)
st.write("Both histograms depict right-skewed distributions, with a few large transactions driving the overall trend.")

# Scatter Plot: Weight vs Value
st.header("Scatter Plot: Weight vs. Value")
fig6, ax7 = plt.subplots()
sns.scatterplot(x='Weight', y='Value', hue='Import_Export', data=data, ax=ax7)
ax7.set_title("Scatter Plot of Weight vs. Value")
ax7.set_xlabel("Weight")
ax7.set_ylabel("Value")
st.pyplot(fig6)
st.write("This scatter plot indicates a relationship between the weight and value of goods. Heavier goods tend to have higher values, particularly for imports.")

# Final Remarks
st.subheader("Final Analysis")
st.write("""
This dashboard provides an in-depth look at trade patterns, shipping methods, and the relationship between different variables like weight and value.
The visualizations offer key insights into how trade is conducted across different countries using varying shipping methods.
""")

