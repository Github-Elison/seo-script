import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import Counter


def get_meta_tags(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('title')
        description_tag = soup.find('meta', attrs={'name': 'description'})
        keywords_tag = soup.find('meta', attrs={'name': 'keywords'})

        title = title_tag.text.strip() if title_tag else "N/A"
        description = description_tag['content'].strip(
        ) if description_tag else "N/A"
        keywords = keywords_tag['content'].strip() if keywords_tag else "N/A"

        return {
            "Title": title,
            "Description": description,
            "Keywords": keywords
        }
    except Exception as e:
        return {"Error": str(e)}


def count_keywords(text):
    words = text.lower().split()
    return Counter(words)


def analyze_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        internal_links = []
        external_links = []

        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(url, href)
            parsed_url = urlparse(full_url)

            if parsed_url.netloc == urlparse(url).netloc:
                internal_links.append(full_url)
            else:
                external_links.append(full_url)

        return {
            "Internal Links": internal_links,
            "External Links": external_links
        }
    except Exception as e:
        return {"Error": str(e)}


def check_robots_txt(url):
    try:
        robots_url = urljoin(url, '/robots.txt')
        response = requests.get(robots_url)
        return response.text
    except Exception as e:
        return {"Error": str(e)}


if __name__ == "__main__":
    website_url = "https://www.unibf.com.br/"

    # Meta Tags
    seo_info = get_meta_tags(website_url)
    print("Meta Tags:")
    for key, value in seo_info.items():
        print(f"{key}: {value}")

    # Keyword Count
    keyword_text = f"{seo_info['Title']} {
        seo_info['Description']} {seo_info['Keywords']}"
    keyword_count = count_keywords(keyword_text)
    print("\nKeyword Count:")
    print(keyword_count)

    # Analyze Links
    links_info = analyze_links(website_url)
    print("\nLinks:")
    print(f"Internal Links: {len(links_info['Internal Links'])}")
    print(f"External Links: {len(links_info['External Links'])}")

    # Check robots.txt
    robots_txt = check_robots_txt(website_url)
    print("\nrobots.txt:")
    print(robots_txt)
