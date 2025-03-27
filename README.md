# Email Sender Agent 📨

A Streamlit web application powered by AI for generating and sending emails. This app allows users to input an email description, generate an email, and then edit or send the email directly from the interface. The emails are sent using the **Google Cloud Gmail API**.

## Features

- **Generate Emails**: Create professional, well-structured emails based on a provided description.
- **Email Editing**: Users can edit the generated email before sending it.
- **Send Emails**: The app can send emails directly to the recipient using **Google Cloud Gmail API**.
- **Login Page**: Requires login for security purposes before using the email sending feature.
- **Customizable Email Content**: You can edit the subject, body, and recipient details before sending.

## Requirements

- Python 3.8+
- Streamlit
- langchain
- langchain_google_community
- langchain_groq
- langgraph
- bleach
- dotenv
- Google API (Gmail integration)
- **Google Cloud API `config.json` file** for Gmail API integration
- **OAuth 2.0 credentials** for Gmail API access

## Usage

- **Login**: Once logged in, you will be redirected to the main interface.
- **Generate Email**: Enter the recipient's email and a description of your email. Click "Generate" to create the email.
- **Edit Email**: After generating the email, you can edit the content.
- **Send Email**: Once satisfied with the email, click "Send Email" to send the email directly from your Gmail account.




