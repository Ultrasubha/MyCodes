#include <stdio.h>
#include <conio.h>

int main()
{
	printf("ENTER THE CODE\n\n");
	
	int size,iteration;
	scanf("%d",&size);
	int input[size];
	char output[size];
	
	for(iteration=0;iteration<size;iteration++)
	{
		scanf("%d",&input[iteration]);
	}
	
	//Demodifying
	for(iteration=0;iteration<size;iteration++)
	{
		input[iteration]+=23;
		input[iteration]/=13;
	}
	
	printf("\n");
	
	for(iteration=0;iteration<size;iteration++)
	{
		switch(input[iteration])
		{
			case 2:
				output[iteration]='a';
				break;
			case 22:
				output[iteration]='b';
				break;
			case 222:
				output[iteration]='c';
				break;
			case 3:
				output[iteration]='d';
				break;
			case 33:
				output[iteration]='e';
				break;
			case 333:
				output[iteration]='f';
				break;
			case 4:
				output[iteration]='g';
				break;
			case 44:
				output[iteration]='h';
				break;
			case 444:
				output[iteration]='i';
				break;
			case 5:
				output[iteration]='j';
				break;
			case 55:
				output[iteration]='k';
				break;
			case 555:
				output[iteration]='l';
				break;
			case 6:
				output[iteration]='m';
				break;
			case 66:
				output[iteration]='n';
				break;
			case 666:
				output[iteration]='o';
				break;
			case 7:
				output[iteration]='p';
				break;
			case 77:
				output[iteration]='q';
				break;
			case 777:
				output[iteration]='r';
				break;
			case 7777:
				output[iteration]='s';
				break;
			case 8:
				output[iteration]='t';
				break;
			case 88:
				output[iteration]='u';
				break;
			case 888:
				output[iteration]='v';
				break;
			case 9:
				output[iteration]='w';
				break;
			case 99:
				output[iteration]='x';
				break;
			case 999:
				output[iteration]='y';
				break;
			case 9999:
				output[iteration]='z';
				break;
			case 12:
				output[iteration]='A';
				break;
			case 122:
				output[iteration]='B';
				break;
			case 1222:
				output[iteration]='C';
				break;
			case 13:
				output[iteration]='D';
				break;
			case 133:
				output[iteration]='E';
				break;
			case 1333:
				output[iteration]='F';
				break;
			case 14:
				output[iteration]='G';
				break;
			case 144:
				output[iteration]='H';
				break;
			case 1444:
				output[iteration]='I';
				break;
			case 15:
				output[iteration]='J';
				break;
			case 155:
				output[iteration]='K';
				break;
			case 1555:
				output[iteration]='L';
				break;
			case 16:
				output[iteration]='M';
				break;
			case 166:
				output[iteration]='N';
				break;
			case 1666:
				output[iteration]='O';
				break;
			case 17:
				output[iteration]='P';
				break;
			case 177:
				output[iteration]='Q';
				break;
			case 1777:
				output[iteration]='R';
				break;
			case 17777:
				output[iteration]='S';
				break;
			case 18:
				output[iteration]='T';
				break;
			case 188:
				output[iteration]='U';
				break;
			case 1888:
				output[iteration]='V';
				break;
			case 19:
				output[iteration]='W';
				break;
			case 199:
				output[iteration]='X';
				break;
			case 1999:
				output[iteration]='Y';
				break;
			case 19999:
				output[iteration]='Z';
				break;
			case 0:
				output[iteration]=' ';
				break;
			case 101:
				output[iteration]=':';
				break;
			case 102:
				output[iteration]=';';
				break;
			case 103:
				output[iteration]='/';
				break;
			case 104:
				output[iteration]=',';
				break;
			case 105:
				output[iteration]='.';
				break;
			case 106:
				output[iteration]='-';
				break;
			case 107:
				output[iteration]='_';
				break;
			case 108:
				output[iteration]='+';
				break;
			case 109:
				output[iteration]='=';
				break;
			case 1001:
				output[iteration]='?';
				break;
			case 1002:
				output[iteration]='<';
				break;
			case 1003:
				output[iteration]='>';
				break;
			case 1004:
				output[iteration]='`';
				break;
			case 110:
				output[iteration]='0';
				break;
			case 111:
				output[iteration]='1';
				break;
			case 112:
				output[iteration]='2';
				break;
			case 113:
				output[iteration]='3';
				break;
			case 114:
				output[iteration]='4';
				break;
			case 115:
				output[iteration]='5';
				break;
			case 116:
				output[iteration]='6';
				break;
			case 117:
				output[iteration]='7';
				break;
			case 118:
				output[iteration]='8';
				break;
			case 119:
				output[iteration]='9';
				break;
			case 1111:
				output[iteration]='!';
				break;
			case 1112:
				output[iteration]='@';
				break;
			case 1113:
				output[iteration]='#';
				break;
			case 1114:
				output[iteration]='$';
				break;
			case 1115:
				output[iteration]='%';
				break;
			case 1116:
				output[iteration]='^';
				break;
			case 1117:
				output[iteration]='&';
				break;
			case 1118:
				output[iteration]='*';
				break;
			case 1119:
				output[iteration]='(';
				break;
			case 11111:
				output[iteration]=')';
				break;
			case 11112:
				output[iteration]='{';
				break;
			case 11113:
				output[iteration]='}';
				break;
			case 11114:
				output[iteration]='[';
				break;
			case 11115:
				output[iteration]=']';
				break;
			case 11116:
				output[iteration]='\\';
				break;
			case 11117:
				output[iteration]='|';
				break;
			case 11118:
				output[iteration]='\'';
				break;
			case 11119:
				output[iteration]='"';
				break;
			default:
				output[iteration]='*';
				break;

		}
	}
	
	for(iteration=0;iteration<size;iteration++)
	{
		printf("%c",output[iteration]);
	}
	
	printf("\n");
	getchar();
}
// Test string : 11 44 33 555 555 666 0 7777 88 22 44 666
