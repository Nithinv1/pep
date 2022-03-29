"""Automatically create PEP 0 (the PEP index),

This file generates and writes the PEP index to disk, ready for later
processing by Sphinx. Firstly, we parse the individual PEP files, getting the
RFC2822 header, and parsing and then validating that metadata.

After collecting and validating all the PEP data, the creation of the index
itself is in three steps:

    1. Output static text.
    2. Format an entry for the PEP.
    3. Output the PEP (both by the category and numerical index).

We then add the newly created PEP 0 file to two Sphinx environment variables
to allow it to be processed as normal.

"""
from __future__ import annotations

import csv
import json
import os
from pathlib import Path
import re
from typing import TYPE_CHECKING

from pep_sphinx_extensions.pep_zero_generator import parser
from pep_sphinx_extensions.pep_zero_generator import writer

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.environment import BuildEnvironment


def create_pep_json(peps: list[parser.PEP], out_dir: str) -> None:
    pep_list = [
        {
            "number": pep.number,
            "title": pep.title,
            "authors": ", ".join(pep.authors.nick for pep.authors in pep.authors),
            "status": pep.status,
            "type": pep.pep_type,
            "url": f"https://peps.python.org/pep-{pep.number:0>4}/",
        }
        for pep in sorted(peps)
    ]

    out_file = os.path.join(out_dir, "peps.json")
    with open(out_file, "w", encoding="UTF-8") as f:
        json.dump(pep_list, f, indent=0)


def create_pep_zero(app: Sphinx, env: BuildEnvironment, docnames: list[str]) -> None:
    # Read from root directory
    path = Path(".")

    pep_zero_filename = "pep-0000"
    peps: list[parser.PEP] = []
    pep_pat = re.compile(r"pep-\d{4}")  # Path.match() doesn't support regular expressions

    # AUTHOR_OVERRIDES.csv is an exception file for PEP0 name parsing
    with open("AUTHOR_OVERRIDES.csv", "r", encoding="utf-8") as f:
        authors_overrides = {}
        for line in csv.DictReader(f):
            full_name = line.pop("Overridden Name")
            authors_overrides[full_name] = line

    for file_path in path.iterdir():
        if not file_path.is_file():
            continue  # Skip directories etc.
        if file_path.match("pep-0000*"):
            continue  # Skip pre-existing PEP 0 files
        if pep_pat.match(str(file_path)) and file_path.suffix in {".txt", ".rst"}:
            pep = parser.PEP(path.joinpath(file_path).absolute(), authors_overrides)
            peps.append(pep)

    pep0_text = writer.PEPZeroWriter().write_pep0(sorted(peps))
    Path(f"{pep_zero_filename}.rst").write_text(pep0_text, encoding="utf-8")

    # Add to files for builder
    docnames.insert(1, pep_zero_filename)
    # Add to files for writer
    env.found_docs.add(pep_zero_filename)

    # Create peps.json
    create_pep_json(peps, app.outdir)
