import re
import random
from graphql.queries import Queries
from graphql.client import run_query
from formater.format_outputs import *


async def get_skills():
    response = await run_query(Queries.LIST_SKILLS)
    formatted_response = await format_skills(response)
    return formatted_response

async def get_rules():
    response = await run_query(Queries.LIST_RULES)
    formatted_response = await format_list(response, 'ruleSections', 'name')
    return formatted_response

async def get_races():
    response = await run_query(Queries.LIST_RACES)
    formatted_response = await format_races(response)
    return formatted_response

async def get_classes():
    response = await run_query(Queries.LIST_CLASSES)
    formatted_response = await format_list(response, 'classes')
    return formatted_response

async def get_conditions():
    response = await run_query(Queries.LIST_CONDITIONS)
    formatted_response = await format_list(response, 'conditions')
    return formatted_response

async def get_spells(var: dict):
    var['limit'] = 205
    response = await run_query(Queries.LIST_SPELLS,variables=var)
    formatted_response = await format_list(response, 'spells', 'name')
    return formatted_response

async def get_spell(spell_name):
    response = await run_query(Queries.LIST_SPELL,{"name":spell_name})
    formatted_response = await dicts_to_str(response['data']['spells'])
    return formatted_response

async def get_monster(monster_name):
    response = await run_query(Queries.LIST_MONSTER,{"name":monster_name})
    formatted_response = await dicts_to_str(response['data']['monsters'])
    return formatted_response

async def get_monsters(var: dict):
    var['limit'] = 205
    response = await run_query(Queries.LIST_MONSTERS,variables=var)
    formatted_response = await format_list(response, 'monsters', 'name')
    return formatted_response

async def roll_dice(expression: str) -> str:
    # regex para validar e separar cada termo (ex: 1d6, 4D2)
    pattern = r'(\d+)[dD](\d+)'
    terms = expression.split('+')

    all_rolls = []

    for term in terms:
        match = re.fullmatch(pattern, term.strip())
        if not match:
            raise ValueError(f"Termo inválido: {term}")
        count, sides = map(int, match.groups())
        rolls = [random.randint(1, sides) for _ in range(count)]
        all_rolls.extend(rolls)

    total = sum(all_rolls)
    rolls_str = " + ".join(map(str, all_rolls))
    return f"{rolls_str} = {total}"

