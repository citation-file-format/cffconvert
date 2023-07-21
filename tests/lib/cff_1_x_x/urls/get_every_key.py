import itertools


def get_every_key():
    indentifiers_url_values = ["I", "_"]
    repository_values = ["R", "_"]
    repository_artifact_values = ["A", "_"]
    repository_code_values = ["C", "_"]
    url_values = ["U", "_"]
    combined = [
        indentifiers_url_values,
        repository_values,
        repository_artifact_values,
        repository_code_values,
        url_values
    ]
    return ["".join(combo) for combo in itertools.product(*combined)]
