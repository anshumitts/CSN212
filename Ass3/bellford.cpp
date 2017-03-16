#include <bits/stdc++.h>

using namespace std;
typedef pair <int,int> pii;
typedef pair <float,pii> pfpii;


int* bellFoll(pfpii Edges[],int V, int E, int S)
{
	float W;
	int v,u;
	int* d = new int[V];
	for (int i = 0; i < V; i++)
	{
		d[i]= INT_MAX;
	}
	d[S-1]=0;
	for (int i = 0; i < V-1; i++)
	{

		for (int j = 0; j < E; j++)
		{
			W = Edges[j].first;
			u = Edges[j].second.first;
			v = Edges[j].second.second;
			if (d[v]>d[u]+W)
			{
				d[v] = d[u]+W;
			}
		}
	}
	for (int j = 0; j < E; j++)
	{
		W = Edges[j].first;
		u = Edges[j].second.first;
		v = Edges[j].second.second;
		if (d[v]>d[u]+W)
		{
			return '\0';
		}
	}
	return d;
}
int main()
{
	int T,V,E,S;
	int u,v;
	float w;
	int tempE;
	cin>>T;
	while(T--)
	{
		cin>>V>>E>>S;
		tempE = E;
		pfpii *Edges = new pfpii[E];
		int* Dist = new int[V];
		while(tempE--)
		{
			cin>>u>>w>>v;
			Edges[tempE] = pfpii(w,pii(u-1,v-1));
		}
		Dist = bellFoll(Edges,V,E,S);
		if (Dist)
		{
			for (int i = 0; i < V; i++)
			{
				if (Dist[i]!=INT_MAX)
				{
					cout<<i+1<<'\t'<<Dist[i]<<endl;
				}
				else
				{
					cout<<i+1<<'\t'<<"Does not exists"<<endl;	
				}
			}
		}
		else
		{
			cout<<"negative cycle exists!!!";
		}
		cout<<'\n';
	}
	return 0;
}