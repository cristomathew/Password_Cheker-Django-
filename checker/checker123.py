import requests
import hashlib
import sys
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+ query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code} check the api and try again')
    return res

def get_pasword_leaks_count(hashes, hashes_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h == hashes_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars, tail = sha1password[:5],sha1password[5:]
    response = request_api_data(first5_chars)
    return get_pasword_leaks_count(response,tail)

def check(password):
    count = pwned_api_check(password)
    if count:
        return f'{password} was found {count} times ... you should probably change the password', 1
    else:
        return  f'{password} was not found carry on', 0
