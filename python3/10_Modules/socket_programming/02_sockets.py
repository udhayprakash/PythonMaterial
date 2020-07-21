import socket

def get_ip_for_website(remote_host):
    ip_address = socket.gethostbyname(remote_host)

    try:
        print(f"{remote_host} IP address: {ip_address}")
    except socket.error  as err_msg:
        print(f'{remote_host} : {err_msg}')
    except Exception as ex:
        print(repr(ex))

get_ip_for_website('www.python.org')
get_ip_for_website('www.google.com')
get_ip_for_website('www.facebook.com')
get_ip_for_website('www.facebook.we')


# DNS
# 151.101.8.223 == 'www.python.org'
