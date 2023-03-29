# Ops301 Code Challenge Day12 
# Author: Justin 'Sage' Tabios
# Date of revision: 28 Mar 2023
# Purpose: 
# Had referred to ChatGPT to help with understanding the function syntax part "print(f"{n + 1 }. {method})"

import requests

destination_url = input("Enter the destination URL: ")

http_methods = ["GET", "POST", "DELETE", "HEAD", "PATCH", "OPTIONS"]
print("\nSelect an HTTP method:")
for i, method in enumerate(http_methods):
    print(f"{i + 1}. {method}")

selected_method = int(input("\nEnter the number corresponding to the method: ")) - 1
http_method = http_methods[selected_method]

print(f"\nYou are about to send a {http_method} request to {destination_url}.")
confirmation = input("Do you want to proceed? (y/n): ")

if confirmation.lower() == "y":
    if http_method == "GET":
        response = requests.get(destination_url)
    elif http_method == "POST":
        response = requests.post(destination_url)
    elif http_method == "DELETE":
        response = requests.delete(destination_url)
    elif http_method == "HEAD":
        response = requests.head(destination_url)
    elif http_method == "PATCH":
        response = requests.patch(destination_url)
    elif http_method == "OPTIONS":
        response = requests.options(destination_url)

    status_code = {
        200: "OK",
        201: "Created",
        204: "No Content",
        301: "Moved Permanently",
        302: "Found",
        400: "Bad request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Site not found",
    }

    if response.status_code in status_code:
        print(f"Response status: {status_code[response.status_code]}")
    else:
        print(f"Response status: {response.status_code}")

    # Print response header information
    print("\nResponse headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

else:
    print("Request canceled.")
