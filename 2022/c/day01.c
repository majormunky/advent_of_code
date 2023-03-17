#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "common.h"


int compare( const void* a, const void* b) {
   int int_a = * ( (int*) a );
   int int_b = * ( (int*) b );

   // an easy expression for comparing
   return (int_a > int_b) - (int_a < int_b);
}


int part1(const char *filename) {
  char *result = read_from_file(filename);
  if (!result) {
        return -1;
    }

    char *line;
    int current_gnome = 0;
    int largest_gnome = 0;
    
    while ((line = strsep(&result, "\n"))) {      
      if (strlen(line) == 0) {
		// We are done counting this gnome's calories
		// if our current gnomes size is bigger than the largest
		if (current_gnome > largest_gnome) {
		  // set the largest gnome to the current gnome size
		  largest_gnome = current_gnome;
		}

		// reset the current gnome size
		current_gnome = 0;
      } else {
		int line_as_int = atoi(line);
		current_gnome += line_as_int;
      }
    }

    free(result);

    return largest_gnome;
}


int part2(const char *filename) {
  char *file_data = read_from_file(filename);

  char *line;

  int array_size = 1000;
  int biggest_gnomes[array_size];
  int b_index = 0;
  int current_gnome = 0;

  for (int i = 0; i < array_size; i++) {
	biggest_gnomes[i] = 0;
  }

  while ((line = strsep(&file_data, "\n"))) {
	if (strlen(line) == 0) {
	  biggest_gnomes[b_index] = current_gnome;
	  b_index++;

	  if (b_index > array_size) {
		fputs("Error, array too small to hold all values", stderr);
		return -1;
	  }

	  current_gnome = 0;
	} else {
	  int line_as_int = atoi(line);
	  current_gnome += line_as_int;
	}
  }

  free(file_data);

  int result = 0;

  qsort(biggest_gnomes, array_size, sizeof(int), compare);

  result += biggest_gnomes[array_size - 1];
  result += biggest_gnomes[array_size - 2];
  result += biggest_gnomes[array_size - 3];
  
  return result;
}


int main(int argc, char **argv) {
    if (argc < 2) {
        fputs("Need an argument.\n", stderr);
        return -1;
    }

    int part1_result = part1(argv[1]);
    int part2_result = part2(argv[1]);
    
    printf("Part 1: %d\n", part1_result);
    printf("Part 2: %d\n", part2_result);
}
