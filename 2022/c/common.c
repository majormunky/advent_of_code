#include <stdio.h>
#include <stdlib.h>
#include "common.h"

char *read_from_file(const char *filename) {
    long int size = 0;
    FILE *file = fopen(filename, "r");

    if (!file) {
        fputs("File Error.\n", stderr);
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    size = ftell(file);
    rewind(file);

    char *result = (char *) malloc(size);
    if (!result) {
        fputs("Memory Error.\n", stderr);
        fclose(file);
        return NULL;
    }

    if (fread(result, 1, size, file) != size) {
        fputs("Read Error.\n", stderr);
        fclose(file);
        return NULL;
    }

    fclose(file);
    return result;
}
