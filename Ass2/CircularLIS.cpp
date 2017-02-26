#include <bits/stdc++.h>
using namespace std;

int DMatrix[10000][10000] = {0};
void CircularLIS(int arr[], int size, int j, int i, int length , int start)
{
	int temp = 0;
	if(start<size)
	{
		i = i%size;
		if (i!=start)
		{
			// if (DMatrix[j][i])
			// {
			// 	CircularLIS(arr,size,i,i+1,length + DMatrix[j][i],start);
			// }
			if(arr[i] > arr[j])
			{
				temp = length +1;
				CircularLIS(arr,size,j,i+1,length,start);
				CircularLIS(arr,size,i,i+1,length+1,start);
			}
			else
			{
				temp = length;
				CircularLIS(arr,size,j,i+1,length,start);
			}
			DMatrix[start][i] = max(temp,DMatrix[start][i]);
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
	int n;
	cin>>n;
	arr = new int[n];
	int k=0;
	int Max = -1;
	while(n--)
	{
		cin>>arr[k];
		k++;
	}
	DMatrix[0][0]=1;
	if(k>0)
		{
			CircularLIS(arr,k,0,1,1,0);
			for (int i = 0; i < k; i++)
			{
				for (int j = 0; j < k; j++)
				{
					if(Max < DMatrix[j][i])
						Max = DMatrix[j][i];
				}
			}
			cout<<Max;
		}
	else
		cout<<0;
	return 0;
}