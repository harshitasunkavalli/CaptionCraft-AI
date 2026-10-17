import streamlit as st

st.set_page_config(page_title="CaptionCraft AI", page_icon="✨", layout="centered")

st.title("✨ CaptionCraft AI")
st.subheader("Your little AI-powered content studio 💗")
st.write("Create captions and hashtags for your next social media post!")

business = st.selectbox(
    "🏪 What is your business?",
    ["Boutique", "Home Bakery", "Jewellery", "Skincare", "Food", "Personal Blog", "Other"]
)

product = st.text_input("🛍️ Product or post topic", placeholder="e.g. Pink floral kurti")
language = st.selectbox("🌐 Choose language", ["English", "Telugu", "Telugu + English"])
tone = st.selectbox("🎭 Choose your vibe", ["Aesthetic", "Funny", "Professional", "Cute", "Trendy"])

if st.button("✨ Generate Caption", use_container_width=True):
    if not product.strip():
        st.warning("Please enter your product or post topic!")
    else:
        st.success("Your inputs are ready! AI integration is our next step.")
        st.write("Business:", business)
        st.write("Product:", product)
        st.write("Language:", language)
        st.write("Tone:", tone)

st.divider()
st.caption("Made with 💗 CaptionCraft AI")