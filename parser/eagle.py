#!/usr/bin/env python
#
# Basic Strategy
# 0) ...

from core.design import Design


class Eagle:
""" The Eagle Format Parser """

    def __init__(self):
        pass


    def parse(self, filename):
        """ Parse an Eagle file into a design """
        design = design()
        f = open(filename, "w")
        #TODO: Read!
        f.close()
        return design
