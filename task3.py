import requests
from bs4 import BeautifulSoup
import requests_cache

# URL of the Batdongsan.com real estate listings page
url = "https://batdongsan.com.vn/nha-dat-ban"

# Enable caching to avoid excessive requests to the server
requests_cache.install_cache('real_estate_cache', expire_after=3600)  # Cache expires after 1 hour

def scrape_real_estate_data():
    try:
        # Make a request to the website
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract real estate details based on the HTML structure
            for listing in soup.find_all('div', class_='product-item'):
                price = listing.find('span', class_='product-price').text.strip()
                availability = listing.find('span', class_='product-availability').text.strip()
                description = listing.find('h2', class_='product-title').text.strip()
                location = listing.find('span', class_='product-location').text.strip()

                # Print or store the extracted data as needed
                print(f"Price: {price}\nAvailability: {availability}\nDescription: {description}\nLocation: {location}\n{'='*30}")

        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scrape_real_estate_data()