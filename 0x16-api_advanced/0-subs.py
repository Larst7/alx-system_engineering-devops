#!/usr/bin/python3
"subscribers count"

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    
    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        # Invalid subreddit
        return 0
    else:
        # Some other error occurred
        print(f"Error: {response.status_code}")
        return 0

# Example usage:
if __name__ == '__main__':
    subreddit = input("Enter subreddit name: ")
    print(number_of_subscribers(subreddit))

