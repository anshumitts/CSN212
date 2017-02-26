/*
Input format
n
1 2 ... n numbers

Ouput : Longest Sequence
*/

#include <bits/stdc++.h>
using namespace std;

int* arrMaxLen[2];

int zigzagLength(int arr[],int size ,int length, int flag, int i)
{
	if(i<size)
	{
		if (arrMaxLen[flag][i+1]>-1)
		{
			return arrMaxLen[flag][i+1];
		}
		else if(flag ==1 && (arr[i] - arr[i+1] < 0))
			arrMaxLen[flag][i+1] = max(zigzagLength(arr,size,length,flag,i+1),zigzagLength(arr,size,length+1,0,i+1));
		else if(flag ==0 && (arr[i] - arr[i+1] > 0))
			arrMaxLen[flag][i+1] = max(zigzagLength(arr,size,length,flag,i+1),zigzagLength(arr,size,length+1,1,i+1));
		else
			arrMaxLen[flag][i+1] = zigzagLength(arr,size,length,flag,i+1);
		return arrMaxLen[flag][i+1];
	}
	return length;
}
int main()
{
	int* arr;
	int n;
	cin>>n;
	arrMaxLen[0] = new int[n+1];
	arrMaxLen[1] = new int[n+1];
	arr = new int[n];
	int k=0;
	while(n--)
	{
		cin>>arr[k];
		arrMaxLen[0][k+1]=-1;
		arrMaxLen[1][k+1]=-1;
		k++;
	}
	if(k>0)
		{
			arrMaxLen[1][0]=1;
			arrMaxLen[1][1]=1;
			cout<<max(zigzagLength(arr,k,1,1,0),zigzagLength(arr,k,1,0,0));
		}
	else
		cout<<0;
	return 0;
}