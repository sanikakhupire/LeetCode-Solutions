class Solution {
    public boolean isValid(String s) {
        
        HashMap<Character, Character> check = new HashMap<>();

        check.put(')', '(');
        check.put('}', '{');
        check.put(']', '[');

        Stack<Character> ans = new Stack<>();

        for (char i : s.toCharArray()){
            if (!check.containsKey(i)){
                ans.push(i);
            }
            else if (!ans.isEmpty() && check.get(i) == ans.peek()){
                ans.pop();
            }
            else {
                return false;
            }
        }
        return ans.isEmpty();
    }
}