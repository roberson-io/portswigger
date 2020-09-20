from collection import LabCollection


def markdown(file_name: str = "LABS.md", include_status: bool = False):
    labs = LabCollection(file_name="labs.json", include_status=include_status)
    with open(file_name, "w") as f:
        f.write(labs.markdown)
