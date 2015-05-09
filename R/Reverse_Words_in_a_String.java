
 /**
 Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.
 **/



 public String reverseWords(String s) {
        String trim=" "+s.trim();
		char[] chararray=trim.toCharArray();
		String word="";
		StringBuffer buffer=new StringBuffer();
		for (int i = chararray.length-1; i>=0; i--) {

			if(!String.valueOf(chararray[i]).equals(" ")){
				word+=chararray[i];
			}else{

				if(buffer.toString().lastIndexOf(" ")!=buffer.length()-1){
					//如果bu是最后一个有空格
					buffer.append(" ");
				}

				StringBuffer re=new StringBuffer(word);
				re.reverse();
				buffer.append(re);
				word="";
			}

		}
		return buffer.toString().trim();
    }