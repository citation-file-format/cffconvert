import itertools


def get_every_key():
    given_name_values = ["G", "_"]
    family_name_values = ["F", "_"]
    alias_values = ["A", "_"]
    name_values = ["N", "_"]
    affiliation_values = ["A", "_"]
    orcid_values = ["O", "_"]
    email_values = ["E", "_"]
    combined = [
        given_name_values,
        family_name_values,
        alias_values,
        name_values,
        affiliation_values,
        orcid_values,
        email_values
    ]
    return ["".join(combo) for combo in itertools.product(*combined)]
