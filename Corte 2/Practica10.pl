% Hechos
% departamento (nombre, capital, área, población, limites[]).
departamento(cundinamarca, bogota, 24210, 2919000, [boyaca, meta, huila, tolima, caldas]).
departamento(antioquia, medellin, 63612, 6407000, [cordoba, bolivar, santander, boyaca, caldas, risaralda, choco]).
departamento('valle del cauca', cali, 22140, 4476000, [choco, caldas, quindio, tolima, cauca]).
departamento(atlantico, barranquilla, 3388, 2536000, [magdalena, bolivar]).
departamento(cauca, popayan, 29308, 1464000, [narino, putumayo, huila, 'valle del cauca', tolima]).
departamento(tolima, ibague, 23562, 1330000,[caldas, cundinamarca, huila, cauca, quindio, risaralda, 'valle del cauca']).


% 1. Cree una regla que permita verificar si un departamento es limítrofe con otro. Para esta regla podrá hacer uso
% de la función member predefinida en el lenguaje:
% member (elemento-a-verificar, lista[elemento1, elemento2,….,elementon]).

esLimitrofeDe(D1,D2):- departamento(D2,_,_,_,L), member(D1,L).

% 2. ¿Cuál(s) son los departamento que tiene una población superior a un valor brindado.

poblacionMayorA(N,D):- departamento(D,_,_,P,_), P > N.

% 3. ¿Cuál es el total de la población de los departamentos de Colombia?

contarPoblacion([],0). % caso-base
contarPoblacion([Cabeza|Cola],T):- contarPoblacion(Cola,P), T is Cabeza + P. % Recive La lista de poblaciones y las divide en cabeza - cola

totalPoblacion(T):- listaPoblacion(L), contarPoblacion(L,T). % Llamar al listado y mandarlo a contarPoblacion
listaPoblacion(L):- findall(P,departamento(_,_,_,P,_),L). % Volver lista las poblaciones

% 4. ¿Con cuántos límites geográficos tiene un departamento y cuáles son?

contarLimites([],0). % caso-base
contarLimites([Cabeza|Cola],N):- write(Cabeza), nl, contarLimites(Cola,P), N is 1 + P.

cantLimitesDe(D,N):- departamento(D,_,_,_,L), contarLimites(L,N).

% 5. ¿Cuál es el departamento con la mayor superficie?

mayorSuperficie([Cabeza|[]],Cabeza).
mayorSuperficie([Cabeza|Cola],M):- mayorSuperficie(Cola, P), (P > Cabeza -> M is P ; M is Cabeza).

deptMayorSuperficie(D):- listaSuperficie(L), mayorSuperficie(L,Mayor), departamento(D,_,Mayor,_,_).
listaSuperficie(L):- findall(S,departamento(_,_,S,_,_),L). % Volver lista las superficies

% 6. ¿Cuál es el departamento con la mayor población?

mayorPoblacion([Cabeza|[]],Cabeza).
mayorPoblacion([Cabeza|Cola],M):- mayorPoblacion(Cola, P), (P > Cabeza -> M is P ; M is Cabeza).

deptMayorPoblacion(D):- listaPoblacion(L), mayorPoblacion(L,Mayor), departamento(D,_,_,Mayor,_).
