height = 10
wigth = 10

grid_model = [0] * height

for i in range(height):
    grid_model[i] = [0] * wigth
grid_model[5][2] = 1
print(grid_model)
print(grid_model[5][2])
