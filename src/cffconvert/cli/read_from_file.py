def read_from_file(infile):
    with open(infile, "r", encoding="utf8") as fid:
        return fid.read()
