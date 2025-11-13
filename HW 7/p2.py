from nicegui import ui
from random import shuffle

# TODO 1: Create list of 8 unique emojis, duplicate, and shuffle
EMOJIS = ['🌊', '🐳', '🪸', '🪼', '🦈', '🐡', '🐠', '🐊'] * 2  # Your task
shuffle(EMOJIS)

buttons = []
opened = []    # indices of currently flipped cards
matched = []   # indices of solved cards
busy = False    # for when user selects before cards are flipped

# initialize counters BEFORE functions
moves = 0
moves_label = None
match_label = None

# TODO 2: Write function to flip non-matching cards back
def reset_pair(i, j):
    global busy
    for k in (i, j):
        if k not in matched:
            buttons[k].text = '❓'
    opened.clear()
    busy = False

# TODO 3: Write click handler
def handle_click(idx):
    global busy, moves
    
    if busy:        # ignore clicks while in waiting period
        return
    if idx in matched or idx in opened:
        return
    
    # flip card and record it in opened
    buttons[idx].text = EMOJIS[idx]
    opened.append(idx)
    
    # if two cards are flipped, evaluate match
    if len(opened) == 2:
        # move counter
        moves += 1
        moves_label.text = f'Moves: {moves}'
        
        i, j = opened
        if EMOJIS[i] == EMOJIS[j]:  # check for match, update matched and clear opened
            matched.extend([i, j]) 
            match_label.text = f'Matches: {len(matched)//2} / 8'    # update match label
            opened.clear()
            
            if len(matched) == 16:
                ui.notify('You win!🎉')
        else:
            busy = True
            # hide cards after a time
            ui.timer(0.5, lambda i=i, j=j: reset_pair(i, j), once=True)

# Build 4x4 grid
with ui.grid(columns=4):
    # TODO 4: Create 16 buttons
    for i in range(16):
        b = ui.button('❓', on_click=lambda i=i: handle_click(i)
                      ).props('flat'
                        ).style('font-size: 50px; width: 120px; height: 120px; background-color: pink; color: blue !important;')   # create each button
        buttons.append(b)
    
# restart button- reload the page
ui.button('Restart', on_click=lambda: ui.navigate.reload()
          ).props('flat'
            ).style('font-size: 20px; background-color: pink; color: deeppink !important; padding: 5px 15px;')

# move counter label
moves = 0
moves_label = ui.label('Moves: ').style('font-size: 24px;')

# matches counter label
match_label = ui.label('Matches: 0 / 8').style('font-size: 24px;')

ui.run(title='Memory Game')