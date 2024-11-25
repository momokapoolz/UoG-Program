#include <stdio.h>
void hamsapxep(int so[], int size){
	for(int i=0;i<size-1;i++){
		for(int j=0;j<size-i;j++){
			if(so[j+1]<so[j]){
				int temp = so[j+1];
				so[j+1] = so[j];
				so[j] = temp;
			}
		}
	}
}
void xuat(int so[], int size){
	for(int i=0;i<size;i++){
		printf("%d\t", so[i]);
	}

}
int main(){
	int so[]={1,5,3,7,4,6,2,9};
	int size = sizeof(so)/sizeof(so[0]);
	hamsapxep(so, size);
	xuat(so, size);
}
	
    
