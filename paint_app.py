from nicegui import ui

with ui.row():
    ui.label('Brush Color:')
    color_picker = ui.color_picker()
    
with ui.row():
    ui.label('Brush Size:')
    brush_slider = ui.slider(min=1, max=20, value=5)
    
ui.button('Clear', on_click=lambda: canvas.clear())
canvas = ui.interactive_canvas(width=600, height=400).classes('border')

ui.run()