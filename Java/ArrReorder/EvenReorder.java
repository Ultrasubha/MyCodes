public int[] moveEvenToFront(int[] arr){
    int temp=0;
    int a=0;
    for(int i=0;i<arr.length;i++){
        if(arr[i]%2==0){

            for (int j=i;j>a;j--){
                temp=arr[j-1];
                arr[j-1]=arr[j];
                arr[j]=temp;
            }
            a++;
        }
    }
    return arr;
}
