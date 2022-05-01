

import requests


def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key)+":")
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))

def print_http_response(res):
    print(f"Status Code: {res.status_code}")

    print("\nHTTP Response Header:")
    pretty(res.headers)

    print("\nHTTP Response Body:")
    print(res.text)
    print()



print("# ====================================== #")
print("# To request an access token")
print("# ====================================== #")
res = requests.post("http://127.0.0.1:5000/auth",
                   json={ # this is the body of the request, it needs to have
                       "username": "jose", # the username and password
                       "password": "asdf"
                       })

access_token = res.json()["access_token"]

print("\nThe Access Token:")
print(access_token)
print("\n")


print("# ====================================== #")
print("# Post /item/chair"  )
print("# ====================================== #")
res = requests.post("http://127.0.0.1:5000/item/chair", json={"price": 1982.00})
print_http_response(res)


print("# ====================================== #")
print("# GET /items"  )
print("# ====================================== #")
res = requests.get("http://127.0.0.1:5000/items")
print_http_response(res)








