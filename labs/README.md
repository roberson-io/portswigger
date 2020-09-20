# Scripts to group PortSwigger Web Security Academy labs

## About
The [PortSwigger Web Security Academy labs](https://portswigger.net/web-security)
are a great resource for learning about web application security, but there is
not an easy way to see the labs grouped by difficulty level. These scripts
allow you to collect data about the labs and generate a markdown file with
links grouped by level and topic.

## Requirements
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/)
- [Requests](https://requests.readthedocs.io/en/master/)

## Install in a virtual environment
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

## Usage
### Collect lab data and save to `labs.json`
```
./labs.py json
```

### Convert `labs.json` to `LABS.md`
```
./labs.py markdown
```

### Collect data and convert to Markdown in single step
```
./labs.py refresh
```

### Display progress while collecting JSON
Also works with `refresh` sub-command.
```
./labs.py json --verbose
```

### Include 'solve' status
Examples:
- [labs_with_status.json](https://github.com/roberson-io/portswigger/blob/master/labs/labs_with_status.json)
- [LABS_WITH_STATUS.md](https://github.com/roberson-io/portswigger/blob/master/labs/LABS_WITH_STATUS.md)

Works with all sub-commands. Prompts for PortSwigger login for `json` or `refresh`.
```
./labs.py refresh --include-status
```

### Specify JSON file name
Also works with `refresh` sub-command.
```
./labs.py json --json-file example.json
```

### Specify Markdown file name
Also works with `refresh` sub-command.
```
./labs.py markdown --markdown-file EXAMPLE.md
```
