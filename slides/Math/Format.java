public class Format {
    public static void main(String[] args) {
        System.out.printf("%.4f %.2f\n", 1.0, 2.0); // note the values are NOT integers

        System.out.printf("%x %X\n", 255, 234);

        System.out.printf("%04x\n", 255);
    }
}
