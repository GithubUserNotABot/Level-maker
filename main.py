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

            # == Control Z ==
            if event.key == pygame.K_LCTRL:
                add_object__.control_z()

            # == Save the level ==
            if event.key == pygame.K_q:
                level_editor.save_level()
            # == Load some Level ==
            if event.key == pygame.K_e:
                level_editor.load_level()
            # == Level Begin ==
            if event.key == pygame.K_z:
                level_editor.begin_level(pygame.mouse.get_pos())
            # == Level End ==
            if event.key == pygame.K_x:
                level_editor.end_level(pygame.mouse.get_pos())
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
                # TODO: Left click and drag to make a block
                left_click = True
                A_.make(color=(0, 255, 255), pos=pygame.mouse.get_pos(), size=block_size)
            if event.button == 3:
                player_x, player_y = pygame.mouse.get_pos()
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
    coll_flag = A_.coll_flagger()  # gets the return
    if coll_flag[0]:  # interprets it
        player_x, player_y = 0, 0  # uses the data!!

    # ==== Working on it ====
    pygame.draw.rect(win, (255, 50, 200), (player_x, player_y, player_size[0], player_size[1]))

    A_.update__(player_x, player_y)
    pygame.display.update()
    win.fill((0, 0, 0))
