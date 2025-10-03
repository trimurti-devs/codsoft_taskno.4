import face_recognition
import cv2
import os

# Load known faces
known_encodings = []
known_names = []

for filename in os.listdir("faces"):
    img_path = os.path.join("faces", filename)
    image = face_recognition.load_image_file(img_path)
    encodings = face_recognition.face_encodings(image)
    if len(encodings) > 0:
        known_encodings.append(encodings[0])
        known_names.append(os.path.splitext(filename)[0])  # filename = name.jpg → "name"

# Open webcam
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)

    for (top, right, bottom, left), encoding in zip(locations, encodings):
        matches = face_recognition.compare_faces(known_encodings, encoding, tolerance=0.6)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        # Draw box and label
        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Face Recognition", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
