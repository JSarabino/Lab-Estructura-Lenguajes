% Hechos
% Motherboards
motherboard(asus_rog_strix_z590e, asus, atx, lga_1200, 4, 128, [3200, 3600, 4000, 4400], 500, [10, 11]).
motherboard(asrock_z590_taichi, asrock, atx, lga_1151, 4, 128, [2666, 3200, 3600, 4000, 4400], 400, [8, 9, 10, 11]).
motherboard(msi_meg_x570_ace, msi, atx, am4, 4, 128, [2666, 3200, 3600, 4000, 4400], 380, [3, 4, 5]).
motherboard(msi_b560m_pro, msi, micro_atx, lga_1200, 2, 64, [2666, 2933, 3200, 3600], 160, [10, 11]).
motherboard(asus_tuf_b460m_plus, asus, micro_atx, lga_1151, 2, 64, [2666, 2933, 3200], 150, [8, 9, 10]).
motherboard(gigabyte_x570_aorus_master, gigabyte, atx, am4, 4, 128, [2666, 3200, 3600, 4000, 4400], 360, [3, 4, 5]).
motherboard(asrock_x570_taichi, asrock, atx, am4, 4, 128, [2666, 3200, 3600, 4000, 4400], 340, [3, 4, 5]).
motherboard(asus_rog_strix_b450f, asus, atx, am4, 4, 64, [2400, 2666, 3200], 130, [1, 2, 3]).
motherboard(gigabyte_h410m_s2h, gigabyte, micro_atx, lga_1200, 2, 64, [2133, 2400, 2666], 90, [10, 11]).
motherboard(asus_h310m_k, asus, micro_atx, lga_1151, 2, 32, [2133, 2400, 2666], 80, [8, 9, 10]).
motherboard(asrock_a320m_hdv_r4_0, asrock, micro_atx, am4, 2, 32, [2133, 2400, 2666], 70, [1, 2, 3]).

% Procesadores
procesador(intel_core_i9_11900k, intel, lga_1200, 8, 16, 3.5, 5.3, [2400, 2666, 2933, 3200, 3600], 600, 11, 125).
procesador(intel_core_i7_8700, intel, lga_1151, 6, 12, 3.2, 4.6, [2133, 2400, 2666, 2800, 3000, 3200], 330, 8, 65).
procesador(amd_ryzen_9_3900x, amd, am4, 12, 24, 3.8, 4.6, [3200, 3600, 3733, 3800, 3866, 4000], 500, 3, 105).
procesador(intel_core_i5_11600k, intel, lga_1200, 6, 12, 3.9, 4.9, [2133, 2400, 2666, 2933, 3200, 3600], 290, 11, 125).
procesador(intel_core_i5_8600k, intel, lga_1151, 6, 6, 3.6, 4.3, [2133, 2400, 2666, 2800, 3000, 3200], 230, 8, 95).
procesador(amd_ryzen_5_5600, amd, am4, 6, 12, 3.7, 4.6, [3200, 3600, 3733, 3800, 3866, 4000], 300, 4, 65).
procesador(intel_core_i3_11100, intel, lga_1200, 4, 8, 3.7, 4.5, [2133, 2400, 2666, 2933, 3200], 180, 11, 65).
procesador(intel_core_i3_8100, intel, lga_1151, 4, 4, 3.6, 3.6, [2133, 2400, 2666, 2800, 3000], 110, 8, 65).
procesador(amd_athlon_3000g, amd, am4, 2, 4, 3.5, 3.9, [1866, 2133, 2400], 85, 3, 35).

% Memoria RAM
memoria_ram(g_skill_trident_z_rgb, 32, 3600, 200).
memoria_ram(team_tforce_delta_rgb, 32, 3200, 150).
memoria_ram(corsair_vengeance_rgb_pro, 16, 3200, 110).
memoria_ram(crucial_ballistix_sport_lt, 16, 3000, 90).
memoria_ram(kingston_hyperx_predator, 16, 2666, 95).
memoria_ram(kingston_hyperx_fury, 8, 2666, 60).
memoria_ram(kingston_hyperx_fury, 8, 2400, 50).

% Ventiladores para procesador
ventilador_procesador(corsair_h100i_rgb_platinum, corsair, 240, [am4, lga_1151, lga_1200], 160).
ventilador_procesador(noctua_nh_d15, noctua, 140, [am4, lga_1151, lga_1200], 100).
ventilador_procesador(cooler_master_hyper_212_rgb, cooler_master, 120, [am4, lga_1151, lga_1200], 66).
ventilador_procesador(enermax_ets_t50_axe, enermax, 120, [am4, lga_1151], 80).

% Tarjetas gráficas
tarjeta_grafica(rtx_3080, nvidia, 10, gddr6x, pcie_4, 700, 320).
tarjeta_grafica(rx_6900_xt, amd, 16, gddr6, pcie_4, 1000, 300).
tarjeta_grafica(gtx_1660_super, nvidia, 6, gddr6, pcie_3, 300, 125).
tarjeta_grafica(rx_5600_xt, amd, 6, gddr6, pcie_4, 350, 150).
tarjeta_grafica(gtx_1650, nvidia, 4, gddr5, pcie_3, 200, 75).
tarjeta_grafica(rx_550, amd, 2, gddr5, pcie_3, 130, 50).

% Discos duros
disco_duro(wd_black_sn850, 2000, nvme, 300).
disco_duro(samsung_970_evo_plus, 1000, nvme, 200).
disco_duro(samsung_970_evo_plus, 500, ssd, 120).
disco_duro(seagate_barracuda, 1000, 7200, 50).
disco_duro(western_digital_blue, 2000, 5400, 65).

% Fuentes de poder
fuente_poder(cooler_master_mwe_gold_750_full_modular, 750, gold, 130).
fuente_poder(corsair_rm850x, 850, gold, 160).
fuente_poder(seasonic_focus_gm_650, 650, bronze, 90).
fuente_poder(corsair_vs450, 450, white, 50).
fuente_poder(thermaltake_smart_500w, 500, white, 40).

% Monitores
monitor(lg_27uk850_w, uhd_4k, 60, 500).
monitor(dell_u2419h, wqhd, 60, 300).
monitor(aoc_c24g1, full_hd, 144, 230).
monitor(asus_vg245h, full_hd, 75, 200).
monitor(viewsonic_vx2457_mhd, hd, 75, 180).

% Clientes
cliente(juan, [intel, amd], [asus, msi, gigabyte], 1500).
cliente(maria, [amd, intel], [asus, gigabyte, asrock], 2000).
cliente(pedro, [intel], [msi, asus], 1200).
cliente(laura, [amd], [gigabyte, asrock], 800).
cliente(carlos, [intel, amd], [asrock, msi], 1800).
cliente(ana, [amd], [asus, gigabyte], 1000).
cliente(luis, [intel], [msi, asrock, gigabyte], 1500).
cliente(patricia, [amd], [asus, msi], 900).
cliente(diego, [intel, amd], [gigabyte, asrock], 700).
cliente(sara, [intel], [asus, msi], 1300).


% 1. Recomendar una motherboard dado el nombre del procesador
ultimoDeLista([Ultimo],Ultimo).
ultimoDeLista([_|Cola],Ultimo):- ultimoDeLista(Cola,Ultimo).

recomendar_motherboard(Procesador, LMotherboards):-
	findall((PlacaMadre, MaxMemoria, PrecioMotherboard), % A encontrar
	(procesador(Procesador, _, Socket, _, _, _, _, LFrecuenciasP,PrecioProcesador,Gen, _),
	 ultimoDeLista(LFrecuenciasP, MaxRAMProcesador),
	 motherboard(PlacaMadre, _, _,Socket, _, MaxMemoria, LFrecuenciasMotherboard, PrecioMotherboard,GeneracionesMotherboard),
	 PrecioMotherboard < PrecioProcesador+50,
	 member(MaxRAMProcesador,LFrecuenciasMotherboard),
	 member(Gen, GeneracionesMotherboard)),
	 LMotherboards). % Lista de retorno
% Consulta: recomendar_motherboard(amd_athlon_3000g,LMotherboards).

% 2. Recomendar procesadores dado el nombre de una motherboard
recomendar_procesador(Motherboard, LProcesadores):-
	findall((Procesador, Marca, Nucleos, FrecuenciaMaxima, Precio, Gen),
	(motherboard(Motherboard, _, _, Socket, _, _, LFrecuenciasM, _, LGenMotherboard),
	 procesador(Procesador, Marca, Socket, Nucleos, _, _, FrecuenciaMaxima, FrecuenciasRAM, Precio, Gen, _),
	 ultimoDeLista(FrecuenciasRAM, MaxRAMProcesador),
	 member(MaxRAMProcesador, LFrecuenciasM),
	 member(Gen, LGenMotherboard)),
	LProcesadores).
% Consulta:  recomendar_procesador(asrock_a320m_hdv_r4_0,Lprocesadores).

% 3. Dado el nombre del procesador, recomendar ventiladores compatibles y contarlos
contar([],0). %caso-base
contar([_|Cola],T):- contar(Cola,P), T is 1 + P.

recomendar_ventilador(Procesador, LVentiladores):- findall((Ventilador, Tamanio, PrecioV),
	(procesador(Procesador, _, Socket, _, _, _, _, _, _, _, _),
	ventilador_procesador(Ventilador, _, Tamanio, LCompatibilidadSocket, PrecioV),
	member(Socket,LCompatibilidadSocket)),
	LVentiladores), contar(LVentiladores,T), write("Total de ventiladores compatibles: "), write(T).
% Consulta: recomendar_ventilador(intel_core_i9_11900k, LVentiladores).

% 4. Recomendar una memoria RAM dado un procesador y motherboard, teniendo en cuenta las frecuencias
recomendar_RAM(Procesador, Motherboard,  Memorias) :-
procesador(Procesador, _, Socket, _, _, _, _, FrecuenciasProcesador, _,_, _), 
motherboard(Motherboard, _, _, Socket, _, _, FrecuenciasMotherboard, _,_),
findall((Memoria, Capacidad, Frecuencia, Precio), (memoria_ram(Memoria, Capacidad, Frecuencia, Precio), 
		member(Frecuencia, FrecuenciasProcesador), 
		member(Frecuencia,FrecuenciasMotherboard)), Memorias).
% Consulta: recomendar_RAM(amd_ryzen_5_5600, asus_rog_strix_b450f,  Memorias).

% 5. Recomendar una combinación de procesador y tarjeta gráfica compatible para un motherboard específico y un presupuesto máximo.
recomendar_combinacion(Motherboard, Presupuesto, L) :- 
findall((Procesador,TarjetaGrafica),
	(
		motherboard(Motherboard, _, _, Socket, _, _, LFrecuenciasM, _, LGenMotherboard),
		procesador(Procesador, _, Socket, _, _, _, _, FrecuenciasRAM, PrecioProcesador, Generacion, _),
		ultimoDeLista(FrecuenciasRAM, MaxRAMProcesador),
		member(MaxRAMProcesador, LFrecuenciasM),
		tarjeta_grafica(TarjetaGrafica, _, _, _, _, PrecioTarjeta,_),
		Presupuesto > PrecioProcesador+PrecioTarjeta,
		member(Generacion, LGenMotherboard),
		PrecioTarjeta > PrecioProcesador-100
	),
L).
% Consulta: recomendar_combinacion(asus_rog_strix_z590e,500,L).

% 6. Cual es el procesador, la gráfica y la motherboard mas costosa?
mayorPrecio([Cabeza|[]],Cabeza).
mayorPrecio([Cabeza|Cola],M):- mayorPrecio(Cola, P), (P > Cabeza -> M is P ; M is Cabeza).

componentesMasCostosos(Procesador, Tarjeta, Motherboard):- listaPrecios(LProcesadores, LGraficas, LMotherboards),
mayorPrecio(LProcesadores,MayorProcesador), procesador(Procesador, _, _, _, _, _, _, _, MayorProcesador, _, _),
mayorPrecio(LGraficas,MayorGrafica), tarjeta_grafica(Tarjeta, _, _, _, _, MayorGrafica,_),
mayorPrecio(LMotherboards,MayorMotherboard), motherboard(Motherboard, _, _, _, _, _, _, MayorMotherboard, _).

listaPrecios(LProcesadores, LGraficas, LMotherboards):- 
findall(PrecioProcesador, procesador(_, _, _, _, _, _, _, _, PrecioProcesador, _, _), LProcesadores),
findall(PrecioTarjeta, tarjeta_grafica(_, _, _, _, _, PrecioTarjeta,_), LGraficas),
findall(PrecioMotherboard, motherboard(_, _, _, _, _, _, _, PrecioMotherboard, _), LMotherboards).

% Consulta: componentesMasCostosos(Procesador, Tarjeta, Motherboard).

% 7. Cual es el procesador, la gráfica mas y la motherboard menos costosa?
menorPrecio([Cabeza|[]],Cabeza).
menorPrecio([Cabeza|Cola],M):- menorPrecio(Cola, P), (P < Cabeza -> M is P ; M is Cabeza).

componentesMenosCostosos(Procesador, Tarjeta, Motherboard):- listaPrecios(LProcesadores, LGraficas, LMotherboards),
menorPrecio(LProcesadores,MayorProcesador), procesador(Procesador, _, _, _, _, _, _, _, MayorProcesador, _, _),
menorPrecio(LGraficas,MayorGrafica), tarjeta_grafica(Tarjeta, _, _, _, _, MayorGrafica, _),
menorPrecio(LMotherboards,MayorMotherboard), motherboard(Motherboard, _, _, _, _, _, _, MayorMotherboard, _).

% Consulta: componentesMenosCostosos(Procesador, Tarjeta, Motherboard).

% 8. Cual es el valor total de todos los discos duros?

sumarPrecios([],0). % caso-base
sumarPrecios([Cabeza|Cola],T):- sumarPrecios(Cola,P), T is Cabeza + P.

totalDiscos(Total):- listaDiscos(LDiscos), sumarPrecios(LDiscos, Total).
listaDiscos(LDiscos):- findall(PrecioDisco, disco_duro(_, _, _, PrecioDisco), LDiscos). 

% Consulta: totalDiscos(Total).

% 9. Recomendar una fuente de poder dada una tarjeta gráfica, dar el nombre de la de mayor y menor precio
recomendar_fuente(Tarjeta, FuenteMenor, FuenteMayor):- 
findall(PrecioFuente,
	(tarjeta_grafica(Tarjeta, _, _, _, _, _, TDP),
	 fuente_poder(_, Potencia, _, PrecioFuente),
	 Potencia > TDP*2),
	LPreciosFuentes),
menorPrecio(LPreciosFuentes, MenorFuente), fuente_poder(FuenteMenor, _, _, MenorFuente),
mayorPrecio(LPreciosFuentes, MayorFuente), fuente_poder(FuenteMayor, _, _, MayorFuente).

% Consulta: recomendar_fuente(rtx_3080, FuenteMenor, FuenteMayor).

 % 10. Recomendar una fuente de poder dada una tarjeta gráfica, motherboard y procesador, dar el nombre de la de mayor y menor precio
recomendarFuenteComponentes(Tarjeta, Motherboard, Procesador,FuenteMenor, FuenteMayor):- 
findall(PrecioFuente,
	(tarjeta_grafica(Tarjeta, _, _, _, _, _, TDPGrafica),
	 motherboard(Motherboard, _, _, _, Slots, _, _, _, _),
	 procesador(Procesador, _, _, _, _, _, _, _, _, _, TDPProcesador),
	 fuente_poder(_, Potencia, _, PrecioFuente),
	 Potencia > TDPGrafica*2+Slots*6+TDPProcesador+50),
	LPreciosFuentes),
menorPrecio(LPreciosFuentes, MenorFuente), fuente_poder(FuenteMenor, _, _, MenorFuente),
mayorPrecio(LPreciosFuentes, MayorFuente), fuente_poder(FuenteMayor, _, _, MayorFuente).

% Consulta: recomendarFuenteComponentes(rtx_3080, asrock_z590_taichi, intel_core_i9_11900k,FuenteMenor, FuenteMayor).

% 11. Recomendar tarjeta gráfica dado el nombre de un procesador
recomendar_grafica(Procesador, LTarjetas):- findall(Tarjeta, 
	(procesador(Procesador, _, _, Nucleos, _, _, _, _, PrecioProcesador, _, _),
	 tarjeta_grafica(Tarjeta, _, Memoria, _, _, PrecioTarjeta, _),
	 Memoria > Nucleos,
	 PrecioTarjeta > PrecioProcesador),
	LTarjetas).

% Consulta: recomendar_grafica(intel_core_i5_11600k, LTarjetas).

% 12. Recomendar un computador completo dado un procesador

recomendarComputadorProcesador(Procesador, NombreMotherboard, RAM, Gb, Ventilador, Tarjeta, FuenteMayor, Monitor, Disco) :-
	recomendar_motherboard(Procesador, LMotherboards), % Encontrar Motherboards compatibles dado el procesador
	nth0(0, LMotherboards, (NombreMotherboard, _, _)), % Encontrar el nombre de la primera motherboard de la lista
	recomendar_RAM(Procesador, NombreMotherboard,  Memorias), % Encontrar RAMs compatibles dado el procesador y la motherboard
	nth0(0, Memorias, (RAM, Gb, _)), % Encontrar el nombre y las Gb de la primera ram de la lista
	recomendar_ventilador(Procesador, LVentiladores), % Encontrar ventiladores compatibles dado el procesador
	nth0(0, LVentiladores, (Ventilador, _, _)), % Encontrar el nombre del ventilador
	recomendar_grafica(Procesador, LTarjetas), % Encotrar graficas compatibles con el procesador
	ultimoDeLista(LTarjetas,Tarjeta), % Encontrar el nombre de la tarjeta
	recomendarFuenteComponentes(Tarjeta, NombreMotherboard, Procesador,_, FuenteMayor), % Recomendar fuente de poder
	findall((PrecioMonitor),monitor(_,_,_,PrecioMonitor),Lmonitores),
	findall((PrecioDisco),disco_duro(_,_,_,PrecioDisco),LDiscos),
	mayorPrecio(Lmonitores, MayorMonitor), monitor(Monitor, _, _, MayorMonitor),
	mayorPrecio(LDiscos, MayorDisco), disco_duro(Disco, _, _, MayorDisco).

% Consulta: recomendarComputadorProcesador(intel_core_i5_11600k,Mother,RAM,Gb,Ventilador,Tarjeta,Fuente,Monitor,Disco).

% 13. Recomendar todos lo componentes de un computador dado el presupuesto de un cliente
imprimir([]):-!.%caso-base
imprimir([X|Y]):- write(X),nl,imprimir(Y).

recomendarComputadorPresupuesto(Presupuesto, LComponentes):-
findall((Procesador, Motherboard, RAM, Ventilador, Tarjeta, Fuente, Monitor, Disco),
	(procesador(Procesador, _, Socket, Nucleos, _, _, _, LFrecuenciasP, PrecioProcesador, Gen, TDPProcesador),
	 motherboard(Motherboard, _, _, Socket, _, Slots, LFrecuenciasM, PrecioMotherboard, LGenMotherboard),
	 memoria_ram(RAM, _, Frecuencia, PrecioRam),
	 ventilador_procesador(Ventilador, _, _, LCompatibilidadSocket, PrecioVentilador),
	 tarjeta_grafica(Tarjeta, _, Memoria, _, _, PrecioTarjeta, TDPGrafica),
	 fuente_poder(Fuente, Potencia, _, PrecioFuente),
	 monitor(Monitor, _, _, PrecioMonitor),
	 disco_duro(Disco, _, _, PrecioDisco),
	 member(Frecuencia, LFrecuenciasP),
	 member(Frecuencia, LFrecuenciasM),
	 member(Socket, LCompatibilidadSocket),
	 member(Gen, LGenMotherboard),
	 Potencia > TDPGrafica*2+Slots*6+TDPProcesador+50,
	 Memoria > Nucleos,
	 Presupuesto > PrecioProcesador+PrecioMotherboard+PrecioRam+PrecioVentilador+PrecioTarjeta+PrecioFuente+PrecioMonitor+PrecioDisco),
	LComponentes).
	%imprimir(LComponentes).

% Consulta: recomendarComputadorPresupuesto(800, LComponentes).

% 14. Dada una marca, encontrar los interesados y los componentes de esa marca
encontrarComponentes(Marca, LInteresados, LComponentes):-
    findall(Cliente,
            (cliente(Cliente, MarcasProcesador, MarcasMotherboard, _),
             (member(Marca, MarcasProcesador);
              member(Marca, MarcasMotherboard))),
            LInteresados),
    findall((Procesador, Motherboard),
            (procesador(Procesador, Marca, _, _, _, _, _, _, _, _, _);
             motherboard(Motherboard, Marca, _, _, _, _, _, _, _)),
            LComponentes).

% Consulta: encontrarComponentes(intel, LInteresados,LComponentes).

% 15. Dado un cliente recomendar componentes, con sus preferencias y con su presuspuesto

recomendarComputadorCliente(Cliente, LComponentes):-
findall((Procesador, Motherboard, RAM, Ventilador, Tarjeta, Fuente, Monitor, Disco),
	(cliente(Cliente, MarcasProcesador, MarcasMotherboard, Presupuesto),
	 procesador(Procesador, MarcaP, Socket, Nucleos, _, _, _, LFrecuenciasP, PrecioProcesador, Gen, TDPProcesador),
	 motherboard(Motherboard, MarcaM, _, Socket, _, Slots, LFrecuenciasM, PrecioMotherboard, LGenMotherboard),
	 memoria_ram(RAM, _, Frecuencia, PrecioRam),
	 ventilador_procesador(Ventilador, _, _, LCompatibilidadSocket, PrecioVentilador),
	 tarjeta_grafica(Tarjeta, _, Memoria, _, _, PrecioTarjeta, TDPGrafica),
	 fuente_poder(Fuente, Potencia, _, PrecioFuente),
	 monitor(Monitor, _, _, PrecioMonitor),
	 disco_duro(Disco, _, _, PrecioDisco),
	 member(Frecuencia, LFrecuenciasP),
	 member(Frecuencia, LFrecuenciasM),
	 member(Socket, LCompatibilidadSocket),
	 member(Gen, LGenMotherboard),
	 member(MarcaP, MarcasProcesador),
	 member(MarcaM, MarcasMotherboard),
	 Potencia > TDPGrafica*2+Slots*6+TDPProcesador+50,
	 Memoria > Nucleos,
	 Presupuesto > PrecioProcesador+PrecioMotherboard+PrecioRam+PrecioVentilador+PrecioTarjeta+PrecioFuente+PrecioMonitor+PrecioDisco),
	LComponentes).
	%imprimir(LComponentes).

% Consulta: recomendarComputadorCliente(Laura, LComponentes).