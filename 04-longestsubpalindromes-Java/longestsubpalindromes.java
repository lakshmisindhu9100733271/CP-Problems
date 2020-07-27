// # Write the function longestSubpalindrome(s), that takes a string s and returns 
// the longest palindrome that occurs as consecutive characters (not just letters, but 
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!") 
// # returns "b-4-b". If there is a tie, return the lexicographically larger value -- 
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce") 
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions, 
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also, 
// from the explanation above, we see that longestSubpalindrome("aba") is "aba", 
// and longestSubpalindrome("a") is "a".
import java.util.*;

class longestsubpalindromes {
	
	public Object[] substring(String a){
		ArrayList<String>al=new ArrayList<String>();
		int i=0;
		int k=0;
		while(i<a.length()){
		    int j=0;
		    while (i+j<=a.length()){
    		    if (a.substring(i,i+j).length()>0){
    		        al.add(a.substring(i,i+j));
		        }
		        j++;
		    }
		    i++;
		}
		Object [] ss=al.toArray();
		return ss;
	}
	public String fun_longestsubpalindromes(String s){
		Object[]ss=substring(s);
		int l=0;
		String word="";
		for (int i=0;i<ss.length;i++){
			String p=(String)ss[i];
			   StringBuilder sb = new StringBuilder(p);
			   StringBuilder rev=sb.reverse();
			   if(p.equals(rev.toString())){
				   if(p.length()>=l){
					   l=p.length();
					   word=(String)ss[i];

				   }
			   }
		}
		return word;
	}
	public static void main(String[]args){

	}
}


		
	
