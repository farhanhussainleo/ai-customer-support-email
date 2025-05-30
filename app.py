import os
from dotenv import load_dotenv

import streamlit as st
from openai import AzureOpenAI
from azure.communication.email import EmailClient

load_dotenv()

# clients
ai = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("OPENAI_ENDPOINT")
)
email_client = EmailClient.from_connection_string(os.getenv("ACS_CONNECTION_STRING"))

st.set_page_config(page_title="AI Support Email Demo")
st.title("🔔 AI-Powered Support Email Demo")

recipient = st.text_input("Recipient email", value=os.getenv("RECIPIENT_EMAIL"))
subject   = st.text_input("Email subject", value="RE: Your Support Request")
query     = st.text_area("Customer query", height=120)

# 1) GENERATE
if st.button("🧠 Generate Reply"):
    if not query.strip():
        st.error("Enter a customer query first.")
    else:
        with st.spinner("Generating…"):
            resp = ai.chat.completions.create(
                model=os.getenv("OPENAI_DEPLOYMENT_ID", "gpt-4o-mini"),
                messages=[
                    # tighten the prompt so it only returns the email
                    {"role":"system","content":
                     "You are a support agent. Respond **only** with the email body (no intro like “Sure…”)."},
                    {"role":"user","content": query}
                ]
            )
            st.session_state["draft"] = resp.choices[0].message.content

# 2) PREVIEW & EDIT
if "draft" in st.session_state:
    st.markdown("**✏️ Edit your email before sending:**")
    st.session_state["edited"] = st.text_area(
        "Email body", 
        value=st.session_state["draft"], 
        height=300
    )

    # 3) SEND
    if st.button("📤 Send Email"):
        msg = {
            "senderAddress": os.getenv("ACS_SENDER_EMAIL"),
            "content": {
                "subject": subject,
                "plainText": st.session_state["edited"]
            },
            "recipients": {"to":[{"address": recipient}]}
        }
        with st.spinner("Sending…"):
            poller = email_client.begin_send(msg)
            result = poller.result()
        st.success(f"Email sent! ID: {result['id']}")
        st.write("Status:", result.get("status"))
