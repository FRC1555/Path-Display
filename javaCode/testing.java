package javaCode;

interface executor {
    void method();
}

public class testing {

    public static void during(executor x, int position) {
        double b = looper(50);
        if(b != position) {
            System.out.println(b);
        }
        else {
            x.method();
        }
    }

    public static double looper(int a) {
        int i = 0;
        while(i < a) {
            i++;
        }
        return i;
    }

    public static void main(String[] args) {

        during(() -> {
                
        }, 50);


    }
}