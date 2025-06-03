#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.communication.email import EmailClient

def main():
    # Load environment variables from .env
    load_dotenv()

    # === Azure OpenAI Setup ===
    ai_client = AzureOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        api_version="2024-12-01-preview",
        azure_endpoint=os.getenv("OPENAI_ENDPOINT")
    )
    deployment_id = os.getenv("OPENAI_DEPLOYMENT_ID", "gpt-4o-mini")

    # Simulated customer query
    customer_query = "Hi, I forgot my password. Can you help me reset it?"

    # Generate AI response
    response = ai_client.chat.completions.create(
        model=deployment_id,
        messages=[
            {"role": "system", "content": "You are a helpful and friendly customer support agent."},
            {"role": "user", "content": customer_query}
        ]
    )
    ai_reply = response.choices[0].message.content
    print("\n🧠 AI-generated reply:\n")
    print(ai_reply)

    # === Azure Communication Services Email Sending ===
    acs_connection_string = os.getenv("ACS_CONNECTION_STRING")
    acs_sender_email      = os.getenv("ACS_SENDER_EMAIL")
    recipient_email       = os.getenv("RECIPIENT_EMAIL", "test@example.com")

    email_client = EmailClient.from_connection_string(acs_connection_string)

    # Build the message as a dict (model-less SDK)
    message = {
        "senderAddress": acs_sender_email,
        "content": {
            "subject": "RE: Your Support Request",
            "plainText": ai_reply
        },
        "recipients": {
            "to": [{"address": recipient_email}]
        }
    }

    print("\n📤 Sending email...")
    poller = email_client.begin_send(message)
    result = poller.result()
    print("✅ Email sent! Message ID:", result["id"])
    print("   Delivery status:", result.get("status"))

if __name__ == "__main__":
    main()
