import streamlit as st

DIFY_URL = "https://udify.app/chat/EbRtbiXuqvvp6EyI"

st.set_page_config(page_title="Syllabus Sakhi AI", page_icon="📘", layout="wide")

st.title("Syllabus Sakhi AI 📘")
st.caption("Bilingual syllabus explorer for Indian competitive exams (Telugu & English)")

# Helpful link button
st.link_button("Open App in New Tab", DIFY_URL, use_container_width=False)

st.info("If the embed doesn’t load, use the button above to open the app in a new tab.")

# Embed the Dify app
st.components.v1.iframe(src=DIFY_URL, height=840, scrolling=True)

with st.expander("About"):
    st.markdown(
        """
        Syllabus Sakhi AI lets you explore syllabi for UPSC, SSC, RRB, TSPSC, APPSC and more — in Telugu or English.\n
        Developed by Kondabathini Manipoojith\n
        This page simply **embeds** the working Dify app.
        """
    )
with st.expander("📝 Feedback"):
    st.markdown("We'd love to hear your thoughts about Syllabus Sakhi AI! Please fill out the form below:")
    st.link_button("Give Feedback / అభిప్రాయం ఇవ్వండి", "https://forms.gle/7EmcNy1c6u3GMLww7")



with st.expander("Disclaimer"):
    st.markdown(
        """
        **English:** Syllabus Sakhi AI shares syllabus info for reference only. We do not guarantee accuracy or updates.
        Please verify details on official exam websites. We are not affiliated with any exam authority.

        **Telugu:** సిలబస్ సఖి AI కేవలం సూచన కోసం మాత్రమే సిలబస్ సమాచారాన్ని అందిస్తుంది.
        మేము ఖచ్చితత్వం లేదా నవీకరణలకు హామీ ఇవ్వము. దయచేసి అధికారిక పరీక్ష వెబ్‌సైట్‌లలో వివరాలను ధృవీకరించండి.
        """
    )
