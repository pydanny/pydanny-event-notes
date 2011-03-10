#include "subprocess.h"
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int subprocess(const char *path, const char *in_data, size_t in_len, char **out_data, size_t *out_len)
{
    int pipe_stdin[2], pipe_stdout[2];
    pid_t pid;
    
    pipe(pipe_stdin);
    pipe(pipe_stdout);
    
    pid = fork();
    if(pid)
    {
        int ret_val;
        size_t len = 0, size=1024, n;
        char *out = malloc(1024);
        close(pipe_stdin[0]);
        close(pipe_stdout[1]);
        write(pipe_stdin[1], in_data, in_len);
        close(pipe_stdin[1]);
        waitpid(pid, &ret_val, 0);
        while((n = read(pipe_stdout[0], out+len, size-len)) > 0)
        {
            len += n;
            if(len == size)
            {
                size *= 10;
                realloc(out, size);
            }
        }
        close(pipe_stdout[0]);
        if(out_data) *out_data = out;
        if(out_len) *out_len = len;
        return ret_val;
    }
    else
    {
        close(pipe_stdin[1]);
        close(pipe_stdout[0]);
        dup2(pipe_stdin[0], 0);
        dup2(pipe_stdout[1], 1);
        execl(path, path, NULL);
        exit(404);
    }
}