heroes = {}

n = int(input())
for _ in range(n):
    data = input().split(' ')
    hero, hp , mp = data
    hp = int(hp)
    mp = int(mp)
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 200
    heroes[hero] = [hp, mp]

command = input()
while command != 'End':
    command = command.split(' - ')
    if command[0] == 'CastSpell':
        cast_spell, hero_name, mp_needed, spell_name = command
        mp_needed = int(mp_needed)
        if mp_needed > heroes[hero_name][1]:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")

    elif command[0] == 'TakeDamage':
        take_damage, hero_name, damage, attacker = command
        damage = int(damage)
        if hero_name in heroes:
            heroes[hero_name][0] -= damage
            if heroes[hero_name][0] > 0:
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
            else:
                print(f"{hero_name} has been killed by {attacker}!")
                heroes.pop(hero_name)


    elif command[0] == 'Recharge':
        recharge, hero_name, amount = command
        amount = int(amount)
        if heroes[hero_name][1] + amount > 200:
            amount = 200 - heroes[hero_name][1]
        heroes[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif command[0] == 'Heal':
        heal, hero_name, amount = command
        amount = int(amount)
        if heroes[hero_name][0] + amount > 100:
            amount = 100 - heroes[hero_name][0]
        heroes[hero_name][0] += amount
        print(f"{hero_name} healed for {amount} HP!")

    command = input()

for key, value in heroes.items():
    print(f'{key}')
    print(f'  HP: {value[0]}')
    print(f'  MP: {value[1]}')