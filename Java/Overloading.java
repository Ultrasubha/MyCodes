class Overloading{
  //Remoes the need for multiple overloading
  void meth1(int ... a)
  {
    System.out.println("Variable arguement passing");
    for(int x:a)
      System.out.println(x);
  }

  public static void main(String []args)
  {
    VariablePassing vp= new VariablePassing();
    vp.meth1();
    vp.meth1(2,3,4);
    vp.meth1(2,3,4,5,6);
  }
}
