- citation.cff has been validated as follows:


    ```
    curl https://raw.githubusercontent.com/citation-file-format/schema/86e6701980d6e43db645ec47f21ceeee17eb30d0/CFF-Core/schema.yaml > schema.yaml
    pip install pykwalifire
    pykwalifire -s schema.yaml -d citation.cff -y cff
    ```

- codemeta.json has been validated using https://json-ld.org/playground/
- zenodo.json has been validated as follows:

    ```
    curl https://raw.githubusercontent.com/zenodo/zenodo/22fbff3df385e917cd02a3282ede2d7e6450cb2f/zenodo/modules/deposit/jsonschemas/deposits/records/record-v1.0.0.json > schema.json
    pip install jsonschema
    jsonschema -i zenodo.json schema.json
    ```

    (valid, except for the _deposit key which is absent)





