from collection import LabCollection


labs = LabCollection()
with open("README.md", "w") as f:
    f.write(labs.markdown)
