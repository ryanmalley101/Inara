import csv
import re

def parse_text_file(text_path):
    objects = []
    current_object = {}

    with open(text_path, 'r') as text_file:
        lines = text_file.readlines()

        for line in lines:

            if line.startswith("####"):
                objects.append(current_object)
                print(current_object)
                current_object = {"name": line.strip("# \n")}
            elif "SP" in line:
                sp_match = re.search(r'(\d+)\s*SP', line)
                if sp_match:
                    current_object["sp"] = int(sp_match.group(1))
            elif "**Activation Time" in line:
                current_object["activation_time"] = line.split(":")[1].strip().replace("** ", "")
            elif "**Affinity:**" in line:
                current_object["affinity"] = line.split(":")[1].strip().replace("** ", "")
            elif "**Duration" in line:
                current_object["duration"] = line.split(":")[1].strip().replace("** ", "")
            elif "**Applicable Arms" in line:
                current_object["applicable_arms"] = line.split(":")[1].strip().replace("** ", "")
            elif line.startswith("*"):
                current_object["lore"] = line.strip("* \n")
            elif line.strip():
                current_object["description"] = line.strip()

    return objects

def save_objects_to_csv(objects, csv_path):
    fieldnames = ["name", "sp", "activation_time", "affinity", "duration", "applicable_arms", "lore", "description"]

    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(objects)

if __name__ == '__main__':
    text_path = 'ashes_of_war.txt'   # Replace with your text file path
    csv_path = 'ashes_of_war.csv'     # Replace with desired CSV file path
    parsed_objects = parse_text_file(text_path)
    save_objects_to_csv(parsed_objects, csv_path)
    print('CSV conversion complete.')