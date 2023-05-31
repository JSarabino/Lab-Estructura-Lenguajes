% Integrantes
% Juan Camilo Sarabino Alegria
% Jorge Andres Ayerbe Caicedo

% Base de conocimiento de un sistema de recomendación de películas y prendas deportivas

%Hechos de peliculas por genero
%pelicula(genero, 'nombre de la pelicula').
pelicula(terror, 'El conjuro').
pelicula(terror, 'El exorcista del papa').
pelicula(comedia, 'Ghosting').
pelicula(comedia, 'Criminales a la vista').
pelicula(accion, 'Rapidos y furiosos 9').
pelicula(accion, 'El caballero oscuro').
pelicula(drama, 'Escape a la libertad').
pelicula(drama, 'El padrino').
pelicula('ciencia ficcion', 'El cazador implacable').
pelicula('ciencia ficcion', 'The Matrix').
pelicula(romantico, 'Ha nacido una estrella').
pelicula(romantico, 'La ciudad de las estrellas').
pelicula(suspenso, 'Perdida').
pelicula(suspenso, 'Prisioneros').
pelicula(fantacia, 'The Lord of the Rings').
pelicula(fantacia, 'Harry Potter').

%Hechos de ropa deportiva
%ropaDeportiva('actividad deportiva', ['lista de ropa deportiva'])
ropaDeportiva(correr, ['tenis de correr', 'tenis de trail' , pantaloneta, camiseta]).
ropaDeportiva(tenis, [tenis, 'pantaloneta de tenis', 'camiseta de tenis']).
ropaDeportiva(natacion, [banador, 'gafas de natacion', 'gorro de natacion']).
ropaDeportiva(yoga, ['pantalon de yoga', 'camiseta de yoga', 'esterilla de yoga']).
ropaDeportiva(futbol, [guayos, 'pantaloneta de futbol', 'camiseta de futbol', 'canilleras']).
ropaDeportiva(baloncesto, ['tenis de baloncesto', 'pantaloneta de baloncesto', 'camiseta de baloncesto']).

%Hecho de persona
%persona(nombre,genero,edad,gustoPeliculas['lista de generos'],actividadDeportiva['lista de actividades'])
persona(juan, hombre, 34, [accion, comedia, 'ciencia ficcion'], [tenis,basketball]).
persona(sara, mujer, 56, [romantico, comedia, drama], [correr, natacion]).
persona(miguel, hombre, 18, [suspenso, terror, accion], [ciclismo, correr]).
persona(emilia, mujer, 23, [fantacia, romantico, drama], [correr, yoga]).
persona(carlos, hombre, 29, [suspenso, accion], [futbol, correr]).
persona(rosa, mujer, 40, [romantico, drama, comedia], [natacion, yoga]).
persona(manuel, hombre, 61, [accion,'ciencia ficcion'], [futbol, baloncesto]).
persona(silvia, mujer, 35, [fantacia, terror, drama], [correr, yoga]).


% 1. Escriba una regla para recomendar películas a una persona tomando como referencia sus preferencias
%Regla
recomendarPeliculaA(P,LPeliculas):- persona(P,_,_,L,_), findall(Pelicula,(pelicula(Genero,Pelicula), member(Genero,L)),LPeliculas).
%Consulta
% recomendarPeliculaA(carlos,LPeliculas).


% 2. Escriba una regla que permita recomendar prendas deportivas en función del género y las aficiones
%Regla
imprimir([]):-!.%caso-base
imprimir([X|Y]):- write(X),nl,imprimir(Y).
recomendarAGeneroPrenda(Genero):- findall(Prenda,(persona(_,Genero,_,_,LActividades) , ropaDeportiva(Actividad,LPrendas), member(Actividad,LActividades), member(Prenda,LPrendas)),LPrendasRecomendadas), imprimir(LPrendasRecomendadas).

%Consulta
% recomendarAGeneroPrenda(mujer).

% 3. Escriba una regla que dada una película permita encontrar quienes estarían interesados en verla
%Regla
interesadosEnPelicula(Pelicula,LInteresados):- pelicula(Genero,Pelicula), findall(Persona,(persona(Persona,_,_,L,_), member(Genero,L)),LInteresados).

%Consulta
% interesadosEnPelicula('Perdida',LInteresados).


% 4. Escriba una regla que dada una prenda deportiva permita encontrar quienes estarían interesados en comprarla
%Regla, 
interesadosEnPrenda(Prenda,LInteresados):- ropaDeportiva(Actividad,LPrendas), member(Prenda,LPrendas) ,findall(Persona,(persona(Persona,_,_,_,LActividades), member(Actividad,LActividades)),LInteresados).

%Consulta
% interesadosEnPrenda('pantaloneta de baloncesto',LInteresados).