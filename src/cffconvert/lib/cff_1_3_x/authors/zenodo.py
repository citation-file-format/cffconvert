from cffconvert.lib.cff_1_x_x.authors.zenodo import ZenodoAuthor

def _get_id_from_ror_url(affiliation):
    return affiliation.get("ror").replace("https://ror.org/", "")

# transform the input json
def _parse_affiliations(json_dict, affiliations):
    # handle multiple affiliations, and output a list
    if type(affiliations) == list:
        new_affil = []
        for affil in affiliations:
            # only string
            if type(affil) == str:
                new_affil.append({'name': affil})
            else:
                # if 'ror' is present replace 'ror' with 'id' in the json
                if 'ror' in affil:
                    affil['id'] = _get_id_from_ror_url(affil)
                    del affil['ror']
                new_affil.append(affil)
        json_dict["affiliations"] = new_affil
    # otherwise default to handling it as plain string
    elif type(affiliations) == str:
        json_dict["affiliation"] = affiliations

    return json_dict

# pylint: disable=too-few-public-methods
class ZenodoAuthorAffiliation(ZenodoAuthor):

    def __init__(self, author):
        super().__init__(author)

    def _from_affiliation(self):
        return _parse_affiliations({}, self._author.get("affiliation"))

    def _from_affiliation_and_orcid(self):
        return _parse_affiliations(
            {
                "affiliation": self._author.get("affiliation"),
                "orcid": self._get_id_from_orcid_url()
            },
            self._author.get("affiliation"))

    def _from_alias_and_affiliation(self):
        return parse_affilations(
            {
                "name": self._author.get("alias")
            },
            self._author.get("affiliation"))

    def _from_alias_and_affiliation_and_orcid(self):
        return _parse_affiliations(
            {
                "name": self._author.get("alias"),
                "orcid": self._get_id_from_orcid_url()
            },
            self._author.get("affiliation"))

    def _from_given_and_affiliation(self):
        return _parse_affiliations(
            {
                "name": self._author.get("given-names")
            },
            self._author.get("affiliation"))
    
    def _from_given_and_affiliation_and_orcid(self):
        return _parse_affiliations(
            {
                "name": self._author.get("given-names"),
                "orcid": self._get_id_from_orcid_url()
            },
            self._author.get("affiliation"))

    def _from_given_and_last_and_affiliation(self):
        return _parse_affiliations(
            {
                "name": self._get_full_last_name() + ", " + self._author.get("given-names")
            },
            self._author.get("affiliation"))
    
    def _from_given_and_last_and_affiliation_and_orcid(self):
        return _parse_affiliations(
            {
            "name": self._get_full_last_name() + ", " + self._author.get("given-names"),
            "orcid": self._get_id_from_orcid_url()
            },
            self._author.get("affiliation")
        )

    def _from_last_and_affiliation(self):
        return _parse_affiliations(
            {
                "name": self._get_full_last_name()
            },
            self._author.get("affiliation"))
    
    def _from_last_and_affiliation_and_orcid(self):
        return _parse_affiliations(
            {
                "name": self._get_full_last_name(),
            "orcid": self._get_id_from_orcid_url()
            },
            self._author.get("affiliation"))
    
    def _from_name_and_affiliation(self):
        return _parse_affiliations(
            {
            "name": self._author.get("name")
            },
            self._author.get("affiliation")
        )

    def _from_name_and_affiliation_and_orcid(self):
        return _parse_affiliations(
            {
                "name": self._author.get("name"),
                "orcid": self._get_id_from_orcid_url()
            },
            self._author.get("affiliation"))
