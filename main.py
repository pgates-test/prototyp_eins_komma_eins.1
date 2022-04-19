import pyautogui


def main():
    screenwidth, screenheight = pyautogui.size()
    current_mouse_x, current_mouse_y = pyautogui.position()
    # print screen size
    print('Screen width, height = ' + str(screenwidth) + ', ' + str(screenheight))

    # write mouse position to a file every  0.1 second
    while True:
        pyautogui.moveTo(current_mouse_x, current_mouse_y, duration=0.1)   #duration is the time interval between position updates, while more than 0,1 makes cursor shake a lot
        current_mouse_x, current_mouse_y = pyautogui.position()
        print('X, Y = ' + str(current_mouse_x) + ', ' + str(current_mouse_y))
        with open('mouseData.txt', 'a') as f:
            f.write(str(current_mouse_x) + ', ' + str(current_mouse_y) + '\n')
        #pyautogui.PAUSE = 1     redundant,
        #pyautogui.FAILSAFE = True  useful


if __name__ == '__main__':
    main()
