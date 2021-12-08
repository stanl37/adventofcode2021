#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

int LIST_SIZE = 2001;

// ***************** main **********************
int
main(const int argc, const char* argv[])
{ 

  int list[LIST_SIZE];
  int list_index = 0;
  int val;

  // parsing stdin
    while ((val = getchar()) && (val != EOF)) { 
      ungetc(val, stdin);
      if (scanf("%d", &val) == 1) {
        list[list_index] = val;
        list_index++;
      }
    }

  // print the list
  for (int i = 0; i < list_index; i++) {
    printf("%d,",list[i]);
  }

  int increaseds = 0;

  // count increases
  for (int i = 1; i < list_index; i++) {
    int last = list[i-1];
    int curr = list[i];
    if (curr > last) {
      increaseds++;
    }
  }

  // print increaseds
  printf("\n");
  printf("there were %d measurements larger than the previous.", increaseds);
  
  printf("\n");
  return 0;

}