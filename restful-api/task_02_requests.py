import requests
import csv
"""Function to fetch and print post titles"""


def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Status Code: {response.status_code}")
        posts = response.json()
        for post in posts:
            print(post["title"])
    else:
        print(f"Failed to fetch posts. Status Code: {response.status_code}")


def fetch_and_save_posts():
    """Fetches posts and saves them to a CSV file (posts.csv)."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        csv_file = "posts.csv"
        fieldnames = ["id", "title", "body"]  # Only include relevant fields

        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(
                {
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"],
                }
                for post in posts
            )

        print(f"Data saved to {csv_file}")
    else:
        print(f"Failed to fetch posts. Status Code: {response.status_code}")
