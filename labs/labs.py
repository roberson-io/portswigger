#!/usr/bin/env python

import argparse
import getpass
import json
import markdown as md
import portswigger


def get_json(args):
    if args.include_status:
        email = input("Email address: ")
        password = getpass.getpass("Password: ")
        session = portswigger.login(email, password)
    else:
        session = portswigger.new_session()
    labs = portswigger.labs(
        session, verbose=args.verbose, include_status=args.verbose
    )
    with open(args.json_file, "w") as f:
        f.write(json.dumps(labs, indent=4))


def markdown(args):
    md.markdown(
        markdown_file=args.markdown_file,
        json_file=args.json_file,
        include_status=args.include_status,
    )


def refresh(args):
    get_json(args)
    markdown(args)


def add_common_args(parser):
    parser.add_argument(
        "-s",
        "--include-status",
        dest="include_status",
        help="Include 'solved' status",
        action="store_true",
    )
    parser.add_argument(
        "-j",
        "--json-file",
        dest="json_file",
        default="labs.json",
        help="JSON file name",
    )


def add_json_args(parser):
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        help="Display info while collecting data",
        action="store_true",
    )


def add_markdown_args(parser):
    parser.add_argument(
        "-m",
        "--markdown-file",
        dest="markdown_file",
        default="LABS.md",
        help="Markdown file name",
    )


description = "Organize PortSwigger Web Security Academy lab links"
parser = argparse.ArgumentParser(description=description)
subparsers = parser.add_subparsers(help="Sub-commands")

json_parser = subparsers.add_parser(
    "json", help="Collect data for each lab and save to a JSON file."
)
add_common_args(json_parser)
add_json_args(json_parser)
json_parser.set_defaults(func=get_json)

markdown_parser = subparsers.add_parser(
    "markdown",
    help="Use data in JSON file to generate Markdown file.",
)
add_common_args(markdown_parser)
add_markdown_args(markdown_parser)
markdown_parser.set_defaults(func=markdown)

refresh_parser = subparsers.add_parser(
    "refresh", help="Collect JSON then generate Markdown."
)
add_common_args(refresh_parser)
add_json_args(refresh_parser)
add_markdown_args(refresh_parser)
refresh_parser.set_defaults(func=refresh)

args = parser.parse_args()
args.func(args)
