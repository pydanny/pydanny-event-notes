#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>

#include "handler.h"

#define HTTP_PORT 8089
#define REQUEST_BUFFER_SIZE (1024*1024)

void die(const char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
    int listenfd, sockfd;
    struct sockaddr_in listen_addr = {0};
    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    if (listenfd < 0) 
        die("Unable to open socket");
    listen_addr.sin_family = AF_INET;
    listen_addr.sin_addr.s_addr = INADDR_ANY;
    listen_addr.sin_port = htons(HTTP_PORT);
    if (bind(listenfd, (struct sockaddr *)&listen_addr, sizeof(listen_addr)) < 0) 
        die("Unable to bind()");
    listen(listenfd, 32);
    while(1)
    {
        struct sockaddr_in client_addr = {0};
        socklen_t addr_len;
        char *request = malloc(REQUEST_BUFFER_SIZE);
        addr_len = sizeof(client_addr);
        sockfd = accept(listenfd, (struct sockaddr *) &client_addr, &addr_len);
        if (sockfd < 0) 
            die("Unable to accept new connection");
        read(sockfd, request, REQUEST_BUFFER_SIZE);
        handle_request(sockfd, request);
        close(sockfd);
        free(request);
    }
    close(listenfd);
    return 0;
}
