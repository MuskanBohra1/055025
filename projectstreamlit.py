# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (assuming the dataset is stored as CSV)
data = pd.read_csv(r"C://Users//dhruv//OneDrive//Documents//python_project//PythonProject_input.csv")

# Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

# Title of the Streamlit app
st.title("Data Visualization Dashboard")

# Sidebar for plot selection
st.sidebar.header("Select Plot")

# Add checkboxes for each plot to control the layout
scatter_plot = st.sidebar.checkbox("Scatter Plot: Quantity vs Value")
line_plot = st.sidebar.checkbox("Line Plot: Quantity Over Time")
box_plot = st.sidebar.checkbox("Box Plot: Quantity, Value, Weight")
histogram = st.sidebar.checkbox("Histogram: Distribution of Quantity and Value")
pie_chart = st.sidebar.checkbox("Pie Chart: Import vs Export Distribution")
bar_plot = st.sidebar.checkbox("Bar Plot: Shipping Methods Frequency")

# Scatter Plot: Quantity vs Value
if scatter_plot:
    st.subheader("Scatter Plot: Quantity vs Value")
    plt.figure(figsize=(8, 6))
    plt.scatter(data['Quantity'], data['Value'], color='b')
    plt.xlabel("Quantity")
    plt.ylabel("Value")
    plt.title("Scatter Plot: Quantity vs Value")
    st.pyplot(plt)

# Line Plot: Quantity Over Time
if line_plot:
    st.subheader("Line Plot: Quantity Over Time")
    data = data.sort_values(by='Date')
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Quantity'], marker='o', color='g', label='Quantity')
    plt.xlabel("Date")
    plt.ylabel("Quantity")
    plt.title("Quantity Over Time")
    plt.grid(True)
    st.pyplot(plt)

# Box Plot: Quantity, Value, and Weight
if box_plot:
    st.subheader("Box Plot: Quantity, Value, Weight")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data[['Quantity', 'Value', 'Weight']])
    plt.title('Box Plot for Quantity, Value, and Weight')
    plt.xlabel("Variables")
    plt.ylabel("Values")
    st.pyplot(plt)

# Histogram: Distribution of Quantity and Value
if histogram:
    st.subheader("Histogram: Distribution of Quantity and Value")
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.hist(data['Quantity'], bins=20, color='skyblue', edgecolor='black')
    plt.title("Distribution of Quantity")
    plt.xlabel("Quantity")
    plt.ylabel("Frequency")
    
    plt.subplot(1, 2, 2)
    plt.hist(data['Value'], bins=20, color='salmon', edgecolor='black')
    plt.title("Distribution of Value")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    
    st.pyplot(plt)

# Pie Chart: Import vs Export Distribution
if pie_chart:
    st.subheader("Pie Chart: Import vs Export Distribution")
    import_export_counts = data['Import_Export'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(import_export_counts, labels=import_export_counts.index, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99'])
    plt.title("Distribution of Imports and Exports")
    st.pyplot(plt)

# Bar Plot: Shipping Methods Frequency
if bar_plot:
    st.subheader("Bar Plot: Shipping Methods Frequency")
    shipping_method_counts = data['Shipping_Method'].value_counts()
    plt.figure(figsize=(8, 6))
    shipping_method_counts.plot(kind='bar', color='skyblue')
    plt.title('Frequency of Shipping Methods')
    plt.xlabel("Shipping Method")
    plt.ylabel("Count")
    st.pyplot(plt)
