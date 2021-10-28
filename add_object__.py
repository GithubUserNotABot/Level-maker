import pygame

rect_update_list = []
update_step = 0
collision_step = 0
win2 = None
player_size2 = None
block_size2 = None
collision_flag = False
prev_pos = 0, 0

def coll_flagger():
    return collision_flag, prev_pos

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
    global rect_update_list, win2
    pygame.draw.rect(win2, color, (pos[0], pos[1], size[0], size[1]))
    if cntrl is None:
        rect_update_list.append([color, (pos[0], pos[1], block_size2[0], block_size2[1])])
    if cntrl is not None:
        if cntrl == "end level":
            rect_update_list.insert(1, [color, (pos[0], pos[1], block_size2[0], block_size2[1])])
        if cntrl == "begin level":
            rect_update_list.insert(0, [color, (pos[0], pos[1], block_size2[0], block_size2[1])])

def update__(x, y):
    global update_step, rect_update_list, win2, collision_flag

    collision_check = collision(x, y)
    if collision_check == "collision":
        collision_flag = True
    if collision_check != "collision":
        collision_flag = False

    if len(rect_update_list) > 0:  # Make sure where not trying to spawn something that isn't there

        for _ in range(len(rect_update_list)):
            new_rect = rect_update_list[update_step]  # loops to find the rect where looking for
            pygame.draw.rect(win2, new_rect[0], new_rect[1])
            update_step += 1
            if update_step == len(rect_update_list):
                update_step = 0
                break

def update_list():
    global rect_update_list
    return rect_update_list

def collision(x, y):
    global collision_step, win2, player_size2, block_size2, prev_pos
    rect_list = update_list()

    for _ in range(len(rect_list)):  # loop over like above except its for collision
        new_rect = rect_list[collision_step]  # loops --> gets the rect pos
        place_in_space = [new_rect[1][0], new_rect[1][1]]
        if x + player_size2[0] >= place_in_space[0] and y + player_size2[1] >= place_in_space[1]:
            if x <= place_in_space[0] + block_size2[0] and y <= place_in_space[1] + block_size2[1]:
                return "collision"

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

def make_beginning():
    pass

def make_end():
    make()