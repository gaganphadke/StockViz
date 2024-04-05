import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title('Stock Price Explorer')

    # File upload
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=['csv'])

    if uploaded_file is not None:
        # Read data from uploaded CSV file
        df = pd.read_csv(uploaded_file)
        
        # Convert 'Date' column to datetime
        df['Date'] = pd.to_datetime(df['Date'])

        # Display data
        st.subheader("Stock Data")
        st.write(df)

        # Plot closing prices
        st.subheader('Closing Prices')
        plt.figure(figsize=(10, 6))
        plt.plot(df['Date'], df['Close'])
        plt.title('Closing Prices')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.grid(True)
        st.pyplot()

if __name__ == "__main__":
    main()
