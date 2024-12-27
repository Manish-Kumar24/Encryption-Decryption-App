import streamlit as st
from cryptography.fernet import Fernet
import base64

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Page config
st.set_page_config(
    page_title="CrypticMessenger",
    page_icon="🔒",
    layout="centered"
)

# Title and description
st.title("🔒 CrypticMessenger")
st.markdown("Secure message encryption and decryption tool")

# Initialize session state for key
if 'key' not in st.session_state:
    st.session_state.key = None

# Sidebar with key management
with st.sidebar:
    st.header("Key Management")
    if st.button("Generate New Key"):
        st.session_state.key = generate_key()
        st.success("New key generated!")
    
    # Key input/display
    key_input = st.text_input(
        "Enter/Paste Key",
        value=st.session_state.key.decode() if st.session_state.key else "",
        type="password"
    )
    
    if key_input:
        try:
            # Handle both raw keys and base64 encoded keys
            if len(key_input) == 44:  # Standard Fernet key length when base64 encoded
                st.session_state.key = key_input.encode()
            else:
                st.session_state.key = base64.b64encode(key_input.encode())
        except Exception:
            st.error("Invalid key format")

# Main content
tab1, tab2 = st.tabs(["Encrypt", "Decrypt"])

with tab1:
    st.header("Encrypt Message")
    message_to_encrypt = st.text_area("Enter message to encrypt", height=100)
    
    if st.button("Encrypt", key="encrypt_button"):
        if not st.session_state.key:
            st.error("Please generate or enter a key first!")
        elif not message_to_encrypt:
            st.warning("Please enter a message to encrypt")
        else:
            try:
                encrypted_message = encrypt_message(st.session_state.key, message_to_encrypt)
                st.code(encrypted_message.decode(), language=None)
                st.success("Message encrypted successfully!")
            except Exception as e:
                st.error(f"Encryption failed: {str(e)}")

with tab2:
    st.header("Decrypt Message")
    encrypted_input = st.text_area("Enter encrypted message", height=100)
    
    if st.button("Decrypt", key="decrypt_button"):
        if not st.session_state.key:
            st.error("Please enter a key first!")
        elif not encrypted_input:
            st.warning("Please enter an encrypted message")
        else:
            try:
                decrypted_message = decrypt_message(st.session_state.key, encrypted_input.encode())
                st.text_area("Decrypted message:", value=decrypted_message, height=100)
                st.success("Message decrypted successfully!")
            except Exception as e:
                st.error("Decryption failed. Please check your key and encrypted message.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")