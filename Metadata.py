#!/bin/python

with open("example.cimg", "wb") as file:
    file.write(b"{MAG")
    file.write((1).to_bytes(8, "little"))
    file.write((79).to_bytes(4, "little"))
    file.write((24).to_bytes(4, "little"))
    file.write(b"W" * (79*24))
