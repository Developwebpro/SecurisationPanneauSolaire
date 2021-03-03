#include <Servo.h>

Servo servo_9;
int angle = 35;

void setup() {
  Serial.begin(9600);
  pinMode(8, INPUT); //Bouton d'arrêt d'urgence
  pinMode(10, INPUT); //Bouton de remise en marche après arrêt
  servo_9.attach(9); //Pin du Servo
  servo_9.write(angle); //Angle initial du Servo
  readSerialPort(); //Lecture de l'angle envoyé par le Raspberry
}

void loop() {
  readSerialPort();
  
  if (digitalRead(8) == HIGH) {
    //Serial.println("Mise en sécurité du panneau");
    securePanneau(); //Mise en sécurité du panneau
  }
  else if(digitalRead(10) == HIGH) {
    //Remise en marche du panneau après un arrêt
    //Serial.println("Remise en marche");
    readSerialPort(); //Lecture de l'angle envoyé par le Raspberry
  }
}

void readSerialPort() {
  angle = 0; //Mise de l'angle à 0
  if (Serial.available() > 0) { //Si le port série est dispo
    delay(1); //Attendre 1 secondes
    angle = Serial.parseInt(); //Conversion de l'angle en entier
    servo_9.write(angle); //Passage de l'angle au Servo
    Serial.print("0");
    //Serial.flush(); //Attend la fin de la transmission des données série
  }
}

void securePanneau() {
  angle = 0;
  servo_9.write(angle);
  Serial.print("1");
}
