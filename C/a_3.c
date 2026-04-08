#include <stdio.h>

int main() {
    int a;
    int fat;

    scanf("%d", &a);
  
    for(int i = 0; i < a; i++) {
      int height, weight;   
      float bmi;              

      scanf("%d %d", &height, &weight);

      bmi = weight / ((height / 100.0) * (height / 100.0));

      if(bmi >= 25) {
        fat += 1;
      }
    }

    printf("%d", fat);
    
    return 0;
}