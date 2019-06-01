//센서 변수 초기화
int sensorPalValue = 0;
int sensorSonValue = 0;
float avg = 0.0;

//안정화 작업 변수
float EMA_a = 0.6; //안정화 계수
int EMA_s = 0; //팔뚝
int EMA_s2 = 0; //손목

int EMA_Pal = 0; //팔뚝
int EMA_Son = 0; //손목
  
int onboardLED = 13;

//팔 제한치
int PalMinhold =0;
int PalMaxhold =0;
//손 제한치
int SonMinhold =0;
int SonMaxhold =0;

//카운트
int count=0;

int Paltest1=0; //평균치 구하는 용도1
int Paltest2=0; //평균치 구하는 용도2
int Paltest3=0; //평균치 구하는 용도3

int Sontest1=0; //평균치 구하는 용도1
int Sontest2=0; //평균치 구하는 용도2
int Sontest3=0; //평균치 구하는 용도3

void setup() {
  Serial.begin(9600);
  pinMode(onboardLED, OUTPUT);

  /*int currentPalVoltage = analogRead(A0); //팔뚝
  int currentSonVoltage = analogRead(A1); //손목*/
  
  //EMA_s = sensorValue; //팔뚝
  //EMA_s2 = sensorValue2; //손목
}

void loop() {
  sensorPalValue = analogRead(A0);
  sensorSonValue = analogRead(A1);

  //안정화
  EMA_s = (EMA_a*sensorPalValue) + ((1-EMA_a)*EMA_s);
  EMA_s2 = (EMA_a*sensorSonValue) + ((1-EMA_a)*EMA_s2);

  //평균화
  Paltest3 = Paltest2;
  Paltest2 = Paltest1;
  Paltest1 = EMA_s;
  
  Sontest3 = Sontest2;
  Sontest2 = Sontest1;
  Sontest1 = EMA_s2;

  EMA_Pal = (Paltest1+Paltest2+Paltest3)/3 ;
  EMA_Son = (Sontest1+Sontest2+Sontest3)/3 ;

  //avg는 보정화, 평균화 작업을 모두 마치고 난 두 값의 평균
  avg = (EMA_Pal + EMA_Son) / 2.0;

  
  if(count>200){
    if(EMA_Pal > PalMaxhold)
    {
       Serial.println("PalUP!!!!!!!!"); 
       digitalWrite(onboardLED, HIGH);  
    }
    if(EMA_Son > SonMaxhold)
    {
       Serial.println("SonUP!!!!!!!!"); 
       digitalWrite(onboardLED, HIGH);  
    }
     
    if (EMA_Pal <= PalMinhold)
    {
       Serial.println("Pal STAY...");
       EMA_Pal = PalMinhold;
       digitalWrite(onboardLED, LOW); 
    }
    if (EMA_Son <= SonMinhold)
    {
       Serial.println("Son STAY...");
       EMA_Son = SonMinhold;
       digitalWrite(onboardLED, LOW); 
    }
    
    else 
    {
       Serial.println("");            
       digitalWrite(onboardLED, LOW); 
    }
  }

  //------------------최소값 구하기----------------------
  else if(count<50)
  {
    PalMinhold += EMA_Pal;
    SonMinhold += EMA_Son;
    count += 2;
    Serial.println("측정중"); 
  }
  
  else if(count >= 50 && count < 100)
  {
    PalMinhold=(PalMinhold/25)*1.2;
    SonMinhold=(SonMinhold/25)*1.2;
    count=120;
    Serial.print("평균 Pal 대기 값 : ");
    Serial.println (PalMinhold);
    Serial.print("평균 Son 대기 값 : ");
    Serial.println (SonMinhold);
    Serial.print("힘빡주세요");
    delay(1000);
  }
  
  //------------------최대값 구하기----------------------
  else if(count >= 110&&count < 170)
  {
    PalMaxhold += EMA_Pal;
    SonMaxhold += EMA_Son;
    count += 2;
    Serial.println("측정중"); 
  }
  
  else if(count >= 170 && count < 190)
  {
    PalMaxhold=(PalMaxhold/25);
    SonMaxhold=(SonMaxhold/25);
    
    count = 220;
    Serial.print("평균 Pal 대기 값 : ");
    Serial.println (PalMaxhold);
    Serial.print("평균 Son 대기 값 : ");
    Serial.println (SonMaxhold);
    delay(1000);
  }

  Serial.print(count); 
  Serial.print(" : "); 
  Serial.print(avg);
  Serial.print(" sensorPalValue: "); 
  Serial.print(EMA_Pal); 
  Serial.print(" sensorSonValue: "); 
  Serial.println(EMA_Son);
  
  delay(50);
}
