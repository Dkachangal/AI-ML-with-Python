#include <bits/stdc++.h>
using namespace std;

const int maxSize = 100001;
vector<int> tree[maxSize];
bool vis[maxSize];

void print(int node, int k) {
    std::queue<int> q;
    q.push(node);
    q.push(-1);
    // vis[node] = true;
    int level = 0;
    
    while (!q.empty()) {
        cout << "in loop" << endl;
        int curr = q.front();
        q.pop();
        
        if (curr == -1) {
            if (!q.empty()) q.push(-1);
            // level increase
            level++;
        } else if (q.front() == -1) {
            if (level + 1 == k) {
                cout << "H";
                for (int i: tree[curr]) cout << i << " ";
                break;
            }
        } else {
            for (int i: tree[curr]) {
                if (!vis[i]) q.push(i);
                vis[i] = true;
            }
        }
    }
}
int main() {
    int n, k;
    cin >> n >> k;
    
    for (int i=0; i<maxSize; i++) vis[i] = false;
    
    for (int i=1; i<n; i++) {
        int u, v;
        cin >> u >> v;
        
        tree[u].push_back(v);
        tree[v].push_back(u);
    }
    
    print(1, k);
    
    return 0;
}
