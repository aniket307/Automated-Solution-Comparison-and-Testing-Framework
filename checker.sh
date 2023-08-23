g++ -std=c++17  correct_solution.cpp -o correct_solution
g++ -std=c++17  incorrect_solution.cpp -o incorrect_solution
g++ -std=c++17  test_case_generator.cpp -o test_case_generator

for((i=1; ; ++i));do
    ./test_case_generator $i >randomInput
    ./incorrect_solution <randomInput >  myOutput
    ./correct_solution <randomInput>  correctOutput
    diff -w myOutput correctOutput || break
    echo "Passed test: " $i
    # cat randomInput
    # cat myOutput

done

echo -e "\nWA on the following test: "
cat randomInput
echo "your ans is : "
cat myOutput
echo "correct ans is: "
cat correctOutput