# Email Sender Agent 📨

A Streamlit web application powered by AI for generating and sending emails. This app allows users to input an email description, generate an email, and then edit or send the email directly from the interface.

## Features

- **Generate Emails**: Create professional, well-structured emails based on a provided description.
- **Email Editing**: Users can edit the generated email before sending it.
- **Send Emails**: The app can send emails directly to the recipient using Gmail integration.
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
- Environment variables for API keys

## Setup Instructions

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/email-sender-agent.git
    cd email-sender-agent
    ```

2. Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your required API keys:

    ```
    GROQ_API_KEY=your_groq_api_key
    ```

5. Run the application:

    ```bash
    streamlit run app.py
    ```

6. The app will start, and you can open it in your web browser.

## Usage

- **Login**: Once logged in, you will be redirected to the main interface.
- **Generate Email**: Enter the recipient's email and a description of your email. Click "Generate" to create the email.
- **Edit Email**: After generating the email, you can edit the content.
- **Send Email**: Once satisfied with the email, click "Send Email" to send the email directly from your Gmail account.

### Email Validation

The app validates the recipient's email format using a regular expression to ensure it's a valid email address before proceeding with sending the email.

### Email Format

The generated email includes:
1. A professional and formal greeting.
2. A clear, concise body based on the provided description.
3. A polite closing and signature.

The email will be sanitized for security using the `bleach` library to remove any unwanted HTML tags or attributes.

## Deployment

To deploy this app, you can use platforms like [Streamlit Sharing](https://streamlit.io/sharing) or [Heroku](https://www.heroku.com/).

1. **For Streamlit Sharing**:
    - Push your code to a GitHub repository.
    - Link the repository on [Streamlit Sharing](https://streamlit.io/sharing) and deploy.
    
2. **For Heroku**:
    - Create a `Procfile` in the root directory with the following content:
    
      ```bash
      web: streamlit run app.py
      ```
    - Push your code to Heroku by following [Heroku deployment guide](https://devcenter.heroku.com/articles/git).

## Troubleshooting

- **Missing API key**: Make sure the `.env` file contains the correct API keys (GROQ API key).
- **Invalid Email**: Ensure that the email addresses entered are in the correct format.
- **App Not Running**: Double-check that all dependencies are installed and the environment variables are set correctly.

## Contributing

Feel free to fork this repository and submit pull requests for bug fixes, improvements, or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
