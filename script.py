from importlib.metadata import version
import requests

def main():
	#print(version('requests'))
	#print(requests.get("http://google.com"))

	url = "https://raw.githubusercontent.com/K4nishk/cmput404lab1/main/script.py"
	r = requests.get(url, allow_redirects=True)

	file = open('script_downloaded.py', 'wb')
	file.write(r.content)
	file.close()
	
	f = open('script_downloaded.py', 'r')
	print(f.read())
	f.close()
	
	return 0

main()