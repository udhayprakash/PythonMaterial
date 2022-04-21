import requests

test_url = 'http://httpbin.org/post'

# format 1
test_files = {
    'test_file_1': open('my_file.txt', 'rb'),
    'test_file_2': open('my_file_2.txt', 'rb'),
    'test_file_3': open('my_file_3.txt', 'rb')
}

# format 2 - both works
test_files = [('test_file_1', open('my_file.txt', 'rb')),
              ('test_file_2', open('my_file_2.txt', 'rb')),
              ('test_file_3', open('my_file_3.txt', 'rb'))]

test_response = requests.post(test_url, files = test_files)

if test_response.ok:
    print('Upload completed successfully!')
    print(test_response.text)
else:
    print('Something went wrong!')
