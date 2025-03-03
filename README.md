# 🔥 FlameMyGame

## 🚀 Overview
FlameMyGame is an AI-powered **roasting and rizzing** app that takes any text input (or extracts text from an uploaded image) and **destroys it with an epic roast**, followed by a **smooth, confident response**. Whether you're looking to get obliterated by sarcasm or need a legendary comeback, this app has got you covered!

## ✨ Features
- **Screenshot OCR Support**: Upload a screenshot, and the app extracts text using AWS Rekognition.
- **Brutal AI Roasting**: Get absolutely flamed by an AI trained to be savage.
- **Ultimate Comeback (Rizz Mode)**: The AI flips the script and provides an irresistible, confident response.
- **Chat History Storage**: Keeps track of past roasts & responses using AWS S3.

## 🏗️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/) for an interactive web UI.
- **AI Model**: Google Gemini API (gemini-1.5-pro-001) for generating text.
- **OCR**: AWS Rekognition for text extraction from images.
- **Cloud Storage**: AWS S3 for storing chat history.
- **Serverless Processing**: AWS Lambda for handling image processing.

## 📂 Project Structure
```
FlameMyGame/
│── app.py              # Main Streamlit app
│── .env                # Environment variables (DO NOT SHARE!)
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

## 🔧 Setup & Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/devrishivermaa/FlameMyGame.git
cd FlameMyGame
```

### 2️⃣ Set Up Environment Variables
Create a `.env` file and add the following:
```
API_KEY=your_google_gemini_api_key
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
BUCKET_NAME=your_s3_bucket_name
LAMBDA_FUNCTION_NAME=your_lambda_function
```

### 3️⃣ Run the App
```sh
streamlit run app.py
```

## 📜 Usage Guide
1. **Upload an image** (screenshot with text) OR **type your message**.
2. Click **"Get Roasted & Rizzed!"**.
3. Get utterly **destroyed** by AI sarcasm. 🤣
4. Receive a **legendary comeback** to redeem yourself. 😎
5. View past chats in the history section.

## 🚀 Deployment
To deploy on **AWS or any cloud provider**, ensure that:
- The AWS Lambda function is correctly configured.
- The S3 bucket has the right permissions.
- API keys are stored securely using environment variables.

## 🤝 Contributing
Want to add more **flame** to the fire? Fork this repo, make changes, and submit a PR! 🔥

## 📜 License
This project is open-source under the **MIT License**.

---
🔥 **Get ready to be roasted & rizzed like never before!** 🔥

