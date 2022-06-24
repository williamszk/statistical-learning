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
    print(f"Status Code: {res.status_code}")
    # resjson = res.json() # use if we wanted to see the json file

    # print("\n\nHTTP Response Header:")
    # pretty(res.headers)

    print("\nHTTP Response Body:")
    print(res.text)
    print()
    print("+-----------------------------------------------------------+")


print("# ====================================== # \n\
# Register a new user Dennis \n\
# ====================================== # \n")
res = requests.post("http://127.0.0.1:5000/register",
                    json={"username": "Dennis",
                          "password": "Ritchie"}
                    )
print_http_response(res)


print("# ====================================== # \n\
# To request an access token for Dennis Ritchie  \n\
# ====================================== # \n")
res = requests.post("http://127.0.0.1:5000/auth",
                    json={"username": "Dennis",
                          "password": "Ritchie"})
access_token = res.json()["access_token"]
print(access_token)

print("# ====================================== # \n\
# Post chair of price 99.00  \n\
# ====================================== # \n")
res = requests.post("http://127.0.0.1:5000/item/chair",
                    headers={"authorization": "jwt " + access_token},
                    json={"price": 99.00})
print_http_response(res)

print("# ====================================== # \n\
# Post (insert) chair of price 10.00\n\
# Again to see if error of posting an item with same name happens\n\
# ====================================== # \n")
res = requests.post("http://127.0.0.1:5000/item/chair",
                    headers={"authorization": "jwt " + access_token},
                    json={"price": 10.00})
print_http_response(res)

print("# ====================================== # \n\
# Get (select) chair from database\n\
# ====================================== # \n")
res = requests.get("http://127.0.0.1:5000/item/chair",
                   headers={"Authorization": "JWT " + access_token})
print_http_response(res)


print("# ====================================== # \n\
# Delete the chair from database\n\
# ====================================== # \n")
res = requests.delete("http://127.0.0.1:5000/item/chair",
                      headers={"authorization": "jwt " + access_token},
                      )
print_http_response(res)

# we snould test the put method
print("# ====================================== # \n\
# Post (insert) piano of price 1999.99\n\
# ====================================== # \n")
res = requests.post("http://127.0.0.1:5000/item/piano",
                    headers={"authorization": "jwt " + access_token},
                    json={"price": 1999.99})
print_http_response(res)


print("# ====================================== # \n\
# Put (Update) the price of piano to 2000.00\n\
# ====================================== # \n")
res = requests.put("http://127.0.0.1:5000/item/piano",
                    headers={"authorization": "jwt " + access_token},
                    json={"price": 2000.00})
print_http_response(res)


print("# ====================================== # \n\
# Get all items in database\n\
# ====================================== # \n")
res = requests.get("http://127.0.0.1:5000/items",
    headers={"authorization": "jwt " + access_token},
)
print_http_response(res)
