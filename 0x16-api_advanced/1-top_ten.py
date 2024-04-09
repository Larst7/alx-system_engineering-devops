#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and print the titles of
the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)

    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if posts:
            for post in posts:
                print(post['data']['title'])
        else:
            print("No posts found.")
    elif response.status_code == 404:
        # Invalid subreddit
        print("None")
    else:
        # Some other error occurred
        print(f"Error: {response.status_code}")

if __name__ == '__main__':
    subreddit = input("Enter subreddit name: ")
    top_ten(subreddit)

