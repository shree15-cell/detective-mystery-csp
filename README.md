# 🕵️ The Mystery of Room 404

## Constraint Satisfaction Problem Detective Game

### 📌 Project Overview

The Mystery of Room 404 is an interactive detective mystery game developed using Python and Streamlit.

The player acts as a detective and must determine the locations of four students using a set of clues.

The game is designed as a **Constraint Satisfaction Problem (CSP)** and uses **backtracking** to find valid solutions.

---

## 🎮 Game Objective

Four students were present during a college event:

- Shreemayee
- Pritheeka
- Shabnam
- Saloni

They were each in a different location.

The player must use the clues to determine where each student was.

---

## 🧩 CSP Formulation

### Variables

The four students are the CSP variables:

- Shreemayee
- Pritheeka
- Shabnam
- Saloni

### Domains

Each student can be assigned one of these locations:

- Library
- Computer Lab
- Cafeteria
- Auditorium

### Constraints

The game contains the following constraints:

1. Shreemaayee was in the Computer Lab.
2. Pritheeka was not in the Cafeteria.
3. Shabnam was not in the Library.
4. Saloni was not in the Auditorium.
5. Every student must have a different location.

---

## 🧠 Algorithm

The game uses a **backtracking algorithm**.

The solver:

1. Selects a student.
2. Tries a possible location.
3. Checks the constraints.
4. Continues if the assignment is valid.
5. Goes back and tries another location if a constraint is violated.
6. Continues until a valid solution is found.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Constraint Satisfaction Problem (CSP)
- Backtracking Algorithm
- Visual Studio Code
- GitHub

---

## 📁 Project Structure

```text
Detective Mystery-CSP/
│
├── app.py
├── csp_solver.py
├── requirements.txt
└── README.md