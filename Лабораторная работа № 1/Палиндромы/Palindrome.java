//Показывает, является ли строка палиндромом. 
public class Palindrome {
	public static void main(String[] args) {
		for (int i = 0; i < args.length; i++) {
			String s = args[i];
			System.out.println(s + " = " + isPalindrome(reverseString(s)));
		}
	}
	//Полностью изменяет символы в строке.
	public static String reverseString(String a) {
		String s = "";
		for(int i=0; i<a.length(); i++)
			s = s + a.charAt(a.length()-i-1);
		return s;
	}
	//Переворачивает слово s, а затем сравнивает с первоначальными данными.
	public static boolean isPalindrome(String s) {
		String a = "";
		for(int i=0; i<s.length(); i++)
			a = a + s.charAt(s.length()-i-1);
		if(a.equals(s))
			return true;
		else
			return false;
	}
}