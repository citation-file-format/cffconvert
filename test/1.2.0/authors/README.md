The subdirectories here contain various combinations of author properties, mirroring the setup in https://github.com/citation-file-format/cff-converter-python/blob/2.0.0/cffconvert/behavior_shared/schemaorg_author_shared.py 

1. `authors[i].given-names`
2. `authors[i].family-names` (including name particle and suffix)
3. `authors[i].alias`
4. `authors[i].name`
5. `authors[i].affiliation`
6. `authors[i].orcid`
7. `authors[i].email`

There are tests for a singular author (`./one`) and tests for when there are two authors (`./two`).

The table below lists the naming convention based on the state of an author in `CITATION.cff`:

| subdirectory | has_given_name | has_family_name | has_alias | has_name | has_affiliation | has_orcid | has_email |
|--------------|----------------|-----------------|-----------|----------|-----------------|-----------|-----------|
| `GFANAOE`    | True           | True            | True      | True     | True            | True      | True      |
| `GFANA_E`    | True           | True            | True      | True     | True            | False     | True      |
| `GFAN_OE`    | True           | True            | True      | True     | False           | True      | True      |
| `GFAN__E`    | True           | True            | True      | True     | False           | False     | True      |
| `GFA_AOE`    | True           | True            | True      | False    | True            | True      | True      |
| `GFA_A_E`    | True           | True            | True      | False    | True            | False     | True      |
| `GFA__OE`    | True           | True            | True      | False    | False           | True      | True      |
| `GFA___E`    | True           | True            | True      | False    | False           | False     | True      |
| `GF_NAOE`    | True           | True            | False     | True     | True            | True      | True      |
| `GF_NA_E`    | True           | True            | False     | True     | True            | False     | True      |
| `GF_N_OE`    | True           | True            | False     | True     | False           | True      | True      |
| `GF_N__E`    | True           | True            | False     | True     | False           | False     | True      |
| `GF__AOE`    | True           | True            | False     | False    | True            | True      | True      |
| `GF__A_E`    | True           | True            | False     | False    | True            | False     | True      |
| `GF___OE`    | True           | True            | False     | False    | False           | True      | True      |
| `GF____E`    | True           | True            | False     | False    | False           | False     | True      |
| `G_ANAOE`    | True           | False           | True      | True     | True            | True      | True      |
| `G_ANA_E`    | True           | False           | True      | True     | True            | False     | True      |
| `G_AN_OE`    | True           | False           | True      | True     | False           | True      | True      |
| `G_AN__E`    | True           | False           | True      | True     | False           | False     | True      |
| `G_A_AOE`    | True           | False           | True      | False    | True            | True      | True      |
| `G_A_A_E`    | True           | False           | True      | False    | True            | False     | True      |
| `G_A__OE`    | True           | False           | True      | False    | False           | True      | True      |
| `G_A___E`    | True           | False           | True      | False    | False           | False     | True      |
| `G__NAOE`    | True           | False           | False     | True     | True            | True      | True      |
| `G__NA_E`    | True           | False           | False     | True     | True            | False     | True      |
| `G__N_OE`    | True           | False           | False     | True     | False           | True      | True      |
| `G__N__E`    | True           | False           | False     | True     | False           | False     | True      |
| `G___AOE`    | True           | False           | False     | False    | True            | True      | True      |
| `G___A_E`    | True           | False           | False     | False    | True            | False     | True      |
| `G____OE`    | True           | False           | False     | False    | False           | True      | True      |
| `G_____E`    | True           | False           | False     | False    | False           | False     | True      |
| `_FANAOE`    | False          | True            | True      | True     | True            | True      | True      |
| `_FANA_E`    | False          | True            | True      | True     | True            | False     | True      |
| `_FAN_OE`    | False          | True            | True      | True     | False           | True      | True      |
| `_FAN__E`    | False          | True            | True      | True     | False           | False     | True      |
| `_FA_AOE`    | False          | True            | True      | False    | True            | True      | True      |
| `_FA_A_E`    | False          | True            | True      | False    | True            | False     | True      |
| `_FA__OE`    | False          | True            | True      | False    | False           | True      | True      |
| `_FA___E`    | False          | True            | True      | False    | False           | False     | True      |
| `_F_NAOE`    | False          | True            | False     | True     | True            | True      | True      |
| `_F_NA_E`    | False          | True            | False     | True     | True            | False     | True      |
| `_F_N_OE`    | False          | True            | False     | True     | False           | True      | True      |
| `_F_N__E`    | False          | True            | False     | True     | False           | False     | True      |
| `_F__AOE`    | False          | True            | False     | False    | True            | True      | True      |
| `_F__A_E`    | False          | True            | False     | False    | True            | False     | True      |
| `_F___OE`    | False          | True            | False     | False    | False           | True      | True      |
| `_F____E`    | False          | True            | False     | False    | False           | False     | True      |
| `__ANAOE`    | False          | False           | True      | True     | True            | True      | True      |
| `__ANA_E`    | False          | False           | True      | True     | True            | False     | True      |
| `__AN_OE`    | False          | False           | True      | True     | False           | True      | True      |
| `__AN__E`    | False          | False           | True      | True     | False           | False     | True      |
| `__A_AOE`    | False          | False           | True      | False    | True            | True      | True      |
| `__A_A_E`    | False          | False           | True      | False    | True            | False     | True      |
| `__A__OE`    | False          | False           | True      | False    | False           | True      | True      |
| `__A___E`    | False          | False           | True      | False    | False           | False     | True      |
| `___NAOE`    | False          | False           | False     | True     | True            | True      | True      |
| `___NA_E`    | False          | False           | False     | True     | True            | False     | True      |
| `___N_OE`    | False          | False           | False     | True     | False           | True      | True      |
| `___N__E`    | False          | False           | False     | True     | False           | False     | True      |
| `____AOE`    | False          | False           | False     | False    | True            | True      | True      |
| `____A_E`    | False          | False           | False     | False    | True            | False     | True      |
| `_____OE`    | False          | False           | False     | False    | False           | True      | True      |
| `______E`    | False          | False           | False     | False    | False           | False     | True      |
| `GFANAO_`    | True           | True            | True      | True     | True            | True      | False     |
| `GFANA__`    | True           | True            | True      | True     | True            | False     | False     |
| `GFAN_O_`    | True           | True            | True      | True     | False           | True      | False     |
| `GFAN___`    | True           | True            | True      | True     | False           | False     | False     |
| `GFA_AO_`    | True           | True            | True      | False    | True            | True      | False     |
| `GFA_A__`    | True           | True            | True      | False    | True            | False     | False     |
| `GFA__O_`    | True           | True            | True      | False    | False           | True      | False     |
| `GFA____`    | True           | True            | True      | False    | False           | False     | False     |
| `GF_NAO_`    | True           | True            | False     | True     | True            | True      | False     |
| `GF_NA__`    | True           | True            | False     | True     | True            | False     | False     |
| `GF_N_O_`    | True           | True            | False     | True     | False           | True      | False     |
| `GF_N___`    | True           | True            | False     | True     | False           | False     | False     |
| `GF__AO_`    | True           | True            | False     | False    | True            | True      | False     |
| `GF__A__`    | True           | True            | False     | False    | True            | False     | False     |
| `GF___O_`    | True           | True            | False     | False    | False           | True      | False     |
| `GF_____`    | True           | True            | False     | False    | False           | False     | False     |
| `G_ANAO_`    | True           | False           | True      | True     | True            | True      | False     |
| `G_ANA__`    | True           | False           | True      | True     | True            | False     | False     |
| `G_AN_O_`    | True           | False           | True      | True     | False           | True      | False     |
| `G_AN___`    | True           | False           | True      | True     | False           | False     | False     |
| `G_A_AO_`    | True           | False           | True      | False    | True            | True      | False     |
| `G_A_A__`    | True           | False           | True      | False    | True            | False     | False     |
| `G_A__O_`    | True           | False           | True      | False    | False           | True      | False     |
| `G_A____`    | True           | False           | True      | False    | False           | False     | False     |
| `G__NAO_`    | True           | False           | False     | True     | True            | True      | False     |
| `G__NA__`    | True           | False           | False     | True     | True            | False     | False     |
| `G__N_O_`    | True           | False           | False     | True     | False           | True      | False     |
| `G__N___`    | True           | False           | False     | True     | False           | False     | False     |
| `G___AO_`    | True           | False           | False     | False    | True            | True      | False     |
| `G___A__`    | True           | False           | False     | False    | True            | False     | False     |
| `G____O_`    | True           | False           | False     | False    | False           | True      | False     |
| `G______`    | True           | False           | False     | False    | False           | False     | False     |
| `_FANAO_`    | False          | True            | True      | True     | True            | True      | False     |
| `_FANA__`    | False          | True            | True      | True     | True            | False     | False     |
| `_FAN_O_`    | False          | True            | True      | True     | False           | True      | False     |
| `_FAN___`    | False          | True            | True      | True     | False           | False     | False     |
| `_FA_AO_`    | False          | True            | True      | False    | True            | True      | False     |
| `_FA_A__`    | False          | True            | True      | False    | True            | False     | False     |
| `_FA__O_`    | False          | True            | True      | False    | False           | True      | False     |
| `_FA____`    | False          | True            | True      | False    | False           | False     | False     |
| `_F_NAO_`    | False          | True            | False     | True     | True            | True      | False     |
| `_F_NA__`    | False          | True            | False     | True     | True            | False     | False     |
| `_F_N_O_`    | False          | True            | False     | True     | False           | True      | False     |
| `_F_N___`    | False          | True            | False     | True     | False           | False     | False     |
| `_F__AO_`    | False          | True            | False     | False    | True            | True      | False     |
| `_F__A__`    | False          | True            | False     | False    | True            | False     | False     |
| `_F___O_`    | False          | True            | False     | False    | False           | True      | False     |
| `_F_____`    | False          | True            | False     | False    | False           | False     | False     |
| `__ANAO_`    | False          | False           | True      | True     | True            | True      | False     |
| `__ANA__`    | False          | False           | True      | True     | True            | False     | False     |
| `__AN_O_`    | False          | False           | True      | True     | False           | True      | False     |
| `__AN___`    | False          | False           | True      | True     | False           | False     | False     |
| `__A_AO_`    | False          | False           | True      | False    | True            | True      | False     |
| `__A_A__`    | False          | False           | True      | False    | True            | False     | False     |
| `__A__O_`    | False          | False           | True      | False    | False           | True      | False     |
| `__A____`    | False          | False           | True      | False    | False           | False     | False     |
| `___NAO_`    | False          | False           | False     | True     | True            | True      | False     |
| `___NA__`    | False          | False           | False     | True     | True            | False     | False     |
| `___N_O_`    | False          | False           | False     | True     | False           | True      | False     |
| `___N___`    | False          | False           | False     | True     | False           | False     | False     |
| `____AO_`    | False          | False           | False     | False    | True            | True      | False     |
| `____A__`    | False          | False           | False     | False    | True            | False     | False     |
| `_____O_`    | False          | False           | False     | False    | False           | True      | False     |
| `_______`    | False          | False           | False     | False    | False           | False     | False     |
