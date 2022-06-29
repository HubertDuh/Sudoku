import pygame
import requests
import copy

# We initialize what will be the characteristics of the window that pops up when we start the game
import solver

WIDTH = 550
background_colour = (255, 255, 255)
original_grid_element_colour = (0, 0, 0)
buffer = 5

difficulty = ""
# The API gives us 3 level of difficulty, so we should ask what the user wants
while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
    difficulty = input("Please type a difficulty between: easy, medium and hard: ")

# Here, we set up the API
URL = f"https://sugoku.herokuapp.com/board?difficulty={difficulty}"
response = requests.get(URL)
grid = response.json()['board']
grid_original = copy.deepcopy(grid)
solved_grid = solver.solve(grid)

def insert(window, position):
    i, j = position[1], position[0]
    my_font = pygame.font.SysFont("Times New Roman", 35)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                print(event.key)

                if (grid_original[i - 1][j - 1] != 0):
                    return
                if (event.key == 8):  # checking with backspace key
                    grid[i - 1][j - 1] = event.key - 8
                    pygame.draw.rect(window, background_colour, (
                        position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    pygame.display.update()
                    return
                if (0 < event.key - 48 < 10):  # We are checking for valid input
                    pygame.draw.rect(window, background_colour, (
                        position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    value = my_font.render(str(event.key - 48), True, (70, 101, 228))
                    window.blit(value, (position[0] * 50 + 16.5, position[1] * 50 + 6.5))
                    grid[i - 1][j - 1] = event.key - 48
                    pygame.display.update()
                    return
                return


def main():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption(f"Sudoku-{difficulty}")
    window.fill(background_colour)
    my_font = pygame.font.SysFont("Times New Roman", 35)

    for i in range(0, 10):
        # vertical
        pygame.draw.line(window, (135, 135, 135), (50 + 50 * i, 53), (50 + 50 * i, 500), 1)
        # horizontal
        pygame.draw.line(window, (135, 135, 135), (53, 50 + 50 * i), (500, 50 + 50 * i), 1)

    # Redoing the for loop so that the border lines are above the interior lines
    for i in range(0, 10):
        if i % 3 == 0:
            # vertical edge
            pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 49), (50 + 50 * i, 502), 4)
            # horizontal edge
            pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

    pygame.display.update()

    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if (0 < grid[i][j] < 10):
                value = my_font.render(str(grid[i][j]), True, original_grid_element_colour)
                window.blit(value, ((j + 1) * 50 + 17, (i + 1) * 50 + 6.5))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()
                print(position)
                insert(window, (position[0] // 50, position[1] // 50))
            if event.type == pygame.QUIT:
                pygame.quit()
                return


main()
