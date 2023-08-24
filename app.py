import streamlit as st
import subprocess

st.title("Differential Code Checker")
st.write("Upload your code files and see the test case where the incorrect_solution gives wrong output.")

incorrect_file = st.file_uploader("Upload file with incorrect code (cpp extension)", type=["cpp"])
correct_file = st.file_uploader("Upload file with correct code (cpp extension)", type=["cpp"])
generator_file = st.file_uploader("Upload file with code that generate test cases (cpp extension)", type=["cpp"])

if st.button("Run Checker"):
    if incorrect_file and correct_file and generator_file:
        with open("incorrect_solution.cpp", "wb") as f:
            f.write(incorrect_file.read())
        with open("correct_solution.cpp", "wb") as f:
            f.write(correct_file.read())
        with open("test_case_generator.cpp", "wb") as f:
            f.write(generator_file.read())

        subprocess.run("chmod +x checker.sh", shell=True)  # Ensure script is executable
        subprocess.run("./checker.sh", shell=True)

        with open("output.txt", "r") as f:
            output = f.read()
            st.text(output)
            st.write("help help")
