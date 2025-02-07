package Basic_Java;


class Person {
    private String name;  // Private fields (hidden from outside)
    private int age;

    // Constructor
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter method (allows read access)
    public String getName() {
        return name;
    }

    // Setter method (allows controlled write access)
    public void setAge(int age) {
        if (age > 0) {  // Adding validation
            this.age = age;
        } else {
            System.out.println("Age must be positive!");
        }
    }

    public int getAge() {
        return age;
    }
}

public class first {
    public static void main(String[] args) {
        Person p = new Person("John", 25);
        System.out.println(p.getName() + " is " + p.getAge() + " years old.");
        p.setAge(5);  
        System.out.println(p.getName() + " is " + p.getAge() + " years old.");
    }
}
