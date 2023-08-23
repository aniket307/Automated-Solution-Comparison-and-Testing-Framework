#include <bits/stdc++.h>
#include <sys/time.h>
using namespace std;

// #define int long long int
// int mod = 1e9 + 7;

int random_number_gererator(int a, int b)
{
  //  random_number_gererator is a function will will generate random number with in range a and b (inclusive)

  if (a > b)
  {
    swap(a, b);
  }

  return a + rand() % (b - a + 1);
}

int main(int argc, char *argv[])
{

  // code to ensure that a random number generated each time is unique and if you run the same code again then same test cases will generated
  ios::sync_with_stdio(0);
  cin.tie(0);
  int seed = atoi(argv[1]);
  srand(seed);

  // code to  print the test case as input

  // simple write the code to print the desired output which can be used as input to other file

  int n = random_number_gererator(2, 10);
  cout<<n<<endl;

  for (int i = 0; i < n; i++)
  {
    int x = random_number_gererator(-10, 10);
    cout << x << " ";
  }
  cout << endl;

  return 0;
}
