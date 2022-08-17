"""This script acts as a client to the backend application"""


def test_main():
    import requests

    from utilmodule import print_http_response, print_message

    print_message("To request an access token")
    res = requests.post("http://127.0.0.1:5000/auth",
                        json={  # this is the body of the request, it needs to have
                            "username": "admin",  # the username and password
                            "password": "password"
                        })
    access_token = res.json()["access_token"]
    print(access_token)

    print_message("POST chair")
    res = requests.post("http://127.0.0.1:5000/item/chair",
                        json={"price": 1982.00},
                        headers={"Authorization": "JWT " + access_token})
    print_http_response(res)

    print_message("POST piano")
    res = requests.post("http://127.0.0.1:5000/item/piano",
                        json={"price": 99999.00},
                        headers={"Authorization": "JWT " + access_token})
    print_http_response(res)

    print_message("POST table")
    res = requests.post("http://127.0.0.1:5000/item/table",
                        json={"price": 789.50},
                        headers={"Authorization": "JWT " + access_token})
    print_http_response(res)


if __name__ == "__main__":
    test_main()
