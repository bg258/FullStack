def main():
    import sys

    try:
        # Read all input 
        input_lines = []
        for line in sys.stdin:
            # Exit if the line is empty (Enter pressed without typing)
            if line.strip() == "":
                return "No input provided. Exiting."
            input_lines.append(line.strip())
        
        # Ensure input has exactly 3 lines
        if len(input_lines) < 3:
            return "Insufficient input"
        
        # Parse the input 
        num1 = int(input_lines[0])
        operator = input_lines[1]
        num2 = int(input_lines[2])

        # Perform the operation 
        if operator == "+":
            return num1 + num2
        elif operator == "*":
            return num1 * num2 
        else:
            return "Invalid operator"
    
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        return "Input interrupted by user"
    except Exception as e:
        # Handle unexpected errors
        return f"Error: {e}"
        
if __name__ == "__main__":
    print(main())

# Buka

"""

## Problem Description
In noisy classrooms, teachers often assign tasks to students to keep them engaged. 
One such task involves performing arithmetic operations (addition or multiplication) on two large numbers. 
The program should compute the result of the given operation.

### Problem Link
[Buka - Kattis Problem](https://open.kattis.com/problems/buka)

---

## Input
1. The first line contains a positive integer `a`, the first operand.
2. The second line contains either the character `+` or `*`, representing addition or multiplication, respectively.
3. The third line contains a positive integer `b`, the second operand.

- Both `a` and `b` are powers of 10.
- Each operand consists of at most 100 digits.


## Sample Input/Output

### Sample Input 1
```
1000
*
100
```
### Sample Output 1
```
100000
```

### Sample Input 2
```
10000
+
10
```
### Sample Output 2
```
10010
```

### Sample Input 3
```
10
+
1000
```
### Sample Output 3
```
1010
```

### Sample Input 4
```
1
*
1000
```
### Sample Output 4
```
1000
```

## Solution Outline
1. Read three lines of input:
   - The first operand (`a`).
   - The operator (`+` or `*`).
   - The second operand (`b`).
2. Parse the input and identify the operation.
3. Perform the operation based on the operator:
   - If the operator is `+`, compute `a + b`.
   - If the operator is `*`, compute `a * b`.
4. Print the result.

"""