Name:   Kanishk Chawla
Course: CMPUT 404 Fa 2021
ID #:   1583231

Lab #: 1


================================ Venv ================================

Q1) What is your GitHub URL?
A: https://github.com/K4nishk

Q2) What version is the requests library installed on the system?
A: 2.25.1
https://stackoverflow.com/questions/20180543/how-to-check-version-of-python-modules

/cshome/kanishk/.local/bin

Q3) What version is the requests library installed in the virtualenv?
A: 2.26.0

Q4) What is the difference between the virtual environment and the not virtual environment python?
A: There is not really any difference between the 2 environments. Since, I was using the lab machine, requests module was already installed at a lower version and since in the virtual environment everything had to be redone, installing the requests module resulted in the installation of the latest version.

================================ Curl ================================

Q5) 
	i) What status code is returned for http://google.com ? 
	A: The status code received is 301 - Moved Permanently. 

	ii) What URL must you visit to get a 200 status code?
	A: In order to get a 200 status code we need a URL to a webpage which returns a successful response like https://webdocs.cs.ualberta.ca/~hindle1/1.py

Q6)
	i) What status code is returned for http://google.com/teapot?
	A: The status code received is 418

	ii) Is it the one returned by curl -i or curl -iL?
	A: It is the same for both, probably because the "connection" wasn't established in the first place and redo-ing the request didn't result in anything meaningful either. 

	iii) What happens when you curl http://www.google.com/teapot?
	A: We get an html document. 
		<!doctype html><html lang="en"> <script nonce="DtmWD2rxuWgYNiQyU/uN3A==">(function(H){H.className=H.className.replace(/\bgoogle\b/,'google-js')})(document.documentElement)</script> <meta charset="utf-8"> <meta content="initial-scale=1, minimum-scale=1, width=device-width" name="viewport"> <title>Error 418 (I&#8217;m a teapot)!?</title> <link href="//www.gstatic.com/teapot/teapot.min.css" rel="stylesheet" nonce="DtmWD2rxuWgYNiQyU/uN3A=="> <a href="http://www.google.com/"><span aria-label="Google" id="logo"></span></a> <p><b>418.</b> <ins>I&#8217;m a teapot.</ins></p> <p>The requested entity body is short and stout. <ins>Tip me over and pour me out.</ins></p> <div id="teaset"><div id="teabot"></div><div id="teacup"></div></div> <script src="//www.gstatic.com/teapot/teapot.min.js" nonce="DtmWD2rxuWgYNiQyU/uN3A=="></script> </html>

Q7) 
	i) What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py when you used -X POST?
	A: The following was introduced under the Form Contents field whereas before it said No form fields.
		<H3>Form Contents:</H3>
		<DL>
		<DT>X: <i>&lt;type 'instance'&gt;</i>
		<DD>MiniFieldStorage('X', 'Y')
		</DL>
	Also, some new shell environments were introduced and the UNIQUE_ID had changed.

	ii) What is this method useful for?
	A: POST method is useful for the purposes of submission of a form securely or more generally uploading a file on the web server based on the date enclosed within the body of the request.

Q8) What is the raw URL to your Python script on GitHub?
A: 