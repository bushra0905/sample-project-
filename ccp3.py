public class FirstClass1
 {
    public static void Addition() 
{
        Integer a = 4;
        Integer b = 5;
        Integer c = a + b; 
        Integer d = 4 + 5;  
        Integer e = a + 5
        System.debug('Addition (a + b) = ' + c);
        System.debug('Addition (4 + 5) = ' + d);
        System.debug('Addition (a + 5) = ' + e);
    }
    public static void Subtraction() 
{
        Integer a = 4;
        Integer b = 5;
        Integer c1 = a - b;  
        Integer d1 = b - a;  
        Integer e1 = 4 - 5;  
        Integer f1 = a - 5; 
        System.debug('Subtraction (a - b) = ' + c1);
        System.debug('Subtraction (b - a) = ' + d1);
        System.debug('Subtraction (4 - 5) = ' + e1);
        System.debug('Subtraction (a - 5) = ' + f1);
    }
    public static void Multiplication() {
        Integer a = 4;
        Integer b = 5;
        Integer c = a * b;  
        Integer d = 4 * 5;  
        Integer e = a * 5;  
        System.debug('Multiplication (a * b) = ' + c);
        System.debug('Multiplication (4 * 5) = ' + d);
        System.debug('Multiplication (a * 5) = ' + e);
        Integer f = -4;
        Integer g = a * f;  
        System.debug('Multiplication (a * f) = ' + g);
    }
    public static void Division()
 {
        Integer a = 4;
        Integer b = 5;
        Integer c = a / b;  
        Integer d = 4 / 5;
        Integer e = a / 5;
        System.debug('Division (a / b) = ' + c);
        System.debug('Division (4 / 5) = ' + d);
        System.debug('Division (a / 5) = ' + e);
        Decimal cDecimal = (Decimal)a / (Decimal)b; 
        System.debug('Decimal Division (a / b) = ' + cDecimal);
    }
}
 
