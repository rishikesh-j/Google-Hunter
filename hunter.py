import requests
import re
import urllib.parse
import time
from bs4 import BeautifulSoup
import urllib3

# Suppress only the single InsecureRequestWarning from urllib3 needed
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Read dorks from the file
def read_dorks(filename):
    with open(filename, 'r') as file:
        dorks = [line.strip() for line in file.readlines()]
    return dorks

# Perform Google search
def google_search(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(f'https://www.google.com/search?q={urllib.parse.quote_plus(query)}', headers=headers, verify=False)
    return response.text

# Parse the search results using regex
def parse_results(html, dork_label):
    results = []
    pattern = re.compile(r'data-id="atritem-(https?://[^"]+)"')
    matches = pattern.findall(html)
    for match in matches:
        results.append(f'[{dork_label}] [{match}]')
    return results

# Main function
def main(target):
    dorks = read_dorks('google_dorks.txt')
    all_results = []
    for dork in dorks:
        dork_label, dork_query = dork.split(' :: ')
        query = dork_query.replace('{target}', target)
        html = google_search(query)
        results = parse_results(html, dork_label)
        all_results.extend(results)
        time.sleep(2)  # Adding a delay of 5 seconds between requests
    
    # Output results
    unique_results = list(set(all_results))  # Remove duplicate results across all dorks
    for result in unique_results:
        print(result)

if __name__ == '__main__':
    target = input("Enter the target domain: ")
    main(target)
