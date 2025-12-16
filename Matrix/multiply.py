a = [[1, 2, 3],[4, 5, 6]]
b = [[1, 2], [3, 4], [5, 6]]

rows_a = len(a)
cols_a = len(a[0]) if a else 0
rows_b = len(b)
cols_b = len(b[0]) if b else 0

result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            result[i][j] += a[i][k] * b[k][j]

print(result)
