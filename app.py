import streamlit as st
from csp_solver import check_constraints, solve_csp

st.set_page_config(
    page_title="The Mystery of Room 404",
    page_icon="🕵️",
    layout="wide"
)

# -------------------- DESIGN --------------------

st.markdown("""
<style>
.stApp {
    background-color: #0b0d12;
    color: white;
}

.block-container {
    max-width: 1100px;
    padding-top: 40px;
}

.hero {
    padding: 35px;
    border-radius: 20px;
    background-color: #151923;
    border: 1px solid #303642;
    margin-bottom: 30px;
}

.case-number {
    font-size: 13px;
    letter-spacing: 3px;
    color: #9ca3af;
}

.hero-title {
    font-size: 55px;
    font-weight: 800;
    line-height: 1.05;
    margin-top: 15px;
}

.hero-subtitle {
    font-size: 17px;
    color: #aeb4c0;
    margin-top: 15px;
}

.card {
    padding: 22px;
    border-radius: 16px;
    background-color: #151923;
    border: 1px solid #303642;
    margin-bottom: 15px;
    min-height: 120px;
}

.card-title {
    font-size: 20px;
    font-weight: 700;
}

.card-text {
    color: #aeb4c0;
    line-height: 1.6;
    margin-top: 8px;
}

.clue {
    padding: 17px;
    margin: 10px 0;
    border-radius: 12px;
    background-color: #151923;
    border-left: 4px solid #7c83ff;
}

.clue-number {
    font-size: 11px;
    letter-spacing: 2px;
    color: #8f96a3;
}

.clue-text {
    margin-top: 6px;
    font-size: 15px;
}

.investigation {
    padding: 25px;
    border-radius: 18px;
    background-color: #151923;
    border: 1px solid #303642;
}

.result-card {
    padding: 30px;
    border-radius: 18px;
    background-color: #151923;
    border: 1px solid #3d7a52;
    margin-top: 25px;
}

.result-title {
    font-size: 30px;
    font-weight: 800;
}

.footer {
    text-align: center;
    color: #666d79;
    margin-top: 50px;
    font-size: 11px;
    letter-spacing: 2px;
}
</style>
""", unsafe_allow_html=True)


# -------------------- HERO --------------------

st.markdown("""
<div class="hero">

<div class="case-number">
CASE FILE // 404 // CLASSIFIED
</div>

<div class="hero-title">
THE MYSTERY<br>OF ROOM 404
</div>

<div class="hero-subtitle">
A Constraint Satisfaction Detective Investigation
</div>

</div>
""", unsafe_allow_html=True)


# -------------------- CASE STATUS --------------------

st.info(
    "🔴 CASE ACTIVE   |   4 SUSPECTS   |   4 LOCATIONS   |   5 CLUES"
)


# -------------------- CASE BRIEF --------------------

st.markdown("## 📁 Case Brief")

st.markdown("""
<div class="card">

<div class="card-title">
The Missing Artifact
</div>

<div class="card-text">
During a college event, a valuable item mysteriously disappeared.
Four students were present at the event, and each student was in
a different location when the incident occurred.

Your mission is to reconstruct their locations using the evidence.
</div>

</div>
""", unsafe_allow_html=True)


# -------------------- SUSPECTS --------------------

st.markdown("## 👥 Suspect Profiles")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <div class="card-title">👩 Shreemayee</div>
    <div class="card-text">
    💻 Connected to the Computer Lab<br>
    Status: Person of interest
    </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <div class="card-title">🤖 Pritheeka</div>
    <div class="card-text">
    ⚙️ Robotics Club Member<br>
    Status: Person of interest
    </div>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="card">
    <div class="card-title">🙋 Shabnam</div>
    <div class="card-text">
    📋 Student Volunteer<br>
    Status: Person of interest
    </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
    <div class="card-title">💃 Saloni</div>
    <div class="card-text">
    🎭 Dance Club Member<br>
    Status: Person of interest
    </div>
    </div>
    """, unsafe_allow_html=True)


# -------------------- LOCATIONS --------------------

st.markdown("## 📍 Possible Locations")

loc1, loc2, loc3, loc4 = st.columns(4)

with loc1:
    st.markdown("### 📚")
    st.write("**Library**")

with loc2:
    st.markdown("### 💻")
    st.write("**Computer Lab**")

with loc3:
    st.markdown("### ☕")
    st.write("**Cafeteria**")

with loc4:
    st.markdown("### 🎭")
    st.write("**Auditorium**")


# -------------------- CLUES --------------------

st.markdown("## 🔎 Evidence Log")

clues = [
    ("EVIDENCE 01", "Shreemayee was in the Computer Lab."),
    ("EVIDENCE 02", "Pritheeka was not in the Cafeteria."),
    ("EVIDENCE 03", "Shabnam was not in the Library."),
    ("EVIDENCE 04", "Saloni was not in the Auditorium."),
    ("EVIDENCE 05", "Each student was in a different location.")
]

for number, clue in clues:
    st.markdown(
        f"""
        <div class="clue">
        <div class="clue-number">{number}</div>
        <div class="clue-text">{clue}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# -------------------- INVESTIGATION --------------------

st.markdown("## 🧠 Investigation Console")

st.markdown("""
<div class="investigation">

<b>Detective Instructions</b><br><br>

Assign one location to each student.
Remember: every student must have a different location.

</div>
""", unsafe_allow_html=True)

locations = [
    "Library",
    "Computer Lab",
    "Cafeteria",
    "Auditorium"
]

col1, col2 = st.columns(2)

with col1:
    shreemayee = st.selectbox(
        "👩 Shreemayee's Location",
        locations
    )

    shabnam = st.selectbox(
        "🙋 Shabnam's Location",
        locations
    )

with col2:
    pritheeka = st.selectbox(
        "🤖 Pritheeka's Location",
        locations
    )

    saloni = st.selectbox(
        "💃 Saloni's Location",
        locations
    )


# -------------------- SOLVE --------------------

st.write("")

if st.button(
    "🔍 SUBMIT INVESTIGATION",
    use_container_width=True
):

    assignment = {
        "Shreemayee": shreemayee,
        "Pritheeka": pritheeka,
        "Shabnam": shabnam,
        "Saloni": saloni
    }

    solution = solve_csp()

    if check_constraints(assignment):

        st.balloons()

        st.markdown("""
        <div class="result-card">

        <div class="result-title">
        🎉 CASE SOLVED
        </div>

        <div class="card-text">
        Detective work successful!
        Your reconstruction satisfies all the constraints.
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🔐 Final Reconstruction")

        for student, location in assignment.items():
            st.write(
                f"👤 **{student}**  →  📍 **{location}**"
            )

        st.success(
            "The mystery was solved using Constraint Satisfaction and Backtracking."
        )

    else:

        st.error("❌ CASE UNSOLVED")

        st.write(
            "Your current reconstruction violates one or more clues."
        )

        st.info(
            "🔎 Re-read the evidence and try another combination."
        )


# -------------------- CSP EXPLANATION --------------------

st.divider()

with st.expander("🧩 How does the CSP Engine work?"):

    st.write("""
    **Variables:** The four students.

    **Domains:** Library, Computer Lab, Cafeteria and Auditorium.

    **Constraints:** The five clues in the case.

    **Backtracking:** The solver tries possible assignments and
    goes back whenever an assignment violates a constraint.

    This means the game uses an actual Constraint Satisfaction
    Problem rather than simply checking a hard-coded answer.
    """)


# -------------------- FOOTER --------------------

st.markdown("""
<div class="footer">
CASE 404 // CONSTRAINT SATISFACTION INVESTIGATION // END OF FILE
</div>
""", unsafe_allow_html=True)