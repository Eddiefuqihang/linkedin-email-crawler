import time
import random
import csv
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

def setup_browser():
    """Set up the Chrome WebDriver with options."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_service = Service()  # Assuming ChromeDriver is in your PATH
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser

def login_to_linkedin(browser, email, password):
    """Log in to LinkedIn using provided credentials."""
    browser.get("https://www.linkedin.com/login")
    try:
        email_element = browser.find_element(By.ID, "username")
        email_element.send_keys(email)

        pass_element = browser.find_element(By.ID, "password")
        pass_element.send_keys(password)
        pass_element.submit()

        print("Success! Logged in, Bot starting")
        browser.implicitly_wait(5)
    except NoSuchElementException:
        print("Login failed. Please check your credentials.")
        browser.quit()
        exit()

def scrape_email_from_profile(browser, url):
    """Navigate to a LinkedIn profile's contact info page and extract the email."""
    info = {"url": url, "email": None}

    try:
        browser.get(f"{url}/overlay/contact-info/")
        browser.implicitly_wait(5)

        contact_page = bs(browser.page_source, "html.parser")
        email_element = contact_page.find('a', href=re.compile("mailto"))

        if email_element:
            email = email_element.get('href')[7:]  # Removes "mailto:" from the href
            print(f"Found email for {url}: {email}")
            info['email'] = email
        else:
            print(f"No email found for {url}")
    except TimeoutException:
        print(f"Timeout occurred while trying to load {url}")

    return info

def save_to_csv(data, filename='network_emails.csv'):
    """Save the scraped data to a CSV file."""
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data['url'], data['email']])

def main():
    # Argument parser to input LinkedIn credentials
    parser = argparse.ArgumentParser()
    parser.add_argument("email", help="LinkedIn email")
    parser.add_argument("password", help="LinkedIn password")
    args = parser.parse_args()

    # Set up the Chrome WebDriver
    browser = setup_browser()

    # Log in to LinkedIn
    login_to_linkedin(browser, args.email, args.password)

    # Read the LinkedIn connections URLs from CSV
    mynetwork = pd.read_csv('./Connections.csv', skiprows=2)['URL'].dropna().tolist()

    # Initialize the counts
    my_network_cnt = 0
    my_network_email_cnt = 0

    # Scrape emails from LinkedIn profiles
    for url in mynetwork:
        my_network_cnt += 1

        info = scrape_email_from_profile(browser, url)

        if info['email']:
            my_network_email_cnt += 1

        save_to_csv(info)
        print(f"{my_network_cnt} URLs traversed, {my_network_email_cnt} emails found.")

        time.sleep(random.uniform(3, 6))  # Random delay to avoid detection

    # Close the browser
    browser.quit()

if __name__ == "__main__":
    main()