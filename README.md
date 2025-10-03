# 👤 Real-Time Face Detection & Recognition (Python)

A real-time **face detection and recognition** system built with Python, OpenCV, and the `face_recognition` library.  
The program captures live video from your webcam, detects faces, and identifies known individuals by comparing them with pre-stored images.

---

## 📁 Project Overview

This project demonstrates how to build a **real-time face recognition application** in Python using deep learning-based face embeddings.  
It loads known faces from a local directory, encodes them, and then continuously scans live video frames from a webcam. Each detected face is compared against the known encodings, and if a match is found, the name is displayed on the video feed.

✅ **Key Capabilities:**
- Detect multiple faces in real time.
- Identify known individuals from a preloaded dataset.
- Label unknown faces dynamically.
- Lightweight and easy to extend for larger face databases.

---

## ⚙️ Features

- 🧠 **Face Detection:** Uses HOG/CNN-based models from `face_recognition` for accurate face localization.  
- 📸 **Real-Time Recognition:** Processes live video from your webcam.  
- 🪪 **Known Face Database:** Automatically loads and encodes faces from a `faces/` folder.  
- 🔍 **Identity Labeling:** Displays the person’s name above the detected face.  
- ❓ **Unknown Handling:** Unrecognized faces are labeled as “Unknown.”  
- 💻 **Simple & Extensible:** Easily scalable for attendance systems, access control, and more.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```Copy Code
git clone https://github.com/yourusername/codsoft_taskno.4.git
```
```Copy Code
cd codsoft_taskno.4
```
2. Install Dependencies
Make sure you have Python 3.7+ installed, then install the required libraries:


```Copy code
pip install opencv-python face_recognition
```
⚠️ Note: On some systems, you may need to install dlib manually before face_recognition.

3. Add Known Faces
Create a folder named faces/ in the project directory and place images of known individuals inside it:

```Copy code
faces/
├── Jeff Bezos.jpg
├── Elon Musk.jpg
```
The filename (without extension) is used as the person's label (e.g., alice.jpg → "Alice").

▶️ How to Run
Run the script directly:


```Copy code
python faceDetect_Recognition.py
```
The webcam will open.

The system will detect and recognize faces in real time.

Press Q to quit the application.

---

🧠 How It Works
Load Known Faces:

Images from the faces/ directory are read and encoded into numerical vectors using face_recognition.face_encodings().

Capture Video Frames:

The system reads frames from the webcam using OpenCV (cv2.VideoCapture).

Face Detection & Encoding:

Each frame is converted to RGB and processed to locate faces.

Encodings for detected faces are computed.

Matching & Labeling:

Encodings are compared with the known encodings using compare_faces().

If a match is found, the corresponding name is displayed.

If not, the label “Unknown” is shown.

Display Results:

Bounding boxes and names are drawn on the video feed in real time.

---

📸 Example Directory Structure
```Copy code
face-recognition/
│
├── faceDetect_Recognition.py
├── faces/
│   ├── Jeff Bezos.jpg
│   ├── Elon Musk.jpg
│
└── README.md
```
🧪 Example Output
When a known face is detected:


```Copy code
[INFO] Detected: Jeff Bezos
[INFO] Detected: Elon Musk
```
And in the live video feed, you’ll see:

A green bounding box around the face.

The name displayed above the box.

"Unknown" label for unfamiliar faces.

---

🚀 Future Improvements
📂 Add a database or JSON storage for face encodings.

🖼️ Implement face registration directly from the webcam.

🌐 Integrate with a web dashboard for attendance tracking.

🔒 Add face verification with confidence scores.

---

🧰 Technologies Used
🐍 Python 3.x

📷 OpenCV – Real-time image processing

🤖 face_recognition (dlib) – Face encoding and comparison

📁 OS Module – Automatic dataset loading
