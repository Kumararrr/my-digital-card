import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Kumar | Digital Business Card", page_icon="📇", layout="centered")

# 2. Profile Picture Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Using your new professional Fiverr profile photo
    profile_url = "https://fiverr-res.cloudinary.com/image/upload/f_auto,q_auto,t_profile_original/v1/attachments/profile/photo/832f05928f61405e3230674092928574-1739793134375/36b9e4a8-9d41-477c-9b16-5623490fd38e.jpg"
    st.image(profile_url, width=180)

# 3. Header Section
st.markdown("<h1 style='text-align: center;'>Kumar</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Python Developer & Freelancer</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Specializing in Web Apps, Automation, and Digital Solutions.</p>", unsafe_allow_html=True)

st.divider()

# 4. About Me Section
st.write("### 🚀 Services I Offer")
st.write("- **Python Development:** Building custom tools and interactive web apps.")
st.write("- **Web Apps with Streamlit:** Creating fast and efficient dashboard solutions.")
st.write("- **Process Automation:** Automating repetitive tasks to save your time.")
st.write("- **Data Management:** High-quality data entry and organization services.")

st.divider()

# 5. Contact & Social Section
st.write("### 📩 Get In Touch")
st.write("Have a project in mind or want to collaborate? Feel free to reach out!")

# Contact Buttons
col_a, col_b = st.columns(2)
with col_a:
    # Professional link to your Fiverr profile
    st.link_button("🌐 View Fiverr Profile", "https://www.fiverr.com/kumararrr") # Update with your exact Fiverr URL

with col_b:
    # Direct WhatsApp Contact
    whatsapp_no = "94743484903" 
    whatsapp_url = f"https://wa.me/{whatsapp_no}?text=Hi%20Kumar,%20I'm%20interested%20in%20your%20services!"
    st.link_button("💬 Message on WhatsApp", whatsapp_url)

# 6. Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2026 | Developed by Kumar")
st.sidebar.caption("Powered by Python & Streamlit")


