from flet import *
from math import pi
import time 
def animation(dictt):
    clockwise_rotate = pi / 4
    counter_clockwise_rotate = -pi / 2
    red_box = dictt["/"].controls[0].content.controls[0].content.controls[0].content.controls[0]
    blue_box = dictt["/"].controls[0].content.controls[0].content.controls[0].content.controls[1]
    counter = 0
    while True:
        if 0 <= counter <= 4:
            red_box.rotate = transform.Rotate(
                counter_clockwise_rotate, alignment.center
            )
            blue_box.rotate = transform.Rotate(
                clockwise_rotate, alignment.center
            )
            red_box.update()
            blue_box.update()
            counter_clockwise_rotate -= pi / 2
            clockwise_rotate += pi / 2
            counter += 1
            time.sleep(0.7)
        if 5 <= counter < 10:
            red_box.rotate = transform.Rotate(
                counter_clockwise_rotate, alignment.center
            )
            blue_box.rotate = transform.Rotate(
                clockwise_rotate, alignment.center
            )
            red_box.update()
            blue_box.update()
            clockwise_rotate -= pi / 2
            counter_clockwise_rotate += pi / 2
            counter += 1
            time.sleep(0.7)
        if counter == 10:
            counter = 0