import os
import pygame
import level_editor

rect_update_list = []
update_step = 0
collision_step = 0
win2 = pygame.display.set_mode((1000, 900))
player_size2 = None
block_size2 = None
prev_pos = 0, 0
reset_position = 0, 0
player_x, player_y = 0, 0
value = False


def get_beginEnd_():
    return find_specialInstance(rect_update_list)
def get_reset_pos():
    return reset_position
def get_win(win1):
    global win2
    win2 = win1
def get_size(player_size, block_size):
    global player_size2, block_size2
    player_size2 = player_size
    block_size2 = block_size
def get_objects():
    return rect_update_list
def make(color, pos, size, cntrl=None):
    global rect_update_list, win2, reset_position
    # == cntrl | Control for beginning and the end ==
    if cntrl is None:
        rect_update_list.append([color, (pos[0], pos[1], size[0], size[1])])
    if cntrl is not None:
        if cntrl == "end level":
            rect_update_list.append(["end level", color, (pos[0], pos[1], size[0], size[1])])
        if cntrl == "begin level":
            rect_update_list.append(["begin level", color, (pos[0], pos[1], size[0], size[1])])
            reset_position = pos[0], pos[1]
def update__(x, y):
    global update_step, rect_update_list, win2, reset_position, player_y, player_x
    # === Checks for collision for blocks ===
    collision_check = collision(x, y)  # player x and y
    if collision_check is not None:
        if collision_check[0] == "collision":
            player_x, player_y = reset_position[0], reset_position[1]
    # === Loop for drawing all rectangles ===
    if len(rect_update_list) > 0:  # Makes sure where not trying to spawn something that isn't there
        for _ in range(len(rect_update_list)):
            new_rect = rect_update_list[update_step]

            # flag
            if new_rect[0] != "begin level" and new_rect[0] != "end level":
                pygame.draw.rect(win2, new_rect[0], new_rect[1])
            else:
                pygame.draw.rect(win2, new_rect[1], new_rect[2])

            # this IS important
            update_step += 1
            if update_step == len(rect_update_list):
                update_step = 0
                break
def update_list():
    global rect_update_list
    return rect_update_list
def collision(x, y):
    global collision_step, player_size2, block_size2, prev_pos, reset_position, player_x, player_y
    rect_list = update_list()
    for _ in range(len(rect_list)):  # loop over for collision
        new_rect = rect_list[collision_step]  # loops --> gets the rect pos and size
        if new_rect[0] != "begin level":
            if new_rect[0] != "end level":
                place_in_space = [new_rect[1][0], new_rect[1][1]]
                rect_size = new_rect[1][2], new_rect[1][3]
                if x + player_size2[0] >= place_in_space[0] and y + player_size2[1] >= place_in_space[1]:
                    if x <= place_in_space[0] + rect_size[0] and y <= place_in_space[1] + rect_size[1]:
                        return "collision", new_rect
            if new_rect[0] == "end level":
                end_levelPIS = [new_rect[2][0], new_rect[2][1]]
                end_levelRS = new_rect[2][2], new_rect[2][3]
                if x + player_size2[0] >= end_levelPIS[0] and y + player_size2[1] >= end_levelPIS[1]:
                    if x <= end_levelPIS[0] + end_levelRS[0] and y <= end_levelPIS[1] + end_levelRS[1]:
                        level_editor.load_next_level()
                        player_x, player_y = get_beginEnd_()[0][2][0], get_beginEnd_()[0][2][1]
        collision_step += 1
        if collision_step == len(rect_list):
            collision_step = 0
            break
def control_z():
    if not rect_update_list:
        print(" === Make something first! === ")
    if rect_update_list:
        last_num = len(rect_update_list)
        rect_update_list.remove(rect_update_list[last_num - 1])
def reset():
    global rect_update_list
    rect_update_list = []
def remove_begin():
    rect_update_list.remove(get_beginEnd_()[0])
def remove_end():
    rect_update_list.remove(get_beginEnd_()[1])
def find_specialInstance(check):
    begin_level = None
    end_level = None
    if check:
        for i in range(len(check)):
            locals()
            if check[i][0] == "begin level":
                begin_level = check[i]

            if check[i][0] == "end level":
                end_level = check[i]

        return begin_level, end_level
def getIndex(block):
    return rect_update_list.index(block)
def makefolder():  # folder name flag
    try:
        os.mkdir("levels")
        print("Made folder named \"levels\"")
        return
    except FileExistsError:
        return
def playerPos():
    return player_x, player_y