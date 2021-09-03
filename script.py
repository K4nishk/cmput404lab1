from importlib.metadata import version
import requests

# print(version('requests'))
print(requests.get("http://google.com"))
