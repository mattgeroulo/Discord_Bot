from bs4 import BeautifulSoup
import requests
from selenium import webdriver

# # Setup the driver (make sure to have the right driver installed)
# driver = webdriver.Chrome()
# driver.get('https://www.phl.org/flights/security-information/checkpoint-hours')

# # Get the page source
# url = driver.page_source
# driver.quit()


# # #url = 'https://www.phl.org/flights/security-information/checkpoint-hours'
# # #page = requests.get(url)
# # soup = BeautifulSoup(url, 'html.parser')
# driver = webdriver.Chrome()
# driver.get('https://www.phl.org/flights/security-information/checkpoint-hours')

# # Get the page source
# html_content = driver.page_source
# driver.quit()

# # Now you can parse with Beautiful Soup
# soup = BeautifulSoup(html_content, 'html.parser')
# #print(soup)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup the driver
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the URL
#driver.get('https://www.phl.org/flights/security-information/checkpoint-hours')

url = 'https://api.livereachmedia.com/api/v1/locations/3951/metrics/live?metrics=waitTime&metrics=waitTimeRange'  # Example placeholder

# Make a request to the API endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print(data)  # Print the full response to understand its structure

    # Extract the relevant wait times
    # This will depend on the structure of the JSON returned
    # Example of accessing a specific terminal's wait time:
    try:
        terminal_a_east_wait_time = data['TerminalA_East']['wait_time']  # Adjust based on actual JSON structure
        print(f"Wait time for Terminal A-East: {terminal_a_east_wait_time} mins")
    except KeyError:
        print("Wait time data not found for Terminal A-East.")
else:
    print(f"Failed to retrieve data: {response.status_code}")







# soup = BeautifulSoup(html_content, 'html.parser')
# x =soup.find_all('div', id = "block-waitapiblock")
# y = soup.find_all('span', id ='aeGen')
# print(y)
#print(y)
# for terminal in y:
#     terminal_name = terminal.find('h2').text
#     hours = terminal.find('p').text
#     print(hours , terminal_name)
#print(hours )
