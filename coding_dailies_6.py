#									~CODING DAILIES~

# 6 - Using a for loop to list all the people currently online on the server

# online_list = ["Bob", "Sally", "Jenkins", "Benny", "Sofia", "Bert", "Dean"]
#
# def check_whos_online():
#     print("People currently online:")
#
#     for name_of_user in online_list:
#         print(name_of_user)
#
# check_whos_online()


# -------------------------------Different Version below using range---------------------------

online_list = ["Bob", "Sally", "Jenkins", "Benny", "Sofia", "Bert", "Dean"]

def check_whos_online():
    print("People currently online:")

    for index in range(len(online_list)):
        print(online_list[index])

check_whos_online()