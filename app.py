import streamlit as st
from langchain_google_community import GmailToolkit
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
import re
from langgraph.prebuilt import create_react_agent
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
import bleach
from login import login_page

st.set_page_config(page_icon="📨", page_title="Email Sender Agent")

import webbrowser    
url='https://www.google.com'
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
webbrowser.get('chrome').open_new_tab(url)

# Check if the user is logged in (using session state)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# If the user is not logged in, show the login page
if not st.session_state.logged_in:
    login = login_page()
    if login is not None:
        if login:  # Successful login
            st.session_state.logged_in = True
            st.rerun()  # Rerun the app to show the main app
        else:  # Failed login
            st.error("Invalid credentials. Please try again.")
else:
    # If the user is logged in, proceed with the app logic
    load_dotenv()
    API_KEY = os.getenv("GROQ_API_KEY")

    if not API_KEY:
        st.error("GROQ API key is missing! Please set it in the .env file.")
    else:
        # Initialize the language model and toolkit
        llm = ChatGroq(model="Gemma2-9b-It")
        toolkit = GmailToolkit()
        tools = toolkit.get_tools()

        # Define the prompt template
        prompt = """ 
        You are a master email writer. Write a clear, formal, and well-structured email with the following details:
        Description: {email_description}

        The email should:
        1.  Have a suitable subject line based on the description.
        2.  Include a polite and clear body that aligns with the description provided.
        3.  Be professional, polite, and concise.
        4.  Ensure proper line breaks, one blank line between sections (greeting, body, closing).
        5.  Reflect the tone and style of a polished, professional email.
        6.  generate only greeting, email body and signature. don't generate subject.
        """

        # Set up the prompt template
        prompt_temp = ChatPromptTemplate.from_messages(
            [("system", prompt), ("human", "{email_description}")]
        )

        # Chain setup
        chain = prompt_temp | llm | StrOutputParser()

        # Streamlit interface
        st.title("AI Agent - Email Sender 📨")

        # Email Validation Function
        def is_valid_email(email):
            """Checks if the email is in a valid format."""
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            return re.match(pattern, email) is not None

        st.write("##### Recipient Email Address")
        recipient_email = st.text_input(
            "None", key="recipient_email", label_visibility="collapsed"
        )
        st.write("##### Email Description (Details of the email)")
        email_description = st.text_area(
            "None", key="email_description", label_visibility="collapsed"
        )

        # Initialize session state variables
        if "generated_email" not in st.session_state:
            st.session_state.generated_email = ""

        if "email_option" not in st.session_state:
            st.session_state.email_option = None

        if "email_sent" not in st.session_state:
            st.session_state.email_sent = False

        if "edit_mode" not in st.session_state:
            st.session_state.edit_mode = False

        if st.button("Generate"):
            st.session_state.email_option = None
            st.session_state.email_sent = False
            st.session_state.edit_mode = False 

            if email_description and recipient_email:
                if not is_valid_email(recipient_email):
                    st.error("Invalid recipient email format.")
                else:
                    with st.spinner("Generating email..."):
                        generated_email = chain.invoke(email_description)
                        st.session_state.generated_email = generated_email
                    st.markdown("##### Generated email:")
                    st.write(generated_email)

            else:
                st.warning("Please provide a description for the email or recipient email address.")

        if st.session_state.generated_email and not st.session_state.edit_mode:
            st.write("##### Select one option:")
            radio_btn = st.radio(
                "None",
                ["Edit Email", "Send Email"],
                index=None,
                horizontal=True,
                label_visibility="collapsed",
            )

            if radio_btn == "Edit Email":
                st.session_state.edit_mode = True
                st.rerun()

            elif radio_btn == "Send Email":
                if not is_valid_email(recipient_email):
                    st.error("Invalid recipient email format.")
                else:
                    with st.spinner("Sending email..."):
                        agent_executor = create_react_agent(llm, tools)
                        paragraphs = st.session_state.generated_email.split("\n\n")
                        html_paragraphs = []
                        for p in paragraphs:
                            html_paragraphs.append(
                                "<p>" + p.replace("\n", "<br>") + "</p>"
                            )
                        html_email_body = "".join(html_paragraphs)
                        sanitized_html = bleach.clean(
                            html_email_body, tags=["p", "br"], attributes={}
                        )
                        example_query = f"Send this email: {sanitized_html} to {recipient_email}. One thing to keep in mind, don't save it as a draft in my account. Send it directly. And add an appropriate subject."
                        response = agent_executor.invoke(
                            {"messages": [("user", example_query)]}
                        )
                        st.session_state.email_option = "Send"
                        st.session_state.generated_email = None
                        st.session_state.email_sent = True
                        st.session_state.edit_mode = False  # Ensure edit mode is reset
                        st.rerun()  # Refresh the app after sending

        if st.session_state.edit_mode:
            st.write("###### Edit Generated Email")
            edited_email = st.text_area(
                "None",
                value=st.session_state.generated_email,
                height=300,
                label_visibility="collapsed",
            )
            st.session_state.generated_email = edited_email

            if st.button("Send"):
                if not is_valid_email(recipient_email):
                    st.error("Invalid recipient email format.")
                else:
                    with st.spinner("Sending email..."):
                        agent_executor = create_react_agent(llm, tools)
                        paragraphs = st.session_state.generated_email.split("\n\n")
                        html_paragraphs = []
                        for p in paragraphs:
                            html_paragraphs.append(
                                "<p>" + p.replace("\n", "<br>") + "</p>"
                            )
                        html_email_body = "".join(html_paragraphs)
                        sanitized_html = bleach.clean(
                            html_email_body, tags=["p", "br"], attributes={}
                        )
                        example_query = (
                            f"Send this email: {sanitized_html} to {recipient_email}."
                        )
                        response = agent_executor.invoke(
                            {"messages": [("user", example_query)]}
                        )
                        st.session_state.email_option = "Send"
                        st.session_state.generated_email = None
                        st.session_state.email_sent = True
                        st.session_state.edit_mode = False  # Ensure edit mode is reset
                        st.rerun()  # Refresh the app after sending

        if st.session_state.email_sent:
            st.success("Email sent successfully!")
