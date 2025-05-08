import re
import webbrowser

def process_links_and_addresses(text):
    url_pattern = r'(https?://(?:www\.)?[a-zA-Z0-9./?=&%_-]+)'
    address_pattern = r'[0-9A-Za-z]+ [a-zA-Z, \n]+(?:\d{5}(?:-\d{4})?|[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d)'

    links = re.findall(url_pattern, text)  # Find all URLs
    addresses = re.findall(address_pattern, text)  # Find all addresses
    addresses = list(map(lambda x: x.replace('\n', ' '), addresses))
    return links, addresses

def callback_open_url(url):
    webbrowser.open(url)

def callback_address(address):
    google_maps_url = f"https://www.google.com/maps/search/{address.replace(' ', '+')}"
    webbrowser.open(google_maps_url)
