async def format_skills(response: dict):
    dictionary = {}
    for skill in response['data']['skills']:
        dictionary[skill['index']] = skill['ability_score']['index']

    lines = []
    for i, (skill, ability) in enumerate(dictionary.items(), start=1):
        lines.append(f"{i} - {skill}: {ability}")
    return "\n".join(lines)


async def format_list(response: dict, key: str, field: str = "index") -> str:
    items = response.get("data", {}).get(key, [])
    if not items:
        return "Nenhum resultado encontrado."

    lines = [f"{i} - {rule.get(field, '')}" for i, rule in enumerate(items, start=1)]
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

async def dicts_to_str(dict_list):
    """
    Recebe uma lista de dicionários e retorna uma string formatada.
    Cada dicionário é separado por '###############'.
    """
    if not isinstance(dict_list, list):
        raise ValueError("A função espera receber uma lista de dicionários.")

    def format_dict(data, indent=0):
        """Formata um único dicionário recursivamente"""
        lines = []
        prefix = " " * indent

        if isinstance(data, dict):
            for key, value in data.items():
                if value is None:  # Ignora nulos
                    continue
                if isinstance(value, (dict, list)):
                    lines.append(f"{prefix}{key}:")
                    lines.append(format_dict(value, indent + 2))
                else:
                    lines.append(f"{prefix}{key}: {value}")

        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    lines.append(f"{prefix}- {format_dict(item, indent + 2)}")
                else:
                    lines.append(f"{prefix}- {item}")

        else:
            lines.append(f"{prefix}{data}")

        return "\n".join(line for line in lines if line.strip())

    # Processa cada dicionário da lista e junta com separador
    formatted_blocks = [format_dict(d) for d in dict_list]
    return "\n###############\n".join(formatted_blocks)


