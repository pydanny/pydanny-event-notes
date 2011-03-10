#pragma once
#include <stddef.h>

int subprocess(const char *path, const char *in_data, size_t in_len, char **out_data, size_t *out_len);
