skumriq_kg = float(input())
caca_kg = float(input())
quantity_palamud_in_kg = float(input())
quantity_safrid_in_kg = float(input())
quantity_midi_in_kg = int(input())

midi_price = 7.50
palamud_price = skumriq_kg * 1.6
safrid_price = caca_kg * 1.8
total_palamud = palamud_price * quantity_palamud_in_kg
total_safrid =safrid_price * quantity_safrid_in_kg
total_midi = midi_price * quantity_midi_in_kg

grand_total = total_palamud + total_safrid + total_midi
print(f"{grand_total:.2f}")

