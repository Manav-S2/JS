class Planet{
     int a =  1;
     int b(){
        System.out.println("Hi Planet");
        return 8 + 4;}
     public static void main(String[] args){
        Planet Earth = new Planet();
        System.out.printf("%d, %d", Earth.a, Earth.b());


        }
     }