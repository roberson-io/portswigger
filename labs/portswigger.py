from bs4 import BeautifulSoup
from typing import Dict, List
import requests


base_url = "https://portswigger.net"
login_url = "{base_url}/users".format(base_url=base_url)
labs_url = "{base_url}/web-security/all-labs".format(base_url=base_url)


def new_session() -> requests.Session:
    return requests.Session()

def login(email: str, password: str) -> requests.Session:
    session = new_session()
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


def lab_urls(session: requests.Session) -> List[str]:
    r = session.get(labs_url)
    labs_page = BeautifulSoup(r.text, features="html.parser")
    lab_divs = labs_page.find_all("div", class_="widgetcontainer-lab-link")
    lab_paths = [
        div.find("a").get("href") for div in lab_divs if div.find("a")
    ]
    return [
        "{base_url}{lab_path}".format(base_url=base_url, lab_path=lab_path)
        for lab_path in lab_paths
    ]


def labs(
    session: requests.Session,
    verbose: bool = True,
    include_status: bool = False,
) -> List[Dict]:
    labs = []
    urls = lab_urls(session)
    lab_count = len(urls)
    for i, url in enumerate(urls):
        if verbose:
            print(
                "Fetching {n} of {count} labs.".format(
                    n=i + 1, count=lab_count
                )
            )
        r = session.get(url)
        lab_page = BeautifulSoup(r.text, features="html.parser")
        title = lab_page.find("h1").text.replace("Lab: ", "").strip()
        breadcrumbs = lab_page.find("ol", class_="ps-breadcrumbs")
        topic = breadcrumbs.find_all("li")[1].text.strip()
        level = lab_page.find(
            "div", class_="widget-container-labelevel"
        ).text.strip()
        lab = {
            "title": title,
            "topic": topic,
            "url": url,
            "level": level,
        }
        if include_status:
            status = (
                lab_page.find("div", class_="widgetcontainer-lab-status")
                .find("p")
                .text
            ).strip()
            lab["status"] = status
        labs.append(lab)
    return labs
