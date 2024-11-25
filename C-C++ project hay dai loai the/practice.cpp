#include <iostream>
#include <math.h>
bool nt(int n){
	for(int i = 2; i < sqrt(n); i++){
		if(n % i == 0){
			return false;
		}
	}
}
int main(){
	for(int i = 1; i <= 100; i++){
		if (nt(i)){
			printf(i);
		}
	}
	
}

