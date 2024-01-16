# 外側nのfor文 --- (*1)
for n in range(1, 9+1):
    line = '|'
    # 内側mのfor文 --- (*2)
    for m in range(1, 9+1):
        value = n * m
        line += f'{value:3d} |' # --- (*3)
    print(line)

