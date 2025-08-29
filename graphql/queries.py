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
    query Spells($skip: Int, $limit: Int) {
      spells(skip: $skip, limit: $limit) {
        name
      }
    }
    '''

    LIST_SPELL = '''
    query Spells($name: String) {
      spells(name: $name) {
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
    query Monsters($skip: Int, $limit: Int) {
      monsters(skip: $skip, limit: $limit) {
        name
      }
    }
    '''

