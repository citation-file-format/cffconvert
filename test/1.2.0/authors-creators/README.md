The subdirectories here contain various combinations of author properties, mirroring the setup in https://github.com/citation-file-format/cff-converter-python/blob/3265d14b2db2c35b5670247c653556f9e6286093/cffconvert/behavior_shared/schemaorg_author.py 

- `authors[i].given-names`: omitted, valid
- `authors[i].name-particle`: omitted, valid
- `authors[i].family-names`: omitted, valid
- `authors[i].name-suffix`: omitted, valid
- `authors[i].name`: omitted, valid
- `authors[i].alias`: omitted, valid
- `authors[i].affiliation`: omitted, valid
- `authors[i].orcid`: omitted, valid

There are tests for a singular author (`./one`) and tests for when there are two authors (`./two`).

