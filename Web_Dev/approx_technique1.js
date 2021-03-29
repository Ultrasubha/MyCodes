	/*
  ___________CODED BY SUBHADEEP MANDAL______________
  
  LICENSING:
  GNU General Public License v3.0  .....Dated: 29.3.2021
  (c) 2021 Guava_Slice. All rights reserved.
  
  OVERVIEW
  After the decimal point it finds 2 repeating numbers it will break
  and approx it at that very point
  
  EXPECTATIONS from this approximation
		1.0000001 ⇒ 1
		6.0299999 ⇒ 6.03
		0.9999999 ⇒ 1
    
    DRAWBACK
    1.000569 ⇒ 1
    If you don't want this kind of approximations don't use it
	*/
document.write(Fixing_Mantisa_Of("6.0299999"));

function Fixing_Mantisa_Of(sampul_str) {
	var dgtcount=0;
	var mantissaPass = false;

	for(dgt=0; dgt<sampul_str.length; dgt++) {

		if (sampul_str[dgt] == "."){
			mantissaPass = true;
			continue;
		}

		if (mantissaPass) {
			/*_____Checks from where 3part repition starts in mantissa and then returns that index____*/
			if(sampul_str[dgt] == sampul_str[dgt+1] && sampul_str[dgt] == sampul_str[dgt+2])
				break;
			dgtcount++;
		}
	}

	sampul_str = Number(sampul_str).toFixed(dgtcount);

	return sampul_str;
}
