import json


with open("labs.json") as f:
    labs = json.loads(f.read())
    apprentice = []
    practitioner = []
    expert = []
    for lab in labs:
        lab.pop("status")
        level = lab.get("level")
        if level == "APPRENTICE":
            apprentice.append(lab)
        elif level == "PRACTITIONER":
            practitioner.append(lab)
        else:
            expert.append(lab)

print("# PortSwigger Web Security Academy Labs")
print()
print("## Apprentice")
for lab in apprentice:
    print(
        "{topic}: [{title}]({url})".format(
            topic=lab.get("topic"),
            title=lab.get("title"),
            url=lab.get("url"),
        )
    )
    print()
print("## Practitioner")
print()
for lab in practitioner:
    print(
        "{topic}: [{title}]({url})".format(
            topic=lab.get("topic"),
            title=lab.get("title"),
            url=lab.get("url"),
        )
    )
    print()
print("## Expert")
print()
for lab in expert:
    print(
        "{topic}: [{title}]({url})".format(
            topic=lab.get("topic"),
            title=lab.get("title"),
            url=lab.get("url"),
        )
    )
    print()