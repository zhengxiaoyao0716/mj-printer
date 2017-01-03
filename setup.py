#!/bin/python
# -*- coding: utf-8 -*-

"""
mj-printer
@author: zhengxiaoyao0716
"""

import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages=[], excludes=[],
    include_files=[],
)

name = 'print_test'

if sys.platform == 'win32':
    name = name + '.exe'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(
        'main.py', base=base, targetName=name,
        compress=True, icon="mjwise.ico",
    )
]

setup(name='main',
      version='1.0',
      description='print_test',
      options=dict(build_exe=buildOptions),
      executables=executables)
