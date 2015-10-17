#! /usr/bin/python3
import re
import time
from urllib import request, parse


def login():
    details = parse.urlencode({
        'username': username,
        'password': password,
        'n': '99',
        'type': '3',
        'drop': '0',
    })
    details = details.encode('UTF-8')
    url = request.Request('http://{}:3333/cgi-bin/do_login'.format(server), details)
    response = request.urlopen(url).read().decode('utf8', 'ignore')

    if re.match('[0-9]+', response):
        state = 'Login success'
    elif 'ip_exist_error' in response:
        state = 'Your IP has not been logout, wait two minutes and try again'
    elif 'ip_error' in response:
        state = 'Your IP address is not valid'
    elif 'username_error' in response:
        state = 'Wrong username'
    elif 'password_error' in response:
        state = 'Wrong password'
    else:
        state = 'Unknown Error {}'.format(response)

    print(state)
    return response


def logout():
    uid = login()
    details = parse.urlencode({'uid': uid})
    details = details.encode('UTF-8')
    url = request.Request('http://{}:3333/cgi-bin/do_logout'.format(server), details)
    response = request.urlopen(url).read().decode('utf8', 'ignore')
    if response == 'logout_ok':
        state = 'Logout success'
    else:
        state = 'Unknown Error {}'.format(response)
    print(state)


def main():
    while True:
        login()
        #logout()
        time.sleep(600)

if __name__ == '__main__':
    server = '202.112.136.131'
    username = 'username'
    password = 'password'
    main()
