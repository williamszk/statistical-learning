
def test_main():

    import requests
    from utilmodule import print_http_response, print_message

    # =============================================================== #
    userdata = {"username": "admin", "password": "password"}

    print_message("Register the root user")
    res = requests.post("http://127.0.0.1:5000/register",
                        json=userdata)

    print_http_response(res)
    # =============================================================== #

    print_message("To request an access token")
    res = requests.post("http://127.0.0.1:5000/auth",
                        json={  # this is the body of the request, it needs to have
                            "username": "admin",  # the username and password
                            "password": "password"
                        })
    access_token = res.json()["access_token"]
    print(access_token)

    res = requests.post("http://127.0.0.1:5000/store/Target",
                        headers={"Authorization": "JWT " + access_token})
    print_http_response(res)


if __name__ == "__main__":
    test_main()