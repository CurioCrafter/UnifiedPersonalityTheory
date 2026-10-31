#!/usr/bin/env python3
"""Look up every DOI in research/ on Crossref and print its real title and year.

Compare the output with the citation by eye. A failed lookup is worth checking,
but not every real DOI is on Crossref. A passing one does not show the claim is right.

Usage: python analysis/check_dois.py
"""
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request

DOI = re.compile(r"10\.\d{4,9}/[^\s\"<>)\]]+")


def main():
    research = pathlib.Path(__file__).resolve().parent.parent / "research"
    for path in sorted(research.glob("*.md")):
        print(f"\n{path.name}")
        for doi in sorted({d.rstrip(".,;*") for d in DOI.findall(path.read_text(encoding="utf-8"))}):
            url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
            try:
                with urllib.request.urlopen(url, timeout=30) as response:
                    work = json.load(response)["message"]
                year = work.get("issued", {}).get("date-parts", [[None]])[0][0]
                print(f"  ok   {doi}  {year}  {(work.get('title') or ['?'])[0]}")
            except (urllib.error.URLError, TimeoutError) as error:
                print(f"  FAIL {doi}  {error}")
            time.sleep(0.2)


if __name__ == "__main__":
    main()
