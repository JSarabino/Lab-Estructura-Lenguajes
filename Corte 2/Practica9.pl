%Hechos
hombre(juan).
hombre(pedro).
hombre(jose).
hombre(camilo).
hombre(daniel).
hombre(yessid).
hombre(julian).

mujer(andrea).
mujer(diana).
mujer(sofia).
mujer(sandra).
mujer(fernanda).

materia(calculo).
materia(etica).
materia(programacion).
materia(ingles).
materia(requisitos).
materia(circuitos).

perteneceA(juan,pis).
perteneceA(pedro,pis).
perteneceA(andrea,pis).
perteneceA(camilo,pai).
perteneceA(diana,pai).
perteneceA(sofia,pai).
perteneceA(jose,pai).

ensenya(julian,caligrafia).
ensenya(julian,ingles).
ensenya(daniel,programacion).
ensenya(daniel,calculo).
ensenya(sandra,requisitos).
ensenya(fernanda,etica).
ensenya(yessid,circuitos).

matriculo(juan,calculo,3.5).
matriculo(juan,programacion,2.8).
matriculo(juan,ingles,4.0).
matriculo(pedro,calculo,4.0).
matriculo(pedro,programacion,3.1).
matriculo(pedro,ingles,3.3).
matriculo(jose,requisitos,2.5).
matriculo(jose,etica,2.8).
matriculo(jose,ingles,2.1).
matriculo(camilo,calculo,3.5).
matriculo(camilo,circuitos,3.1).
matriculo(camilo,caligrafia,4.9).
matriculo(andrea,calculo,4.6).
matriculo(andrea,circuitos,3.8).
matriculo(andrea,ingles,3.2).
matriculo(sofia,caligrafia,4.3).
matriculo(sofia,etica,2.5).
matriculo(diana,circuitos,2.9).
matriculo(diana,etica,3.9).



%Reglas
%Regla 1: Escriba una regla que permita retornar cuáles son los estudiantes de un profesor.
estudiantesDe(P,E):-ensenya(P,A),matriculo(E,A,_).

%Regla 2: Escriba una regla que permita retornar cuáles son los profesores las asignaturas matriculadas por un
%estudiante. Haga uso de una lista.
%findall
%estructura findall((tR1,tR2),objetivo,nL). 
profesoresDe(E,L):- findall((P,A),(matriculo(E,A,_),ensenya(P,A)),L).

%Regla 3: Escriba una regla para retornar las estudiantes pertenecientes a un programa académico. Haga uso de
%una lista.
estProgramaV1(P,L):- findall(E,perteneceA(E,P),L).

%Version 2: funcion de imprimir
imprimir([]):-!.%caso-base
imprimir([X|Y]):- write(X),nl,imprimir(Y).

estProgramaV2(P):- listaEstPrograma(P,L),imprimir(L).
listaEstPrograma(P,L):- findall(E,perteneceA(E,P),L).

%Regla 4: 
%.Escriba una regla que permita recuperar a todas las estudiantes mujeres en una lista, la cual deberá contener:
% Estudiante, programa y materias matricularon.

estMujeres(L):- findall((E,P,A),(mujer(E),perteneceA(E,P),matriculo(E,A,_)),L).

%Regla 5: Escriba una regla que permita recuperar una lista de las materias que no ha matriculado un estudiante.

noMatriculadas(E,L):- findall(A,(materia(A),not(matriculo(E,A,_))),L).

%Regla 6: Escriba una regla que permita recuperar a todos los estudiantes que vieron una asignatura de forma ordenada.
listEstMateria(A,L):- setof((N,E),matriculo(E,A,N),L).

%Regla 7: Escriba una regla que permita recuperar a todos los estudiantes que perdieron materias.
perdieronMateria(L):- findall(E,(matriculo(E,A,N),N<3.0),L).

%Regla 8: Escriba una regla que permita contar el numero matriculas que se realizaron en un programa.

contar([],0):-!.%caso-base
contar([Cabeza|Cola],N):- contar(Cola,P), P is 1+N.

contarMatriculas(P):- listaMatriculaPrograma(P,L),contar(L,N).
listaMatriculaPrograma(P,L):- findall(P,(perteneceA(E,P),matriculo(E,_,_)),L).