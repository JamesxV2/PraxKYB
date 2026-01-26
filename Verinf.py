#!/bin/python

with open ("example.cimg", "wb") as file:
    file.write(b"cm6e")
    file.write((135).to_bytes(2, "little"))
