import requests
from bs4 import BeautifulSoup
from tkinter import messagebox

def fetch_url_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        content = soup.get_text()[:200]
        image_count = len(soup.find_all('img'))

        return title, content, image_count

    except requests.exceptions.RequestException as e:
        return None, str(e), None
    except Exception as e:
        return None, str(e), None

def fetch_and_display_info(url, title_label, content_label, image_count_label):
    title, content, image_count = fetch_url_info(url)

    if title is not None:
        title_label.config(text=f"Title: {title}")
        content_label.config(text=f"First 200 chars: {content}")
        image_count_label.config(text=f"Image Count: {image_count}")
    else:
        messagebox.showerror("Error", content)
