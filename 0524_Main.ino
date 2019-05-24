int onboardLED = 13;            
int voltageThreshold = 600;
int minhold =0;
int count=0;
int test1=0,test2=0,test3=0;
void setup() {
  Serial.begin(9600);
  pinMode(onboardLED, OUTPUT);
}

void loop() {
  int currentVoltage = analogRead(A0);  
  currentVoltage = currentVoltage;

  test1 = currentVoltage;
  test2 = test1;
  test3 = test2;

  currentVoltage = (test1+test2+test3)/3 ;
  if(count>200){
    if(currentVoltage > voltageThreshold){
       // trigger actions
       Serial.println(" CONTRACTION!"); 
       digitalWrite(onboardLED, HIGH);  
    } 
    else if (currentVoltage<= minhold){
        Serial.println(" STAY...");
        currentVoltage = minhold;
       digitalWrite(onboardLED, LOW); 
    }
    else {
        Serial.println("");            
       digitalWrite(onboardLED, LOW); 
       
    }
  }
  //------------------------------------------------------
  else if(count<50){
    minhold+=currentVoltage;
    count++;
    count++;
    Serial.println("측정중"); 
  }else if(count>=50 && count<100){
    minhold=(minhold/25)*1.2;
    count=120;
     Serial.print("평균 대기 값은");
     Serial.println (minhold);
     Serial.print("힘빡주세요");
     delay(1000);
  }
  //---------------------------------------------------------
  else if(count>=110&&count<170){
    voltageThreshold+=currentVoltage;
    count++;
    count++;
    Serial.println("측정중"); 
  }else if(count>=170 &&count<190){
    voltageThreshold=(voltageThreshold/25);
    count=220;
     Serial.print("평균 대기 값은");
     Serial.println (voltageThreshold);
     delay(1000);
  }
  Serial.print(count); 
  Serial.print(" : "); 
  Serial.print(currentVoltage);        

  delay(200);
}
