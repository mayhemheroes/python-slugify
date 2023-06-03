#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from slugify import slugify

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    text = fdp.ConsumeUnicodeNoSurrogates(100)
    ent = fdp.ConsumeBool()
    dec = fdp.ConsumeBool()
    hex = fdp.ConsumeBool()
    max_len = fdp.ConsumeIntInRange(0, 1000)
    word_bound = fdp.ConsumeBool()
    sep = fdp.ConsumeUnicodeNoSurrogates(1)
    so = fdp.ConsumeBool()

    slugify(text, entities=ent, decimal=dec, hexadecimal=hex, max_length=max_len, word_boundary=word_bound, separator=sep, save_order=so)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()