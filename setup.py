#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# To generate DEB package from Python Package:
# sudo pip3 install stdeb
# python3 setup.py --verbose --command-packages=stdeb.command bdist_deb
#
#
# To generate RPM package from Python Package:
# sudo apt-get install rpm
# python3 setup.py bdist_rpm --verbose --fix-python --binary-only
#
#
# To generate EXE MS Windows from Python Package (from MS Windows only):
# python3 setup.py bdist_wininst --verbose
#
#
# To generate PKGBUILD ArchLinux from Python Package (from PyPI only):
# sudo pip3 install git+https://github.com/bluepeppers/pip2arch.git
# pip2arch.py PackageNameHere
#
#
# To Upload to PyPI by executing:
# sudo pip install --upgrade pip setuptools wheel virtualenv
# python3 setup.py bdist_egg bdist_wheel --universal sdist --formats=zip upload --sign


from setuptools import setup


setup(
    py_modules=["apistar_session_cookie"],
)
