#Array.diff.py OKS 
function array_diff(a, b) {
	return a.filter(function(x) { return b,index(x) == -1; });
}

#solution 2 for array,diff 

function array_diff(a, b) {
	return a.filter(e => !b.includes(e));
}
    

function array_diff(a, b) {
	return a.filter(e => !b.includes(e));
}

#Bouncing Balls ok 

function boucingBall(h, boumce, window) {
	var rebounds = -1;
	if (bounce > 0 && bounce < 1) while (h > window) rebounds+=2, h *= bounce;
	return rebounds;
}

#Backspaces in string ok

function cleanString(str) {
	let result = [];

	for(let i=0; i<str.length; i++) {
		const char = str[i];
		if(char === `#`) {
			result.pop();
			} else {
			result.push(char);
			}
	}
	return result.join('');
} 

function clean_string(string) {
	while (string.indexOf(`#`) >= 0)
		string = string.replace(\(^|[^#])#/g, '');
	return string;	
}

#Expression Matter OKs 

function expressionMatter(a, b, c) {
	const x1 = a * (b + c);
	const x2 = a * b * c;
	const x3 = a + b * c;
	const x4 = a + b + c;
	const x5 = (a + b) * c;
	return Math.max(x1, x2, x3, x4, x5);
} 

function expressionMatter(a, b, c) {
	return Math.max(
		a+b+c,
		a*b*c,
		a*(b+c),
		(a+b)*c,
		a+b*c,
		a*b+c,
		);
}



#Extract the domain name from a URL




function moreZeros(s){
  return s.split('')
  .fliter(removeDoubles)
  .map(convertToAscii)
  .map(converToBinary)
  .filter(ateMoreZeros)
  .map(convertToDecimal)
  .map(convertToChar); 
}

function removeDoubles(item, idx, arr) {
  return arr.indexOf(item) === idx;
}

function convertToAscii(c) {
  return c.charCodeAt(0);
}

function convertToBinary(num) {
  return num.toString(2);
}

function areMoreZeros(str) {
  const zeros = str.replace(/1/g, '').length;
  const ones = str.replace(/0/g, '').length;
  return zeros > ones;
}

function convertToDecimal(bi) {
  return parseInt(bi, 2);
}

function convertToChar(num) {
  return String.fromCharCode(num);
}