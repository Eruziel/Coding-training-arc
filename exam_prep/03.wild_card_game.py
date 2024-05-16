def draw_cards(*args: tuple, **kwargs):
    monster = []
    spell = []

    for name, card_type in args:
        if card_type == 'monster':
            monster.append(name)
        elif card_type == 'spell':
            spell.append(name)

    for name, card_type in kwargs.items():
        if card_type == 'monster':
            monster.append(name)
        elif card_type == 'spell':
            spell.append(name)

    if monster and spell:
        monster_str = '\n'.join(f"  ***{n}" for n in reversed(sorted(monster)))
        spell_str = '\n'.join(f"  $$${s}" for s in sorted(spell))
        result = f"Monster cards:\n{monster_str}\nSpell cards:\n{spell_str}"
    elif monster:
        monster_str = '\n'.join(f"  ***{n}" for n in reversed(sorted(monster)))
        result = f"Monster cards:\n{monster_str}"
    elif spell:
        spell_str = '\n'.join(f"  $$${s}" for s in sorted(spell))
        result = f"Spell cards:\n{spell_str}"

    return result


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))