from importlib.metadata import version
import requests

def main():
	#print(version('requests'))
	#print(requests.get("http://google.com"))

	url = "https://raw.githubusercontent.com/K4nishk/cmput404lab1/main/script.py?token=AIHLPKB5W5RRIZ24THRDJXLBGHHRY"
	r = requests.get(url, allow_redirects=True)
	print(r.content)

	return 0

main()