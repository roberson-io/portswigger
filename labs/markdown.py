from collection import LabCollection


def markdown(
    markdown_file: str = "LABS.md",
    json_file: str = "labs.json",
    include_status: bool = False,
):
    labs = LabCollection(file_name=json_file, include_status=include_status)
    with open(markdown_file, "w") as f:
        f.write(labs.markdown)
