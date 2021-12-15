import pygame
import add_object__
import level_editor

win = pygame.display.set_mode((1000, 900))
A_ = add_object__

player_x, player_y = 0, 0
key = [None, None, None, None]
break_key = [False, False, False, False]
force = 5
block_size = 100, 100
player_size = 50, 65

left_click = False
left_click_xy_first = None
left_click_xy_second = None

to_draw = []

# == colors ==
begin_block = None

clock = pygame.time.Clock()
# === Main Loop ===

A_.get_win(win)
A_.get_size(player_size, block_size)

while True:
    # == FPS ==
    clock.tick(60)

    # == For Loop ==
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

        # == Get key press ==
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                break_key[0] = False
                key[0] = 'd'
            if event.key == pygame.K_a:
                break_key[1] = False
                key[1] = 'a'
            if event.key == pygame.K_s:
                break_key[2] = False
                key[2] = 's'
            if event.key == pygame.K_w:
                break_key[3] = False
                key[3] = 'w'

            # == Escape key ==
            if event.key == pygame.K_ESCAPE:
                print(" ==== Shutting down... ====")
                raise SystemExit
            # == Control Z ==
            if event.key == pygame.K_LCTRL:
                add_object__.control_z()
            # == Save the level ==
            if event.key == pygame.K_3:
                level_editor.save_level()
            # == Load some Level ==
            if event.key == pygame.K_4:
                level_editor.load_level()
            # == Manage Levels ==
            if event.key == pygame.K_5:
                level_editor.merge_levels()
            # == Create blank level files
            if event.key == pygame.K_6:
                level_editor.create_levels()
            # == Delete level files ==
            if event.key == pygame.K_7:
                level_editor.delete_levels()
            # == Level Begin ==
            if event.key == pygame.K_1:
                level_editor.begin_level()
            # == Level End ==
            if event.key == pygame.K_2:
                level_editor.end_level()
        # === Key Button Up ===
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                break_key[0] = True
                key[0] = None
            if event.key == pygame.K_a:
                break_key[1] = True
                key[1] = None
            if event.key == pygame.K_s:
                break_key[2] = True
                key[2] = None
            if event.key == pygame.K_w:
                break_key[3] = True
                key[3] = None
        # == Get mouse press ==
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                left_click = True
                left_click_xy_first = pygame.mouse.get_pos()
            if event.button == 3:
                player_x, player_y = pygame.mouse.get_pos()
        # == Get mouse up press ==
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_click = False
                left_click_xy_second = pygame.mouse.get_pos()
                to_draw.append((left_click_xy_first, left_click_xy_second))

    # == Left click ==
    if left_click:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(win, (255, 0, 255), (left_click_xy_first[0], left_click_xy_first[1]), (mouse_pos[0], left_click_xy_first[1]))
        pygame.draw.line(win, (255, 0, 255), (left_click_xy_first[0], left_click_xy_first[1]), (left_click_xy_first[0], mouse_pos[1]))
        pygame.draw.line(win, (255, 0, 255), (mouse_pos[0], mouse_pos[1]), (left_click_xy_first[0], mouse_pos[1]))
        pygame.draw.line(win, (255, 0, 255), (mouse_pos[0], mouse_pos[1]), (mouse_pos[0], left_click_xy_first[1]))

    # == For making the blocks custom size ==
    if not left_click:
        if to_draw:

            if left_click_xy_second[0] >= left_click_xy_first[0] and left_click_xy_second[1] >= left_click_xy_first[1]:  # bottom right
                block_size = to_draw[0][0][0] - to_draw[0][1][0], to_draw[0][0][1] - to_draw[0][1][1]
                add_object__.make((0, 255, 255), (to_draw[0][0][0], to_draw[0][0][1]), (abs(block_size[0]), abs(block_size[1])))
            if left_click_xy_second[0] <= left_click_xy_first[0] and left_click_xy_second[1] <= left_click_xy_first[1]:  # top left
                block_size = to_draw[0][0][0] - to_draw[0][1][0], to_draw[0][0][1] - to_draw[0][1][1]
                add_object__.make((0, 255, 255), (to_draw[0][1][0], to_draw[0][1][1]), (block_size[0], block_size[1]))
            if left_click_xy_second[0] >= left_click_xy_first[0] and left_click_xy_second[1] <= left_click_xy_first[1]:  # top right
                block_size = to_draw[0][1][0] - to_draw[0][0][0], to_draw[0][1][1] - to_draw[0][0][1]
                add_object__.make((0, 255, 255), (to_draw[0][1][0] - block_size[0], to_draw[0][1][1]), (abs(block_size[0]), abs(block_size[1])))
            if left_click_xy_second[0] <= left_click_xy_first[0] and left_click_xy_second[1] >= left_click_xy_first[1]:  # bottom left
                block_size = to_draw[0][1][0] - to_draw[0][0][0], to_draw[0][1][1] - to_draw[0][0][1]
                add_object__.make((0, 255, 255), (to_draw[0][1][0], to_draw[0][1][1] - block_size[1]), (abs(block_size[0]), abs(block_size[1])))
            to_draw.clear()

    # == Movement ==
    if key[0] == 'd':
        if not break_key[0]:
            player_x += force
    if key[1] == 'a':
        if not break_key[1]:
            player_x -= force
    if key[2] == 's':
        if not break_key[2]:
            player_y += force
    if key[3] == 'w':
        if not break_key[3]:
            player_y -= force

    # === Collision system ===
    coll_flag = A_.coll_flagger()
    if coll_flag[0]:
        player_x, player_y = A_.get_reset_pos()

    # ==== Working on it ====
    pygame.draw.rect(win, (255, 50, 200), (player_x, player_y, player_size[0], player_size[1]))

    A_.update__(player_x, player_y)
    pygame.display.update()
    win.fill((0, 0, 0))
