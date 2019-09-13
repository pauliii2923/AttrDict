AttrDict is a class that is able to be passed a dictionary or initiated by itself.
It will recurse through it's entries and update any dictionaries or dictionaries inside lists and make them AttrDicts.
It can have values retrieved by indexing as if it were a regular dictionary or by getting the attribute, as if it were an object.

Required: python3.5
virtualenv --python=/Users/$USER/.pyenv/versions/3.5.0/bin/python3.5 venv
