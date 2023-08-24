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
    echo "Passed test: " $i
    echo "Passed test: $i" >> output.txt
    cat randomInput >> output.txt
    cat myOutput >> output.txt

    # cat randomInput
    # cat myOutput

done

echo -e "\nWA on the following test: "
cat randomInput
echo "your ans is : "
cat myOutput
echo "correct ans is: "
cat correctOutput

echo "\nWA on the following test:" >> output.txt
cat randomInput >> output.txt
echo "your ans is : " >> output.txt
cat myOutput >> output.txt
echo "correct ans is : " >> output.txt
cat correctOutput >> output.txt