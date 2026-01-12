import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1, # Kita fokus 1 tangan dulu biar tidak pusing
    min_detection_confidence=0.7
)

tip_ids = [4, 8, 12, 16, 20]

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success: break
    
    img = cv2.flip(img, 1) 
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    fingers_status = []

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            
            h, w, c = img.shape
            lm_list = [] # Menyimpan semua koordinat (x,y) dari 21 titik
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])

            if len(lm_list) != 0:
                fingers_status = [] # Reset status

                if lm_list[tip_ids[0]][1] < lm_list[tip_ids[0] - 1][1]:
                    fingers_status.append(1) # Jempol Buka
                else:
                    fingers_status.append(0) # Jempol Tutup

                for id in range(1, 5):
                    if lm_list[tip_ids[id]][2] < lm_list[tip_ids[id] - 2][2]:
                        fingers_status.append(1)
                    else:
                        fingers_status.append(0)

                total_fingers = fingers_status.count(1)
                
                
                cv2.rectangle(img, (20, 20), (170, 170), (0, 255, 0), cv2.FILLED)
                
                cv2.putText(img, str(total_fingers), (45, 145), cv2.FONT_HERSHEY_SIMPLEX, 
                            5, (255, 0, 0), 15)
                

    cv2.imshow("Penghitung Jari", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()