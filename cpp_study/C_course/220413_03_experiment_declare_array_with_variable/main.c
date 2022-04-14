// the objective here is to experiment with the declaration of
// arrays, let's try to use a variable to define the size of the
// the array

#include <stdio.h>

void main()
{
    // int arr[] = {1,2,3,4,5,6,7, 99, 87};
    // int lenArr = sizeof(arr)/sizeof(arr[0]);
    // int arrCopy[lenArr];
    // the above is an example of situation where we can use a variable lenArr
    // to declare another array

    int arr[] = {1, 2, 3, 4, 5, 6, 7, 99, 87};
    int arrLen = sizeof(arr) / sizeof(arr[0]);
    int arrCopy[arrLen]; // this works

    int i;
    for (i = 0; i < arrLen; i++)
    {
        printf("%d\n", arrCopy[i]); // this works too
    }

    // ------------------------------------------------------------- //
    int myArrLen = 13;
    int defArr[myArrLen]; // will this work?

    for (i = 0; i < myArrLen; i++)
    {
        printf("%d\n", defArr[i]); // this works too
    }

    // ------------------------------------------------------------- //
    // What if we use a variable to be used as the len of the array
    // but initialize it with {0}, for all elements to be 0?

    // int arrLen2 = 15;
    // int arr2[arrLen2] = {0};
    // variable "arr2" may not be initializedC/C++(145)
    // why?
    // this doesn't work...
    // main.c:39:5: error: variable-sized object may not be initialized
    //    39 |     int arr2[arrLen2] = {0};
    //       | 

    // ------------------------------------------------------------- //
    // We saw that using a variable as the size of the array and also giving
    // a default initial value doesn't work.
    // But if we give the exact number of elements that the variable specifies?
    // int arrLen3 = 4;
    // int arr3[arrLen3] = {1,2,3,4};
    // variable "arr3" may not be initializedC/C++(145)
    // main.c:52:5: error: variable-sized object may not be initialized
    // 52 |     int arr3[arrLen3] = {1,2,3,4};    
    // This does not work too.
    // Interestingly arr3 is called a "variable-sized object"
    // Take a look at what this means.

    // Another idea:
    // We could try to see if we can change the size of the array dynamically
    // We can declare an array using a variable as its size, then we can calculate
    // its length using sizeof(), then we can change the variable value
    // and see if its length is the same.

    // ------------------------------------------------------------- //
    // Conclusion
    // We can declare an array using a variable as its size.
    // But if we do this, we can't initialize the array with elements.
    // Even if use the exact same number of elements as specified in the
    // variable length. 

    // Another question:
    // If we declare an array using a variable as its size
    // are we sure that always and all its elements will be 0?
    // 

}