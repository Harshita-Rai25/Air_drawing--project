# ✍️ Air Drawing

Air Drawing is a computer vision project built using **Python, OpenCV, and NumPy** that allows users to draw in the air using a webcam. The project tracks the movement of an object in real time and converts its motion into a virtual drawing on the screen.

This project explores computer vision concepts such as **HSV color detection, contour tracking, thresholding, and real-time object tracking** to create an interactive air drawing experience.

## 🚀 Features

* 📷 Real-time webcam tracking
* 🎨 Virtual drawing using object movement
* 🔴 Color-based object detection using HSV
* ✋ Contour-based tracking mode
* 🖌️ Real-time line drawing
* 🧹 Clear drawing canvas
* 🪞 Mirror view for a natural drawing experience

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy

## 📂 Project Structure

```text
Air-Drawing/
│
├── air_drawing.py        # Main air drawing using color tracking
├── contour_drawing.py    # Air drawing using contour detection
├── test_cam.py           # Webcam testing script
├── README.md             # Project documentation
└── requirements.txt      # Required Python libraries
```

## ⚙️ How It Works

1. The webcam captures live video frames.
2. Each frame is processed using OpenCV.
3. The program detects the drawing object using different computer vision techniques:

   * **HSV color detection** to track a specific colored object.
   * **Thresholding and contour detection** to track object movement.
4. The position of the detected object is calculated.
5. The movement points are stored.
6. Lines are drawn between these points to create a virtual drawing.

---

## 📦 Installation

Clone this repository:

```bash
git clone https://github.com/your-username/Air-Drawing.git
cd Air-Drawing
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

### Color Tracking Mode

```bash
python air_drawing.py
```

### Contour Tracking Mode

```bash
python contour_drawing.py
```

### Camera Test

```bash
python test_cam.py
````
## 🎮 Controls

| Key     | Action               |
| ------- | -------------------- |
| **C**   | Clear the drawing    |
| **ESC** | Exit the application |

## 🔍 Computer Vision Techniques Used

### HSV Color Segmentation

Detects a specific color range and tracks the movement of the object.

### Thresholding

Converts images into binary format to make object detection easier.

### Contour Detection

Finds object boundaries and identifies the largest detected object.

### Coordinate Tracking

Stores object positions and connects them to create a virtual drawing.

## 🔮 Future Improvements

* Smooth drawing using filtering techniques
* Multiple color support
* Adjustable brush size
* Save drawings as images
* AI-based hand tracking
* Gesture-based controls
* Virtual whiteboard mode
* Improved accuracy with advanced tracking algorithm

## 📚 Learning Outcomes

Through this project, I learned:

* Webcam handling using OpenCV
* Image preprocessing techniques
* HSV color detection
* Contour detection
* Real-time object tracking
* Building interactive computer vision applications


## 🤝 Contributing

Suggestions and improvements are welcome! Feel free to fork this repository and experiment with new features.

## 👨‍💻 Author

**Harshita Rai**

Built with ❤️ using Python and OpenCV.

⭐ If you like this project, consider giving it a star on GitHub! It motivates me to create more projects and keep improving.
