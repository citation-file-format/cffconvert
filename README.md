[![Build Status](https://travis-ci.org/citationcff/citationcff.svg?branch=master)](https://travis-ci.org/citationcff/citationcff)

# citationcff

read [CFF formatted CITATION](https://github.com/citation-file-format) file from a GitHub
url and convert it to BibTex, EndNote, and RIS. Does not support the full
[CFF spec](https://citation-file-format.github.io/assets/pdf/cff-specifications-1.0.3.pdf) yet.

# Install

```bash
# get a copy of the citationcff software
git clone https://github.com/citationcff/citationcff.git
# change directory into citationcff
cd citationcff
# make a Python3.5 virtual environment named .venv35
virtualenv -p /usr/bin/python3.5 .venv35
# activate the virtual environment
source ./.venv35/bin/activate
# install any packages that citationcff needs
pip install -r requirements.txt
```

# Running tests

```bash
# (from the project root)

# run unit tests
python -m unittest discover -s livetest -p "*_test.py"

# run tests against live system (GitHub)
python -m unittest discover -s livetest -p "*_test.py"
```
