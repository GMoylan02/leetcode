class Solution {
    public void reverseString(char[] s) {
        char l;
        int len = s.length;
        for (int i = 0; i < ((int)len/2); i++){
            l = s[i];
            s[i] = s[len-1-i];
            s[len-1-i] = l;
        }
    }
}