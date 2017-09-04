public class Vector {
    protected double x;
    protected double y;

    public Vector(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public Vector add(Vector other) {
        return new Vector(this.x + other.x, this.y + other.y);
    }

    public Vector negate() {
        return new Vector(-this.x, -this.y);
    }

    public Vector subtract(Vector other) {
        return this.add(other.negate());
    }

    public double dot(Vector other) {
        return this.x * other.x + this.y * other.y;
    }

    public double magnitude() {
        return Math.sqrt(this.dot(this));
    }

    public double cross(Vector other) {
        return this.x * other.y - this.y * other.x;
    }

    public String toString() {
        return "" + this.x + "," + this.y;
    }

    public static void main(String[] args) {
        Vector v = new Vector(1, 0);
        Vector w = new Vector(0, 1);

        System.out.println(v.dot(w));
        System.out.println(v.cross(w));
        System.out.println(v.add(w));
        System.out.println(v.negate());
        System.out.println(v.add(w).magnitude());
    }
}
