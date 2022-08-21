
def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key)+":")
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))


def print_http_response(res):
    print(f"Status Code: {res.status_code}")
    # resjson = res.json() # use if we wanted to see the json file

    # print("\n\nHTTP Response Header:")
    # pretty(res.headers)

    print("\nHTTP Response Body:")
    print(res.text)


def print_message(message):
    print("\n# ====================================== #\n"
          f"# {message}\n"
          "# ====================================== #\n")
