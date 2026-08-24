class Solution {
    public boolean repeatedSubstringPattern(String s) {
        String newString = s + s;
        String subPart = newString.substring(1,newString.length()-1);
        return subPart.contains(s);
    }
}