// This is a module, it contains some functions
// that are used in other programs

void printArrayInt(int *array, int lenArray){
    printf("{");
    for (int j; j < lenArray; j++){
        if (j < lenArray-1){
            printf("%d, ",array[j]);
        } else {
            printf("%d",array[j]);
        }
    }
    printf("}\n");
}











