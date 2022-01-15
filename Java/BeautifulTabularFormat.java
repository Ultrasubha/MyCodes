/**
*BeautifulTabularFormat
Created on 15 Jan 2022
@author : Subhadeep Mandal
*/

import java.util.Scanner;

class BeautifulTabularFormat
{
	public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int z = sc.nextInt();		//Number of rows to make

        System.out.println("================================");
        for(int i=0;i<z;i++){
            String s1=sc.next();	//Column1 info added
			
            while(s1.length() < 15)	//Spaces added
            	s1+=" ";
                
            s1+=sc.nextLine();		//Column2 info added
			
            System.out.println(s1);	//Prints 1st row and proceeds to next
        }
        System.out.println("================================");
    }
}


/*
Input:
10
[CSE306] Computer Networks
[CSE307] Internetworking Essentials
[CSE310] Programming in Java
[CSE316] Operating Systems
[CSE325] Operating Systems Laboratory
[CSE408] Design and Analysis of Algorithms
[INT209] Computing Project-1
[INT404] Artificial Intelligence
[MTH302] Probability and Statistics
[PEV106] Verbal Ability-1

Output:
================================
[CSE306]        Computer Networks
[CSE307]        Internetworking Essentials
[CSE310]        Programming in Java
[CSE316]        Operating Systems
[CSE325]        Operating Systems Laboratory
[CSE408]        Design and Analysis of Algorithms
[INT209]        Computing Project-1
[INT404]        Artificial Intelligence
[MTH302]        Probability and Statistics
[PEV106]        Verbal Ability-1
================================
*/
