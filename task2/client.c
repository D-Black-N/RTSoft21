#include <unistd.h>
#include <stdio.h>

#define O_RDONLY         00

//using namespace std;

int main(){
    int fd;

    fd = open("/dev/test", O_RDONLY);
    while(1) {
        sleep(1);
        unsigned int t = 123;
        unsigned int t2 = 456;

        t2 = read(fd, &t, sizeof(t));

        printf("%d\n", t2);
    }
}