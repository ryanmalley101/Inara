import csv
import json
import re


def csv_to_dict(csv_path):
    csv_data = []

    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        header = csv_reader.fieldnames

        for row in csv_reader:
            csv_data.append({header[i]: row[header[i]] for i in range(len(header))})

    print(csv_data)
    return csv_data


def parse_aow_text_file(text_path):
    objects = []
    current_object = {}

    with open(text_path, 'r') as text_file:
        lines = text_file.readlines()

        for line in lines:
            if line.startswith("####"):
                weapon_name = line.strip("# \n")
                current_object["name"] = weapon_name
                current_object["slug"] = weapon_name
            elif "SP" in line:
                sp_match = re.search(r'(\d+)\s*SP', line)
                if sp_match:
                    current_object["sp"] = int(sp_match.group(1))
            elif "**Activation Time" in line:
                current_object["activation_time"] = line.split(":")[1].strip()
            elif "**Affinity" in line:
                current_object["affinity"] = line.split(":")[1].strip()
            elif "**Duration" in line:
                current_object["duration"] = line.split(":")[1].strip()
            elif "**Applicable Arms" in line:
                current_object["applicable_arms"] = line.split(":")[1].strip()
            elif line.startswith("*"):
                current_object["lore"] = line.strip("* \n")
            elif line.strip() == "___":
                if current_object != {}:
                    objects.append(current_object)
                    current_object = {"description": ""}
            elif line.strip():
                current_object["description"] += line.strip()

    objects.append(current_object)

    return objects


def parse_weapon_table(input_file):
    def parse_weapon(weapon):
        parts = weapon.split('|')
        print(parts)
        if len(parts) == 6:
            return {
                'type': parts[1].strip(),
                'damage_dice': parts[2].strip().split()[0],
                'damage_type': parts[2].strip().split()[1],
                'weight': parts[3].strip(),
                'attributes': parts[4].strip()
            }
        else:
            return None

    output = []

    with open(input_file, 'r') as file:
        for line in file:
            entry = line.strip()
            if entry:
                parsed_entry = parse_weapon(entry)
                if parsed_entry:
                    output.append(parsed_entry)

    print('parsed weapon table')
    print(output)
    return output


def parse_weapon_text_file(text_path, weapons):
    def find_weapon(weapontype):
        for w in weapons:
            if w["type"].lower().strip() == weapontype.lower().strip():
                print(weapontype)
                return w

    objects = []
    current_object = {}

    with open(text_path, 'r') as text_file:
        lines = text_file.readlines()

        for line in lines:
            if line.startswith("### "):
                print(current_object)
                if current_object != {}:
                    objects.append(current_object)
                current_object = {"name": line.strip("# \n").replace("â€™", "'"),
                                  "slug": line.strip("# \n").replace("â€™", "'")}

            elif "Weapon (" in line:
                weapon_info = line.split("(")[1].split(", ")
                weapon_type = weapon_info[0].replace(')', '').title()
                t = find_weapon(weapon_type)
                print(weapon_type, t)
                current_object["type"] = t["type"]
                current_object["category"] = t["type"] + 's'
                current_object["damage_dice"] = t["damage_dice"]
                current_object["damage_type"] = t["damage_type"]
                current_object["weight"] = t["weight"]
                current_object["properties"] = t["attributes"].split(",")
                current_object["rarity"] = weapon_info[1].replace('\n', '')
            elif line.startswith("**Weapon Skill:"):
                skill_match = re.search(r'(\*\*Weapon Skill: (.+?) \((\d+) SP\)\*\*) (.+)', line)
                if skill_match:
                    current_object["skill_name"] = skill_match.group(2)
                    current_object["skill_sp"] = int(skill_match.group(3))
                    current_object["skill_description"] = skill_match.group(4)
            elif line.startswith("*"):
                current_object["lore"] = line.strip("*#_\n")
            elif line.strip():
                current_object["description"] = line.strip().replace('*', '', -1)

    objects.append(current_object)

    return objects

def parse_magic_weapon_text_file(text_path):

    objects = []
    current_object = {}

    with open(text_path, 'r') as text_file:
        lines = text_file.readlines()

        for line in lines:
            if line.startswith("### "):
                print(current_object)
                if current_object != {}:
                    objects.append(current_object)
                current_object = {"name": line.strip("# \n").replace("â€™", "'"),
                                  "slug": line.strip("# \n").replace("â€™", "'")}

            elif "##### " in line:
                item_type = line.strip()
                current_object["type"] = item_type.strip('##### ')
            elif line.startswith("*"):
                current_object["lore"] = line.strip("*#_\n")
            elif line.strip():
                if "description" in current_object:
                    current_object["desc"] += line
                else:
                    current_object["desc"] = line

    objects.append(current_object)

    return objects


if __name__ == '__main__':
    spells_csv = 'elden_ring_spells.csv'  # Replace with your CSV file path
    elden_ring_spells = csv_to_dict(spells_csv)

    aow_txt = 'ashes_of_war.txt'  # Replace with your text file path
    aow_csv = 'ashes_of_war.csv'  # Replace with desired CSV file path
    parsed_aow = csv_to_dict(aow_csv)

    weapon_table_file = 'elden_ring_weapon_table.txt'
    weapon_table = parse_weapon_table(weapon_table_file)

    weapons_txt = 'elden_ring_weapons.txt'
    parsed_weapons = parse_weapon_text_file(weapons_txt, weapon_table)

    magic_items_txt = 'magic_items.txt'
    parsed_magic_weapons = parse_magic_weapon_text_file(magic_items_txt)

    data = [{"name": "Spells", "items": elden_ring_spells},
            {"name": "Ashes of War", "items": parsed_aow},
            {"name": "Weapons", "items": parsed_weapons},
            {"name": "Magic Items", "items": parsed_magic_weapons}]

    elden_ring_json = 'elden_ring.json'  # Replace with the desired JSON output file path

    with open(elden_ring_json, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print('CSV to JSON conversion complete.')
