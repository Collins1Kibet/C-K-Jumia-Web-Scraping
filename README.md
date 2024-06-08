## Laptop Finder on Jumia

This is a simple web application built with Streamlit to find laptops on Jumia Kenya based on specific specifications provided by the user. The app scrapes Jumia Kenya's website to find laptops that match the given specifications and displays the product description and price.

### Features

- Input specifications to filter laptops.
- Scrapes Jumia Kenya for laptops that match the given specifications.
- Displays the product description and price for matching laptops.

### Requirements

- Python 3.6+
- Streamlit
- BeautifulSoup4
- Requests

### Code Overview
find_laptop(specs): Function to scrape Jumia Kenya's website for laptops that match the given specifications. Returns a list of tuples containing the product description and price.
**Streamlit app setup:**
- Title and description of the app.
- Input field for the user to enter specifications.
- Button to trigger the search for laptops.
- Display the results or a message if no laptops are found.

#### Example
- Input Specifications: 'SSD'
- Click the "Find Laptops" button.
- View the results with the product description and price.
