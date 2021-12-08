#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

int twoArg(const float temp, const float vel);

// ***************** main **********************
int
main(const int argc, const char* argv[])
{

  float temp;
  float vel;

  // interpret arguments
  if (argc == 1) {
    // no arguments (other than the command) - run no arg output
    noArg();

  } else if (argc == 2) {
    // one argument - run one arg output
    str2float(argv[1], &temp);
    if (-99 < temp && temp < 50) {
      oneArg(temp);
    } else {
      // error message if input is not in range
      printf("%s: Temperature must be less than 50F and greater than -99F.\n", argv[0]);
    }

  } else if (argc == 3) {
    // two arguments - run two arg output
    str2float(argv[1], &temp);
    str2float(argv[2], &vel);
    if ((-99 < temp && temp < 50) && (0.5 <= vel)) {
      twoArg(temp, vel);
    } else {
      // error messages, which vary depending on what went wrong
      if (vel < 0.5) {
        printf("%s: Wind velocity must be greater than or equal to 0.5 MPH.\n", argv[0]);
      }
      if (-99 >= temp || temp >= 50) {
        printf("%s: Temperature must be less than 50F and greater than -99F.\n", argv[0]);
      }
    }

  } else {
    // too many arguments
    printf("usage: %s [temperature] [velocity]\n", argv[0]);
    exit(2);

  }

  printf("\n");
  return 0;
}

// ***************** noArg **********************
/*
 * Runs wind chill output without any specification to temperature or velocity
 * uses temp from -10 to 40 by 10's, and vel from 5 to 15 by 5's
 */
int
noArg()
{
  printf("%5s  %5s  %5s\n", "Temp", "Wind", "Chill");
  printf("%5s  %5s  %5s\n", "-----", "-----", "-----");


  const float temps[] = {-10, 0, 10, 20, 30, 40};
  const float vels[] = {5, 10, 15};
  float chill;

  for (int t = 0; t < 6; t++) {
    for (int v = 0; v < 3; v++) {\
      chill = calculate(temps[t], vels[v]);
      printf("%5.1f  %5.1f  %5.1f\n", temps[t], vels[v], chill);
    }
  }

  return 0;
}