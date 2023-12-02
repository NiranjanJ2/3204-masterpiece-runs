int motor1 = 3;
int motor2 = 5;
int motor3 = 7;


void setup() {
  // put your setup code here, to run once:
  //pinMode(pwm,OUTPUT) ;  	//we have to set PWM pin as output
  pinMode(motor3,OUTPUT) ; 	//Logic pins are also set as output
  pinMode(motor2,OUTPUT) ;
  pinMode(motor1,OUTPUT);
}

int dol(){
  delay(1000);
}
int re(){
  analogWrite(motor1, 255);
  analogWrite(motor3, 255);
  delay(1000);
  analogWrite(motor1, 0);
  analogWrite(motor3, 0);
}
int mi(){
  analogWrite(motor2, 255);
  analogWrite(motor1, 255);
  delay(1000);
  analogWrite(motor2, 0);
  analogWrite(motor1, 0); 
}
void loop() {
  // put your main code here, to run repeatedly:
  mi();
  re();
  dol();
  re();
  mi();
  mi();
  mi();
  re();
  re();
  re();
  mi();
  mi();
  mi();
  mi();
  re();
  dol();
  re();
  mi();
  mi();
  re();
  re();
  mi();
  re();
  dol();


}
