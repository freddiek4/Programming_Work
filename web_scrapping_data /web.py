import requests
import lxml.html as lx
import re
import time
import nltk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster



# a, i

def get_movie_links():
    base_url = "https://www.imsdb.com/alpha.php"
    response = requests.get(base_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: {response.status_code}")
    tree = lx.fromstring(response.content)
    movie_links = tree.xpath("//a[contains(@href, '/Movie Scripts/')]/@href")
    movie_links = [f"https://www.imsdb.com{link}" for link in movie_links]
    return movie_links


movie_links = get_movie_links()
print(f"Number of movie links found: {len(movie_links)}")
Number of movie links found: 1290

def fetch_script(link):
    base_url = "https://www.imsdb.com"
    url = base_url + link
    #code here is just fetching w/ request package
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch: {url}")
        return None
    tree = lx.fromstring(response.content)
    title = tree.xpath('//title/text()')[0]
    writers = tree.xpath('//b[text()="Writers"]/following-sibling::node()[self::a and following-sibling::b[1][text()="Genres"]]/text()')
    genres = tree.xpath('//b[text()="Genres"]/following-sibling::a[following-sibling::b]/text()')
    script_date = tree.xpath('normalize-space(//b[text()="Script Date"]/following-sibling::text()[1])')
    script_link = tree.xpath('//a[contains(text(), "Read")]/@href')[0]
    script_url = base_url + script_link
    script_response = requests.get(script_url)
    if script_response.status_code != 200:
        print(f"Failed to fetch script: {script_url}")
        return None
    script_tree = lx.fromstring(script_response.content)
    script_texts = script_tree.xpath('//pre/text()') #pre!!!!!!!!!!!!!!!!!!!!!!!!!! <pre>...<pre>
    script_text = ''.join(script_texts) if script_texts else "Script not found."
    return {
        "title": title,
        "writers": writers,
        "genres": genres,
        "script_date": script_date,
        "script": script_text 
    }

link = '/Movie Scripts/10 Things I Hate About You Script.html'
fetch_movie = fetch_script(link)
print(fetch_movie)  
