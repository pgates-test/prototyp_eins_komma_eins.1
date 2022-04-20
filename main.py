import pyautogui
import matplotlib.pyplot as plt
import os
#for now it plots mouse movement
#probably will be changed to plot mouse clicks
#also probably laughably inefficient and obscure way of doing this but whatever

# import numpy as np
def check_file_size():
    file_size = os.path.getsize('mouseData.txt')
    print(file_size)


def print_screen_size():
    screenwidth, screenheight = pyautogui.size()

    # print screen size
    print('Screen width, height = ' + str(screenwidth) + ', ' + str(screenheight))


def write_mouse_position():
    current_mouse_x, current_mouse_y = pyautogui.position()
    # write mouse position to a file every  0.1 second
    i = 0
    while i != 50:  # primitive timer
        pyautogui.moveTo(current_mouse_x, current_mouse_y,
                         duration=0.1)  # duration is the time interval between position updates, while more than 0,1 makes cursor shake a lot
        current_mouse_x, current_mouse_y = pyautogui.position()
        print('X, Y = ' + str(current_mouse_x) + ',' + str(current_mouse_y))
        with open('mouseData.txt', 'a') as f:
            f.write(str(current_mouse_x) + ',' + str(current_mouse_y) + '\n')
        # pyautogui.PAUSE = 1     redundant,
        # pyautogui.FAILSAFE = True  useful, on by default
        i += 1


def plot_mouse_position():
    x_list = []
    y_list = []
    with open('mouseData.txt', 'r') as f:
        for line in f:
            x, y = line.split(',')
            x_list.append(float(x))
            y_list.append(float(y))
    # plt.figure(dpi=1200)  # dpi is the resolution of the image, let it stay for testing purposes
    plt.plot(x_list, y_list)
    plt.show()


def main():
    print_screen_size()
    write_mouse_position()
    plot_mouse_position()
    check_file_size()
    open('mouseData.txt', 'w').close()
    os.remove('mouseData.txt')  # cleanup of a temp file


if __name__ == '__main__':
    main()
