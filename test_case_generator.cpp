#include <bits/stdc++.h>
#include <sys/time.h>
using namespace std;

// #define int long long int
// int mod = 1e9 + 7;

int random_number_gererator(int a, int b)
{

  if (a > b)
  {
    swap(a, b);
  }

  return a + rand() % (b - a + 1);
}

int main(int argc, char *argv[])
{

  // code to ensure that random number each time is different
  ios::sync_with_stdio(0);
  cin.tie(0);
  // srand(time(0));
  // timeval t1;
  // gettimeofday(&t1, NULL);
  // srand(t1.tv_usec * t1.tv_sec);

  int seed = atoi(argv[1]);
  srand(seed);



  // code to  print the test case input










  int n=random_number_gererator(2,10002);
  int m=random_number_gererator(2,n);

  cout<<n<<endl;

  // for(int i=0;i<n;i++){
  //   int x=random_number_gererator(-10,10);
  //   cout<<x<<" ";
  // }
  // cout<<endl;

  return 0;
}
