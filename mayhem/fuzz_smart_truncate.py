#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from slugify import smart_truncate

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    text = fdp.ConsumeUnicodeNoSurrogates(1000)
    sep = fdp.ConsumeUnicodeNoSurrogates(1)

    try:
        smart_truncate(text, separator=sep, max_length=30, word_boundary=True, save_order=True)
    except ValueError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()