# Assignment: Mini-project 3; Stopwatch: The Game
# Author: Andrew Ludwar
# Due date: May 11, 2013; 11:00 PM MST
# Date: May 9, 2013

import simplegui

# define global variables
timer = 0
interval = 100
time = 0
success_counter = 0
stop_counter = 0
count_display = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = 0
    ones = 0
    tens = 0
    hundreds = 0
    
    hundreds = int(t / 600)
    tens = int(t / 10 % 60 // 10)
    ones = int(t / 10 % 60 % 10)
    tenths = t % 10
        
    formatted_time = str(hundreds) + ":" + str(tens) + str(ones) + "." + str(tenths)
    
    return formatted_time
    

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global time, stop_counter, success_counter, count_display
    
    tenths = time % 10
        
    if tenths == 0 and timer.is_running():
        success_counter = success_counter + 1
        stop_counter = stop_counter + 1
    elif timer.is_running():
        stop_counter = stop_counter + 1
        
    count_display = str(success_counter) + "/" + str(stop_counter)
    
    timer.stop()
    
def reset():
    global time, stop_counter, success_counter, count_display
    timer.stop()
    time = 0
    success_counter = 0
    stop_counter = 0

    count_display = str(success_counter) + "/" + str(stop_counter)

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    tenths_of_seconds = 1
    time = time + tenths_of_seconds
    return int(time)


# define draw handler
def draw(canvas):
    global time
    canvas.draw_text(str(format(time)), (65,95), 24, "White")
    canvas.draw_text(str(count_display), (140,25), 24, "Green")
    

# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 150)


# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(interval, tick)


# start frame
frame.start()
