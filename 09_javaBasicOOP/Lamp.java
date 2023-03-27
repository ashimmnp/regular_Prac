class Lamp{
    boolean isOn;//variable for storing the value 
    //declaring a first method when lamp is turned on.
    void turnon(){
        isOn = true;
        System.out.println("Light on? " +isOn);
    }
    //declaring another method when lamp is turned off.
    void turnoff(){
        isOn = false;
        System.out.println("Light on? " +isOn);
        
    }
}
/* class main{
    public static void main(String args[]){
        Lamp led = new Lamp();
        Lamp halogen = new Lamp();
        
        led.turnon();
        
        halogen.turnoff();
    }
}
*/