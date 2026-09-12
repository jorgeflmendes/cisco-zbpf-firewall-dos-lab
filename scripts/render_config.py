#!/usr/bin/env python3
import argparse
import os
from pathlib import Path
import re


PLACEHOLDER = re.compile(r"\{\{([A-Z][A-Z0-9_]*)\}\}")


def replacement(match: re.Match[str]) -> str:
    name = match.group(1)
    value = os.environ.get(name)
    if not value:
        raise ValueError(f"{name} is required")
    if "\n" in value or "\r" in value:
        raise ValueError(f"{name} must be a single line")
    if len(value) > 25:
        raise ValueError(f"{name} must not exceed 25 characters")
    return value


parser = argparse.ArgumentParser()
parser.add_argument("template", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()

source = args.template.read_text(encoding="utf-8")
args.output.write_text(PLACEHOLDER.sub(replacement, source), encoding="utf-8")
