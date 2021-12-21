// Ejercicio 4
// https://cses.fi/problemset/submit/1680/

#include <bits/stdc++.h>
#define t_int long long
#define SIZE 100005
using namespace std;

t_int n, m;
t_int list[SIZE] = {-1};
vector<t_int> graph[SIZE];
bool visited[SIZE];

void depthFirstSearch(t_int raiz, vector<t_int>& ruta) {
  visited[raiz] = true;
  for(t_int i = 0; i < graph[raiz].size(); i++)
    if(!visited[graph[raiz][i]])
        depthFirstSearch(graph[raiz][i], ruta);
  ruta.push_back(raiz);
}

void imprimir(t_int raiz) {
  if(raiz == -1) return;
  imprimir(list[raiz]);
  cout << raiz + 1 << " ";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  vector<t_int> vertex;
  t_int x, y;
  cin >> n >> m;
  for(t_int i = 0; i < m; i++) {
    cin >> x >> y;
    graph[x - 1].push_back(y - 1);
  }
  memset(visited, false, sizeof(visited));
  depthFirstSearch(0, vertex);
  if(!visited[n - 1]) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  reverse(vertex.begin(), vertex.end());
  t_int dist[n];
  for(t_int i = 0; i < n; i++) {
    dist[i] = 1;
  }
  for(t_int i = 0; i < vertex.size(); i++)
    for(t_int j = 0; j < graph[vertex[i]].size(); j++) {
      if (dist[graph[vertex[i]][j]] < dist[vertex[i]] + 1)
        dist[graph[vertex[i]][j]] = dist[vertex[i]] + 1;
        list[graph[vertex[i]][j]] = vertex[i];
      }
  cout << dist[n - 1] << endl;
  imprimir(n - 1);
  return 0;
}