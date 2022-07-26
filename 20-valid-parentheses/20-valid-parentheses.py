class Solution:
    def isValid(self, s: str) -> bool:
        #The stack to keep track of opening paranthesis
        stack = []
        
        #Hash map for keeping track of mappings. This keeps the code very clean.
        #Also makes adding more types of paranthesis easier
        mapping = {")": "(", "}": "{", "]":"["}
        
        #for every bracket in the expression
        for char in s:
            
            #if the character is an closing bracket
            if char in mapping:
                
                #pop the topmost element from the stack, if it is non empty
                #otherwise assign a dummy variable of "#" to the top_element variable
                top_element = stack.pop() if stack else "#"
                
                #The mapping for the opening bracket in our hash and the top 
                #element of the stack dont match, return False
                if mapping[char] != top_element:
                    return False
            
            else:
                #we have an opening bracket, simply push it onto the stack
                stack.append(char)
        
        #in the end, if the stack is empty, then we have a valid expression
        #The stack wont be empty for cases like ((()
        return not stack