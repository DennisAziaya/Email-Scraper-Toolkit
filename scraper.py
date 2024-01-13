import requests
from bs4 import BeautifulSoup
import re

def scrape_emails_from_url(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad requests

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the email addresses using a regular expression
        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        emails = set(re.findall(email_pattern, soup.get_text()))

        if not emails:
            return "No emails found on the page."

        return emails

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Example usage:
url = "https://example.com/contact-us/"
result = scrape_emails_from_url(url)

if isinstance(result, set):
    # Print the email addresses
    for email in result:
        print(email)
else:
    print(result)
