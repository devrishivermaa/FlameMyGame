import streamlit as st
import boto3
import json
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure APIs
genai.configure(api_key=os.getenv("API_KEY"))
s3_client = boto3.client("s3", region_name=os.getenv("AWS_REGION"))
lambda_client = boto3.client("lambda", region_name=os.getenv("AWS_REGION"))

# Constants
BUCKET_NAME = os.getenv("BUCKET_NAME")
LAMBDA_FUNCTION_NAME = os.getenv("LAMBDA_FUNCTION_NAME")
CHAT_HISTORY_KEY = os.getenv("CHAT_HISTORY_KEY")

st.title("🔥 Flame your Game")
st.write("Upload a screenshot or type text. AI will **destroy & fix it** for you.")

uploaded_file = st.file_uploader("Upload Screenshot", type=["png", "jpg", "jpeg"])
user_input = st.text_area("Or, enter your text:")

if st.button("Get Roasted & Rizzed!"):
    if uploaded_file:
        image_key = uploaded_file.name
        s3_client.upload_fileobj(uploaded_file, BUCKET_NAME, image_key)

        lambda_payload = json.dumps({"bucket_name": BUCKET_NAME, "image_key": image_key})
        response = lambda_client.invoke(FunctionName=LAMBDA_FUNCTION_NAME, Payload=lambda_payload)

        response_payload = json.loads(response["Payload"].read())
        extracted_text = response_payload.get("extracted_text", "")

        if not extracted_text:
            st.error("❌ Failed to extract text. Try another image.")
        else:
            user_input = extracted_text  

    if not user_input.strip():
        st.warning("Don't be shy, type something or upload an image.")
    else:
        try:
            model = genai.GenerativeModel("gemini-1.5-pro-001")

            prompt = f"""
            🔥 Step 1: Roast it like hell  
            Completely tear apart the following message. Be brutally honest, sarcastic, and absolutely hilarious. No mercy.  

            🔥 Step 2: Fix the Damage  
            Now that you've humiliated the message, give me a **legendary, smooth AF response** that actually works.  
            Make it **confident, playful, and irresistible**.

            Respond in this format:
            Roast: [your roast here]  
            Rizz: [your ultra-smooth response here]  

            Here's the message: "{user_input}"
            """

            response = model.generate_content(prompt)
            roast, rizz = response.text.split("\n\n")[:2]

            st.subheader("🔥 Roast:")
            st.write(roast.replace("Roast:", "").strip())

            st.subheader("💖 Rizzed-Up Reply:")
            st.write(rizz.replace("Rizz:", "").strip())

            chat_entry = {
                "input": user_input,
                "roast": roast.replace("Roast:", "").strip(),
                "rizz": rizz.replace("Rizz:", "").strip()
            }

            chat_history = []
            try:
                response = s3_client.get_object(Bucket=BUCKET_NAME, Key=CHAT_HISTORY_KEY)
                chat_history = json.loads(response["Body"].read().decode("utf-8"))
            except Exception:
                pass

            chat_history.append(chat_entry)
            s3_client.put_object(
                Bucket=BUCKET_NAME,
                Key=CHAT_HISTORY_KEY,
                Body=json.dumps(chat_history, indent=4),
                ContentType="application/json"
            )

        except Exception as e:
            st.error("API Error: " + str(e))

try:
    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=CHAT_HISTORY_KEY)
    chat_history = json.loads(response["Body"].read().decode("utf-8"))
    if chat_history:
        st.subheader("📜 Chat History:")
        for entry in reversed(chat_history[-5:]):
            st.markdown(f"""
            💬 You: {entry['input']}
            
            🔥 {entry['roast']}
            
            💖 {entry['rizz']}
            """)
except Exception:
    pass
