class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<String>();
        backTrack(0,0,n,res,"");
        return res;
    }
    public void backTrack(int openN, int closeN, int n, List<String> res, String curr){
        if (openN == closeN && closeN == n){
            res.add(curr);
            return;
        }
        if (openN < n){
            backTrack(openN+1, closeN, n, res, curr + "(");
        }
        if (closeN < openN){
            backTrack(openN, closeN+1, n, res, curr + ")");
        }
    }
}