#include<bits/stdc++.h>
using namespace std;

class Graph{
    public:
    void printgraph(vector<vector<int>>graph){
        for(int i=1;i<graph.size();i++){
            cout<<i<<": ";
            for(int j=0;j<graph[0].size();j++){
                if(graph[i][j]==1){
                    cout<< j<<" ";
                }
            }
            cout<<endl;
        }
    }

    void printgraph(unordered_map<int,vector<int>>& list){
        for(auto &it : list){
            cout << it.first << ": ";

            for(auto &neighbor : it.second){
                cout << neighbor << " ";
            }

            cout << endl;
        }
    }

    void bfs(unordered_map<int,vector<int>>& list, int source, int n){
        vector<int>visited(n+1,0);
        queue<int>q;
        q.push(source);
        visited[source]=1;

        while(!q.empty()){
            int node=q.front();
            q.pop();
            cout<<node<<" ";
            for(int i=0;i<list[node].size();i++){
                int nei=list[node][i];
                if(!visited[nei]){
                    q.push(nei);
                    visited[nei]=1;
                }
            }
        }
    }

    void dfs(int source, unordered_map<int,vector<int>>list, vector<int>&visited){
        visited[source]=1;
        cout<<source<<" ";
        for(int i=0;i<list[source].size();i++){
            int nei=list[source][i];
            if(!visited[nei]){
                dfs(nei,list,visited);
            }
        }
    }
};
int main(){
    vector<vector<int>> edgeList = {{1, 2}, {1, 3}, {1, 4}, {4, 5}, {2, 5}, {3, 6}, {5, 6}, {5, 7}};
    int n=7;
    vector<vector<int>>graph(n+1,vector<int>(n+1,0));
    for(int i=0;i<edgeList.size();i++){
        int u=edgeList[i][0];
        int v=edgeList[i][1];

        graph[u][v]=1;
        graph[v][u]=1;
    }

    unordered_map<int,vector<int>>list;
    for(int i=0;i<edgeList.size();i++){
        int u=edgeList[i][0];
        int v=edgeList[i][1];

        list[u].push_back(v);
        list[v].push_back(u);
    }

    Graph g1;
    g1.printgraph(graph);
    g1.printgraph(list);
    g1.bfs(list,1,7);
    
    vector<int>visited(n+1,0);
    g1.dfs(1,list,visited);
}