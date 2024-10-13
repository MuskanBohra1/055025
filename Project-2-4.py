import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page configuration for a more professional appearance
st.set_page_config(page_title="Trade and Shipping Dashboard", layout="wide")

# Load dataset (assuming the dataset is stored as CSV)
data = pd.read_csv("PythonProject_input.csv")

# Set up the dashboard layout and heading
st.title("Trade and Shipping Data Dashboard")
st.markdown("### A comprehensive view of imports, exports, shipping methods, and more.")

# Sidebar for filtering (optional for enhancement)
st.sidebar.header("Filter Options")
country_list = data['Country'].unique()
selected_countries = st.sidebar.multiselect("Select Countries to View", country_list, default=country_list)

if selected_countries:
    data = data[data['Country'].isin(selected_countries)]

# First graph: Pie chart for imports and exports
st.header("Distribution of Imports and Exports")
import_export_counts = data['Import_Export'].value_counts()

fig1, ax1 = plt.subplots()
ax1.pie(import_export_counts, labels=import_export_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#ff9999'])
ax1.axis('equal')
st.pyplot(fig1)
st.write("This pie chart illustrates the share of imports and exports in the dataset, showing the balance between trade activities.")

# Second graph: Bar plot of shipping method frequency
st.header("Frequency of Shipping Methods")
shipping_method_counts = data['Shipping_Method'].value_counts()

fig2, ax2 = plt.subplots()
shipping_method_counts.plot(kind='bar', color='lightgreen', ax=ax2)
ax2.set_title("Frequency of Shipping Methods")
ax2.set_xlabel("Shipping Method")
ax2.set_ylabel("Count")
st.pyplot(fig2)
st.write("This bar chart displays the frequency of each shipping method. Sea shipping is the most common, followed by Air and Land.")

# Heatmap: Shipping Methods by Country
st.header("Heatmap: Shipping Methods by Country")
grouped_data = data.groupby(['Country', 'Shipping_Method']).size().unstack(fill_value=0)

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(grouped_data, annot=True, fmt='d', cmap='coolwarm', ax=ax3, linewidths=0.5, cbar_kws={'label': 'Count'})
ax3.set_title("Shipping Methods by Country")
st.pyplot(fig3)
st.write("The heatmap highlights how different countries prefer specific shipping methods. The color intensity shows the shipping frequency.")

# Box Plot for Quantity, Value, and Weight
st.header("Box Plot for Quantity, Value, and Weight")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=data[['Quantity', 'Value', 'Weight']], ax=ax4, palette="Set3")
ax4.set_title("Box Plot: Quantity, Value, and Weight")
st.pyplot(fig4)
st.write("The box plot helps visualize the spread of Quantity, Value, and Weight. The presence of outliers is apparent, especially in Value.")

# Histogram for Quantity and Value
st.header("Distribution of Quantity and Value")
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
st.write("Both histograms show the distribution of Quantity and Value. The right skew suggests that most transactions occur at lower values.")

# Scatter Plot: Weight vs. Value with Import/Export categories
st.header("Scatter Plot: Weight vs. Value (Import/Export)")
fig6, ax7 = plt.subplots()
sns.scatterplot(x='Weight', y='Value', hue='Import_Export', data=data, ax=ax7, palette="coolwarm", s=100)
ax7.set_title("Scatter Plot: Weight vs. Value")
ax7.set_xlabel("Weight")
ax7.set_ylabel("Value")
st.pyplot(fig6)
st.write("The scatter plot reveals a correlation between Weight and Value, with imports typically having higher weights and values.")

# Additional Heatmap: Correlation between numerical variables (optional for added depth)
st.header("Correlation Heatmap: Quantity, Value, and Weight")
corr_matrix = data[['Quantity', 'Value', 'Weight']].corr()

fig7, ax8 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='Blues', ax=ax8, linewidths=0.5)
ax8.set_title("Correlation Heatmap of Quantity, Value, and Weight")
st.pyplot(fig7)
st.write("This heatmap shows the correlation between the key variables. There is a moderate positive correlation between Quantity and Value.")

# Conclusion
st.subheader("Conclusion")
st.write("""
This dashboard gives a thorough view of trade and shipping data. The heatmaps provide clear visualizations of shipping trends across countries and 
methods, while scatter and box plots give insights into the relationship between key variables such as weight, value, and quantity.
""")
