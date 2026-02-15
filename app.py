import streamlit as st

# Page Configuration
st.set_page_config(page_title="Kumar | Digital Business Card", page_icon="📇", layout="centered")

# Profile Picture (Using GitHub Profile Image)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://github.com/Kumararrr.png", width=150)

# Header Section
st.markdown("<h1 style='text-align: center;'>Kumar! 👋</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Python Developer & Freelancer</h3>", unsafe_allow_html=True)
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
col_a, col_b = st.columns(2)
with col_a:
    st.link_button("📧 Email Me", "mailto:your-email@example.com")

with col_b:
    whatsapp_no = "94743484903" 
    whatsapp_url = f"https://wa.me/{whatsapp_no}?text=Hi%20Kumar,%20I%20saw%20your%20digital%20card!"
    st.link_button("💬 WhatsApp Me", whatsapp_url)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Developed by Kumar")


