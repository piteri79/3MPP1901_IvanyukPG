//Класс вычисления площади треугольника по формуле Герона
public class Lab1 {
	private static Point3d obj1 = new Point3d();
	private static Point3d obj2 = new Point3d();
	private static Point3d obj3 = new Point3d();
	//основной метод, проверяющий ввод пользователя
	public static void main (String[] args) {
		if(args.length == 9)
			System.out.println(computeArea(args));
		else if(args.length < 9)
			System.out.println("too small parametrs");
		else
			System.out.println("too many parametrs");
	}
	//Ввод данных и вычисление площади
	public static double computeArea(String[] s) {
		obj1.setX(Double.parseDouble(s[0]));
		obj1.setY(Double.parseDouble(s[1]));
		obj1.setZ(Double.parseDouble(s[2]));
		obj2.setX(Double.parseDouble(s[3]));
		obj2.setY(Double.parseDouble(s[4]));
		obj2.setZ(Double.parseDouble(s[5]));
		obj3.setX(Double.parseDouble(s[6]));
		obj3.setY(Double.parseDouble(s[7]));
		obj3.setZ(Double.parseDouble(s[8]));
		double a = obj1.distanceTo(obj1.getX(),obj2.getX(),obj1.getY(),obj2.getY());
		double b = obj1.distanceTo(obj1.getX(),obj3.getX(),obj1.getY(),obj3.getY());
		double c = obj1.distanceTo(obj2.getX(),obj3.getX(),obj2.getY(),obj3.getY());
		double p = (a+b+c)/2;
		return Math.sqrt(p*(p-a)*(p-b)*(p-c));
	}
}