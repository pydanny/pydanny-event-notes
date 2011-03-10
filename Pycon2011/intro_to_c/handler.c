#include <string.h>
#include <stdio.h>

#include "handler.h"

void handle_request(int sockfd, const char *request)
{
    int i;
    int b;
    char path[16];
    char msg[100];
    
    for (i=0;i<16;i++) {
        if (request[i] == ' ') {
            i++;
            for (b=0;b<16;b++) {
                if (request[b+i] != ' ') {
                    path[b] = request[b+i]; 
                } else {
                    break;
                }
            }
            break;
        }
    }
    path[b] = '\0';
    snprintf(msg, 100, "HTTP 200 OK\r\n\r\nHello  %s", path);
    write(sockfd, msg, strlen(msg));
}