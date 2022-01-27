/* OUTPUT : 
0
0
0
55
21
63
45*/
public class ZeroReorder {
  public static void main(String[] args) {
    int[] arr = {55,0,21,0,63,0,45,0};
    int len = arr.length - 1;
    
    for(int i=len;i>=0;i--)
      if(arr[i]!=0) {
        arr[len] = arr[i];
        len--;
      }
    
    while(len>=0) {
      arr[len] = 0;
      len--;
    }
    
    return arr;
  }
}
