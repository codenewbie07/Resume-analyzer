import streamlit as st

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("Smart Resume Analyzer")
st.caption("Analyze your resume based on your target role")

tab1, tab2 = st.tabs(["Resume", "Target Role"])

job_roles = {
    "Data Scientist": ["python", "machine learning", "pandas", "numpy", "statistics", "data analysis"],
    "Data Analyst": ["excel", "sql", "python", "power bi", "data visualization"],
    "Web Developer": ["html", "css", "javascript", "react", "node"],
    "Android Developer": ["java", "kotlin", "android"],
    "Software Engineer": ["c++", "java", "python", "algorithms", "data structures"]
}

# TAB 1
with tab1:
    resume = st.text_area("Paste Your Resume", height=200)

# TAB 2
with tab2:
    selected_role = st.selectbox("Select Target Role", list(job_roles.keys()))

def extract_skills(text):
    text = text.lower()
    skills = []
    keywords = [
        "python","machine learning","sql","excel","power bi",
        "html","css","javascript","react","node",
        "java","kotlin","android","c++","data structures",
        "algorithms","pandas","numpy","statistics","data analysis"
    ]
    for word in keywords:
        if word in text:
            skills.append(word)
    return skills

if st.button("Analyze Resume"):

    st.markdown("---")

    user_skills = extract_skills(resume)

    st.subheader("Target Role")
    st.write(selected_role)

    required_skills = job_roles[selected_role]

    matched = list(set(user_skills) & set(required_skills))
    missing = list(set(required_skills) - set(user_skills))

    score = len(matched) / len(required_skills)

    st.subheader("Match Score")
    st.progress(int(score * 100))
    st.write(f"{round(score*100,2)}% match")

    st.markdown("---")

    st.subheader("Detected Skills")
    if user_skills:
        st.write(", ".join(user_skills))
    else:
        st.write("No major skills detected")

    st.markdown("---")

    st.subheader("Skill Analysis")

    st.write("Matched Skills:")
    if matched:
        for m in matched:
            st.write(f"-> {m}")
    else:
        st.write("None")

    st.write("Missing Skills:")
    if missing:
        for m in missing:
            st.write(f"-> {m}")
    else:
        st.write("None")

    if missing:
        st.markdown("---")
        st.subheader("Suggestions to Improve")

        skills_text = ", ".join(missing[:5])
        st.write(f"-> Add skills: {skills_text}")
    else:
        st.success("Your resume is well aligned with this role")