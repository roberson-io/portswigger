import collections
import json
from jinja2 import Template
from typing import Dict, List


class LabCollection:
    def __init__(self, file_name="labs.json"):
        with open(file_name) as f:
            self.all = json.loads(f.read())
        self.categorized = self.categorize(self.all)
        self.markdown = self.to_markdown()
    
    def categorize(self, labs: List) -> Dict:
        levels = collections.defaultdict(collections.OrderedDict)
        for lab in labs:
            levels[lab.get("level")].setdefault(
                lab.get("topic"), []
            ).append(
                {
                    "title": lab.get("title"),
                    "url": lab.get("url"),
                    "status": lab.get("status"),
                }
            )
        return levels

    def to_markdown(self):
        with open("labs.jinja2") as f:
            template = Template(f.read())
        return template.render(collection=self.categorized)
