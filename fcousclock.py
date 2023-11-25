import tkinter as tk
import time

def start_timer():
    global timer_running
    if not timer_running:
        update_timer()
        timer_running = True

def update_timer():
    global remaining_time
    if remaining_time > 0:
        mins, secs = divmod(remaining_time, 60)
        time_label.config(text=f"{mins:02d}:{secs:02d}")
        remaining_time -= 1
        window.after(1000, update_timer)
    else:
        time_label.config(text="00:00")
        timer_running = False
        # 可以在这里加入声音提醒或弹窗

def reset_timer():
    global remaining_time, timer_running
    remaining_time = 25 * 60  # 重置为25分钟
    timer_running = False
    time_label.config(text="25:00")

def pause_timer():
    global timer_running
    timer_running = False

# 初始化变量
remaining_time = 25 * 60  # 25分钟
timer_running = False

# 设置界面
window = tk.Tk()
window.title("专注时钟")

time_label = tk.Label(window, text="25:00", font=("Arial", 50))
time_label.pack()

start_button = tk.Button(window, text="开始", command=start_timer)
start_button.pack()

pause_button = tk.Button(window, text="暂停", command=pause_timer)
pause_button.pack()

reset_button = tk.Button(window, text="重置", command=reset_timer)
reset_button.pack()

window.mainloop()
