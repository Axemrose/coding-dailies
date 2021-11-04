#									~CODING DAILIES~

# 7 - using 2D Lists to make something like a map, you insert what you want each room to be

number_grid_map = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in number_grid_map:
    for column in row:
        room_desc_input = input("What would you like room " + str(column) + " to be: ")
        print(room_desc_input)


# vvv somehow this works, but I'd recommend something not using range for now
# for row in number_grid_map:
#     for index in range(len(row)):
#         print(row[index])




# my_rows = 3
# my_columns = 3
# my_grid_map = [[0]*my_columns] * my_rows
# print(my_grid_map)
#
# def insert_room_desc():
#     room_desc_input = input("Insert the desired name of room " + str(column) + ".")
#
# for row in my_grid_map:
#     for column in my_grid_map:
#         insert_room_desc()


