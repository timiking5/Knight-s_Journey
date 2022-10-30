import pygame





def solution(n, m, x0, y0):
    cells_total = n * m
    # Ð˜Ð½Ð¸Ñ†Ð¸Ð°Ð»Ð¸Ð·Ð°Ñ†Ð¸Ñ Ð´Ð¾ÑÐºÐ¸.
    board = [[-1] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    # Ð¡Ð¿Ð¸ÑÐ¾Ðº Ð´Ð¾Ð¿ÑƒÑÑ‚Ð¸Ð¼Ñ‹Ñ… Ñ…Ð¾Ð´Ð¾Ð² ÐºÐ¾Ð½Ñ.
    moves = [(1, 2), (-1, -2),
             (2, 1), (-2, -1),
             (-1, 2), (1, -2),
             (-2, 1), (2, -1)]


    def check_bounds(x, y):
        """
        Ð¤ÑƒÐ½ÐºÑ†Ð¸Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ¸ ÐºÐ¾Ð¾Ñ€Ð´Ð¸Ð½Ð°Ñ‚
        Ð½Ð° ÑÐ¾Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²Ð¸Ðµ Ð³Ñ€Ð°Ð½Ð¸Ñ†Ð°Ð¼ Ð´Ð¾ÑÐºÐ¸.
        """
        return -1 < x < n and -1 < y < m


    def is_visited(x, y):
        """
        Ð¤ÑƒÐ½ÐºÑ†Ð¸Ñ Ð¿Ñ€Ð¾Ð²ÐµÑ€ÐºÐ¸ ÑÐ¾ÑÑ‚Ð¾ÑÐ½Ð¸Ñ ÐºÐ»ÐµÑ‚ÐºÐ¸
        (Ð¿Ð¾ÑÐµÑ‰ÐµÐ½Ð° ÐºÐ»ÐµÑ‚ÐºÐ° Ð¸Ð»Ð¸ ÐµÑ‰Ðµ Ð½ÐµÑ‚).
        """
        return visited[x][y]


    def get_move_list(x, y):
        """
        Ð¤ÑƒÐ½ÐºÑ†Ð¸Ñ, Ð²Ð¾Ð·Ð²Ñ€Ð°Ñ‰Ð°ÑŽÑ‰Ð°Ñ ÑÐ¿Ð¸ÑÐ¾Ðº
        Ð½ÐµÐ¿Ð¾ÑÐµÑ‰Ñ‘Ð½Ð½Ñ‹Ñ… ÐºÐ»ÐµÑ‚Ð¾Ðº Ð´Ð¾ÑÐºÐ¸,
        Ð½Ð° ÐºÐ¾Ñ‚Ð¾Ñ€Ñ‹Ðµ ÐºÐ¾Ð½ÑŒ Ð¼Ð¾Ð¶ÐµÑ‚ Ð¿Ð¾Ð¹Ñ‚Ð¸
        Ñ Ð´Ð°Ð½Ð½Ð¾Ð¹ Ð¿Ð¾Ð·Ð¸Ñ†Ð¸Ð¸.
        """
        available_moves = []
        for dx, dy in moves:
            xnew, ynew = x + dx, y + dy
            if check_bounds(xnew, ynew):
                if not is_visited(xnew, ynew):
                    available_moves.append((xnew, ynew))
        return available_moves


    def tour(x, y, move_number):
        """
        Ð ÐµÐºÑƒÑ€ÑÐ¸Ð²Ð½Ð°Ñ Ñ„ÑƒÐ½ÐºÑ†Ð¸Ñ Ñ€ÐµÑˆÐµÐ½Ð¸Ñ
        Ð·Ð°Ð´Ð°Ñ‡Ð¸ Ð¾ Ð¿ÑƒÑ‚Ð¸ ÐºÐ¾Ð½Ñ Ð¿Ð¾ Ð´Ð¾ÑÐºÐµ.
        Ð’Ð¾Ð·Ð²Ñ€Ð°Ñ‰Ð°ÐµÑ‚ True, ÐµÑÐ»Ð¸ Ð¿ÑƒÑ‚ÑŒ
        Ð½Ð°Ð¹Ð´ÐµÐ½, Ð¸ False Ð¸Ð½Ð°Ñ‡Ðµ.
        """
        # ÐžÑ‚Ð¼ÐµÑ‡Ð°ÐµÐ¼ Ñ‚ÐµÐºÑƒÑ‰ÑƒÑŽ ÐºÐ»ÐµÑ‚ÐºÑƒ
        # ÐºÐ°Ðº Ð¿Ð¾ÑÐµÑ‰ÐµÐ½Ð½ÑƒÑŽ.
        visited[x][y] = True
        # Ð•ÑÐ»Ð¸ Ð¾Ñ‚Ð¼ÐµÑ‡Ð°ÐµÐ¼Ñ‹Ð¹ Ð½Ð¾Ð¼ÐµÑ€ ÑÐ¾Ð¾Ñ‚Ð²ÐµÑ‚ÑÑ‚Ð²ÑƒÐµÑ‚
        # ÑÑƒÐ¼Ð¼Ð°Ñ€Ð½Ð¾Ð¼Ñƒ ÐºÐ¾Ð»Ð¸Ñ‡ÐµÑÑ‚Ð²Ñƒ ÐºÐ»ÐµÑ‚Ð¾Ðº Ð´Ð¾ÑÐºÐ¸,
        # Ñ‚Ð¾ Ð²Ð¾Ð·Ð²Ñ€Ð°Ñ‰Ð°ÐµÐ¼ True (Ð½Ð°ÑˆÐ»Ð¸ Ñ€ÐµÑˆÐµÐ½Ð¸Ðµ).
        answer = False
        if move_number == cells_total - 1:
            board[x][y] = move_number;
            answer = True
        else:
            move_list = get_move_list(x, y)
            if len(move_list) != 0:
                # ÐŸÐ¾Ð»ÑƒÑ‡ÐµÐ½Ð¸Ðµ ÐºÐ¾Ð»Ð¸Ñ‡ÐµÑÑ‚Ð²Ð° Ð¿Ð¾Ð»ÐµÐ¹,
                # ÐºÐ¾Ñ‚Ð¾Ñ€Ñ‹Ðµ Ð´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹Ñ… Ñ Ð¿Ð¾Ð»ÐµÐ¹
                # Ð¸Ð· Ñ‚ÐµÐºÑƒÑ‰ÐµÐ³Ð¾ ÑÐ¿Ð¸ÑÐºÐ°.
                neighbors = [ \
                    (len(get_move_list(xnew, ynew)), (xnew, ynew)) \
                     for xnew, ynew in move_list]
                # ÐžÐ¿Ñ€ÐµÐ´ÐµÐ»ÐµÐ½Ð¸Ðµ Ð¼Ð¸Ð½Ð¸Ð¼Ð°Ð»ÑŒÐ½Ð¾Ð³Ð¾
                # ÐºÐ¾Ð»Ð¸Ñ‡ÐµÑÑ‚Ð²Ð° Ð¿Ð¾Ð»ÐµÐ¹, Ð´Ð¾ÑÑ‚ÑƒÐ¿Ð½Ñ‹Ñ…
                # Ñ ÐºÐ»ÐµÑ‚Ð¾Ðº Ð¸Ð· ÑÐ¿Ð¸ÑÐºÐ°.
                neighbors_min = min([pair[0] for pair in neighbors])
                # ÐžÑ‚Ð±Ð¾Ñ€ Ñ‚ÐµÑ… Ð¿Ð¾Ð»ÐµÐ¹ Ð¸Ð· ÑÐ¿Ð¸ÑÐºÐ°,
                # Ñ ÐºÐ¾Ñ‚Ð¾Ñ€Ñ‹Ñ… Ð¼Ð¾Ð¶Ð½Ð¾ Ð¿Ð¾Ð¹Ñ‚Ð¸ Ð½Ð°
                # Ð¼Ð¸Ð½Ð¸Ð¼Ð°Ð»ÑŒÐ½Ð¾Ðµ Ñ‡Ð¸ÑÐ»Ð¾ ÐµÑ‰Ñ‘ Ð½Ðµ
                # Ð¿Ñ€Ð¾Ð¹Ð´ÐµÐ½Ð½Ñ‹Ñ… Ð¿Ð¾Ð»ÐµÐ¹.
                canditates = [pair[1] for pair in neighbors \
                              if pair[0] == neighbors_min]
                # Ð ÐµÐºÑƒÑ€ÑÐ¸Ð²Ð½Ð¾ Ð²Ñ‹Ð·Ñ‹Ð²Ð°ÐµÐ¼ Ñ„ÑƒÐ½ÐºÑ†Ð¸ÑŽ
                # Ð´Ð»Ñ ÐºÐ°Ð¶Ð´Ð¾Ð³Ð¾ Ð¸Ð· Ð¿Ð¾Ð»ÐµÐ¹-ÐºÐ°Ð½Ð´Ð¸Ð´Ð°Ñ‚Ð¾Ð²,
                # Ð¿Ð¾ÐºÐ° Ð½Ðµ Ñ€ÐµÑˆÐ¸Ð¼ Ð·Ð°Ð´Ð°Ñ‡Ñƒ Ð¸Ð»Ð¸ Ð½Ðµ
                # Ð¿ÐµÑ€ÐµÐ±ÐµÑ€ÐµÐ¼ Ð²ÑÐµÑ… ÐºÐ°Ð½Ð´Ð¸Ð´Ð°Ñ‚Ð¾Ð².
                for xnew, ynew in canditates:
                    if tour(xnew, ynew, move_number + 1):
                        board[x][y] = move_number;
                        answer = True
                        break
        visited[x][y] = False
        return answer


    if tour(x0, y0, 0):
        return board
    else:
        print("ÐÐµÑ‚ Ñ€ÐµÑˆÐµÐ½Ð¸Ñ.")










n = int(input())
x, y = map(int, input().split())
free_mode = False
sol_running = False
green_pool = []
back_stack = -1

screen = pygame.display.set_mode((n * 50, n * 50))
pygame.display.set_caption("Chess")

run = True
while run:
    pygame.time.delay(30)
    
    if free_mode == False and sol_running == False:
        command = input()
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
                
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_UP]:
        y -= 0.2
    if keys[pygame.K_DOWN]:
        y += 0.2
    if keys[pygame.K_LEFT]:
        x -= 0.2
    if keys[pygame.K_RIGHT]:
        x += 0.2
    
    if keys[pygame.K_c]:
        green_pool = []
        
    if keys[pygame.K_s]:
        x, y = map(int, input().split())
        
    if keys[pygame.K_SPACE] or command == 'mode':
        free_mode = not free_mode
    
    if free_mode == False:
        if command == 'solution':
            sol_board = solution(n, n, x, y)
            sol_running = True
            command = 'continue'
            back_stack = 1
        elif command == 'continue':
            for finder1 in range(n):
                for finder2 in range(n):
                    if sol_board[finder1][finder2] == back_stack:
                        green_pool.append([y,x])
                        x, y = finder2,finder1
                        back_stack += 1
                        #pygame.time.delay(700)
            if back_stack == n ** 2:
                sol_running = False
        
        elif command[0] == 'f':
            green_pool.append([y,x])
            if command[1] == 'U':
                y -= 2
            elif command[1] == 'D':
                y += 2
            elif command[1] == 'L':
                x -= 2
            elif command[1] == 'R':
                x += 2
                    
            if command[2] == 'U':
                y -= 1
            elif command[2] == 'D':
                y += 1
            elif command[2] == 'L':
                x -= 1
            elif command[2] == 'R':
                x += 1
        elif len(command.split()) == 2:
            x = int(command.split()[1])
            y = int(command.split()[0])
        elif command == 'clear':
            green_pool = []
        
        
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > n-1:
        x = n - 1
    if y > n-1:
        y = n - 1
    
    screen.fill((0,0,0))
    
    for i1 in range(n):
        for i2 in range(int(i1 % 2 == 0),n,2):
            pygame.draw.rect(screen, (255,255,255), (i1 * 50, i2 * 50,50,50))
            
    for green in green_pool:
        pygame.draw.rect(screen, (0,255,127), (green[1] * 50, green[0] * 50,50,50))
    
    pygame.draw.rect(screen, (255,127,80), (x * 50, y * 50,50,50))
    
    pygame.display.update()
    
    if sol_running == False:
        command = '   '