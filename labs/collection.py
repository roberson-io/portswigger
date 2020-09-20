import collections
import json
from jinja2 import Template
from typing import Dict, List


class LabCollection:
    def __init__(self, file_name="labs.json", include_status=True):
        with open(file_name) as f:
            self.all = json.loads(f.read())
        self.include_status = include_status
        self.categorized = self.categorize(self.all)
        self.markdown = self.to_markdown()

    def categorize(self, labs: List) -> Dict:
        levels = collections.defaultdict(dict)
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
        keys = ("APPRENTICE", "PRACTITIONER", "EXPERT")
        return collections.OrderedDict((k, levels[k]) for k in keys)

    def to_markdown(self) -> str:
        with open("labs.jinja2") as f:
            template = Template(f.read())
        return template.render(
            collection=self.categorized, include_status=self.include_status
        )
