#include <stdio.h>
#include <string.h>
enum day{mon, tue, wed, thu, fri, sat, sun};
int main(){
    char days;
    printf("input the day:");
    scanf("%s", &days);
    while(days!=mon || days!=tue || days!=wed || days!=thu || days !=fri || days!=sat || days!=sun){
        printf("me may beo");
        scanf("%s", &days);
    }
    enum day today = days;
    if(today == sun || today == sat){
        printf("\nweekend");
    }else{
        printf("\nwork");
    }
}