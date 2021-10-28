# TODO: Make it so that the user can control the size of the block they place and how big on each axis it is
import pygame
import add_object__

rect_list = None
step = 2
counter_file = 0

def __get_objects(list__):
    global step
    new_list = []
    for _ in range(len(list__) - 2):
        new_list.append(list__[step])
        step += 1
    return new_list

def save_level():
    global rect_list
    rect_list = add_object__.get_objects()
    if rect_list:
        user = input("Are you sure you want to save the level? (Y or N) : ")
        if user.upper() == "Y":
            obstacles = __get_objects(rect_list)
            game_object = {
                "obstacles": obstacles,
                "begin_level": rect_list[0],
                "end_level": rect_list[1]
            }
            file = open("levels.txt", 'a')
            file.write("\n" + str(game_object))
            file.close()
            print(" == Saved Successfully! == ")
            raise SystemExit
    if not rect_list:
        print("You need to make something first, silly!")

def load_level():
    global counter_file
    file = open("levels.txt", 'r')
    file_read = file.read()
    file.close()
    CoList = file_read.split("\n")
    for i in CoList:
        if i:
            counter_file += 1

    user = input("You have " + str(counter_file) + " levels! Which one do you want to load (give it an integer) : ")
    counter_file = 0

    try:
        new_user = int(user)
    except:
        print("has to be an int")
        return None

    # == actually loading the level ==
    file = open("levels.txt", 'r')
    file_lines = file.readlines()
    file.close()

    add_object__.reset()
    level_list_raw = file_lines[new_user - 1]
    level_list = dict(eval(level_list_raw))

    dict_obstacles = level_list.get("obstacles")
    dict_begin = level_list.get("begin level")
    dict_end = level_list.get("end level")

    counter_block = 0
    for _ in range(len(level_list.get("obstacles")) - 1):

        add_object__.make(dict_obstacles[counter_block][0], (dict_obstacles[counter_block][1][0], dict_obstacles[counter_block][1][1]), (dict_obstacles[counter_block][1][2], dict_obstacles[counter_block][1][3]))
        counter_block += 1

    print(" === Loaded Successfully === ")

def begin_level(mouse_pos):
    pass

def end_level(mouse_pos):
    pass
