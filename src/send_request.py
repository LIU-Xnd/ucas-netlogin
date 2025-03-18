#!/home/xndliu/Apps/ucas-netlogin/.venv/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time


def main(USERNAME: str, PASSWORD: str) -> None:

    # Set up the WebDriver (ensure you have the correct driver installed, e.g., chromedriver for Chrome)
    # options = Options()
    service = webdriver.ChromeService(executable_path="../lib/chromedriver")
    # options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        service=service,
    )

    # Open the network portal URL
    portal_url = "https://portal.ucas.ac.cn/"  # Replace with actual URL
    print("Loading page ...")
    driver.get(portal_url)

    # Wait for the page to load
    time.sleep(2)
    # Locate form elements and fill them out
    username_field = driver.find_element(By.ID, "username")  # Update selector as needed
    password_field = driver.find_element(By.ID, "password")  # Update selector as needed

    username_field.send_keys(USERNAME)  # Replace with actual username
    password_field.send_keys(PASSWORD)  # Replace with actual password

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to process
    time.sleep(5)

    print("Form submitted successfully.")

    input("Press Any to exit:")
    # Close the browser
    driver.quit()
    return


if __name__ == "__main__":
    with open("../data/config", "r") as f:
        config: str = f.read().strip()
    config = config.replace(" ", "").replace("\t", "").replace("\n", "")
    iloc_username: int = config.index("USERNAME:") + 9
    iloc_end_of_username: int = config.index("PASSWORD:")
    iloc_password: int = iloc_end_of_username + 9
    USERNAME = config[iloc_username:iloc_end_of_username]
    PASSWORD = config[iloc_password:]

    main(USERNAME, PASSWORD)
