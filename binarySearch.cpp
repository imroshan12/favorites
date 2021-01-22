#include<bits/stdc++.h>
using namespace std;

int binarySearch(int a[], int l, int h, int key)
{
    int mid = (l+h)/2;
    if(l<=h)
    {
        if(key == a[mid])
            return mid;
        else if(key > a[mid])
            return binarySearch(a, mid+1, h, key);
        else
            return binarySearch(a, l, mid-1, key);
    }
    return -1;
}

int bSearch(int a[], int n, int key)
{
    int l = 0, h = n-1;
    while(l <= h)
    {
        int mid = (l+h)/2;
        if (key == a[mid])
            return mid;
        else if(key > a[mid])
            l = mid+1;
        else
            h = mid -1;
    }
    return -1;
}

int main()
{
    int a[10] = {1,2,3, 5, 6, 11, 13, 19, 20, 30};
    cout << bSearch(a, 10, 12);

    return 0;
}
