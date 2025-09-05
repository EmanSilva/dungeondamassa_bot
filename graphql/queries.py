from enum import Enum

class Queries(str,  Enum):
    LIST_RULES = '''
    query Rules {
      ruleSections {
        name
      }
    }
    '''

    LIST_SKILLS = '''
    query Skills {
      skills {
        index
        ability_score {
          index
        }
      }
    }
    '''

    LIST_RACES = '''
    query Racas {
      races {
        index
        subraces {
          index
        }
      }
    }
    '''

    LIST_CLASSES = '''
    query Class {
      classes {
        index
      }
    }
    '''

    LIST_CONDITIONS = '''
    query Conditions {
      conditions {
        index
      }
    }
    '''

    LIST_SPELLS = '''
    query Spells($level: [Int!], $class: [String!], $limit: Int) {
      spells(level: $level, class: $class, limit: $limit) {
        name
      }
    }
    '''

    LIST_SPELL = '''
    query Spells($name: String) {
      spells(name: $name) {
        name
        concentration
        duration
        material
        range
        desc
        higher_level
      }
    }
    '''

    LIST_MONSTERS = '''
    query Monsters($name: String, $limit: Int, $type: String, $challengeRating: NumberFilterInput, $size: String) {
      monsters(name: $name, limit: $limit, type: $type, challenge_rating: $challengeRating, size: $size) {
        name
      }
    }
    '''

    LIST_MONSTER='''
    query Monsters($name: String) {
      monsters(name: $name) {
        name
        type
        size
        hit_points
        armor_class {
          ... on ArmorClassNatural {
            value
          }
        }
        dexterity
        intelligence
        charisma
        constitution
        strength
        wisdom
        damage_immunities
        damage_resistances
        damage_vulnerabilities
        languages
        proficiencies {
          proficiency {
            name
          }
        }
        speed {
          burrow
          climb
          fly
          hover
          swim
          walk
        }
        actions {
          name
          desc
        }
        legendary_actions {
          name
          desc
        }
        reactions {
          name
          desc
        }
        special_abilities {
          name
          desc
        }
      }
    }
    '''

