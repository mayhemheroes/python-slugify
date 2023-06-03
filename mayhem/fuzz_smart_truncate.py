#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from slugify import smart_truncate

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    text = fdp.ConsumeUnicodeNoSurrogates(1000)
    sep = fdp.ConsumeUnicodeNoSurrogates(1)
    ml = fdp.ConsumeIntInRange(0, 1000)
    wb = fdp.ConsumeBool()
    so = fdp.ConsumeBool()

    try:
        smart_truncate(text, separator=sep, max_length=ml, word_boundary=wb, save_order=so)
    except ValueError:
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()