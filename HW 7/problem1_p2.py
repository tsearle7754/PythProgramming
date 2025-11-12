from nicegui import ui

def TwistHash(text):
    h = 0x9E3779B1
    mult = 0x517CC1C7
    mask = 0xFFFFFFFF
    
    
    for c in text:
        # char code, XOR, multiplier, & mask
        char_code = ord(c)
        h = h ^ char_code
        h = (h * mult) & mask
    
    # final mix with length
    h = h ^ len(text)
    return h

# wrap with card for styling
with ui.card().style('width: 850px; height: 550px; background-color: pink; padding: 160px;'):
    ui.label('Simple Pink Hasher').style('color: hotpink; font-size: 30px; font-weight: bold;')
    # input box
    text_input = ui.input('Enter text:').props('label-color="blue"').style('color: aqua !important; font-size: 16px; font-weight: bold;')
    
    # label to display results
    result_label = ui.label('').style('font-size: 20px; color: hotpink; font-weight: bold;')  # initially empty; updated by get_hash when button is clicked
    
    # define what happens when button is clicked
    def get_hash():
        text = text_input.value     # read user input
        hashed = TwistHash(text)    # run algorithm
        result_label.text = f"Hash value: {hashed}"     # update label
    
    # create button that triggers get_hash()
    ui.button('Get Hash', on_click=get_hash).props('flat').style('background-color: hotpink; color: royalblue !important; font-size: 18px;')
    
    # create button to copy hash to clipboard using javascript
    def copy_hash():
        ui.run_javascript(f'navigator.clipboard.writeText("{result_label.text}")')
        ui.notify('Copied to clipboard!', color='pink')

    # create the button just once
    copy_button = ui.button('Copy', on_click=copy_hash).props('flat').style('background-color: hotpink; color: royalblue !important; font-weight: bold;')
    
# add dark mode
dark_mode = ui.dark_mode()

with ui.row().style('position: absolute; top: 10px; right: 10px;'):
    ui.button('Dark Mode', on_click=dark_mode.toggle).props('flat').style('background-color: pink; color: hotpink !important; font-weight: bold;')

ui.run()