#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

char * get_flag() {
    int     fd;
    char *  flag;
    ssize_t read_bytes;

    if ( ( fd = open( "./flag.txt", O_RDONLY ) ) == -1 ) {
        printf( "couldn't open flag.txt file\n" );
        exit( 1 );
    }

    if ( ( flag = (char *)calloc( 0x50, sizeof( char ) ) ) == NULL ) {
        printf( "calloc failed\n" );
        close( fd );
        exit( 1 );
    }

    if ( ( read_bytes = read( fd, flag, 0x50 ) ) == -1 ) {
        printf( "couldn't read flag.txt file\n" );
        free( flag );
        close( fd );
        exit( 1 );
    }

    close( fd );
    return flag;
}

typedef struct {
    char username[20];
    char password[20];
    char pad[64 - sizeof( char ) * 40];
} User;

typedef struct {
    int  duck;
    char pad[64 - sizeof( int )];
} Secret;

void win() {
    char * flag;
    flag = get_flag();
    printf( "\nhow did you get in here? this is duck's secret storage!\n" );
    printf( "\n%s\n", flag );
    free( flag );
    exit( 0 );
}

void banner() {
    printf( "Welcome to duck's secret storage!\n" );
    printf( "Please enter your username and password to access the secret!~ \n" );
}

int main( int argc, char ** argv ) {
    setbuf( stdin, 0 );
    setbuf( stdout, 0 );

    User *   user;
    Secret * duck;

    user = malloc( sizeof( User ) );
    duck = malloc( sizeof( Secret ) );

    duck->duck = 0xcafebabe;

    banner();

    printf( "\nUsername: " );
    gets( user->username );

    printf( "Password: " );
    gets( user->password );

    if ( strcmp( user->username, "duck" ) ) {
        printf( "Invalid username!\n" );
        exit( 1 );
    }

    printf( "welcome back, %s!\n", user->username );

    if ( duck->duck == 0xdeadbeef ) {
        win();
    } else {
        printf( "Sorry, the secret is not ready yet!\n" );
    }

    return 0;
}