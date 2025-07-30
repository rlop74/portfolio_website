import streamlit as st

st.set_page_config(layout="wide")

# st.markdown('<h1 style="text-align: center">Home</h1>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 3], border=False)

with col1:
    st.image("images/profile_pic.png")
with col2:
    st.title("Hi, I am Russel!")
    content = """
        I'm an IT Team Lead with hands-on sysadmin experience in diverse environments, 
        now specializing in backend development and cloud automation. Skilled in Python 
        and Go for building APIs and data-driven applications, with experience using 
        Flask/Django, SQL, and RESTful design. Proficient in Docker, Terraform, and AWS 
        for deploying secure, scalable systems. Strong focus on writing clean, production-ready code 
        and integrating DevOps best practices. Actively transitioning into a Backend Engineer or DevOps/Cloud Engineer role.
        """
    st.write(content)

# col4, col5, col6 = st.columns(3, border=True)

content2 = """
Below you can find some of the apps I have built. Feel free to contact me!
"""

st.write(content2)