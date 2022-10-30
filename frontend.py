import pygame

n = int(input())
x, y = map(int, input().split())
free_mode = False
green_pool = []

screen = pygame.display.set_mode((n * 50, n * 50))
pygame.display.set_caption("Chess")

run = True
while run:
    pygame.time.delay(30)

    if free_mode == False:
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
        if command[0] == 'f':
            green_pool.append([y, x])
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
    if x > n - 1:
        x = n - 1
    if y > n - 1:
        y = n - 1

    screen.fill((0, 0, 0))

    for i1 in range(n):
        for i2 in range(int(i1 % 2 == 0), n, 2):
            pygame.draw.rect(screen, (255, 255, 255), (i1 * 50, i2 * 50, 50, 50))

    for green in green_pool:
        pygame.draw.rect(screen, (0, 255, 127), (green[1] * 50, green[0] * 50, 50, 50))

    pygame.draw.rect(screen, (255, 127, 80), (x * 50, y * 50, 50, 50))

    pygame.display.update()

    command = '   '
