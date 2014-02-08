vCard4 module
=============

[![Build Status](https://jenkins.engmark.name:8080/buildStatus/icon?job=vcard4)](https://jenkins.engmark.name:8080/job/vcard4/)

**This is not anywhere near ready for use yet.**

This program can be used for validation and parsing of vCard 4 ([RFC 6350](http://tools.ietf.org/html/rfc6350)) files.

Installation / upgrade
----------------------

If your system uses Python 3 as the system Python, you'll have to install `pip2` and use that instead of `pip` below.

    sudo pip install --upgrade vcard4

Development
-----------

**Download:**

    git clone --recurse-submodules https://github.com/l0b0/vcard4.git

**Test:**

    make test

To test a specific Python version:

    make python_version_major=2 python_version_minor=7 python_version_patch=5 test

Test requirements:

- `gcc`
- `gpg`
- `tar`
- `make`
- `openssl` development headers/libraries
- `wget`
- `zlib` development headers/libraries
