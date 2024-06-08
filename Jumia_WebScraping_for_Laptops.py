import streamlit as st
from bs4 import BeautifulSoup
import requests

def find_laptop(specs):
    html_text = requests.get('https://www.jumia.co.ke/catalog/?q=laptops#catalog-listing').text
    soup = BeautifulSoup(html_text, 'html.parser')
    laptops = soup.find_all('div', class_='info')

    results = []
    for laptop in laptops:
        product_description = laptop.find('h3', class_='name').text
        if 'SSD' in product_description and specs in product_description:
            price = laptop.find('div', class_='prc').text
            results.append((product_description, price))
    
    return results

# Streamlit App
st.title('Laptop Finder on Jumia')
st.write('Input some Specs')

specs = st.text_input('Enter Specifications...')
st.write('Filtering: ', specs)

if st.button('Find Laptops'):
    laptops = find_laptop(specs)
    if laptops:
        for description, price in laptops:
            st.write(f'**Short Product Description:** {description}')
            st.write(f'**Product Price:** {price}')
    else:
        st.write('No laptops found with the given specifications.')



