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

The table below lists the naming convention based on the state of an author in `CITATION.cff`:

| subdirectory | has_given_name | has_family_name | has_alias | has_name | has_affiliation | has_orcid | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `GFANAO` | True | True | True | True | True | True |
| `GFANA_` | True | True | True | True | True | False |
| `GFAN_O` | True | True | True | True | False | True |
| `GFAN__` | True | True | True | True | False | False |
| `GFA_AO` | True | True | True | False | True | True |
| `GFA_A_` | True | True | True | False | True | False |
| `GFA__O` | True | True | True | False | False | True |
| `GFA___` | True | True | True | False | False | False |
| `GF_NAO` | True | True | False | True | True | True |
| `GF_NA_` | True | True | False | True | True | False |
| `GF_N_O` | True | True | False | True | False | True |
| `GF_N__` | True | True | False | True | False | False |
| `GF__AO` | True | True | False | False | True | True |
| `GF__A_` | True | True | False | False | True | False |
| `GF___O` | True | True | False | False | False | True |
| `GF____` | True | True | False | False | False | False |
| `G_ANAO` | True | False | True | True | True | True |
| `G_ANA_` | True | False | True | True | True | False |
| `G_AN_O` | True | False | True | True | False | True |
| `G_AN__` | True | False | True | True | False | False |
| `G_A_AO` | True | False | True | False | True | True |
| `G_A_A_` | True | False | True | False | True | False |
| `G_A__O` | True | False | True | False | False | True |
| `G_A___` | True | False | True | False | False | False |
| `G__NAO` | True | False | False | True | True | True |
| `G__NA_` | True | False | False | True | True | False |
| `G__N_O` | True | False | False | True | False | True |
| `G__N__` | True | False | False | True | False | False |
| `G___AO` | True | False | False | False | True | True |
| `G___A_` | True | False | False | False | True | False |
| `G____O` | True | False | False | False | False | True |
| `G_____` | True | False | False | False | False | False |
| `_FANAO` | False | True | True | True | True | True |
| `_FANA_` | False | True | True | True | True | False |
| `_FAN_O` | False | True | True | True | False | True |
| `_FAN__` | False | True | True | True | False | False |
| `_FA_AO` | False | True | True | False | True | True |
| `_FA_A_` | False | True | True | False | True | False |
| `_FA__O` | False | True | True | False | False | True |
| `_FA___` | False | True | True | False | False | False |
| `_F_NAO` | False | True | False | True | True | True |
| `_F_NA_` | False | True | False | True | True | False |
| `_F_N_O` | False | True | False | True | False | True |
| `_F_N__` | False | True | False | True | False | False |
| `_F__AO` | False | True | False | False | True | True |
| `_F__A_` | False | True | False | False | True | False |
| `_F___O` | False | True | False | False | False | True |
| `_F____` | False | True | False | False | False | False |
| `__ANAO` | False | False | True | True | True | True |
| `__ANA_` | False | False | True | True | True | False |
| `__AN_O` | False | False | True | True | False | True |
| `__AN__` | False | False | True | True | False | False |
| `__A_AO` | False | False | True | False | True | True |
| `__A_A_` | False | False | True | False | True | False |
| `__A__O` | False | False | True | False | False | True |
| `__A___` | False | False | True | False | False | False |
| `___NAO` | False | False | False | True | True | True |
| `___NA_` | False | False | False | True | True | False |
| `___N_O` | False | False | False | True | False | True |
| `___N__` | False | False | False | True | False | False |
| `____AO` | False | False | False | False | True | True |
| `____A_` | False | False | False | False | True | False |
| `_____O` | False | False | False | False | False | True |
| `______` | False | False | False | False | False | False |
