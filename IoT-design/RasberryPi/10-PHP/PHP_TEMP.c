#include <stdio.h>
#include <stdint.h>
#include <wiringPi.h>

#define MAX_TIME 100
#define PIN 7

int val[5] = {0,0,0,0,0};

int main(void){
        uint8_t lststate = 1;
        uint8_t cnt = 0;
        uint8_t j=0,i;

        if(wiringPiSetup() == -1) return 1;
	pullUpDnControl(PIN,PUD_UP);
        pinMode(PIN,OUTPUT);

        digitalWrite(PIN,LOW);
        delay(18);
        digitalWrite(PIN,HIGH);
        delayMicroseconds(40);
        pinMode(PIN,INPUT);

        for(i=0;i<MAX_TIME;i++){
                cnt=0;

                while(digitalRead(PIN) == lststate){
                        cnt++;
                        delayMicroseconds(1);
                        if(cnt == 255) break;
                }

                lststate = digitalRead(PIN);

                if(cnt == 255) break;

                if((i>=4) && (i%2==0)){
                        val[j/8]<<=1;
                        if(cnt>50) val[j/8]|=1;
                        j++;
                }
        }

        if((j>=40) && (val[4] == ((val[0]+val[1]+val[2]+val[3]) & 0xFF))){
             printf("%d",val[2]);
        }else 
	     printf("-1");
}
