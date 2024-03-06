import requests

def is_instagram_down():
	url = "https://www.instagram.com/"
	response = requests.get(url)
	return response.status_code != 200

def is_facebook_down():
	url = "https://www.facebook.com/"
	response = requests.get(url)
	return response.status_code != 200

if __name__ == '__main__':
	if is_instagram_down():
		print("Instagram is down.")

	else:
		print("Instagram is up and running!")

	if is_instagram_down():
		print("Facebook is down.")

	else:
		print("Facebook is up and running!")