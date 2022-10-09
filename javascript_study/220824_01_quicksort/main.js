/**
 * The objective of this script is to implement and test a quicksort algorithm
 */

const main = () => {
	// create array of random integers
	const lenArr = 20;
	const myArr01 = Array(lenArr).fill(0);
	const myArr02 = myArr01.map(() => {
		return Math.floor(Math.random() * 100);
	});

	console.log(myArr02);
	// build a quicksort for ascending

	quickSort(myArr02, 0, myArr02.length - 1);
	console.log(myArr02);

};

const quickSort = (arr, low, high) => {
	if (low < high) {
		pi = findPivot(arr, low, high);

		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
};

/**
 * `pi` is the pivot, it is the position of the pivot.
 *
 */
const findPivot = (arr, low, high) => {
	let temp;
	let i = low - 1;
	let pivot = arr[high]; // by convention the pivot will
	// be set as the last element of the array

	for (let j = low; j < high; j++) {
		if (arr[j] < pivot) {
			i++;
			// swap j and i
			temp = arr[j];
			arr[j] = arr[i];
			arr[i] = temp;
		}
	}
	// swap i+1 and high (which is the pivot)
	temp = arr[i + 1];
	arr[i + 1] = arr[high];
	arr[high] = temp;

	return i + 1;
};

main();
