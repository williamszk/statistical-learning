import requests

test_url = "http://httpbin.org/post"

with open("my_file.txt", "rb") as test_file:
    # Note: it's important to read the file in binary mode. The requests library typically 
    # determines the Content-Length header, which is a value in bytes. If the file is not read 
    # in bytes mode, the library may get an incorrect value for Content-Length, which would 
    # cause errors during file submission.
    test_response = requests.post(
        test_url, 
        files = {"form_field_name": test_file}
    )

    if test_response.ok:
        print("Upload completed successfully!")
        print(test_response.text)
    else:
        print("Something went wrong!")



