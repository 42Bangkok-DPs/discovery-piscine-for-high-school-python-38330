for i in range(11):
    table = [i * j for j in range(11)]
    print(f"Table de {i}: {' '.join(map(str, table))}")