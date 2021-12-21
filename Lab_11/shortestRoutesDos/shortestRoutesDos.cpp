// Ejercicio 3
// https://cses.fi/problemset/submit/1672/

#include<iostream>
#include <bits/stdc++.h>
#define t_int long long
#define MAX 500

using namespace std;

t_int arr[MAX][MAX];
int n, m, q;

int main() {
  cin >> n >> m >> q;
  memset(arr, 0x3f, sizeof(arr));
  for(int i = 0; i < m; i++){
    t_int a, b, c;
    cin >> a >> b >> c;
    a = a - 1;
    b = b - 1;
    arr[a][b] = min(arr[a][b], c);
    arr[b][a] = min(arr[b][a], c);
  }
  for(int i = 0; i < n ; i++)
    arr[i][i] = 0;
  for(int k = 0; k < n; k++)
    for(int i = 0; i < n; i++)
      for(int j = 0; j < n; j++)
        arr[i][j] = min(arr[i][j], (arr[i][k] + arr[k][j]));
  for(int i = 0; i < q ; i++){
    int a , b;
    cin >> a >> b;
    a = a - 1;
    b = b - 1;
    if(arr[a][b] >= 1e18)
      cout << -1<<endl;
    else
      cout << arr[a][b]<<endl;
  }
  return 0;
}