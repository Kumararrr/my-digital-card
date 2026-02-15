import streamlit as st

# Page Configuration
st.set_page_config(page_title="Kumar | Digital Business Card", page_icon="📇", layout="centered")

# Header Section
st.title("Hello, I'm Kumar! 👋")
st.subheader("Python Developer & Freelancer")
st.write("I specialize in building interactive web applications and automating tasks using Python.")

st.divider()

# About Me Section
st.write("### 🚀 What I Do")
st.write("- **Web Development:** Creating functional web apps with Streamlit.")
st.write("- **Automation:** Writing Python scripts to simplify repetitive tasks.")
st.write("- **Data Entry:** Providing accurate and efficient data management services.")

st.divider()

# Contact Section
st.write("### 📩 Let's Connect")
st.write("If you have a project or just want to say hi, feel free to reach out!")

# Contact Buttons
col1, col2 = st.columns(2)
with col1:
    if st.button('📧 Email Me'):
        st.info("You can reach me at: your-email@example.com") # ඔයාගේ email එක මෙතනට දාන්න

with col2:
    if st.button('💬 WhatsApp Me'):
        st.success("Connecting to WhatsApp...")
        st.balloons()

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Developed by Kumar")
