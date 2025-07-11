# Step 1: Create .gitignore
echo venv/ > .gitignore
echo __pycache__/ >> .gitignore
echo *.pyc >> .gitignore
echo *.h5 >> .gitignore
echo .DS_Store >> .gitignore

# Step 2: Freeze requirements
pip freeze > requirements.txt

# Step 3: Create README.md
cat > README.md << EOF
# 🧠 Digit Recognition with CNN (MNIST)

This project implements a Convolutional Neural Network (CNN) to recognize handwritten digits using the popular **MNIST dataset**. It includes training, evaluation, and even **real-time digit prediction from drawings**.

---

## 📌 Features

- 🧮 Trains a CNN on MNIST (0–9 digits)
- 📊 Evaluates test accuracy
- 💾 Saves and loads trained models
- 🖼️ Supports real-time digit prediction via drawing input
- 🔍 Displays incorrect predictions for debugging

---

## 🚀 Getting Started

### 1. Clone the repo

\`\`\`bash
git clone https://github.com/Divyansh123456789haha/Digit-Recognition-.git
cd Digit-Recognition-
\`\`\`

### 2. Create virtual environment

\`\`\`bash
python -m venv venv
venv\Scripts\activate  # On Windows
\`\`\`

### 3. Install dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Train the model

\`\`\`bash
python train_model.py
\`\`\`

This will:
- Load MNIST
- Normalize data
- Train the CNN
- Save the model as \`mnist_cnn_model.h5\`

---

## 🧪 Real-Time Testing

To draw a digit and predict it using webcam or canvas:

\`\`\`bash
python realtimetest.py
\`\`\`

Make sure \`mnist_cnn_model.h5\` exists in your project folder.

---

## 📂 Project Structure

\`\`\`
digit-recognition/
│
├── train_model.py           # Trains the CNN on MNIST
├── realtimetest.py          # Predicts digits from drawn input
├── mnist_cnn_model.h5       # Saved trained model
├── requirements.txt         # Python packages
└── README.md                # This file
\`\`\`

---

## 📈 Accuracy

| Metric       | Value     |
|--------------|-----------|
| Accuracy     | ~98%      |
| Dataset      | MNIST     |
| Epochs       | 10        |

---

## 🛡️ License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## ✨ Credits

Built by
