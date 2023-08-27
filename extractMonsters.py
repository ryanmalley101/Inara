import requests
import json

def get_monsters_by_slug(slug):
    url = f'https://api.open5e.com/monsters/?document__slug={slug}'
    monsters = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            monsters.extend(data['results'])
            url = data['next']
        else:
            print(f"Failed to retrieve data from API. Status code: {response.status_code}")
            return

    simplified_monsters = [{'name': monster['name'], 'slug': monster['slug']} for monster in monsters]
    json_filename = "srd_monsters.json"
    export_to_json(simplified_monsters, json_filename)
    print(f"Data exported to {json_filename} successfully.")
    return simplified_monsters

def get_spells_by_slug(slug):
    url = f'https://api.open5e.com/spells/?document__slug={slug}'
    spells = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            spells.extend(data['results'])
            url = data['next']
        else:
            print(f"Failed to retrieve data from API. Status code: {response.status_code}")
            return

    simplified_spells = [{'name': spell['name'], 'slug': spell['slug']} for spell in spells]
    json_filename = "srd_spells.json"
    export_to_json(simplified_spells, json_filename)
    print(f"Data exported to {json_filename} successfully.")
    return simplified_spells

def get_feats_by_slug(slug):
    url = f'https://api.open5e.com/feats/?document__slug={slug}'
    feats = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            feats.extend(data['results'])
            url = data['next']
        else:
            print(f"Failed to retrieve data from API. Status code: {response.status_code}")
            return

    simplified_feats = [{'name': feat['name'], 'slug': feat['slug']} for feat in feats]
    json_filename = "srd_feats.json"
    export_to_json(simplified_feats, json_filename)
    print(f"Data exported to {json_filename} successfully.")
    return simplified_feats

def get_conditions_by_slug(slug):
    url = f'https://api.open5e.com/conditions/?document__slug={slug}'
    conditions = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            conditions.extend(data['results'])
            url = data['next']
        else:
            print(f"Failed to retrieve data from API. Status code: {response.status_code}")
            return

    simplified_conditions = [{'name': condition['name'], 'slug': condition['slug']} for condition in conditions]
    json_filename = "srd_conditions.json"
    export_to_json(simplified_conditions, json_filename)
    print(f"Data exported to {json_filename} successfully.")
    return simplified_conditions

def get_magic_items_by_slug(slug):
    url = f'https://api.open5e.com/magicitems/?document__slug={slug}'
    magic_items = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            magic_items.extend(data['results'])
            url = data['next']
        else:
            print(f"Failed to retrieve data from API. Status code: {response.status_code}")
            return

    simplified_magic_items = [{'name': magic_item['name'], 'slug': magic_item['slug']} for magic_item in magic_items]
    json_filename = "srd_magic_items.json"
    export_to_json(simplified_magic_items, json_filename)
    print(f"Data exported to {json_filename} successfully.")
    return simplified_magic_items

def get_weapons_by_slug(slug):
    url = f'https://api.open5e.com/weapons/?document__slug={slug}'
    weapons = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weapons.extend(data['results'])
            url = data['next']
        else:
            print(f"Failed to retrieve data from API. Status code: {response.status_code}")
            return

    simplified_weapons = [{'name': weapon['name'], 'slug': weapon['slug']} for weapon in weapons]
    json_filename = "srd_weapons.json"
    export_to_json(simplified_weapons, json_filename)
    print(f"Data exported to {json_filename} successfully.")
    return simplified_weapons

def get_armors_by_slug(slug):
    url = f'https://api.open5e.com/armor/?document__slug={slug}'
    armors = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            armors.extend(data['results'])
            url = data['next']
        else:
            print(f"Failed to retrieve data from API. Status code: {response.status_code}")
            return

    simplified_armors = [{'name': armor['name'], 'slug': armor['slug']} for armor in armors]
    json_filename = "srd_armors.json"
    export_to_json(simplified_armors, json_filename)
    print(f"Data exported to {json_filename} successfully.")
    return simplified_armors

def export_to_json(dictionary, filename):
    with open(filename, 'w') as file:
        json.dump(dictionary, file, indent=4)

if __name__ == "__main__":
    document_slug = 'wotc-srd'

    monsters = get_monsters_by_slug(document_slug)
    spells = get_spells_by_slug(document_slug)
    feats = get_feats_by_slug(document_slug)
    conditions = get_conditions_by_slug(document_slug)
    magic_items = get_magic_items_by_slug(document_slug)
    weapons = get_weapons_by_slug(document_slug)
    armor = get_armors_by_slug(document_slug)

    srd_objects = [
        {
            "name": "Monsters",
            "items": monsters
        },
        {
            "name": "Spells",
            "items": spells
        },
        {
            "name": "Feats",
            "items": feats
        },
        {
            "name": "Conditions",
            "items": conditions
        },
        {
            "name": "Magic Items",
            "items": magic_items
        },
        {
            "name": "Weapons",
            "items": weapons
        },
        {
            "name": "Armor",
            "items": armor
        }
    ]

    export_to_json(srd_objects, "5esrd.json")

    # Extracting only the relevant information (name and document slug) for each monster

