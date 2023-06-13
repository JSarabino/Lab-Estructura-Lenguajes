package practica_12;
import java.io.Console;
import static java.lang.System.console;
import java.util.InputMismatchException;
import org.jpl7.*;
import java.util.Scanner;


/**
 *
 * @author juan sarabino
 */
public class Practica_12 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        //Cargar base del conocimiento y reglas        
        String t = "consult('practica_12.pl')";
        Query q1 = new Query(t);
        System.out.println(t+""+(q1.hasSolution()?"satisfactoria":"insatisfactoria"));
        
        //Manejo del menú
        Scanner scanner = new Scanner(System.in);
        boolean salir = false;
        int opcion;
        
        while (!salir) {
 
            System.out.println("------ MENÚ ------");
            System.out.println("1. Recomendar una motherboard dado el nombre del procesador.");
            System.out.println("2. Recomendar procesadores dado el nombre de una motherboard.");
            System.out.println("3. Dado el nombre del procesador, recomendar ventiladores compatibles.");
            System.out.println("4. Recomendar una memoria RAM dado un procesador y motherboard.");
            System.out.println("5. Recomendar procesador y tarjeta gráfica dada una motherboard y un presupuesto.");
            System.out.println("6. Cual es el procesador, la gráfica y la motherboard mas costosa?");
            System.out.println("7. Cual es el procesador, la gráfica y la motherboard menos costosa?");
            System.out.println("8. Cual es el valor total de todos los discos duros?");
            System.out.println("9. Recomendar una fuente de poder dada una tarjeta gráfica, da el nombre de la de mayor y menor precio.");
            System.out.println("10. Recomendar fuente de poder dada una tarjeta gráfica, motherboard y procesador, da el nombre de la de mayor y menor precio.");
            System.out.println("11. Recomendar tarjeta gráfica dado el nombre de un procesador.");
            System.out.println("12. Recomendar un computador completo dado un procesador.");
            System.out.println("13. Recomendar todos lo componentes de un computador dado el presupuesto de un cliente.");
            System.out.println("14. Dada una marca, encontrar los interesados y los componentes de esa marca.");
            System.out.println("15. Dado un cliente recomendar ensambles, con sus preferencias, con su presuspuesto.");
            System.out.println("0. Salir");
            System.out.println("-------------------");
            
 
            try {
                //Manejo de peticiones
                String procesador;
                String motherboard;
                String presupuesto;
                String tarjeta;
                String marca;
                String cliente;
                
                //Manejo de opciones
                System.out.print("Ingrese una opción: ");
                opcion = scanner.nextInt();
 
                switch (opcion) {
                    case 1:
                        System.out.println("Consulta en SWI-Prolog: recomendar_motherboard(amd_athlon_3000g,LMotherboards).");
                        System.out.println("Motherboard compatible: ");
                        procesador = pedirProcesador();
                        regla1(procesador);
                        break;
                    case 2:
                        System.out.println("Consulta en SWI-Prolog: recomendar_procesador(asrock_a320m_hdv_r4_0,Lprocesadores).");
                        System.out.println("Procesador compatible: ");
                        motherboard = pedirMotherboard();
                        regla2(motherboard);
                        break;
                    case 3:
                        System.out.println("Consulta en SWI-Prolog: recomendar_ventilador(intel_core_i9_11900k, LVentiladores).");
                        System.out.println("Ventilador compatible: ");
                        procesador = pedirProcesador();
                        regla3(procesador);
                        break;
                    case 4:
                        System.out.println("Consulta en SWI-Prolog: recomendar_RAM(amd_ryzen_5_5600, asus_rog_strix_b450f,  Memorias).");
                        System.out.println("Memoria RAM compatible: ");
                        procesador = pedirProcesador();
                        motherboard = pedirMotherboard();
                        regla4(procesador,motherboard);
                        break;
                    case 5:
                        System.out.println("Consulta en SWI-Prolog: recomendar_combinacion(asus_rog_strix_z590e,500,L).");
                        System.out.println("Procesador y tarjeta gráfica: ");
                        motherboard = pedirMotherboard();
                        presupuesto = pedirPresupuesto();
                        regla5(motherboard,presupuesto);
                        break;
                    case 6:
                        System.out.println("Consulta en SWI-Prolog: componentesMasCostosos(Procesador, Tarjeta, Motherboard).");
                        System.out.println("Procesador, gráfica y motherboard mas costosa: ");
                        regla6();
                        break;
                    case 7:
                        System.out.println("Consulta en SWI-Prolog: componentesMenosCostosos(Procesador, Tarjeta, Motherboard).");
                        System.out.println("Procesador, gráfica y motherboard menos costosa: ");
                        regla7();
                        break;
                    case 8:
                        System.out.println("Consulta en SWI-Prolog: totalDiscos(Total).");
                        System.out.println("El valor total de los discos es de: ");
                        regla8();
                        break;
                    case 9:
                        System.out.println("Consulta en SWI-Prolog: recomendar_fuente(rtx_3080, FuenteMenor, FuenteMayor).");
                        tarjeta = pedirTarjeta();
                        System.out.println("Fuentes recomendadas: ");
                        regla9(tarjeta);
                        break;
                    case 10:
                        System.out.println("Consulta en SWI-Prolog: recomendarFuenteComponentes(rtx_3080, asrock_z590_taichi, intel_core_i9_11900k,FuenteMenor, FuenteMayor).");
                        tarjeta = pedirTarjeta();
                        motherboard = pedirMotherboard();
                        procesador = pedirProcesador();
                        System.out.println("Fuentes recomendadas:");
                        regla10(tarjeta,motherboard,procesador);
                        break;
                    case 11:
                        System.out.println("Consulta en SWI-Prolog: recomendar_grafica(intel_core_i5_11600k, LTarjetas).");
                        procesador = pedirProcesador();
                        regla11(procesador);
                        break;
                    case 12:
                        System.out.println("Consulta en SWI-Prolog: recomendarComputadorProcesador(intel_core_i5_11600k,Mother,RAM,Gb,Ventilador,Tarjeta,Fuente,Monitor,Disco).");
                        procesador = pedirProcesador();
                        System.out.println("Partes del Computador: ");
                        regla12(procesador);
                        break;
                    case 13:
                        System.out.println("Consulta en SWI-Prolog: recomendarComputadorPresupuesto(800, LComponentes).");
                        presupuesto = pedirPresupuesto();
                        System.out.println("Combinaciones de computador: ");
                        regla13(presupuesto);
                        break;
                    case 14:
                        System.out.println("Consulta en SWI-Prolog: encontrarComponentes(intel, LInteresados,LComponentes).");
                        marca = pedirMarca();
                        regla14(marca);
                        break;
                    case 15:
                        System.out.println("Consulta en SWI-Prolog: recomendarComputadorCliente(Laura, LComponentes).");
                        cliente = pedirCliente();
                        regla15(cliente);
                        break;
                    case 0:
                        salir = true;
                        System.out.println("Saliendo del programa...");
                        break;
                    default:
                        System.out.println("Opción inválida. Por favor, ingrese una opción válida.");
                        break;
                }
                
                System.out.println();
                
            } catch (InputMismatchException e) {
                System.out.println("Debes ingresar un número");
                scanner.next();
            }
        }

    }
    
    public static String pedirProcesador() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el nombre del procesador: ");
        String procesador = scanner.nextLine();
        return procesador;
    }
    
    public static String pedirMotherboard() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el nombre de la motherboard: ");
        String motherboard = scanner.nextLine();
        return motherboard;
    }
    
    public static String pedirPresupuesto() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el presupuesto: ");
        String presupuesto = scanner.nextLine();
        return presupuesto;
    }
    
    public static String pedirTarjeta() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese la tarjeta: ");
        String tarjeta = scanner.nextLine();
        return tarjeta;
    }
    
    public static String pedirMarca() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese la marca: ");
        String marca = scanner.nextLine();
        return marca;
    }
    
    public static String pedirCliente() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el cliente: ");
        String cliente = scanner.nextLine();
        return cliente;
    }
    
    public static void regla1(String procesador) {
                        String t1 = "recomendar_motherboard('" + procesador + "', LMotherboards)";
                        Query qRegla1 = new Query(t1);
                        String Resregla1 = qRegla1.oneSolution().get("LMotherboards").toString();
                        System.out.println("Motherboards: " + Resregla1);
    }
    
    public static void regla2(String motherboard) {
                        String t2 = "recomendar_procesador('" + motherboard + "', LProcesadores)";
                        Query qRegla2 = new Query(t2);
                        String Resregla2 = qRegla2.oneSolution().get("LProcesadores").toString();
                        System.out.println("Procesadores: " + Resregla2);
    }
    
    public static void regla3(String procesador) {
                        String t3 = "recomendar_ventilador('" + procesador + "', LVentiladores)";
                        Query qRegla3 = new Query(t3);
                        String Resregla3 = qRegla3.oneSolution().get("LVentiladores").toString();
                        System.out.println("Ventiladores: " + Resregla3);
    }
    
    public static void regla4(String procesador, String motherboard) {
                        String t4 = "recomendar_RAM('" + procesador + "','" + motherboard + "', LVentiladores)";
                        Query qRegla4 = new Query(t4);
                        String Resregla4 = qRegla4.oneSolution().get("LVentiladores").toString();
                        System.out.println("RAMs: " + Resregla4);
    }
    
    public static void regla5(String motherboard, String presupuesto) {
                        String t5 = "recomendar_combinacion('" + motherboard + "'," + presupuesto + ", L)";
                        Query qRegla5 = new Query(t5);
                        String Resregla5 = qRegla5.oneSolution().get("L").toString();
                        System.out.println("Combinaciones: " + Resregla5);
    }
    
    public static void regla6() {
                        String t6 = "componentesMasCostosos(Procesador, Tarjeta, Motherboard)";
                        Query qRegla6 = new Query(t6);
                        String ResPregla6 = qRegla6.oneSolution().get("Procesador").toString();
                        String ResTregla6 = qRegla6.oneSolution().get("Tarjeta").toString();
                        String ResMregla6 = qRegla6.oneSolution().get("Motherboard").toString();
                        System.out.println("Procesador: " + ResPregla6);
                        System.out.println("Tarjeta: " + ResTregla6);
                        System.out.println("Motherboard: " + ResMregla6);
    }
    
    public static void regla7() {
                        String t7 = "componentesMenosCostosos(Procesador, Tarjeta, Motherboard)";
                        Query qRegla7 = new Query(t7);
                        String ResPregla7 = qRegla7.oneSolution().get("Procesador").toString();
                        String ResTregla7 = qRegla7.oneSolution().get("Tarjeta").toString();
                        String ResMregla7 = qRegla7.oneSolution().get("Motherboard").toString();
                        System.out.println("Procesador: " + ResPregla7);
                        System.out.println("Tarjeta: " + ResTregla7);
                        System.out.println("Motherboard: " + ResMregla7);
    }
    
    public static void regla8() {
                        String t8 = "totalDiscos(Total)";
                        Query qRegla8 = new Query(t8);
                        String Resregla8 = qRegla8.oneSolution().get("Total").toString();
                        System.out.println("$" + Resregla8);

    }
    
    public static void regla9(String tarjeta) {
                        String t9 = "recomendar_fuente('" + tarjeta + "', FuenteMenor, FuenteMayor)";
                        Query qRegla9 = new Query(t9);
                        String ResFMeregla9 = qRegla9.oneSolution().get("FuenteMenor").toString();
                        String ResFMaregla9 = qRegla9.oneSolution().get("FuenteMayor").toString();
                        System.out.println("Fuente de menor precio: " + ResFMeregla9);
                        System.out.println("Fuente de mayor precio: " + ResFMaregla9);
    }
    
    public static void regla10(String tarjeta, String motherboard, String procesador) {
                        String t10 = "recomendarFuenteComponentes('" + tarjeta + "','" + motherboard + "','" + procesador + "', FuenteMenor, FuenteMayor)";
                        Query qRegla10 = new Query(t10);
                        String ResFMeregla10 = qRegla10.oneSolution().get("FuenteMenor").toString();
                        String ResFMaregla10 = qRegla10.oneSolution().get("FuenteMayor").toString();
                        System.out.println("Fuente de menor precio: " + ResFMeregla10);
                        System.out.println("Fuente de mayor precio: " + ResFMaregla10);
    }
    
    public static void regla11(String procesador) {
                        String t11 = "recomendar_grafica('" + procesador + "', LTarjetas)";
                        Query qRegla11 = new Query(t11);
                        String Resregla11 = qRegla11.oneSolution().get("LTarjetas").toString();
                        System.out.println("Tarjetas graficas: " + Resregla11);
    }
    
    public static void regla12(String procesador) {
                        String t12 = "recomendarComputadorProcesador('" + procesador + "', NombreMotherboard, RAM, Gb, Ventilador, Tarjeta, FuenteMayor, Monitor, Disco)";
                        Query qRegla12 = new Query(t12);
                        String ResMregla12 = qRegla12.oneSolution().get("NombreMotherboard").toString();
                        String ResRregla12 = qRegla12.oneSolution().get("RAM").toString();
                        String ResGregla12 = qRegla12.oneSolution().get("Gb").toString();
                        String ResVregla12 = qRegla12.oneSolution().get("Ventilador").toString();
                        String ResTregla12 = qRegla12.oneSolution().get("Tarjeta").toString();
                        String ResFregla12 = qRegla12.oneSolution().get("FuenteMayor").toString();
                        String ResMoregla12 = qRegla12.oneSolution().get("Monitor").toString();
                        String ResDregla12 = qRegla12.oneSolution().get("Disco").toString();
                        System.out.println("Motherboard: " + ResMregla12);
                        System.out.println("RAM: " + ResRregla12);
                        System.out.println("Gb RAM: " + ResGregla12);
                        System.out.println("Ventilador: " + ResVregla12);
                        System.out.println("Tarjetas grafica: " + ResTregla12);
                        System.out.println("Fuente de poder: " + ResFregla12);
                        System.out.println("Monitor: " + ResMoregla12);
                        System.out.println("Disco duro: " + ResDregla12);
    }
    
    public static void regla13(String presupuesto) {
                        String t13 = "recomendarComputadorPresupuesto(" + presupuesto + ", LComponentes)";
                        Query qRegla13 = new Query(t13);
                        String Resregla13 = qRegla13.oneSolution().get("LComponentes").toString();
                        System.out.println(Resregla13);
    }
    
    public static void regla14(String marca) {
                        String t14 = "encontrarComponentes(" + marca + ", LInteresados, LComponentes)";
                        Query qRegla14 = new Query(t14);
                        String ResIregla14 = qRegla14.oneSolution().get("LInteresados").toString();
                        String ResCregla14 = qRegla14.oneSolution().get("LComponentes").toString();
                        System.out.println("Interesados en la marca: " + marca);
                        System.out.println(ResIregla14);
                        System.out.println("Componentes de la marca: " + marca);
                        System.out.println(ResCregla14);
    }
    
    public static void regla15(String cliente) {
                        String t15 = "recomendarComputadorCliente(" + cliente + ", LComponentes)";
                        Query qRegla15 = new Query(t15);
                        String Resregla15 = qRegla15.oneSolution().get("LComponentes").toString();
                        System.out.println("Recomendaciones para el cliente: " + cliente);
                        System.out.println(Resregla15);
    }
    
}
