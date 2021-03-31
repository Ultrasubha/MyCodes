/*
  ___________CODED BY SUBHADEEP MANDAL______________
  
  LICENSING:
  GNU General Public License v3.0  .....Dated: 31.3.2021
  (c) 2021 Guava_Slice. All rights reserved.
  
  OVERVIEW
  If any 4 consequent digits are repeated the loop breaks and sends that digit index for approxing.
  But this method only gets called above a certain limit for our case it's 8.
  
  EXPECTATIONS from this approximation
		1.0000009 ⇒ 1
    6.0299999 ⇒ 6.03
    0.9999999 ⇒ 1
    1.000999 ⇒ 1.000999
    1.6666666 ⇒ 1.67
    1.20999998 ⇒ 1.21
    29.999999999999996 ⇒ 30  [A viable fix for atan(0.5773502691896257)]
    0.5773502691896257 ⇒ 0.5773502691896257  [doesn't approx tan30 value which is a good thing]
    
    DRAWBACK
    This approximation is very much based on personal prefference.
    if you like this style feel free to use it. Add your test cases in the array and check out yourself
    if this is the right one for you.
*/

function Fixing_Mantisa_Of(sampul_str) {

	if (sampul_str.includes(".")) {
		if(sampul_str.length > 8) {
			var Maxrepititiondigit = sampul_str[sampul_str.length-1];
			var caseFound = false;

			for(dgt=0;dgt<sampul_str.length-1;dgt++) {
				if(sampul_str[dgt] == sampul_str[dgt+1] && sampul_str[dgt] == sampul_str[dgt+2] && sampul_str[dgt] == sampul_str[dgt+3] && sampul_str[dgt] == sampul_str[dgt+4]) {
					Maxrepititiondigit = sampul_str[dgt];
					caseFound = true;
					break;
				}
			}
			if(caseFound) {
				var exactposi = sampul_str.indexOf(Maxrepititiondigit);

				//If exactposi goes beyond decimal this will fix this
				while(exactposi < sampul_str.indexOf("."))
					exactposi++;

				sampul_str = Number(sampul_str).toFixed(exactposi);

				//Removing unnecessary 0 after decimal
				while(sampul_str[sampul_str.length-1] == "0")
					sampul_str = sampul_str.slice(0, -1);

				//Removing unnecessary . after decimal
				if(sampul_str[sampul_str.length-1] == ".")
					sampul_str = sampul_str.slice(0, -1);
			}
		}
	}

	return sampul_str;
}
