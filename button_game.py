from nicegui import ui
from datetime import datetime
import random

# Random
x = random.randint(50, 500)
y = random.randint(50, 300)

# Labels
time = ui.label('')
score = ui.label('')
final_label = ui.label('')

points = 0
game_running = False
time_left = 30

def button():
    global points, game_running
    
    if not game_running:
        return
    
    points += 1
    score.set_text(f'Score: {points}')
    move_button()
    
    
def update_function():
    global game_running, time_left
    
    if not game_running:
        return
    
    time_left -= 1
    time.set_text(f"Time: {time_left}")
    
    if time_left <= 0:
        end_game()
    
def end_game():
    global points, game_running
    game_running = False
    catch_button.style('display: none;')
    final_label.set_text(f"Game Over! Final Score: {points}")
    
def reset():
    global points, time_left, game_running

    # 1. reset variables
    points = 0
    time_left = 30
    game_running = True

    # 2. reset labels
    score.set_text("Score: 0")
    time.set_text("Time: 30")
    final_label.set_text('')

    # 3. show the button again
    catch_button.style('display: block;')

    # 4. move button to random position
    move_button()


def move_button():
    x = random.randint(50, 600)
    y = random.randint(100, 400)
    
    catch_button.style(f'position: absolute; left: {x}px; top: {y}px;')
    
# Buttons
catch_button = ui.button("Catch Me!", on_click=button).style(f'position: absolute; left: {x}px; top: {y}px;')
reset_button = ui.button("Start Game", on_click=reset)

# Timer
timer = ui.timer(1.0, update_function)

ui.run()