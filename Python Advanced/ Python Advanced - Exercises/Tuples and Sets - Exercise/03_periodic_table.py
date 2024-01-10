n = int(input())

chemical_compounds = set()
for _ in range(n):
    for compound in input().split():
        chemical_compounds.add(compound)

print(*chemical_compounds, sep="\n")
