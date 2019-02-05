public class MathsOper {
	public static void main(String[] args) {
		double a,b,res=0;
		char c;

		a=Integer.parseInt(args[0]);
		c=args[1].charAt(0);
		b=Integer.parseInt(args[2]);
		System.out.println(a + " " + c + " " + b );

		switch(c)
		{
			case '+' :
				res=a+b;
				break;
			case '-' :
				res=a-b;
				break;
			case '*' :
				res=a*b;
				break;
			case '/' :
				if(Math.abs(b) <= Double.MIN_VALUE){
					System.out.println("Divide by zero error");
					System.exit(0);
				}
				else{

					res=a/b;
				}
				break;
			default :
				System.out.println("Invalid Entry");
				System.exit(0);
		}
		System.out.println("Result is : "+res);
	}
}
