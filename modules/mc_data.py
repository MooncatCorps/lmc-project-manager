def display_requests(data: dict, values: list[str], terse = True) -> None:
    for value in values:
        proper_name = "" if terse else value.capitalize().replace(".", " ")
        separator = "" if terse else ": "

        value = get_property_or_unspecified(value, data)
        print(f"{proper_name}{separator}{value}")


def get_property(fqname: str, data: dict) -> str:
    sections = fqname.split(".")
    mut_data = data
    for section in sections:
        if not section in mut_data:
            return ""
        mut_data = mut_data[section]

        if type(mut_data) is str:
            return mut_data

    return ""


def get_property_or_unspecified(fqname: str, data: dict):
    val = get_property(fqname, data)
    if not val:
        return "Unspecified"

    return val

