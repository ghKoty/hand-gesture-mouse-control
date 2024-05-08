#!/usr/bin/python3

# Hand gesture mouse control © 2024 by ghKoty is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International. To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/

from time import sleep
import mediapipe as mp
import numpy as np
import pyautogui
import cv2

mpHands = mp.solutions.hands
mpDrawing = mp.solutions.drawing_utils
hands = mpHands.Hands(static_image_mode=False, max_num_hands=1)


# ==========some settings===========
drag_threshold = 3
drag_sensitivity = 0.1
scroll_threshold = 3
scroll_sensitivity = 0.4
press_threshold_multiplyer = 1
# ==================================


def getVector(p1, p2):
    return np.array([p2.x - p1.x, p2.y - p1.y])

def isFingerExtended(base, tip, is_thumb=False):
    base_to_tip = getVector(base, tip)
    base_to_tip_norm = np.linalg.norm(base_to_tip)
    return base_to_tip_norm > extension_threshold

def getDistanceBeetween(base, tip, is_thumb=False):
    base_to_tip = getVector(base, tip)
    base_to_tip_norm = np.linalg.norm(base_to_tip)
    return base_to_tip_norm


pyautogui.FAILSAFE = False
cap = cv2.VideoCapture(0)

tipIds = [4, 8, 12, 16, 17]

isLMousePressed = False
isRMousePressed = False
isScrollReset = True
isMoveReset = True

while True:
    isMainFingerPressed = False
    isRCFingerPressed = False
    isMoveFingerPressed = False
    isScrollFingerPressed = False
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        isMainFingerPressed = True
        isMoveFingerPressed = True
        isRCFingerPressed = True
        isScrollFingerPressed = True
        
        for handLandmarks in results.multi_hand_landmarks:
            mpDrawing.draw_landmarks(frame, handLandmarks, mpHands.HAND_CONNECTIONS)
        if handLandmarks:
            landmarks = handLandmarks.landmark
            
            handDistance = getDistanceBeetween(landmarks[0], landmarks[1])
            extension_threshold = handDistance * press_threshold_multiplyer
            sensitivity = (1/handDistance) * drag_sensitivity
            scrollSensitivity = (1/handDistance) * scroll_sensitivity
            
            for fingerIndex, tipId in enumerate(tipIds):
                if isFingerExtended(landmarks[tipId], landmarks[tipIds[0]]) or tipId == tipIds[0]:
                
                    if tipId == tipIds[1]: isMainFingerPressed = False
                    if tipId == tipIds[2]: isMoveFingerPressed = False; isMoveReset = True
                    if tipId == tipIds[3]: isRCFingerPressed = False
                    if tipId == tipIds[4]: isScrollFingerPressed = False; isScrollReset = True
                    
                    x, y = int(landmarks[tipId].x * frame.shape[1]), int(landmarks[tipId].y * frame.shape[0])
                    
                    if tipId == tipIds[0]:
                        thumbPosX = x
                        thumbPosY = y
                    
                    if tipId == tipIds[0]:
                        cv2.circle(frame, (x, y), 10, (255, 0, 0), cv2.FILLED)
                    elif tipId == tipIds[1]:
                        cv2.circle(frame, (x, y), 10, (255, 255, 0), cv2.FILLED)
                    elif tipId == tipIds[2]:
                        cv2.circle(frame, (x, y), 10, (0, 255, 0), cv2.FILLED)
                    elif tipId == tipIds[3]:
                        cv2.circle(frame, (x, y), 10, (0, 255, 255), cv2.FILLED)
                    else:
                        cv2.circle(frame, (x, y), 10, (0, 0, 255), cv2.FILLED)
                        
    else:
        sleep(0.2)
    
    
    if isMainFingerPressed:
        if not isLMousePressed:
            pyautogui.mouseDown()
            isLMousePressed = True
    else:
        if isLMousePressed:
            pyautogui.mouseUp()
            isLMousePressed = False
    
    if isRCFingerPressed:
        if not isRMousePressed:
            pyautogui.mouseDown(button='right')
            isRMousePressed = True
    else:
        if isRMousePressed:
            pyautogui.mouseUp(button='right')
            isRMousePressed = False
    
    if isMoveFingerPressed:
        if isMoveReset:
            oldMoveX = thumbPosX
            oldMoveY = thumbPosY
            isMoveReset = False
        xDiff = thumbPosX - oldMoveX
        yDiff = thumbPosY - oldMoveY
        if not xDiff in range(drag_threshold*-1, drag_threshold) or not yDiff in range(drag_threshold*-1, drag_threshold):
            pyautogui.moveRel(xDiff*-1*sensitivity, yDiff*sensitivity)
        oldMoveX = thumbPosX
        oldMoveY = thumbPosY
    
    if isScrollFingerPressed:
        if isScrollReset:
            oldScrollY = thumbPosY
            isScrollReset = False
        yDiff = thumbPosY - oldScrollY
        if not yDiff in range(scroll_threshold*-1, scroll_threshold):
            pyautogui.scroll(round(yDiff*scrollSensitivity))
        oldScrollY = thumbPosY
    
    cv2.imshow('Fingers', frame)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()
