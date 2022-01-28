class Overloading{
  //Removes the need for multiple overloading
  void meth1(int ... a)
  {
    System.out.println("Variable arguement passing");
    for(int x:a)
      System.out.println(x);
  }

  public static void main(String []args)
  {
    Overloading ov= new Overloading();
    ov.meth1();
    ov.meth1(2,3,4);
    ov.meth1(2,3,4,5,6);
  }
}
