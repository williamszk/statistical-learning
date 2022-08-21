
def test_main():

    import requests
    from utilmodule import print_http_response, print_message

    # userdata = {"username": "Dennis", "password": "unix123"}
    userdata = {"username": "Obi-Wan", "password": "1234"}

    print_message("Register new user")
    res = requests.post("http://127.0.0.1:5000/register",
                        json=userdata)

    print_http_response(res)
    # =============================================================== #


if __name__ == "__main__":
    test_main()
