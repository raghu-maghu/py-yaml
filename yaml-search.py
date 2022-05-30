import yaml


def get_recursively(search_dict, field):
    """
    Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []

    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = get_recursively(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)

    return fields_found


stream = open('db2.yaml', 'r')
data = yaml.load(stream,Loader=yaml.FullLoader)

for val in get_recursively(data, 'sca'):
    print(val)
    dict1 = val[0]
    print(type(val))
    print(dict1)
    for val2 in get_recursively(dict1, 'notifications'):
        print(val2)
