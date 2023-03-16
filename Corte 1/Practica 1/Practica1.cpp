#include <iostream>
#include <stdlib.h>
#include <string>

using namespace std;

//Declarar la estructura
struct Estudiante
{
    //Componentes de la estructura
    int codigo;
    string nombre;
    int telefono;
    int edad;
};

void llenar(Estudiante vE[], int n){
	for(int i=0; i<n; i++){
		cout <<"Ingresar datos estudiante"<< (i+1) << endl;
		cout <<"Digite codigo"<<endl;
		cin >>vE[i].codigo;
		cout <<"Digite nombre"<<endl;
		fflush(stdin);
		getline(cin, vE[i].nombre);
		cout <<"Digite telefono"<<endl;
		cin >>vE[i].telefono;
		cout <<"Digite edad"<<endl;
		cin >>vE[i].edad;
		
	}
}

void mostrar(Estudiante vE[], int n){
	for(int i=0; i<n; i++){
		cout <<"Estudiante "<< (i+1) << endl;
		cout <<"Codigo: "<<vE[i].codigo<<endl;
		cout <<"Nombre: "<<vE[i].nombre<<endl;
		cout <<"Telefono: "<<vE[i].telefono<<endl;
		cout <<"Edad: "<<vE[i].edad<<endl;
	}
}

bool validar(Estudiante vE[], int n, int cod){
	for(int i=0; i<n; i++){
		if (vE[i].codigo == cod){
			return true;
		}
	}
	return false;
}

Estudiante consultar(Estudiante vE[], int n, int cod){
	Estudiante est;
	for(int i=0; i<n; i++){
		if (vE[i].codigo == cod){
			est = vE[i];
		}
	}
	return est;
} 

void mayorEdad(Estudiante vE[], int n){
	int mayor = vE[0].edad;
	for (int i=0; i<n; i++){
		if(mayor < vE[i].edad){
			mayor = vE[i].edad;
		}
	}
	
	for(int i=0; i<n; i++){
		if(vE[i].edad == mayor){
			cout <<"Estudiante "<< (i+1) << endl;
			cout <<"Codigo: "<<vE[i].codigo<<endl;
			cout <<"Nombre: "<<vE[i].nombre<<endl;
			cout <<"Telefono: "<<vE[i].telefono<<endl;
			cout <<"Edad: "<<vE[i].edad<<endl;
		}
	}

}

void menorEdad(Estudiante vE[], int n){
	int menor = vE[0].edad;
	for (int i=0; i<n; i++){
		if(menor > vE[i].edad){
			menor = vE[i].edad;
		}
	}

	for(int i=0; i<n; i++){
		if(vE[i].edad == menor){
			cout <<"Estudiante "<< (i+1) << endl;
			cout <<"Codigo: "<<vE[i].codigo<<endl;
			cout <<"Nombre: "<<vE[i].nombre<<endl;
			cout <<"Telefono: "<<vE[i].telefono<<endl;
			cout <<"Edad: "<<vE[i].edad<<endl;
		}
	}
}

int main()
{
	int t, op;
	do{
		cout <<"Digite tamanio de la struct estudiante"<<endl;
		cin >>t;
	}while(t<=0);
	//Declarar el array de struct
	struct Estudiante vE[t];
	
	llenar(vE, t);
	
	do{
		cout <<"Digite la funcionalidad a realizar"<<endl;
		cout <<"1. Mostrar la struct estudiante"<<endl;
		cout <<"2. Validar estudiante"<<endl;
		cout <<"3. Consultar estudiante"<<endl;
		cout <<"4. Estudiante (s) de mayor y menor edad de la estructura"<<endl;
		cout <<"5. Salir"<<endl;
		cin >>op;
		
		switch(op){
			case 1: 
				mostrar(vE, t);
				break;
				
			case 2:
				int cod;
				bool encontrado;
				cout << "Digite codigo a validar" << endl;
				cin >>cod;
				encontrado = validar(vE, t, cod);
				if (encontrado == false){
					cout << "Estudiante NO registrado" << endl;
				}else{
					cout << "Estudiante registrado" << endl;
				}
				break;
			
			case 3:
				int codB;
				bool encontradoB;
				cout << "Digite codigo a consultar" << endl;
				cin >>codB;
				encontradoB = validar(vE, t, codB);
				if (encontradoB == false){
					cout << "Estudiante NO registrado" << endl;
				}else{
					Estudiante est;
					est = consultar(vE, t, codB);
					cout <<"Codigo: "<<est.codigo<<endl;
					cout <<"Nombre: "<<est.nombre<<endl;
					cout <<"Telefono: "<<est.telefono<<endl;
					cout <<"Edad: "<<est.edad<<endl;
				}
				break;

			case 4:
				cout << "Estudiante (s) de mayor edad:" << endl;
				mayorEdad(vE, t);
				cout << "Estudiante (s) de menor edad:" << endl;
				menorEdad(vE, t);
				break;

			case 5:
				system("exit");
				break;
		}
	}while(op!=5);
	
	return 0;
}







