PK
     wNq��M�  �     blinking-name.ino/*  =====Wiring Schematics=====
    D6: LED (OUTPUT)
*/

int led1  = D6;
int p_led = D7;

const int UNIT = 100;

int morse_units(char morse_component){
    /*  Translates a morse code component into the correct
        number of morse units. 
        Returns a positive number for a sound, and a negative number for a pause.
        A return value of 0 indicates an error
        
        Inputs:  morse_component: '.' '-' ' ' '_'
        Returns: [3, 1, -1, -3, -7]
    */
    
    switch(morse_component){
        case '.':   //dit
            return 1;
        case '-':   //dah
            return 3;
        case ' ':   //char space
            return -3;
        case '_':   //word space
            return -7;
    }   
    return 0;      //component space
}

void setup() {
    pinMode(led1,  OUTPUT);
    pinMode(p_led, OUTPUT);
}

void loop() {
    String phrase = ".--. .- ..- .-.._- --- -- --- .. .- --. .-_...-.-"; //PAUL TOMOIAGA <SK> in morse 
                                                                         //<SK> = End of transmission
    
    for(int i = 0; i < phrase.length(); i++){
        char morse_component = phrase.charAt(i);
        int units = morse_units(morse_component);
        
        if(units > 0){
            delay(UNIT);    //component space
            digitalWrite(led1, HIGH);
            delay(UNIT*units);  //dit or dah
            digitalWrite(led1, LOW);
        }else{
            delay(UNIT*-units); //char or word space
        }
    }
    delay(UNIT*20); //wait some time
}
PK 
     wNq��M�  �                   blinking-name.inoPK      ?   )    