import os
import sys

project_slug = "{{ cookiecutter.project_slug }}"
author_name = "{{ cookiecutter.author_name }}"

ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if not project_slug or project_slug.startswith(" "):
    print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template.{RESET_ALL}")

    sys.exit(1)

if not author_name or author_name.startswith(" "):
    print(f"{ERROR_COLOR}ERROR: {author_name=} is not a valid name for this template.{RESET_ALL}")

    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're going to create something awesome!")