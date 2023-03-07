#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "common.h"


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
  int result = 0;

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
