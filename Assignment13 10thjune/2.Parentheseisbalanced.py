#2. Given a string containing just the characters '(', ')', '{', '}', '['and ']', determine if the input string is valid.
#Examples:
#Input: "()" Output: Valid
#Input: "()[]{}" Output: Valid
#Input: "([)]" Output: Not Valid


def Paranthesis(expr) : 
	stack = [] 
	for char in expr: 
		if char in ["(", "{", "["]:  
			stack.append(char) 
		else: 
			if not stack: 
				return False
			current_char = stack.pop() 
			if current_char == '(': 
				if char != ")": 
					return False
			if current_char == '{': 
				if char != "}": 
					return False
			if current_char == '[': 
				if char != "]": 
					return False 
	if stack: 
		return False
	return True
 
if __name__== "__main__" : 
	expr = "[]{([])}"; 
	if Paranthesis(expr) : 
		print("Valid"); 
	else : 
		print("Not Valid"); 
