from tkinter import *
import random
import time

# Changeable Variables
# values not fixed
time_for_small_vehicles = 2
time_for_medium_vehicles = 5
time_for_large_vehicles = 10
max_small_vehicles = 15
max_medium_vehicles = 10
max_large_vehicles = 5
time_for_yellow = 4
signal = {1: ["grey", "grey", "red"], 2: ["grey", "grey", "red"], 3: ["grey", "grey", "red"],
          4: ["grey", "grey", "red"]}


# Changes Sequence for emergency road
def Emergency_Signal(Sequenced_time_list, timelist, emergency):
    for i in range(1, 5):
        if emergency[i]:
            Sequenced_time_list.remove((i, timelist[i]))
            Sequenced_time_list.insert(0, (i, timelist[i]))

# changes signals
def Smart_traffic_system(Sequenced_time_list, emergency, speed, text_part):
    for i in range(4):
        a = Sequenced_time_list[i][0]  # a = ith priroty road number
        print("Traffic Releasing at Road", a)

        signal[a][0] = "green"
        signal[a][2] = "grey"
        if a == 1 or a == 3:
            Traffic_signal[a].create_oval(1, 1, 40, 40, fill=signal[a][0])
            Traffic_signal[a].create_oval(40, 0, 80, 40, fill=signal[a][1])
            Traffic_signal[a].create_oval(80, 0, 120, 40, fill=signal[a][2])
        else:
            Traffic_signal[a].create_oval(1, 1, 40, 40, fill=signal[a][0])
            Traffic_signal[a].create_oval(1, 40, 40, 80, fill=signal[a][1])
            Traffic_signal[a].create_oval(1, 80, 40, 120, fill=signal[a][2])

        root.update_idletasks()
        print("Signal of all Roads:", signal)
        print("Green Signal ON for", (Sequenced_time_list[i][1]))
        time.sleep((Sequenced_time_list[i][1]) / speed)

        signal[a][0] = "grey"
        signal[a][1] = "yellow"
        if a == 1 or a == 3:
            Traffic_signal[a].create_oval(1, 1, 40, 40, fill=signal[a][0])
            Traffic_signal[a].create_oval(40, 0, 80, 40, fill=signal[a][1])
            Traffic_signal[a].create_oval(80, 0, 120, 40, fill=signal[a][2])
        else:
            Traffic_signal[a].create_oval(1, 1, 40, 40, fill=signal[a][0])
            Traffic_signal[a].create_oval(1, 40, 40, 80, fill=signal[a][1])
            Traffic_signal[a].create_oval(1, 80, 40, 120, fill=signal[a][2])

        root.update_idletasks()
        print("Signal of all Roads:", signal)
        print("Yellow Signal ON for", time_for_yellow)
        time.sleep(time_for_yellow / speed)

        signal[a][1] = "grey"
        signal[a][2] = "red"
        if a == 1 or a == 3:
            Traffic_signal[a].create_oval(1, 1, 40, 40, fill=signal[a][0])
            Traffic_signal[a].create_oval(40, 0, 80, 40, fill=signal[a][1])
            Traffic_signal[a].create_oval(80, 0, 120, 40, fill=signal[a][2])
        else:
            Traffic_signal[a].create_oval(1, 1, 40, 40, fill=signal[a][0])
            Traffic_signal[a].create_oval(1, 40, 40, 80, fill=signal[a][1])
            Traffic_signal[a].create_oval(1, 80, 40, 120, fill=signal[a][2])

        root.update_idletasks()
        print("Signal of all Roads:", signal)
        print("Red Signal ON")
        print("Traffic Sealed at Road", Sequenced_time_list[i][0])
        print("\n")
    for i in text_part:
        Display.delete(i)


# random vehicles & displaying info
def start_round(emergency_for_road, speed):
    emergency = {1: False, 2: False, 3: False, 4: False}  # max & min not fixed
    if (emergency_for_road != 0):
        emergency[emergency_for_road] = True
    small_vehicle_list = []
    for y in range(4):
        small_vehicle_list.append(random.randrange(0, max_small_vehicles))
    print("\nNo. of Small Vehicle on Road 1,2,3,4 are:", small_vehicle_list)

    medium_vehicle_list = []
    for y in range(4):
        medium_vehicle_list.append(random.randrange(0, max_medium_vehicles))
    print("No. of Medium Vehicle on Road 1,2,3,4 are:", medium_vehicle_list)

    large_vehicle_list = []
    for y in range(4):
        large_vehicle_list.append(random.randrange(0, max_large_vehicles))
    print("No. of Large Vehicle on Road 1,2,3,4 are:", large_vehicle_list)

    timelist = {}
    for i in range(4):
        timelist[i + 1] = (small_vehicle_list[i] * time_for_small_vehicles) + (
                medium_vehicle_list[i] * time_for_medium_vehicles) + (
                                  large_vehicle_list[i] * time_for_large_vehicles)

    Sequenced_time_list = sorted(timelist.items(), key=lambda i: (i[1], i[0]), reverse=True)
    Emergency_Signal(Sequenced_time_list, timelist, emergency)
    print("The sequence and time set that will be followed:", Sequenced_time_list, end="\n\n")

    # text area
    R1_SV = Display.create_text(183.3 + 150.7, 50, text=small_vehicle_list[0], fill="white", font="Arial 8")
    R1_MV = Display.create_text(183.3 + 150.7, 60, text=medium_vehicle_list[0], fill="white", font="Arial 8")
    R1_LV = Display.create_text(183.3 + 150.7, 70, text=large_vehicle_list[0], fill="white", font="Arial 8")
    R1_TV = Display.create_text(183.3 + 105.7, 90,
                                text=small_vehicle_list[0] + medium_vehicle_list[0] + large_vehicle_list[0],
                                fill="white", font="Arial 10")
    R1_time = Display.create_text(183.3 + 150.7, 110, text=timelist[1], fill="white", font="Arial 10")

    R2_SV = Display.create_text(150.7, 183.3 + 50, text=small_vehicle_list[1], fill="white", font="Arial 8")
    R2_MV = Display.create_text(150.7, 183.3 + 60, text=medium_vehicle_list[1], fill="white", font="Arial 8")
    R2_LV = Display.create_text(150.7, 183.3 + 70, text=large_vehicle_list[1], fill="white", font="Arial 8")
    R2_TV = Display.create_text(105.7, 183.3 + 90,
                                text=small_vehicle_list[1] + medium_vehicle_list[1] + large_vehicle_list[1],
                                fill="white", font="Arial 10")
    R2_time = Display.create_text(150.7, 183.3 + 110, text=timelist[2], fill="white", font="Arial 10")

    R4_SV = Display.create_text(2 * 183.3 + 150.7, 183.3 + 50, text=small_vehicle_list[3], fill="white", font="Arial 8")
    R4_MV = Display.create_text(2 * 183.3 + 150.7, 183.3 + 60, text=medium_vehicle_list[3], fill="white",
                                font="Arial 8")
    R4_LV = Display.create_text(2 * 183.3 + 150.7, 183.3 + 70, text=large_vehicle_list[3], fill="white", font="Arial 8")
    R4_TV = Display.create_text(2 * 183.3 + 105.7, 183.3 + 90,
                                text=small_vehicle_list[3] + medium_vehicle_list[3] + large_vehicle_list[3],
                                fill="white", font="Arial 10")
    R4_time = Display.create_text(2 * 183.3 + 150.7, 183.3 + 110, text=timelist[4], fill="white", font="Arial 10")

    R3_SV = Display.create_text(183.3 + 150.7, 2 * 183.3 + 50, text=small_vehicle_list[2], fill="white", font="Arial 8")
    R3_MV = Display.create_text(183.3 + 150.7, 2 * 183.3 + 60, text=medium_vehicle_list[2], fill="white",
                                font="Arial 8")
    R3_LV = Display.create_text(183.3 + 150.7, 2 * 183.3 + 70, text=large_vehicle_list[2], fill="white", font="Arial 8")
    R3_TV = Display.create_text(183.3 + 105.7, 2 * 183.3 + 90,
                                text=small_vehicle_list[2] + medium_vehicle_list[2] + large_vehicle_list[2],
                                fill="white", font="Arial 10")
    R3_time = Display.create_text(183.3 + 150.7, 2 * 183.3 + 110, text=timelist[3], fill="white", font="Arial 10")

    text_part = [R1_TV, R1_time, R1_LV, R1_SV, R1_MV,
                 R2_TV, R2_time, R2_LV, R2_SV, R2_MV,
                 R3_TV, R3_time, R3_LV, R3_SV, R3_MV,
                 R4_TV, R4_time, R4_LV, R4_SV, R4_MV, ]

    Smart_traffic_system(Sequenced_time_list, emergency, speed, text_part)


# DESIGN
def start():
    pass
    loops = continue_loop.get()
    emergency_for_road_variable = emergency_for_road.get()
    while loops:
        start_round(emergency_for_road_variable, speed_scale.get())
        loops -= 1
        emergency_for_road_variable = 0
        root.update_idletasks()


def stop():
    exit()


# Main root
root = Tk()
root.title("Group 8 Captone Project 2")
root.geometry("650x790")
root.maxsize(650, 790)
root.minsize(650, 790)

# variables
emergency_for_road = IntVar()
emergency_for_road.set(0)

# Title
Label(root, text="Smart Traffic Signal System", font="Arial 15 bold").grid(row=0, column=1)

# UI frame
UI = Frame(root)
UI.grid(row=2, column=1)

Label(root, text="Emergency at ").grid(row=1, column=1)
Radiobutton(UI, text="Road 1", variable=emergency_for_road, value=1).grid(row=0, column=0)
Radiobutton(UI, text="Road 2", variable=emergency_for_road, value=2).grid(row=0, column=1)
Radiobutton(UI, text="Road 3", variable=emergency_for_road, value=3).grid(row=0, column=2)
Radiobutton(UI, text="Road 4", variable=emergency_for_road, value=4).grid(row=0, column=3)

Label(UI, text="Speed", font="Arial").grid(row=1, column=1)
speed_scale = Scale(UI, from_=10, to=30, orient=HORIZONTAL)
speed_scale.set(20)
speed_scale.grid(row=2, column=1)

Label(UI, text="Rounds", font="Arial").grid(row=1, column=2)
continue_loop = Scale(UI, from_=1, to=10, orient=HORIZONTAL)
continue_loop.set(5)
continue_loop.grid(row=2, column=2)

Button(UI, text="start", command=start).grid(row=2, column=0, pady=5)
Button(UI, text="Stop", command=stop).grid(row=2, column=3, pady=5)

# Canvas
Display = Canvas(root, width=550, height=550)
Display.grid(row=4, column=1)

# Backgroud design
Display.create_rectangle(0, 0, 183.3, 183.3, fill="pale green", outline="white")
Display.create_rectangle(183.3, 0, 2 * 183.3, 183.3, fill="gray46", outline="white")
Display.create_rectangle(2 * 183.3, 0, 3 * 183.3, 183.3, fill="pale green", outline="white")

Display.create_rectangle(0, 183.3, 3 * 183.3, 2 * 183.3, fill="gray46", outline="white")
Display.create_rectangle(183.3, 183.3, 2 * 183.3, 2 * 183.3, fill="gray46", outline="white")

Display.create_rectangle(0, 2 * 183.3, 183.3, 3 * 183.3, fill="pale green", outline="white")
Display.create_rectangle(183.3, 2 * 183.3, 2 * 183.3, 3 * 183.3, fill="gray46", outline="white")
Display.create_rectangle(2 * 183.3, 2 * 183.3, 3 * 183.3, 3 * 183.3, fill="pale green", outline="white")

Display.create_line(180.3, 183.3, 180.3, 2 * 183.3, fill='white')
Display.create_line(2 * 183.3 + 3, 183.3, 2 * 183.3 + 3, 2 * 183.3, fill='white')
Display.create_line(183.3, 180.3, 2 * 183.3, 180.3, fill='white')
Display.create_line(183.3, 2 * 183.3 + 3, 2 * 183.3, 2 * 183.3 + 3, fill='white')

# text design
Display.create_text(183.3 + 91.7, 30, text="ROAD 1", fill="white", font="Arial 15 bold")
Display.create_text(183.3 + 81.7, 50, text="No. of small vehicles: ", fill="white", font="Arial 8")
Display.create_text(183.3 + 81.7, 60, text="No. of medium vehicles: ", fill="white", font="Arial 8")
Display.create_text(183.3 + 81.7, 70, text="No. of large vehicles: ", fill="white", font="Arial 8")
Display.create_text(183.3 + 81.7, 90, text="Total: ", fill="white", font="Arial 10")
Display.create_text(183.3 + 81.7, 110, text="Green light period(s): ", fill="white", font="Arial 10")

Display.create_text(91.7, 183.3 + 30, text="ROAD 2", fill="white", font="Arial 15 bold")
Display.create_text(81.7, 183.3 + 50, text="No. of small vehicles: ", fill="white", font="Arial 8")
Display.create_text(81.7, 183.3 + 60, text="No. of medium vehicles: ", fill="white", font="Arial 8")
Display.create_text(81.7, 183.3 + 70, text="No. of large vehicles: ", fill="white", font="Arial 8")
Display.create_text(81.7, 183.3 + 90, text="Total: ", fill="white", font="Arial 10")
Display.create_text(81.7, 183.3 + 110, text="Green light period(s): ", fill="white", font="Arial 10")

Display.create_text(2 * 183.3 + 91.7, 183.3 + 30, text="ROAD 4", fill="white", font="Arial 15 bold")
Display.create_text(2 * 183.3 + 81.7, 183.3 + 50, text="No. of small vehicles: ", fill="white", font="Arial 8")
Display.create_text(2 * 183.3 + 81.7, 183.3 + 60, text="No. of medium vehicles: ", fill="white", font="Arial 8")
Display.create_text(2 * 183.3 + 81.7, 183.3 + 70, text="No. of large vehicles: ", fill="white", font="Arial 8")
Display.create_text(2 * 183.3 + 81.7, 183.3 + 90, text="Total: ", fill="white", font="Arial 10")
Display.create_text(2 * 183.3 + 81.7, 183.3 + 110, text="Green light period(s): ", fill="white", font="Arial 10")

Display.create_text(183.3 + 91.7, 2 * 183.3 + 30, text="ROAD 3", fill="white", font="Arial 15 bold")
Display.create_text(183.3 + 81.7, 2 * 183.3 + 50, text="No. of small vehicles: ", fill="white", font="Arial 8")
Display.create_text(183.3 + 81.7, 2 * 183.3 + 60, text="No. of medium vehicles: ", fill="white", font="Arial 8")
Display.create_text(183.3 + 81.7, 2 * 183.3 + 70, text="No. of large vehicles: ", fill="white", font="Arial 8")
Display.create_text(183.3 + 81.7, 2 * 183.3 + 90, text="Total: ", fill="white", font="Arial 10")
Display.create_text(183.3 + 81.7, 2 * 183.3 + 110, text="Green light period(s): ", fill="white", font="Arial 10")

# Traffic Signal Design
Traffic_signal1 = Canvas(root, height=40, width=120, bg="black")
Traffic_signal1.grid(row=3, column=1, pady=1)
Traffic_signal2 = Canvas(root, height=120, width=40, bg="black")
Traffic_signal2.grid(row=4, column=0, pady=1)
Traffic_signal3 = Canvas(root, height=40, width=120, bg="black")
Traffic_signal3.grid(row=5, column=1, pady=1)
Traffic_signal4 = Canvas(root, height=120, width=40, bg="black")
Traffic_signal4.grid(row=4, column=2, pady=1)

Traffic_signal = [0, Traffic_signal1, Traffic_signal2, Traffic_signal3, Traffic_signal4]

Traffic_signal1.create_oval(1, 1, 40, 40, fill=signal[1][0])
Traffic_signal1.create_oval(40, 0, 80, 40, fill=signal[1][1])
Traffic_signal1.create_oval(80, 0, 120, 40, fill=signal[1][2])

Traffic_signal2.create_oval(1, 1, 40, 40, fill=signal[2][0])
Traffic_signal2.create_oval(1, 40, 40, 80, fill=signal[2][1])
Traffic_signal2.create_oval(1, 80, 40, 120, fill=signal[2][2])

Traffic_signal3.create_oval(1, 1, 40, 40, fill=signal[3][0])
Traffic_signal3.create_oval(40, 0, 80, 40, fill=signal[3][1])
Traffic_signal3.create_oval(80, 0, 120, 40, fill=signal[3][2])

Traffic_signal4.create_oval(1, 1, 40, 40, fill=signal[4][0])
Traffic_signal4.create_oval(1, 40, 40, 80, fill=signal[4][1])
Traffic_signal4.create_oval(1, 80, 40, 120, fill=signal[4][2])

root.mainloop()