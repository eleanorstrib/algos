myArray = [8, 2, 7, 0, 15, 27, -2]

function bubble(myArray) {
	var passes = 0
	while (passes <= myArray.length){
		for (i = 0; i < myArray.length; i++) {
			if (myArray[i] > myArray[i+1]) {
				var temp = myArray[i];
				myArray[i] = myArray[i+1];
				myArray[i+1] = temp;
			}
		};
		passes++
	};
	return myArray;
}

console.log(bubble(myArray))