# OpenCV MediaPipe Real-Time Gesture Recognition

A real-time computer vision project that uses OpenCV and Google's MediaPipe framework to detect hand gestures, count fingers, and recognize facial expressions from a live camera feed.

## 🚀 Features

- **Real-time finger counting**: Detects and counts raised fingers from both hands
- **Facial expression recognition**: Detects smiles and tongue-out expressions
- **Interactive visual feedback**: Displays images/GIFs when specific expressions are detected
- **Multi-hand support**: Can track up to 2 hands simultaneously
- **Visual landmark overlay**: Shows hand and face landmarks in real-time

## 📋 Prerequisites

- Python 3.7 or higher
- Camera access (webcam or built-in camera)

## 🛠️ Installation

1. Clone or download this repository
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. Make sure your camera is connected and accessible
2. Run the main script:
   ```bash
   python main.py
   ```
3. Press 'q' to quit the application

## 🎯 How It Works

### Finger Counting
- The system identifies hand landmarks using MediaPipe's hand tracking
- Counts raised fingers based on landmark positions:
  - Thumb: compared by X-axis position (relative to wrist)
  - Other fingers: compared by Y-axis position (relative to knuckles)
- Displays total finger count in real-time

### Facial Expression Detection
- **Smile Detection**: Analyzes the position of mouth corners relative to upper lip
- **Tongue Detection**: Measures the distance between upper and lower lips

### Visual Feedback
- When a smile is detected, an image (`media/perfect_cell.jpg`) is displayed
- When tongue-out expression is detected, an animated GIF (`media/tongue.gif`) plays in the corner

## 📁 Project Structure

```
opencv_mediapipe_project/
├── main.py                 # Main application code
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── AGENTS.md              # Agent configuration
└── media/
    ├── perfect_cell.jpg   # Image displayed when smiling
    └── tongue.gif         # Animation displayed when tongue is out
```

## 🔧 Configuration

You can adjust these parameters in `main.py`:

- `max_num_hands`: Maximum number of hands to detect (default: 2)
- `min_detection_confidence`: Minimum confidence for hand detection (default: 0.7)
- `max_num_faces`: Maximum number of faces to detect (default: 1)
- `min_detection_confidence`: Minimum confidence for face detection (default: 0.7)

## 📦 Dependencies

This project uses:

- **OpenCV**: For camera capture and image processing
- **MediaPipe**: For hand and face landmark detection
- **imageio**: For GIF handling
- **NumPy**: For numerical operations

For a complete list, see `requirements.txt`.

## ⚠️ Known Issues & Limitations

- Performance may vary based on hardware capabilities
- Lighting conditions can affect detection accuracy
- May require calibration for different face shapes
- GIF animation may be choppy on lower-end systems

## 📚 Learn More

- [MediaPipe Documentation](https://google.github.io/mediapipe/)
- [OpenCV Documentation](https://docs.opencv.org/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgements

- Google's MediaPipe team for providing the landmark detection models
- OpenCV community for computer vision tools
- [imageio](https://imageio.github.io/) for GIF support