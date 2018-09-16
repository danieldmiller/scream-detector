 //double num = python_value * 5;
void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
 
}void loop() {
  
  // put your main code here, to run repeatedly:
 double num = 2 ; //erase double
  if (num >=4){
   digitalWrite(13, HIGH);
  } if(num >= 3){
    digitalWrite(12, HIGH);
  }if (num >= 2){
    digitalWrite(11, HIGH);
  }if (num >= 1){
    digitalWrite(10, HIGH);
  }
  
}
