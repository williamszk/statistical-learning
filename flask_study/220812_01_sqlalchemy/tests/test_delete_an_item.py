
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

    print_message("DELETE chair")
    res = requests.delete("http://127.0.0.1:5000/item/chair",
                        headers={"Authorization": "JWT " + access_token})
    print_http_response(res)

    # what happens if we try to delete an item that doesn't exist?
    print_message("DELETE apple")
    res = requests.delete("http://127.0.0.1:5000/item/apple",
                        headers={"Authorization": "JWT " + access_token})
    print_http_response(res)

if __name__ == "__main__":
    test_main()