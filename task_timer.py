from nicegui import ui
from datetime import datetime

# Input
task_input = ui.input("Add Task")

# Labels
running_task = ui.label('')
elapsed_time = ui.label('')

# Create table ONCE
task_table = ui.table(
    columns=[
        {'label': 'Task', 'field': 'task'},
        {'label': 'Elapsed (s)', 'field': 'elapsed'},
    ],
    rows=[]
)

# Store
task_times = {}
current_task = None
start_time = None

# Timer updates elapsed label
def update_elapsed():
    if current_task and start_time:
        seconds = (datetime.now() - start_time).total_seconds()
        elapsed_time.set_text(f'{seconds:.0f} seconds')

ui.timer(1.0, update_elapsed)

# Start task
def start():
    global current_task, start_time

    task_name = task_input.value

    if not task_name:
        return

    # First time a task is started
    if task_name not in task_times:
        task_times[task_name] = 0

    current_task = task_name
    start_time = datetime.now()
    running_task.set_text(current_task)

    refresh_table()

# Stop task
def stop():
    global current_task, start_time

    if current_task is None:
        return

    elapsed = (datetime.now() - start_time).total_seconds()
    task_times[current_task] += elapsed

    current_task = None
    start_time = None
    elapsed_time.set_text('')

    refresh_table()

# Update the table in-place
def refresh_table():
    rows = [
        {'task': name, 'elapsed': f'{secs:.0f}'}
        for name, secs in task_times.items()
    ]
    task_table.rows = rows
    task_table.update()

# Buttons
ui.button("Start", on_click=start)
ui.button("Stop", on_click=stop)

ui.run()