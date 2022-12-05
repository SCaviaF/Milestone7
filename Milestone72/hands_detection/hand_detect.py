import cv2
import utils.setup as sp


def hand_cap(cap, hands, mp_hands, mp_drawing_styles, mp_drawing):
    success, image = cap.read()
    #if not success:
    #    print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
    #    continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    #cv2.imshow('MediaPipe Hands', cv2.flip(image, 1)) #mostrar pantalla de camara
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

            #return hand_landmarks.landmark[8]
            #print("Coord", hand_landmarks.landmark[8])
            return hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y, hand_landmarks.landmark[8].z
            #time.sleep(1)
    else:
        return [sp.X0, sp.Y0, sp.Z0]