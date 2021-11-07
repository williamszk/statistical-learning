program namer
! use gfortran to compile a fortran program
! https://www.youtube.com/watch?v=GSJL6E1A6gM&ab_channel=CyprienRusu
! Ask me to write my name
! recognize the typing from the terminal
! print out my name

implicit none


! declare the variable
character :: name*10

print *,'What is your name?'
read *, name
print *,'Welcome to Fortran, ',name



end program namer