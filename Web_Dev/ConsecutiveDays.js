//Can find all consecutive days that will occur at a given frequency
function daysInMonth(year,month) {
    var monthcap = 0;
    switch(month) {
        case 1: monthcap = 31;break;
        case 2: monthcap = ((0 == year % 4) && (0 != year % 100) || (0 == year % 400)) ? 29 : 28;break;
        case 3: monthcap = 31;break;
        case 4: monthcap = 30;break;
        case 5: monthcap = 31;break;
        case 6: monthcap = 30;break;
        case 7: monthcap = 31;break;
        case 8: monthcap = 31;break;
        case 9: monthcap = 30;break;
        case 10: monthcap = 31;break;
        case 11: monthcap = 30;break;
        case 12: monthcap = 31;break;
        default: monthcap = -1;break;
    }
    return monthcap;
}
var date = "2022 7 9".split(" ");
let frequency = 14;
var y = parseInt(date[0]);
var m = parseInt(date[1]);
let d = parseInt(date[2]);
mCap = daysInMonth(y,m);
while(m<13){
    if(d+frequency>mCap) {
        m+=1;
        d=d+frequency-mCap;
        document.writeln(y+" "+m+" "+d+"<br>");
        mCap = daysInMonth(y,m);
    }
    else {
        d+=frequency;
        document.writeln(y+" "+m+" "+d+"<br>");
    }
}
