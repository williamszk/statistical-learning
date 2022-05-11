
import requests

# Util functions


def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key)+":")
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))


def print_http_response(res):
    print("+-----------------------------------------------------------+")
    print(f"URL: {res.url}")
    print(f"Status Code: {res.status_code}")

    print("\n\nHTTP Response Header:")
    pretty(res.headers)

    print("\n\nHTTP Response Body:")
    print(res.text)
    print()
    print("+-----------------------------------------------------------+")


test_url = "http://localhost:5000/"

with open("file01.json", "rb") as test_file:

    test_response = requests.post(
        test_url,
        headers={"Content-Type": "application/octet-stream"},
        files={"form_field_name": test_file}
    )

    print("Upload completed successfully!")
    print_http_response(test_response)
