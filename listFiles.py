import os
import json


def get_directory_structure(path):
    data = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        data['type'] = 'directory'
        data['children'] = [get_directory_structure(os.path.join(path, child)) for child in os.listdir(path)]
    else:
        data['type'] = 'file'
    return data


def save_directory_structure(path, output_file):
    directory_structure = get_directory_structure(path)
    with open(output_file, 'w') as f:
        json.dump(directory_structure, f, indent=4)


# Usage example:
fileDirectory = "C:/Users/ryanm/WebstormProjects/spellbound/public/tokens"
output_file = 'token_directory.json'
save_directory_structure(fileDirectory, output_file)
