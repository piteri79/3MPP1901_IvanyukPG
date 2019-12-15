/** трёхмерный класс точки. **/
public class Point3d {
	/** координата X **/
	private double xCoord;
	/**  координата Y **/
	private double yCoord;
	/**  координата Z **/
	private double zCoord;
	/** Конструктор инициализации **/
	public Point3d ( double x,  double y,  double z) {
		xCoord = x;
		yCoord = y;
		zCoord = z;
	}
	/** Конструктор по умолчанию. **/
	public Point3d () {
	//Вызовите конструктор с тремя параметрами и определите источник.
		this(0, 0, 0);
	}
	/** Возвращение координаты X **/
	public double getX () {
		return xCoord;
	}
	/** Возвращение координаты Y **/
	public double getY () {
		return yCoord;
	}
	/** Возвращение координаты Z **/
	public double getZ () {
		return zCoord;
	}
	/** Установка значения координаты X. **/
	public void setX ( double val) {
		xCoord = val;
	}
	/**  Установка значения координаты Y. **/
	public void  setY ( double val) {
		yCoord = val;
	}
	/**  Установка значения координаты Z. **/
	public void  setZ ( double val) {
		zCoord = val;
	}
	/** Cравнениt значений двух трёхмерных объектов **/
	public boolean compare (Object a, Object b) {
		if(a == b)
			return true;
		else
			return false;
	}
	//Вычисляет расстояние между двумя точками
	public double distanceTo (double a,double b,double c,double d) {
		double rx = Math.abs((a-b)/2);
		double ry = Math.abs((c-d)/2);
		return Math.sqrt((rx*rx)+(ry*ry));
	}
}