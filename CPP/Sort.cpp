#include <iostream>
using namespace std;

void print(int A[], int size)
{
	for (auto i = 0; i < size; i++)
		cout << A[i] << " ";
}

void merge(int array[], int const left, int const mid, int const right)
{
	auto const subArrayOne = mid - left + 1;
	auto const subArrayTwo = right - mid;

	auto *L = new int[subArrayOne],
		*R = new int[subArrayTwo];

	for (auto i = 0; i < subArrayOne; i++)
		L[i] = array[left + i];
	for (auto j = 0; j < subArrayTwo; j++)
		R[j] = array[mid + 1 + j];

	auto indexOfSubArrayOne = 0, indexOfSubArrayTwo = 0;
	int indexOfMergedArray = left;

	// Merge the temp arrays back into array[left..right]
	while (indexOfSubArrayOne < subArrayOne && indexOfSubArrayTwo < subArrayTwo) {
		if (L[indexOfSubArrayOne] <= R[indexOfSubArrayTwo]) {
			array[indexOfMergedArray] = L[indexOfSubArrayOne];
			indexOfSubArrayOne++;
		}
		else {
			array[indexOfMergedArray] = R[indexOfSubArrayTwo];
			indexOfSubArrayTwo++;
		}
		indexOfMergedArray++;
	}

	//Remaining
	while (indexOfSubArrayOne < subArrayOne) {
		array[indexOfMergedArray] = L[indexOfSubArrayOne];
		indexOfSubArrayOne++;
		indexOfMergedArray++;
	}
    
	while (indexOfSubArrayTwo < subArrayTwo) {
		array[indexOfMergedArray] = R[indexOfSubArrayTwo];
		indexOfSubArrayTwo++;
		indexOfMergedArray++;
	}
}

void mergeSort(int array[], int const begin, int const end)
{
	if (begin >= end)
		return;

	auto mid = begin + (end - begin) / 2;
	mergeSort(array, begin, mid);
	mergeSort(array, mid + 1, end);
	merge(array, begin, mid, end);
}

void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
 
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main()
{
    int N = 0;  cin >> N; int arr[N];
    for(int i=0;i<N;i++)    cin>> arr[i];
    if(N>43) mergeSort(arr, 0, N - 1);   else insertionSort(arr, N);

	//cout << "\nSorted array is \n"; print(arr, N);
	return 0;
}