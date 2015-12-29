# jdoradic-lite
A simple web app that basically sends request to j-doradic.com and extract the result table and present it the user in a more clean-looking manner.

![screenshot](https://github.com/sdiox/jdoradic-lite/blob/master/readme/screenshot.png?raw=true)
Why bother?
* It is way faster to look up words on this web app because the web layout is very simple and clean.
* You can click the link at the end of each row to look for more information on jisho.org

Dependencies:
* j-doradic.com (this website needs to be up and running in order to use this web app)
* Python 2.7
* Flask
* flask-bootstrap
* flask-script
* flask-wtf
* bs4
* requests
* wanakana.js (for converting romanji to kana automatically)

How to run this web app?

1. Install Python 2.7
2. Install all the aforementioned dependencies
3. Run the web app with command: "python main.py runserver"

Special thanks to: j-doradic.com for providing such a great dictionary database!