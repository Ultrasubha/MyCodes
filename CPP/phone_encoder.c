#include <stdio.h>

int main()
{
	printf("ENTER THE MESSAGE\n\n");
	int iteration,lim=0;
	char tempo[500];
	gets(tempo);
	
	for(iteration=0;tempo[iteration]!='\0';iteration++)
	{
		lim=lim+1;
	}

	char input[lim];
	int store[lim];
	
	printf("\nENTER THE MESSAGE AGAIN\n\n");
	//Taking inputs
	for(iteration=0;iteration<lim;iteration++)
	{
		scanf("%c",&input[iteration]);
	}
	
	printf("\n\n");
	//Print numericals
	for(iteration=0;iteration<lim;iteration++)
	{
		switch(input[iteration])
		{
			case 'a':
				store[iteration]=2;
				break;
			case 'b':
				store[iteration]=22;
				break;
			case 'c':
				store[iteration]=222;
				break;
			case 'd':
				store[iteration]=3;
				break;
			case 'e':
				store[iteration]=33;
				break;
			case 'f':
				store[iteration]=333;
				break;
			case 'g':
				store[iteration]=4;
				break;
			case 'h':
				store[iteration]=44;
				break;
			case 'i':
				store[iteration]=444;
				break;
			case 'j':
				store[iteration]=5;
				break;
			case 'k':
				store[iteration]=55;
				break;
			case 'l':
				store[iteration]=555;
				break;
			case 'm':
				store[iteration]=6;
				break;
			case 'n':
				store[iteration]=66;
				break;
			case 'o':
				store[iteration]=666;
				break;
			case 'p':
				store[iteration]=7;
				break;
			case 'q':
				store[iteration]=77;
				break;
			case 'r':
				store[iteration]=777;
				break;
			case 's':
				store[iteration]=7777;
				break;
			case 't':
				store[iteration]=8;
				break;
			case 'u':
				store[iteration]=88;
				break;
			case 'v':
				store[iteration]=888;
				break;
			case 'w':
				store[iteration]=9;
				break;
			case 'x':
				store[iteration]=99;
				break;
			case 'y':
				store[iteration]=999;
				break;
			case 'z':
				store[iteration]=9999;
				break;
			case 'A':
				store[iteration]=12;
				break;
			case 'B':
				store[iteration]=122;
				break;
			case 'C':
				store[iteration]=1222;
				break;
			case 'D':
				store[iteration]=13;
				break;
			case 'E':
				store[iteration]=133;
				break;
			case 'F':
				store[iteration]=1333;
				break;
			case 'G':
				store[iteration]=14;
				break;
			case 'H':
				store[iteration]=144;
				break;
			case 'I':
				store[iteration]=1444;
				break;
			case 'J':
				store[iteration]=15;
				break;
			case 'K':
				store[iteration]=155;
				break;
			case 'L':
				store[iteration]=1555;
				break;
			case 'M':
				store[iteration]=16;
				break;
			case 'N':
				store[iteration]=166;
				break;
			case 'O':
				store[iteration]=1666;
				break;
			case 'P':
				store[iteration]=17;
				break;
			case 'Q':
				store[iteration]=177;
				break;
			case 'R':
				store[iteration]=1777;
				break;
			case 'S':
				store[iteration]=17777;
				break;
			case 'T':
				store[iteration]=18;
				break;
			case 'U':
				store[iteration]=188;
				break;
			case 'V':
				store[iteration]=1888;
				break;
			case 'W':
				store[iteration]=19;
				break;
			case 'X':
				store[iteration]=199;
				break;
			case 'Y':
				store[iteration]=1999;
				break;
			case 'Z':
				store[iteration]=19999;
				break;
			case ' ':
				store[iteration]=0;
				break;
			case '0':
				store[iteration]=110;
				break;
			case '1':
				store[iteration]=111;
				break;
			case '2':
				store[iteration]=112;
				break;
			case '3':
				store[iteration]=113;
				break;
			case '4':
				store[iteration]=114;
				break;
			case '5':
				store[iteration]=115;
				break;
			case '6':
				store[iteration]=116;
				break;
			case '7':
				store[iteration]=117;
				break;
			case '8':
				store[iteration]=118;
				break;
			case '9':
				store[iteration]=119;
				break;
			case '!':
				store[iteration]=1111;
				break;
			case '@':
				store[iteration]=1112;
				break;
			case '#':
				store[iteration]=1113;
				break;
			case '$':
				store[iteration]=1114;
				break;
			case '%':
				store[iteration]=1115;
				break;
			case '^':
				store[iteration]=1116;
				break;
			case '&':
				store[iteration]=1117;
				break;
			case '*':
				store[iteration]=1118;
				break;
			case '(':
				store[iteration]=1119;
				break;
			case ')':
				store[iteration]=11111;
				break;
			case '{':
				store[iteration]=11112;
				break;
			case '}':
				store[iteration]=11113;
				break;
			case '[':
				store[iteration]=11114;
				break;
			case ']':
				store[iteration]=11115;
				break;
			case '\\':
				store[iteration]=11116;
				break;
			case '|':
				store[iteration]=11117;
				break;
			case '\'':
				store[iteration]=11118;
				break;
			case '"':
				store[iteration]=11119;
				break;
			case ':':
				store[iteration]=101;
				break;
			case ';':
				store[iteration]=102;
				break;
			case '/':
				store[iteration]=103;
				break;
			case ',':
				store[iteration]=104;
				break;
			case '.':
				store[iteration]=105;
				break;
			case '-':
				store[iteration]=106;
				break;
			case '_':
				store[iteration]=107;
				break;
			case '+':
				store[iteration]=108;
				break;
			case '=':
				store[iteration]=109;
				break;
			case '?':
				store[iteration]=1001;
				break;
			case '<':
				store[iteration]=1002;
				break;
			case '>':
				store[iteration]=1003;
				break;
			case '`':
				store[iteration]=1004;
				break;
			default:
				store[iteration]=1;
				break;
		}
	}
	
	//Modifying
	for(iteration=0;iteration<lim;iteration++)
	{
		store[iteration]*=13;
		store[iteration]-=23;
	}
	
	//Printing it
	printf("%d ",lim);
	
	for(iteration=0;iteration<lim;iteration++)
	{
		printf("%d ",store[iteration]);
	}
	
	printf("\n\n");
}
