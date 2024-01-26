#!/usr/bin/python3
"""Import the required packages"""


import requests
import sys


if __name__ == "__main__":
    # Get the username and password from the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Define the GitHub API URL for the user endpoint
    api_url = "https://api.github.com/user"

    # Make a GET request with Basic Authentication
    response = requests.get(api_url, auth=(username, password))

    r_id = response.json().get("id")
    print(r_id)
