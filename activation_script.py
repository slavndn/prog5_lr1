import sys
import requests
import importlib.util

class URLLoader:
    def __init__(self, url):
        self.url = url

    def get_code(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Проверка на ошибки
        return response.text

def url_hook(path):
    if path.startswith("http://"):
        return URLLoader(path)
    return None

# url_hook в sys.path_hooks
sys.path_hooks.append(url_hook)
sys.path.append("http://localhost:8000")  