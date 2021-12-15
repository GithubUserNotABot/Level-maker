import pygame.mouse
import add_object__
import os

rect_list = None
BeginLevel = None
EndLevel = None

def save_level():
    global rect_list, BeginLevel, EndLevel, file_name
    file_name = None

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

    # get user to save as or to a project
    user = input("say: \"[project name]\" : ")
    files = os.listdir(path='levels')
    findList = []
    for i in range(len(os.listdir(path='levels'))):
        if files[i].find(".txt") != -1:
            findList.append(files[i])
    # finds all txt files and puts it in findList
    for i in range(len(findList)):
        if (user + ".txt") == findList[i]:
            file_name = user + ".txt"
    if file_name is None:
        print("couldn't find file, please use \"6\" to create file")
        return

    if rect_list:
        user = input("Are you sure you want to save the level? (Y or N) : ")
        if user.upper() == "Y":
            BeginLevel = [beginEnd[0][1], beginEnd[0][2]]
            EndLevel = [beginEnd[1][1], beginEnd[1][2]]
            rect_list.remove((beginEnd[0]))
            rect_list.remove((beginEnd[1]))

            game_object = {
                "end level": EndLevel,
                "begin level": BeginLevel,
                "obstacles": rect_list,
            }

            file_name = "levels/" + file_name
            file = open(file_name, 'a')
            file.write((str(game_object) + "\n"))
            file.close()
            print(" == Saved Successfully! == ")
            add_object__.make(BeginLevel[0], (BeginLevel[1][0], BeginLevel[1][1]), (BeginLevel[1][2], BeginLevel[1][3]), cntrl="begin level")
            add_object__.make(EndLevel[0], (EndLevel[1][0], EndLevel[1][1]), (EndLevel[1][2], EndLevel[1][3]), cntrl="end level")
            return
    if user.upper() != "Y":
        print("okay, returning to game...")
        return
def load_level():
    # Seeing how many lines there are in the file
    global BeginLevel, EndLevel, file_name
    file_name = None
    user = input("Name of level: ") + ".txt"
    files = os.listdir(path='levels')
    findList = []
    # finds all txt files and puts it in findList
    for i in range(len(os.listdir(path='levels'))):
        if files[i].find(".txt") != -1:
            findList.append(files[i])
    for i in range(len(findList)):
        if user == findList[i]:
            file_name = user
            print(" == file found >> " + str(user) + " << ")
    if file_name is None:
        user = input(" == found no files with that name == \nCreate One? (y or n) : ")
        if user.upper() != "Y":
            print(" === returning to game... === ")
            return
        if user.upper() == "Y":
            user = input("File name: ") + ".txt"
            file_name = user
            file_name = "levels/" + file_name
            file = open(file_name, 'x')
            file.close()
            print(" == File created == ")
            return

    file_name = "levels/" + file_name
    file = open(file_name, 'r')
    file_read = file.read()
    file.close()
    CoList = file_read.split("\n")
    counter_file = 0
    for i in CoList:
        if i:
            counter_file += 1
    # Getting user input for the file they want to open
    user = input("You have " + str(counter_file) + " levels! Which one do you want to load (give it an integer) : ")

    # flag
    try:
        int(user)
    except ValueError:
        print(" === don't tell me something, say a whole number... === ")
        return

    # == actually loading the level ==
    file = open(file_name, 'r')
    file_lines = file.readlines()
    file.close()

    add_object__.reset()
    level_list_raw = file_lines[int(user) - 1]
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
def merge_levels():
    files = os.listdir(path='levels')
    findList = []
    for i in range(len(os.listdir(path='levels'))):
        if files[i].find(".txt") != -1:
            findList.append(files[i])
    user = input(f"\nWhich levels do you want to merge? \n{findList}\n(say: \"[level], [level]\" ex: \"level1, level2\" level1 would be given all the files from level2)\n:")

    # interpret user
    find_comma = user.find(",")
    firstFile = ""
    for i in range(find_comma):
        firstFile = str(firstFile) + user[i]
    find_secondFile = len(firstFile) + 2
    length_secondFile = abs(find_secondFile - len(user))
    secondFile = ""
    for i in range(length_secondFile):
        secondFile = secondFile + str(user[i + find_secondFile])
    firstFile, secondFile = firstFile + ".txt", secondFile + ".txt"
    # flag
    if firstFile == secondFile:
        print(" == both files are the same bro.. why? == ")
        return
    flag1, flag2 = False, False
    for i in range(len(findList)):
        if findList[i] == firstFile:
            flag1 = True
        if findList[i] == secondFile:
            flag2 = True
    if not flag1 or not flag2:
        print(" == No file found or you typed something wrong.. == ")
        return
    # merge second file with first file
    with open(f"levels/{secondFile}") as file:
        while line := file.readline().rstrip():
            first = open(f"levels/{firstFile}", 'a')
            first.write((str(line)) + "\n")
            first.close()

    print(" === Merge Successful === ")
def create_levels():
    user = input("level name (say quit to not make one): ")
    if user.upper() == "QUIT":
        print("== No level was made == ")
        return
    user = user + ".txt"
    file = open(f"levels/{user}", "x")
    file.close()
    print(f" === level {user} was made === ")
def delete_levels():
    user = input("input file to be deleted (say quit to return to game): ")
    if user.upper() == "QUIT":
        print(" == okay returning to game... == ")
        return
    user = user + ".txt"
    files = os.listdir(path='levels')
    findList = []
    for i in range(len(os.listdir(path='levels'))):
        if files[i].find(".txt") != -1:
            findList.append(files[i])
    for i in range(len(findList)):
        if user == findList[i]:
            os.remove("levels/" + user)
            print(f" === okay {user} was deleted === ")
            return
    print("File that you inputted was not found ")
