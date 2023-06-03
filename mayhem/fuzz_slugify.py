#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from slugify import slugify

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    text = fdp.ConsumeUnicodeNoSurrogates(100)

    slugify(text)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()