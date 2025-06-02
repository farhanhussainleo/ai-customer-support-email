# 🧠 AI-Powered Support Email Demo

This is a simple web app that uses **Azure OpenAI** to generate customer support replies and sends them via **Azure Communication Services Email** — all through an interactive UI built with **Streamlit**.

> Perfect for demos, testing, or building your own AI support assistant!

---

## 🚀 Features

- ✨ AI-generated support replies using GPT (via Azure OpenAI)
- 📝 Editable response before sending
- 📤 Sends email to customer using Azure Communication Services
- ⚡ Clean, simple Streamlit UI

---

## 📸 Preview

![screenshot](screenshot.png) <!-- Optional: replace with your own screenshot -->

---

## 🧱 Tech Stack

- [Streamlit](https://streamlit.io/) – UI framework
- [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) – for generating replies
- [Azure Communication Services Email](https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/send-email) – for sending emails
- [python-dotenv](https://pypi.org/project/python-dotenv/) – to manage environment variables

---

## 🛠 Setup

### 1. Clone this repo

```bash
git clone https://github.com/your-username/ai-support-email-demo.git
cd ai-support-email-demo
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a .env file
```bash
OPENAI_API_KEY=your_azure_openai_key
OPENAI_ENDPOINT=https://your-openai-resource.openai.azure.com/
ACS_CONNECTION_STRING=endpoint=https://your-resource.communication.azure.com/;accesskey=your_key
ACS_SENDER_EMAIL=DoNotReply@your-resource.communication.azure.com
RECIPIENT_EMAIL=someone@example.com
```

### 4. Run the app
```bash
streamlit run app.py
```
### 5. Run Non-UI app

If you prefer to run via terminal and want a non-UI setup:

1. Navigate to your folder:
```bash
cd path/to/your/project
```
2. Activate your environment
```bash
source venv/bin/activate   # macOS/Linux
# or
.\venv\Scripts\activate     # Windows
```

3. Run the python file:
```bash
python nonUI.py
```

## 🧪 Example Flow

Follow these simple steps:

1. Type a customer query (e.g. “I forgot my password”)

2. Click **🧠 Generate Reply**

3. Edit the reply if needed

4. Click **📤 Send Email**

5. Done! Email gets delivered to the customer inbox


📄 License

MIT License. Free to use, modify, and share.

👨‍💻 Author

Made with ❤️ by [Farhan Hussain](https://www.schoolofmachinelearning.com)

