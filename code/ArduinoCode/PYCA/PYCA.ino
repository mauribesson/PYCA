/*#include <thermistor.h>*/

const int EchoPin = 5;
const int TriggerPin = 6;
const int BuzPin = 9;
const int temperaturaPin= A0;
const int FotoresistorPin = A1;
const int LedPin = 8;
 
void setup() {
   Serial.begin(9600);
   pinMode(LedPin, OUTPUT);
   pinMode(TriggerPin, OUTPUT);
   pinMode(EchoPin, INPUT);
   

  pinMode(BuzPin, OUTPUT);
  beep(50);
  beep(50);
  beep(50);
  delay(1000);
}
 
void loop() {
//----------------------ULTRASONIDO---------------------------------
  
//   int cm = ping(TriggerPin, EchoPin);
//   Serial.println(cm);
//   if (cm < 10){
//      Serial.println("Entro alguien");
//      beep(200);
//   }


//--------------------------------------------------------------------
   
//----------------------TEPERATURA---------------------------------
   
   float temp = termometro(temperaturaPin);
   if (temp > 16){
      Serial.print(temp);
      Serial.println("Considere encender un ventilador"); 
   }
   delay(1000);
//-------------------------------------------------------------



//---------------------LUZ---------------------------------------------

//   int luzz = fotoresistor(FotoresistorPin);
//   Serial.println(luzz);
//   delay(1000);
//   if (luzz<30){
//      digitalWrite(LedPin , HIGH);   // poner el Pin en HIGH
//      //delay(1000);                   // esperar un segundo
//      //digitalWrite(LedPin , LOW);    // poner el Pin en LOW
//      //delay(1000); 
//    }else{
//      digitalWrite(LedPin , LOW);
//      }

//------------------------------------------------------------------
      
}

int fotoresistor (int FotoresistorPin){
     int luz = analogRead(LedPin);         
     return  luz;
     delay(1000);
}


float termometro(int temperaturaPin){
  //float temperatura = analogRead(temperaturaPin);
  //temperatura = temperatura/9.31;
  //return temperatura;


//----mauri
 int reading = analogRead(temperaturaPin); 
  
 float voltage = reading * 5.0;
 voltage /= 1024.0; 
 
 // print out the voltage
 //Serial.print(voltage); Serial.println(" volts");
 
 // now print out the temperature
 float temperatureC = (voltage - 0.5) * 100 ;  //converting from 10 mv per degree wit 500 mV offset
                                               //to degrees ((voltage - 500mV) times 100)
  //Serial.print(temperatureC); Serial.println(" degrees C");

  return temperatureC;
  
  delay(1000);
  } 
  
int ping(int TriggerPin, int EchoPin) {
   long duration, distanceCm;
   
   digitalWrite(TriggerPin, LOW);  //para generar un pulso limpio ponemos a LOW 4us
   delayMicroseconds(1);
   digitalWrite(TriggerPin, HIGH);  //generamos Trigger (disparo) de 10us
   delayMicroseconds(1);
   digitalWrite(TriggerPin, LOW);
   
   duration = pulseIn(EchoPin, HIGH);  //medimos el tiempo entre pulsos, en microsegundos
   
   distanceCm = duration * 10 / 292/ 2;   //convertimos a distancia, en cm
   return distanceCm;
}


//-----BUZZER--------------
void beep(unsigned char pausa){
  analogWrite(BuzPin, 20);
  delay(pausa);                 // Espera
  analogWrite(BuzPin, 0);            // Apaga
  delay(pausa);                 // Espera
}
