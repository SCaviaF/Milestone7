import test_alpha.test_alpha1 as talpha
import test2_win as t2

import numpy as np
import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def test():
    #talpha.test_1()
    talpha.test_2()


def test2():
    # For webcam input:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

        t2.main(cap, hands, mp_hands, mp_drawing_styles, mp_drawing)




if __name__ == "__main__":
    #test()
    #main()
    #t2.main()
    test2()



