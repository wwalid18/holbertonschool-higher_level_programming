#!/usr/bin/python3
import requests
import json
"""api = 'https://jsonplaceholder.typicode.com/posts'"""


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    posts = response.json()
    for post in posts:
        print(post['title'])


def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    posts = response.json()
    with open('posts.json', 'w') as file:
        json.dump(posts, file)
