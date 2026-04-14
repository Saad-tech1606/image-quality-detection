# 🚀 Image Quality Detection & Enhancement System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)

---

## 📌 Overview

This project presents an **end-to-end Image Quality Detection and Enhancement System** built using **Computer Vision and Deep Learning concepts**.

It analyzes image quality using multiple visual metrics, classifies images as **Good or Poor Quality**, and automatically enhances low-quality images using advanced image processing techniques.

---

## ⚡ Key Features

* 🔍 **Blur Detection** using Laplacian Variance
* 💡 **Brightness & Contrast Analysis**
* ⭐ **Custom Quality Scoring System**
* 🧠 **Rule-based Image Classification (Good vs Poor)**
* 🛠 **Automatic Image Enhancement**

  * Sharpening Filter
  * Histogram Equalization
* 🤖 **Deep Learning Integration**

  * Pretrained **ResNet (PyTorch)** for feature extraction
* 💻 **Command-Line Interface (CLI) Support**

---

## 🧠 How It Works

1. **Input Image** is loaded from dataset or CLI argument

2. Extracts key features:

   * Blur (sharpness)
   * Brightness
   * Contrast

3. Computes a **Quality Score**:

   ```
   Score = 0.5 × Blur + 0.25 × Brightness + 0.25 × Contrast
   ```

4. Classifies image:

   * Low Score → Poor Quality
   * High Score → Good Quality

5. Enhances image if needed:

   * Applies sharpening
   * Performs histogram equalization

6. Outputs:

   * Console metrics
   * Enhanced image (`output.jpg`)

---

## 🧰 Tech Stack

* **Python**
* **OpenCV**
* **NumPy**
* **Matplotlib**
* **PyTorch**
* **Torchvision (ResNet)**

---

## 🤖 Deep Learning Component

This project explores **Convolutional Neural Networks (CNNs)** using a pretrained **ResNet18 model** from `torchvision.models`.

> Used for feature extraction and understanding deep learning-based image representation.

---

## 📂 Project Structure

```
image-quality-detection/
│── dataset/
│   └── sample.jpg
│
│── src/
│   ├── preprocessing.py
│   ├── quality_metrics.py
│   ├── enhancement.py
│   └── model.py
│
│── main.py
│── requirements.txt
│── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run the Project

```
python main.py --image dataset/sample.jpg
```

---

## 📸 Output

* 📊 Displays image quality metrics in terminal
* 🖼 Saves enhanced image as:

```
output.jpg
```

---

## 🚀 Future Improvements

* 🔬 CNN-based image quality classification
* 📊 Visualization of quality metrics
* 📁 Batch image processing
* 🌐 Web-based interface (Flask/Streamlit)
* 🤖 Autoencoder-based noise reduction

---

## 💼 Resume Description

**Image Quality Detection & Enhancement System (OpenCV, PyTorch)**

* Developed an end-to-end **computer vision pipeline** for image quality assessment using **blur detection, brightness, and contrast analysis**
* Designed a **custom image quality scoring algorithm** combining multiple visual features for intelligent classification
* Implemented **automated image enhancement techniques** including sharpening and histogram equalization
* Integrated **pretrained ResNet (PyTorch)** for deep learning-based feature extraction and representation learning
* Built a **CLI-based scalable image processing tool** supporting dynamic input handling


---

## ⭐ Conclusion

This project demonstrates practical application of:

* Computer Vision
* Feature Engineering
* Image Processing
* Deep Learning Integration

It reflects a real-world pipeline used in **image preprocessing systems, photography tools, and AI-based quality analysis platforms**.

---

## 📌 Author

**Md Saad Alam**
🚀 Aspiring Software Engineer | AI & ML Enthusiast
