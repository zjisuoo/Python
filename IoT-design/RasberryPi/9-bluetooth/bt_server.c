#include "bt_master.h"
#include <unistd.h>

int main(){
    int client = init_server();

    char *recv_message;

    while(1){
        recv_message = read_server(client);
        if(recv_message == NULL){
            printf("client disconnected\n");
            break;
        }
        write_server(client, recv_message);
    }
}