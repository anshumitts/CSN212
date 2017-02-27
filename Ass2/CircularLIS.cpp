/*

m -> Number of Trial cases
n -> Number of memebers

eg 
input:

2
3
3 2 1
6
4 8 6 1 5 2

ouput:
2
4

*/

#include <bits/stdc++.h>
using namespace std;

int DMatrix[10000][10000] = {0};
int Max = -1;
void CircularLIS(int arr[], int size, int j, int i, int length, int start)
{
	int temp = 0;
	if(start<size)
	{
		i = i%size;
		if (i!=start)
		{
			if (DMatrix[j][i])
			{
				CircularLIS(arr,size,i,i+1,length + DMatrix[j][i]-1,start);
				CircularLIS(arr,size,j,i+1,length,start);
			}
			else if(arr[i] > arr[j])
			{
				DMatrix[start][i] = length +1;
				CircularLIS(arr,size,i,i+1,length+1,start);
				CircularLIS(arr,size,j,i+1,length,start);
			}
			else
			{
				temp = length;
				CircularLIS(arr,size,j,i+1,length,start);
			}
			DMatrix[start][i] = temp;
			if (Max < DMatrix[start][i])
				Max = DMatrix[start][i];
		}
		else
		{
			DMatrix[start+1][start+1] = 1;
			CircularLIS(arr,size,start+1,start+2,1,start+1);
		}
	}
}

int main()
{
	int* arr;
	int n,m;
	arr = new int[n];
	cin>>m;
	while(m--)
	{
		int k=0;
		Max=-1;
		cin>>n;
		while(n--)
		{
			cin>>arr[k];
			k++;
		}
		DMatrix[0][0]=1;
		if(k>0)
		{
			CircularLIS(arr,k,0,1,1,0);
			cout<<Max<<endl;
		}
		else
			cout<<0<<endl;
		for (int i = 0; i < k; i++)
		{
			for (int j = 0; j < k; j++)
			{
				DMatrix[i][j]=0;
			}
		}
	}
	return 0;
}