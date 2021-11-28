import requests

test_url = "http://httpbin.org/post"

test_file = open("my_file.txt", "rb")

test_response = requests.post(
    test_url,
    files={"form_field_name": test_file})
if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print("Something went wrong!")
