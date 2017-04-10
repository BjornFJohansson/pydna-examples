#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import os
import pathlib
import sys

exit_=0

thisdir = os.path.dirname(os.path.realpath(__file__))

for dirpath, dirnames, filenames in os.walk(thisdir):
    if dirpath.startswith(('.','_')): continue
    for file_ in filenames:
        if not file_.endswith(".ipynb"): continue
        if file_=="index.ipynb": continue
        p = pathlib.Path(os.path.join(dirpath, file_))
        if any( [f for f in p.parts if f.startswith(("_","."))] ): continue    
        os.chdir(dirpath)
        print(file_)
        exit_+=pytest.cmdline.main( ["--verbose", "--capture=no", "--nbval", file_] )
print("run_test.py finished with exit code {}".format(exit_))

sys.exit(exit_)