// https://www.youtube.com/watch?v=Lktyz-vojCQ&ab_channel=EduardoCasavella

#include <stdio.h>

void main()
{

    int number;
    float grade;
    char name[40];

    float grades[20];

    float mgrades[10][2];

    // store different types of data from student

    struct studentInfo // this is a new data type
    {
        // members of the struct
        char name[40];
        int number;
        float grade;
    };

    struct studentInfo student;

    printf("\n-------------- Student Sing Up -------------------------------\n\n");

    printf("Student's name .................: ");
    fgets(student.name, 40, stdin);

    printf("What the student's number ......: ");
    scanf("%d", &student.number);

    printf("What is the student's grade ....: ");
    scanf("%f", &student.grade);

    printf("\n-------------- Review the Student's Info ----------------------\n\n");
    printf("Name .................: %s", student.name);
    printf("Student's number .....: %d\n", student.number);
    printf("Student's grade ......: %.2f\n", student.grade);





}