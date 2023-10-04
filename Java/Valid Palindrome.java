class Solution {
    public boolean isPalindrome(String s) {
        s = format(s.toLowerCase());

        int len = s.length();
        for (int i = 0; i < (len/2); i++){
            if (s.charAt(i) != s.charAt(len-1-i)){
                return false;
            }
        }
        return true;
    }
    static String format(String s){
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if (((int)ch >= 97 && (int)ch <= 122) || (int)ch >= 48 && (int)ch <= 57){
                result.append(ch);
            }
        }
        return result.toString();
    }
}