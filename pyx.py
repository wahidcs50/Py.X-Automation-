# Driver_path= r"C:\Users\Wahid\Downloads\Compressed\chromedriver-win64\chromedriver.exe"
# import selenium
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
# import time
# # Set up the Selenium WebDriver (Chrome in this case)
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run headless mode for no UI
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# # Provide path to your chromedriver executable
# service = Service(Driver_path)  # Update with the correct path

# driver = webdriver.Chrome(service=service, options=chrome_options)
# # driver=webdriver.Chrome()
# print("Running")
# driver.get("https://phy-x.net/module/physics/shielding/")
# # driver.implicitly_wait(50)
# register_button = WebDriverWait(driver, 120).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']"))
#     )
# register=driver.find_element(By.XPATH, "//button[text()='Register']")
# register_button.click()
# print('clicked register button')
# # # time.sleep(5)
# # login_button = WebDriverWait(driver, 30).until(
# #         EC.presence_of_element_located((By.XPATH, "//button[@class='secondary']"))
# #     )
# # print('before clicking button:', login_button)
# # login_button.click()


# input("Press Enter to close the browser...")
# driver.quit()



# # register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
# # print('before clicking button',register_button)
# # register_button.click()
# # time.sleep(5)
# # login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
# # print('before clicking button',login_button)
# # login_button.click()

# #     # Wait for the login form to appear
# # time.sleep(2)
# # input("Press Enter to close the browser...")
# # driver.quit()
# # driver.implicitly_wait(60)











# ############ Working untill authentication ################

# Driver_path= r"C:\Users\Wahid\Downloads\Compressed\chromedriver-win64\chromedriver.exe"
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# import pandas as pd
# data=pd.read_csv(r"C:\Users\Wahid\Desktop\PYTHON-PROJECTS\Web-Scrapping\Py.X-scrapping\data.csv")
# # print(data.head())
# # for index, row in data[:3].iterrows():
# #     composition = row['Composition_Formula']
# #     density = row['Theoretical_Density']
# #     print(composition)
# #     print(density)

# # # Set up the Selenium WebDriver (Chrome in this case)
# chrome_options = Options()
# # chrome_options.add_argument("--headless")  # Run headless mode for no UI (remove this if you want to see the browser)
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-images")  # Disable images loading
# chrome_options.add_argument("--disable-javascript")  # 

# # Provide path to your chromedriver executable
# service = Service(Driver_path)  # Replace with the correct path

# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Open the webpage
# driver.get("https://phy-x.net/module/physics/shielding/")  # Replace with the actual URL
# print("Website loaded successfully")

# # Wait for the "Register" button to be clickable
# register_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']"))
# )
# register_button.click()
# print("Register button clicked")

# # Wait for the "Login" button to be clickable
# login_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
# )
# login_button.click()
# print("Login button clicked")

# time.sleep(2)
# print("Time to login")
# # Wait for the login form to appear
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.ID, "user_mail"))
# )

# # Enter username
# # username_input = driver.find_element(By.ID, "user_mail")
# username_input = driver.find_element(By.XPATH, "//input[@label='Username']")
# username_input.send_keys("wahidhussainali98@gmail.com")  # Replace with the actual username
# print("Username entered")

# # Enter password
# # password_input = driver.find_element(By.ID, "user_pass")
# password_input = driver.find_element(By.XPATH, "//input[@label='Password']")
# password_input.send_keys("paper24")  # Replace with the actual password
# print("Password entered")


# # Click the "Authenticate" button
# authenticate_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//button[text()='Authenticate']"))
# )
# authenticate_button.click()
# print("Authenticate button clicked")

# print("Loading data\n",data.head(2))

# time.sleep(5)

# # Wait for the page to load
# # WebDriverWait(driver, 10).until(
# #     EC.visibility_of_element_located((By.ID, "formula"))
# # )
# print("Page loaded, ready to fill data")

# # Iterate over the data and fill the form
# for index, row in data[:3].iterrows():
#     composition = row['Composition_Formula']
#     density = row['Theoretical_Density']
    
#     # Wait for the Chemical Composition field to be clickable and fill it
#     composition_input = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "formula"))
#     )
#     composition_input.clear()
#     composition_input.send_keys(composition)
#     print(f"Composition '{composition}' entered")

#     # Wait for the Density field to be clickable and fill it
#     density_input = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "density"))
#     )
#     density_input.clear()
#     density_input.send_keys(str(density))
#     print(f"Density '{density}' entered")
    
#     # print('debugging')
#     # # Print all elements with the given ID to debug
#     # elements = driver.find_elements(By.ID, "fweight")
#     # print(f"Found {len(elements)} elements with ID 'fweight'")

#     # # Print all elements of type radio to debug
#     # radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
#     # print(f"Found {len(radio_buttons)} radio buttons")
#     # print("end debugging")

#    # Wait for and select the Weight radio button using XPATH
#     time.sleep(2)
#     # Wait for the Weight radio button to be clickable
#     # Locate the Weight radio button
#     weight_radio_button = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.ID, "fweight"))
#     )
#     print("wight radio button object: " + str(weight_radio_button))
#     # Debug: Check if the button is enabled and selected
#     is_enabled = weight_radio_button.is_enabled()
#     is_selected = weight_radio_button.is_selected()
#     print(f"Radio button enabled: {is_enabled}")
#     print(f"Radio button selected: {is_selected}")

#     # Scroll the element into view
#     driver.execute_script("arguments[0].scrollIntoView(true);", weight_radio_button)
#     time.sleep(1)
    
#     # Use JavaScript to click the element
#     driver.execute_script("arguments[0].click();", weight_radio_button)
#     print("Weight radio button selected")
#     # Wait for the new fields to appear
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'composition')]//textarea[@id='formula']"))
#         )
#     except:
#         print("No new fields appeared. Exiting loop.")
#         break

#     time.sleep(2)  # Short delay to ensure the next set of fields is fully loaded



#     # Wait a moment before processing the next row
#     WebDriverWait(driver, 2)

# print("All data entered. Ready for further actions.")
# input('press enter to close the browser')
############ End of Working untill authentication ################


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

Driver_path = r"C:\Users\Wahid\Downloads\Compressed\chromedriver-win64\chromedriver.exe"
data = pd.read_csv(r"C:\Users\Wahid\Desktop\PYTHON-PROJECTS\Web-Scrapping\Py.X-scrapping\data.csv")

# Set up the Selenium WebDriver (Chrome in this case)
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-images")
chrome_options.add_argument("--disable-javascript")

service = Service(Driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the webpage
driver.get("https://phy-x.net/module/physics/shielding/")
print("Website loaded successfully")

# Wait for the "Register" button to be clickable and click it
register_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']"))
)
register_button.click()
print("Register button clicked")

# Wait for the "Login" button to be clickable and click it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
)
login_button.click()
print("Login button clicked")

time.sleep(2)
print("Time to login")

# Wait for the login form to appear
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "user_mail"))
)

# Enter username and password
username_input = driver.find_element(By.XPATH, "//input[@label='Username']")
username_input.send_keys("wahidhussainali98@gmail.com")
print("Username entered")

password_input = driver.find_element(By.XPATH, "//input[@label='Password']")
password_input.send_keys("paper24")
print("Password entered")

# Click the "Authenticate" button
authenticate_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Authenticate']"))
)
authenticate_button.click()
print("Authenticate button clicked")

print("Loading data\n", data.head(2))
time.sleep(5)

# Wait for the initial set of fields to appear
print("Page loaded, ready to fill data")

for index, row in data.iterrows():
    composition = row['Composition_Formula']
    density = row['Theoretical_Density']
    
    # Calculate tab indexes
    composition_tabindex = index * 2 + 1
    density_tabindex = index * 2 + 2
    
    # Determine the correct fraction name
    fraction_name = f"fraction{index}" if index > 0 else "fraction"

    # Create XPath for the fields
    composition_xpath = f"//textarea[@tabindex='{composition_tabindex}']"
    density_xpath = f"//input[@tabindex='{density_tabindex}']"
    weight_radio_xpath = f"//input[@name='{fraction_name}' and @value='weight']"

    print(f"Trying to find Composition XPath: {composition_xpath}")
    print(f"Trying to find Density XPath: {density_xpath}")
    print(f"Trying to find Weight Radio XPath: {weight_radio_xpath}")

    try:
        # Check if the composition field is present
        composition_elements = driver.find_elements(By.XPATH, composition_xpath)
        print(f"Found {len(composition_elements)} composition elements")

        # Check if the density field is present
        density_elements = driver.find_elements(By.XPATH, density_xpath)
        print(f"Found {len(density_elements)} density elements")

        # Check if the weight radio button is present
        weight_radio_elements = driver.find_elements(By.XPATH, weight_radio_xpath)
        print(f"Found {len(weight_radio_elements)} weight radio elements")

        if composition_elements and density_elements and weight_radio_elements:
            # Proceed if all elements are found
            composition_input = composition_elements[0]
            density_input = density_elements[0]
            weight_radio_button = weight_radio_elements[0]

            # Fill the current set of fields
            composition_input.clear()
            composition_input.send_keys(composition)
            print(f"Composition '{composition}' entered")

            density_input.clear()
            density_input.send_keys(str(density))
            print(f"Density '{density}' entered")

            # Select the Weight radio button
            driver.execute_script("arguments[0].scrollIntoView(true);", weight_radio_button)
            time.sleep(1)
            weight_radio_button.click()
            print("Weight radio button selected")

    except Exception as e:
        print(f"An error occurred: {e}")
        # Print the current page source to debug the issue
        print(driver.page_source)
        # Optionally take a screenshot for debugging
        driver.save_screenshot(f"error_{index}.png")

    # Wait for the next set of fields to appear before proceeding
    time.sleep(2)

print("All data entered. Ready for further actions.")
input('Press enter to close the browser')















# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options

# # Set up the Selenium WebDriver (Chrome in this case)
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run headless mode for no UI
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# # Provide path to your chromedriver executable
# service = Service(Driver_path)  # Update with the correct path

# driver = webdriver.Chrome(service=service, options=chrome_options)

# try:
#     # Open the webpage
#     driver.get("https://phy-x.net/module/physics/shielding/")  # Replace with the actual URL

#     # Wait for the "Register" button to be clickable
#     register_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']"))
#     )
#     register_button.click()

#     # Wait for the "Login" button in the registration dialog to be clickable
#     login_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
#     )
#     login_button.click()

#     # Wait for the login form to appear and be ready
#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "user_mail"))
#     )

#     # Enter username
#     username_input = driver.find_element(By.ID, "user_mail")
#     username_input.send_keys("wahidhussainali98@gmail.com")  # Replace with the actual username

#     # Enter password
#     password_input = driver.find_element(By.ID, "user_pass")
#     password_input.send_keys("your_password")  # Replace with the actual password

#     # Click the "Authenticate" button
#     authenticate_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[text()='Authenticate']"))
#     )
#     authenticate_button.click()

#     # Wait for authentication to complete, or for any post-login element to appear
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "some_post_login_element"))  # Replace with a relevant element after login
#     )

#     # Scrape the required data after authentication
#     # Example: Scraping data from an element with id 'data'
#     # data_element = driver.find_element(By.ID, "data")  # Replace with the actual ID or locator
#     # print(data_element.text)

# finally:
#     driver.quit()

