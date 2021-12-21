// Ejercicio 2
// https://cses.fi/problemset/task/1671/

#include <bits/stdc++.h>
using namespace std;

#define t_int long long 
#define MAX 100000

vector<pair<int, int>> graph[MAX];
t_int distaceList[MAX];
int numNodes;

void dijkstra(int start){
  using T = pair<t_int, int>;
  priority_queue<T, vector<T>, greater<T>> queuePriority;
  for (int i = 0; i < numNodes; i++)
    distaceList[i] = LLONG_MAX;
  distaceList[start] = 0;
  queuePriority.push({0, start});
  while (queuePriority.size()){
    t_int distance;
    int node;
    tie(distance, node) = queuePriority.top();
    queuePriority.pop();
    if (distance != distaceList[node])
      continue;
    for (pair<int, int> i: graph[node])
      if (distance + i.second < distaceList[i.first])
        queuePriority.push({distaceList[i.first] = distance + i.second, i.first});
  }
}

int main(){
  int m;
  cin >> numNodes >> m;
  for (int i = 0; i < m; i++){
    int a, b, c;
    cin >> a >> b >> c;
    graph[a - 1].push_back({b - 1, c});
  }
  dijkstra(0);
  for (int i = 0; i < numNodes; i++)
    cout << distaceList[i] << " ";
}