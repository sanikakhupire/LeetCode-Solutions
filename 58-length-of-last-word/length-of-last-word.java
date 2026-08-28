class Solution {
    public int lengthOfLastWord(String s) {
        int i = s.length() - 1;
        while (i >= 0 && s.charAt(i) == ' ') {
            i = i - 1;
        }
        int res = 0;
        while (i >= 0 && s.charAt(i) != ' ') {
            res = res + 1;
            i -= 1;
        }
        return res;
    }
}
