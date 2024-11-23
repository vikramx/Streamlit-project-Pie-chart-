import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
def load_data():
    uploaded_file=st.file_uploader("Upload your Csv file here:",type='csv')
    if uploaded_file is not None:
        content=pd.read_csv(uploaded_file)
        return content
    else:
        return "Please upload a file with content in it"

def product_count_categories(data):
    product_sales=data['Product_Category']
    product_counts=product_sales.value_counts()

    product_list=product_counts.index.tolist()
    sales_list=product_counts.values.tolist()

    return product_list,sales_list

def plotpie(sales_list,product_list):
    plt.figure(figsize=(8,8))
    plt.pie(sales_list,labels=product_list,autopct='%1.2f%%',startangle=90,colors=['r','b','gold'],
            wedgeprops={"edgecolor":'k','linewidth':3,'linestyle':'-.'})
    plt.title("Pie chart of store sales data")
    st.pyplot(plt)


def main():
    st.title("Pie chart visualization of storeSalesData file")

    data=load_data()

    if data is not None:
        product_list,sales_list=product_count_categories(data)

        st.write("Product And Sales Information")
        st.write("Product List:",product_list)
        st.write("Sales List:",sales_list)

        plotpie(sales_list,product_list)
    else:
        st.warning("Please upload a file:")
main()