import random
import sys
import pygame

pygame.init()
stage = pygame.display.set_mode((600, 600))
pygame.display.set_caption("snake game")
pygame.display.update()
pygame.mixer.init()
pygame.mixer.music.load('Snake_Music.mp3')
pygame.mixer.music.play(-1)


def showsnake(game, color, l):
    for x2, y2 in l[0]:
        pygame.draw.rect(game, color, [x2, y2, l[1], l[1]])


font = pygame.font.SysFont(None, 30)


def display_text(text, color, x1, y1):
    t = font.render(text, True, color)
    stage.blit(t, [x1, y1])


def welcome():
    exit_game = False
    img = pygame.image.load("Home.jpg")
    img = pygame.transform.scale(img, (600, 600)).convert_alpha()
    stage.fill((255, 255, 255))
    stage.blit(img, (0, 0))
    pygame.display.update()
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    gameloopeasy()
                if event.key == pygame.K_2:
                    gameloopmedium()
                if event.key == pygame.K_3:
                    gameloophard()
                if event.key == pygame.K_4:
                    sys.exit()
                if event.key == pygame.K_5:
                    img1 = pygame.image.load("instruction.jpg")
                    img1 = pygame.transform.scale(img1, (600, 600)).convert_alpha()
                    stage.blit(img1, (0, 0))
                    pygame.display.update()
                if event.key == pygame.K_SPACE:
                    welcome()


def gameloopeasy():
    with open("highscoreeasy.txt", "r") as f:
        hiscore = int(f.read())
    exit_game = False
    game_over = False
    foodx = random.randint(50, 550)
    foody = random.randint(50, 550)
    score = 0
    x = 50
    y = 100
    size = 20
    direction = "r"
    time = pygame.time.Clock()
    snakelist = []
    snakelength = 1
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    welcome()
                if event.key == pygame.K_RIGHT:
                    if direction != "l":
                        direction = "r"
                if event.key == pygame.K_UP:
                    if direction != "d":
                        direction = "u"
                if event.key == pygame.K_DOWN:
                    if direction != "u":
                        direction = "d"
                if event.key == pygame.K_LEFT:
                    if direction != "r":
                        direction = "l"
        if x < 0 or x > 600:
            game_over = True
        if y < 30 or y > 600:
            game_over = True
        if direction == "r":
            x += 1.5
        if direction == "u":
            y -= 1.5
        if direction == "d":
            y += 1.5
        if direction == "l":
            x -= 1.5
        stage.fill((0, 0, 0))
        # stage.blit(img,(0,30))
        pygame.draw.rect(stage, (255, 192, 203), [0, 0, 600, 30])
        pygame.draw.rect(stage, (246, 213, 0), [foodx, foody, size, size])
        if abs(foodx - x) < 10 and abs(foody - y) < 10:
            foodx = random.randint(50, 550)
            foody = random.randint(50, 450)
            score += 1
            snakelength += 20
            if score > hiscore:
                hiscore = score
        display_text("Score: " + str(score), (0, 0, 0), 500, 10)
        display_text("Highscore: " + str(hiscore), (0, 0, 0), 10, 10)
        if game_over:
            stage.fill((255, 255, 255))
            img1 = pygame.image.load("GAMEOVER.jpg")
            img1 = pygame.transform.scale(img1, (600, 600)).convert_alpha()
            stage.blit(img1, (0, 0))
            pygame.draw.rect(stage, (255, 192, 203), [0, 0, 600, 30])
            display_text("Score: " + str(score), (0, 0, 0), 500, 10)
            display_text("Highscore: " + str(hiscore), (0, 0, 0), 10, 10)
            with open("highscoreeasy.txt", "w") as f:
                f.write(str(hiscore))
            snakelist = []
        # pygame.draw.rect(stage,(5,144,0),[x,y,size,size])
        if not game_over:
            snakelist.append([x, y])
        if [x, y] in snakelist[:-1]:
            game_over = True
        if len(snakelist) > snakelength:
            snakelist.pop(0)
        showsnake(stage, (5, 144, 0,), [snakelist, size])
        pygame.display.update()
        time.tick(60)
    pygame.quit()
    sys.exit()


def gameloopmedium():
    with open("highscoremedium.txt", "r") as f:
        hiscore = int(f.read())
    exit_game = False
    game_over = False
    foodx = random.randint(50, 550)
    foody = random.randint(50, 550)
    score = 0
    x = 50
    y = 100
    size = 20
    direction = "r"
    time = pygame.time.Clock()
    snakelist = []
    snakelength = 1
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    welcome()
                if event.key == pygame.K_RIGHT:
                    if direction != "l":
                        direction = "r"
                if event.key == pygame.K_UP:
                    if direction != "d":
                        direction = "u"
                if event.key == pygame.K_DOWN:
                    if direction != "u":
                        direction = "d"
                if event.key == pygame.K_LEFT:
                    if direction != "r":
                        direction = "l"
        if x < 0 or x > 600:
            game_over = True
        if y < 30 or y > 600:
            game_over = True
        if direction == "r":
            x += 2.5
        if direction == "u":
            y -= 2.5
        if direction == "d":
            y += 2.5
        if direction == "l":
            x -= 2.5
        stage.fill((0, 0, 0))
        pygame.draw.rect(stage, (255, 192, 203), [0, 0, 600, 30])
        pygame.draw.rect(stage, (246, 213, 0), [foodx, foody, size, size])
        if abs(foodx - x) < 10 and abs(foody - y) < 10:
            foodx = random.randint(50, 550)
            foody = random.randint(50, 450)
            score += 1
            snakelength += 20
            if score > hiscore:
                hiscore = score
        display_text("Score: " + str(score), (0, 0, 0), 500, 10)
        display_text("Highscore: " + str(hiscore), (0, 0, 0), 10, 10)
        if game_over:
            stage.fill((255, 255, 255))
            img1 = pygame.image.load("GAMEOVER.jpg")
            img1 = pygame.transform.scale(img1, (600, 600)).convert_alpha()
            stage.blit(img1, (0, 0))
            pygame.draw.rect(stage, (255, 192, 203), [0, 0, 600, 30])
            display_text("Score: " + str(score), (0, 0, 0), 500, 10)
            display_text("Highscore: " + str(hiscore), (0, 0, 0), 10, 10)
            with open("highscoremedium.txt", "w") as f:
                f.write(str(hiscore))
            snakelist = []
        if not game_over:
            snakelist.append([x, y])
        if [x, y] in snakelist[:-1]:
            game_over = True
        if len(snakelist) > snakelength:
            snakelist.pop(0)
        showsnake(stage, (5, 144, 0,), [snakelist, size])
        pygame.display.update()
        time.tick(60)
    pygame.quit()
    sys.exit()


def gameloophard():
    with open("highscorehard.txt", "r") as f:
        hiscore = int(f.read())
    exit_game = False
    game_over = False
    foodx = random.randint(50, 550)
    foody = random.randint(50, 550)
    score = 0
    x = 50
    y = 100
    size = 20
    direction = "r"
    time = pygame.time.Clock()
    snakelist = []
    snakelength = 1
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    welcome()
                if event.key == pygame.K_RIGHT:
                    if direction != "l":
                        direction = "r"
                if event.key == pygame.K_UP:
                    if direction != "d":
                        direction = "u"
                if event.key == pygame.K_DOWN:
                    if direction != "u":
                        direction = "d"
                if event.key == pygame.K_LEFT:
                    if direction != "r":
                        direction = "l"
        if x < 0 or x > 600:
            game_over = True
        if y < 30 or y > 600:
            game_over = True
        if direction == "r":
            x += 5
        if direction == "u":
            y -= 5
        if direction == "d":
            y += 5
        if direction == "l":
            x -= 5
        stage.fill((0, 0, 0))
        pygame.draw.rect(stage, (255, 192, 203), [0, 0, 600, 30])
        pygame.draw.rect(stage, (246, 213, 0), [foodx, foody, size, size])
        if abs(foodx - x) < 10 and abs(foody - y) < 10:
            foodx = random.randint(50, 550)
            foody = random.randint(50, 450)
            score += 1
            snakelength += 20
            if score > hiscore:
                hiscore = score
        display_text("Score: " + str(score), (0, 0, 0), 500, 10)
        display_text("Highscore: " + str(hiscore), (0, 0, 0), 10, 10)
        if game_over:
            stage.fill((255, 255, 255))
            img1 = pygame.image.load("GAMEOVER.jpg")
            img1 = pygame.transform.scale(img1, (600, 600)).convert_alpha()
            stage.blit(img1, (0, 0))
            pygame.draw.rect(stage, (255, 192, 203), [0, 0, 600, 30])
            display_text("Score: " + str(score), (0, 0, 0), 500, 10)
            display_text("Highscore: " + str(hiscore), (0, 0, 0), 10, 10)
            with open("highscorehard.txt", "w") as f:
                f.write(str(hiscore))
            snakelist = []
        # pygame.draw.rect(stage,(5,144,0),[x,y,size,size])
        if not game_over:
            snakelist.append([x, y])
        if [x, y] in snakelist[:-1]:
            game_over = True
        if len(snakelist) > snakelength:
            snakelist.pop(0)
        showsnake(stage, (5, 144, 0,), [snakelist, size])
        pygame.display.update()
        time.tick(60)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    welcome()
