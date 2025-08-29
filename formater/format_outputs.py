async def format_skills(response: dict):
    dictionary = {}
    for skill in response['data']['skills']:
        dictionary[skill['index']] = skill['ability_score']['index']

    lines = []
    for i, (skill, ability) in enumerate(dictionary.items(), start=1):
        lines.append(f"{i} - {skill}: {ability}")
    return "\n".join(lines)


async def format_rules(response: dict):
    lines = []
    for i, rule in enumerate(response['data']['ruleSections'], start=1):
        lines.append(f"{i} - {rule['name']}")

    return "\n".join(lines)

async def format_races(response: dict):
    races = response.get("data", {}).get("races", [])
    lines = []
    for i, race in enumerate(races, start=1):
        race_name = race["index"]
        subraces = race.get("subraces", [])
        if subraces:
            sub_list = ", ".join([s["index"] for s in subraces])
            lines.append(f"{i} - {race_name} (subraces: {sub_list})")
        else:
            lines.append(f"{i} - {race_name}")

    return "\n".join(lines)

async def format_classes(response: dict):
    lines = []
    for i, rule in enumerate(response['data']['classes'], start=1):
        lines.append(f"{i} - {rule['index']}")

    return "\n".join(lines)

async def format_conditions(response: dict):
    lines = []
    for i, rule in enumerate(response['data']['conditions'], start=1):
        lines.append(f"{i} - {rule['index']}")

    return "\n".join(lines)

async def format_spells(response: dict):
    lines = []
    for i, rule in enumerate(response['data']['spells'], start=1):
        lines.append(f"{i} - {rule['name']}")
    return "\n".join(lines)

async def format_spell_description(response: dict):
    lines = []
    concentration = str(response['data']["spells"][0]['concentration'])
    duration = str(response['data']["spells"][0]['duration'])
    material = str(response['data']["spells"][0]['material'])
    alcance = str(response['data']["spells"][0]['range'])

    lines.append(f"concentration: {concentration}")
    lines.append(f"duration: {duration}")
    lines.append(f"material: {material}")
    lines.append(f"alcance: {alcance}")

    lines.append(response["data"]["spells"][0]["desc"][0])
    if response["data"]["spells"][0].get("higher_level"):
        lines.append(response["data"]["spells"][0]["higher_level"][0])

    return "\n".join(lines)

async def format_monsters(response: dict):
    lines = []
    for i, rule in enumerate(response['data']['monsters'], start=1):
        lines.append(f"{i} - {rule['name']}")

    return "\n".join(lines)
