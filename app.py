import streamlit as st
import subprocess

bash_script = """
g++ -std=c++17  correct_solution.cpp -o correct_solution
g++ -std=c++17  incorrect_solution.cpp -o incorrect_solution
g++ -std=c++17  test_case_generator.cpp -o test_case_generator
if [ -f output.txt ]; then
    > output.txt  # Clear the file if it exists
fi

for((i=1; ; ++i));do
    ./test_case_generator $i >randomInput
    ./incorrect_solution <randomInput >  myOutput
    ./correct_solution <randomInput>  correctOutput
    diff -w myOutput correctOutput || break
    # echo "Passed test: " $i
    echo "Passed test: $i" >> output.txt
    cat randomInput >> output.txt
    cat myOutput >> output.txt

    # cat randomInput
    # cat myOutput

done

echo "\nWA on the following test:" >> output.txt
cat randomInput >> output.txt
echo "your ans is : " >> output.txt
cat myOutput >> output.txt
echo "correct ans is : " >> output.txt
cat correctOutput >> output.txt

"""

st.title("Differential Code Checker")
st.write("Upload your code files and see the test case where the incorrect_solution gives wrong output.")

incorrect_file = st.file_uploader("Upload file with incorrect code (cpp extension)", type=["cpp"])
correct_file = st.file_uploader("Upload file with correct code (cpp extension)", type=["cpp"])
generator_file = st.file_uploader("Upload file with code that generate test cases (cpp extension)", type=["cpp"])


def run_bash_script(script):
    output_file = "output.txt"
    with open(output_file, 'w') as f:
        completed_process = subprocess.run(['bash', '-c', script], stdout=f, stderr=subprocess.PIPE, text=True)
        if completed_process.returncode == 0:
            print("Bash script executed successfully")
        else:
            print("Error executing Bash script:", completed_process.stderr)




if st.button("Run Checker"):
    if incorrect_file and correct_file and generator_file:
        with open("incorrect_solution.cpp", "wb") as f:
            f.write(incorrect_file.read())
        with open("correct_solution.cpp", "wb") as f:
            f.write(correct_file.read())
        with open("test_case_generator.cpp", "wb") as f:
            f.write(generator_file.read())



        run_bash_script(bash_script)
        # output_file = "output.txt"
        # st.text(output_file)

        with open("output.txt", "r") as f:
            output = f.read()
            st.text(output)




