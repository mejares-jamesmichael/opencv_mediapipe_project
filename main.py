import cv2
import mediapipe as mp
import imageio

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Load GIF
gif = imageio.get_reader('media/tongue.gif')
frames = [cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) for frame in gif]
gif_frame_idx = 0

# Load image
perfect_cell = cv2.imread('media/perfect_cell.jpg')

# Initialize Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, min_detection_confidence=0.7)

# Function to count raised fingers
def count_fingers(landmarks):
    # Finger tips and bases
    tips = [4, 8, 12, 16, 20]  # thumb, index, middle, ring, pinky
    bases = [2, 5, 9, 13, 17]  # corresponding bases
    
    count = 0
    # Thumb (check x position)
    if landmarks[tips[0]].x > landmarks[bases[0]].x:
        count += 1
    # Other fingers (check y position)
    for i in range(1, 5):
        if landmarks[tips[i]].y < landmarks[bases[i]].y:
            count += 1
    return count

# Capture video
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip frame horizontally for mirror effect
    frame = cv2.flip(frame, 1)
    
    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process with MediaPipe
    results = hands.process(rgb_frame)
    face_results = face_mesh.process(rgb_frame)
    
    smile = False
    tongue_out = False
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            left_corner = face_landmarks.landmark[61]
            right_corner = face_landmarks.landmark[291]
            upper_lip = face_landmarks.landmark[13]
            lower_lip = face_landmarks.landmark[14]
            if left_corner.y < upper_lip.y and right_corner.y < upper_lip.y:
                smile = True
            if lower_lip.y - upper_lip.y > 0.05:
                tongue_out = True
            break

    if results.multi_hand_landmarks:
        total_fingers = 0
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Count fingers
            finger_count = count_fingers(hand_landmarks.landmark)
            total_fingers += finger_count
        
        # Display total count
        cv2.putText(frame, f'Total Fingers: {total_fingers}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    if smile and perfect_cell is not None:
        img = cv2.resize(perfect_cell, (200, 200))
        h, w = img.shape[:2]
        fh, fw = frame.shape[:2]
        frame[fh - h:fh, fw - w:fw] = img
    
    if tongue_out and frames:
        gif_frame = frames[gif_frame_idx % len(frames)]
        img = cv2.resize(gif_frame, (200, 200))
        h, w = img.shape[:2]
        fh, fw = frame.shape[:2]
        frame[10:10+h, 10:10+w] = img
        gif_frame_idx += 1
    
    # Show frame
    cv2.imshow('Real-time Cam Feed', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()