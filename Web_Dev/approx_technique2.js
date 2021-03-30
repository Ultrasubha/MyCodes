/*
  ___________CODED BY SUBHADEEP MANDAL______________
  
  LICENSING:
  GNU General Public License v3.0  .....Dated: 30.3.2021
  (c) 2021 Guava_Slice. All rights reserved.
  
  OVERVIEW
  REVERSE LOOP Applied :
		Checks from behind.If the prev number doesn't match the loop breaks
		It's mainly useful to avoid stuffs like 1.6666666 for that
		1.6666666 ⇒ 1.67
		Sometimes we might need to do 0.005 so some liberty is given
  
  EXPECTATIONS from this approximation
		1.0000009 ⇒ 1.0000009
		6.0299999 ⇒ 6.03
		0.9999999 ⇒ 1
		1.000999 ⇒ 1.001
		1.2045999999999998 ⇒ 1.2046
    
    DRAWBACK
    Not a very strict approximation so it might not suit your taste
    But for me this is exactly what I wanted.
*/

document.write(Fixing_Mantisa_Of("1.6666666"));

function Fixing_Mantisa_Of(sampul_str) {
	var dgtcount=0;
	if (sampul_str.includes(".")) {
		var mantissaposi = sampul_str.indexOf(".");
		for(dgt = sampul_str.length-1; dgt > mantissaposi;dgt--) {
			if(sampul_str[dgt] != sampul_str[dgt-1]){
				dgtcount = dgt - mantissaposi;
				break;
			}

			//For numbers like 1.6666666
			if (dgt == mantissaposi+2) {
				dgtcount = dgt - mantissaposi;
				break;
			}
		}
		sampul_str = Number(sampul_str).toFixed(dgtcount);

		//Second time approximation using recusion for mantissa ending with 99
		if (sampul_str[sampul_str.length-1]=="9" && sampul_str[sampul_str.length-2]=="9" )
			sampul_str = Fixing_Mantisa_Of(sampul_str);

		//To Remove the extra zero or decimals after decimals
		while(sampul_str[sampul_str.length-1] == "0" || sampul_str[sampul_str.length-1] == ".")
			sampul_str = sampul_str.slice(0, -1);

		return sampul_str;
	}
	else
		return sampul_str;
}
}
