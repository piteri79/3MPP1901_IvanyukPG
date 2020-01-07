//Находит и выводит все простые числа меньше 100.
public class Primes {
	public static void main(String[] args) {
		for(int i=2; i<=100; i++) {
			if(isPrime(i))
				System.out.print(i + ",");
		}
	}
	//Является ли аргумент простым числом или нет.
	public static boolean isPrime(int n) {
		for(int i=2; i<=(int)Math.sqrt(n); i++) {
			if((n%i) == 0)
				return false;
		}
		return true;
	}
}