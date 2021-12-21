// Ejercicio 4
// https://cses.fi/problemset/task/1744/

#include <bits/stdc++.h>
#define dbgv(v) cout<<'>'<< #v <<':'; for(auto ii:v)cout<<ii<<' ';cout<<endl;
#define dbg(x) cout<<'>'<< #x <<':'<< x <<endl;
using namespace std;
#define int long long

void run_case(){
	int a, b;
	cin >> a >> b;
	vector<vector<int>> dp(a + 1,vector<int>(b + 1,0));
	for(int i=1;i<=a;i++){
		for(int j=1;j<=b;j++){
			if(i==j){
				dp[i][j]=0;
				continue;
			}
			int mini = LLONG_MAX;
			for(int k = 1; k < i; k++)
				mini = min(mini,dp[k][j]+dp[i-k][j]);
			for(int l = 1; l < j; l++)
				mini = min(mini,dp[i][l]+dp[i][j-l]);
			dp[i][j] = 1 + mini;
		}
	}
	cout << dp[a][b];
}

signed main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int tc=1;
	while(tc--)
		run_case();
	return 0;
}