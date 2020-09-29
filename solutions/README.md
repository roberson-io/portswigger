# PortSwigger Web Security Academy lab solutions

## Disclaimer
I do not work for PortSwigger. I am just learning this stuff myself. I appreciate that they have provided all of the Web Security Academy learning material and labs for free. Please be respectful of PortSwigger's environment when running scripts.

## Python Scripts

Most (all?) of the labs provide a solution below the button to access the lab on the lab description page. Occasionally the solution walks you through using a feature that is throttled in Burp Suite Community Edition. I think Burp Suite is great and worth the cash for a Professional license if you're a professional. However, if you're just starting out, it can be hard to justify spending $399/year out of your own pocket.

I will include Python scripts to solve some of these labs as I get to them. If you're using Burp Suite Community Edition, I would encourage you to walk through the steps in the solution on the PortSwigger site until you get to the painfully slow automation step, then try writing your own script before running one of mine. Hopefully this helps you learn so that you can get a job or bug bounty that pays for that Professional license!

## Requirements
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://requests.readthedocs.io/en/master/)

## Install in a virtual environment (recommended)
### Linux
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Windows (PowerShell)
```
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

You may run into issues depending on how Python is installed in your environment. Check out the [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) guide.

When you're finished with your virtual environment, deactivate with the `deactivate` command.

## Using scripts
- Log into PortSwigger first and launch the lab with the "Access the lab" button.
- Replace the lab URL in the script with your lab URL.
- The script will prompt you for your PortSwigger account credentials.
- The script will get you the information you need to solve the lab, but may require you to log in to the lab to complete the final step yourself (going to the account page, deleting Carlos, etc.).
