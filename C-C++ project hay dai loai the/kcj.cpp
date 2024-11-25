#include <stdio.h>
int main(){
	int age = 24;
	char name[]="Suzuhara Asahi";
	char description[]="Software Engineer, Tokyo";
	float salary_per_month= 3500.5;
	printf("Boku wa %s desu\n", name);
	printf("%dsai desu\n", age);
	printf("ima wa %s desu\n", description);
	printf("Boku no okane wa %.2f desu, douzo yoroshiku onegaishimasu", salary_per_month);
}
