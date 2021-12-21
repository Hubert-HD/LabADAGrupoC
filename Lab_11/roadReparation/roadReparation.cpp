// Ejercicio 1
// https://cses.fi/problemset/task/1675

#include <bits/stdc++.h>
#define t_int long long
#define MAX 100005

using namespace std;

vector<array<t_int, 3>> graph;
t_int n, m;
bool visited[MAX];
t_int edge[MAX];

t_int find(t_int x) {
  if(edge[x] == x) return x;
  return edge[x] = find(edge[x]);
}

void addEdge(t_int x, t_int y) {
  t_int a = find(x);
  t_int b = find(y);
  if(a != b)
    edge[a] = b;
}

t_int prim() {
  for(t_int i = 0; i < n; i++) {
    edge[i] = i;
    visited[i] = false;
  }
  sort(graph.begin(), graph.end());
  t_int cost = 0;
  for(t_int i = 0; i < graph.size(); i++) {
    if(find(graph[i][1]) != find(graph[i][2])) {
      cost += graph[i][0];
      addEdge(graph[i][1], graph[i][2]);
    }
  }
  t_int count = 0;
  for(t_int i = 0; i < n; i++) {
    if(edge[i] == i)
      count++;
  }
  if(count > 1)
    return -1;
  return cost;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cin >> n >> m;
  for(t_int i = 0; i < m; i++) {
    t_int a, b, c;
    cin >> a >> b >> c;
    a--; b--;
    graph.push_back({c, a, b});
  }
  t_int res = prim();
  if(res == -1)
    cout << "IMPOSSIBLE" << endl;
  else cout << res << endl;
  return 0;
}
