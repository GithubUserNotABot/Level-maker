import pygame.mouse
import add_object__

rect_list = None
step = 2
counter_file = 0
BeginLevel = None
EndLevel = None

def save_level():
    global rect_list, BeginLevel, EndLevel
    rect_list = add_object__.get_objects()
    beginEnd = add_object__.get_beginEnd_()
    # flags
    if not rect_list:
        # empty flag
        print("You need to make stuff before Saving...")
        return Exception
    if rect_list:
        # no begin-level, and end-level flag
        if beginEnd[0] is None:
            print("\nYou need to have a Begin level\nPress 1 to make one")
            return Exception
        if beginEnd[1] is None:
            print("\nYou need to have a End level\nPress 2 to make one ")
            return Exception

    BeginLevel = [beginEnd[0][1], beginEnd[0][2]]
    EndLevel = [beginEnd[1][1], beginEnd[1][2]]
    rect_list.remove((beginEnd[0]))
    rect_list.remove((beginEnd[1]))


    if rect_list:
        user = input("Are you sure you want to save the level? (Y or N) : ")
        if user.upper() == "Y":

            game_object = {
                "end level": EndLevel,
                "begin level": BeginLevel,
                "obstacles": rect_list,
            }

            file = open("levels.txt", 'a')
            file.write(str(game_object) + "\n")
            file.close()
            print(" == Saved Successfully! == ")
            add_object__.make(BeginLevel[0], (BeginLevel[1][0], BeginLevel[1][1]), (BeginLevel[1][2], BeginLevel[1][3]), cntrl="begin level")
            add_object__.make(EndLevel[0], (EndLevel[1][0], EndLevel[1][1]), (EndLevel[1][2], EndLevel[1][3]), cntrl="end level")
            return None

def load_level():
    # Seeing how many lines there are in the file
    global counter_file, BeginLevel, EndLevel
    file = open("levels.txt", 'r')
    file_read = file.read()
    file.close()
    CoList = file_read.split("\n")
    for i in CoList:
        if i:
            counter_file += 1
    # Getting user input for the file they want to open
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

    BeginLevel = dict_begin[0], (dict_begin[1][0], dict_begin[1][1], dict_begin[1][2], dict_begin[1][3])
    EndLevel = dict_end[0], (dict_end[1][0], dict_end[1][1], dict_end[1][2], dict_end[1][3])

    counter = 0
    for i in range(len(dict_obstacles)):
        add_object__.make(dict_obstacles[counter][0], (dict_obstacles[counter][1][0], dict_obstacles[counter][1][1]), (dict_obstacles[counter][1][2], dict_obstacles[counter][1][3]))
        counter += 1
    # makes the "begin level" block
    begin_level(override=(BeginLevel[1][0], BeginLevel[1][1]))
    # makes the "end level" block
    end_level(override=(EndLevel[1][0], EndLevel[1][1]))

    # YAY!!!
    print(" === Loaded Successfully === ")
def begin_level(override=(int, int)):
    # flag
    if add_object__.get_beginEnd_() is not None:
        if add_object__.get_beginEnd_()[0] is not None:
            add_object__.remove_begin()
    x, y = pygame.mouse.get_pos()
    if isinstance(list(locals().values())[0][0], int) and isinstance(list(locals().values())[0][1], int):
        add_object__.make((0, 255, 255), override, (50, 65), cntrl="begin level")
        return None
    add_object__.make((0, 255, 255), (x, y), (50, 65), cntrl="begin level")
def end_level(override=(int, int)):
    # flag
    if add_object__.get_beginEnd_() is not None:
        if add_object__.get_beginEnd_()[1] is not None:
            add_object__.remove_end()
    x, y = pygame.mouse.get_pos()
    if isinstance(list(locals().values())[0][0], int) and isinstance(list(locals().values())[0][1], int):
        add_object__.make((255, 0, 255), override, (50, 65), cntrl="end level")
        return None
    add_object__.make((255, 0, 255), (x, y), (50, 65), cntrl="end level")

