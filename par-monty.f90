! 2021 - 21 - 11
! Buffon.f90
! Félix Cabrera (walberto.cabrera@gmail.com)

! Este es un programa que simula un tiro parabolico por
! medio del metodo de montecarlo

! Codificación del texto: ASCII text
! Compiladores probados: GNU Fortran (Ubuntu 9.2.1-9ubuntu2) 9.2.1 2019008
! Instrucciones de compilación: no requiere nada más
! gfortran -Wall -pedantic -std=f95 par-monty.f90 -o par-monte
! ./par-monte

! para su caracterización
! /usr/bin/time -f "%e, %M, %P," ./par-monte

PROGRAM parabola
  IMPLICIT Instrucciones

  ! Iniciamos variables
  REAL(8) :: v0, ang, x, y,
  INTEGER(8) :: n

  ! variables auxiliares
  REAL(8) :: ang0, angN, xN, yN
  INTEGER(8):: i

  CALL RANDOM_SEED (put =sem)

  n = 300 !Pasos montecarlo
  v0 = 8.0 ! Velocidad inicial
  ang = 0.7853981633974483 ! angulo inicial (rads)


END PROGRAM parabola
