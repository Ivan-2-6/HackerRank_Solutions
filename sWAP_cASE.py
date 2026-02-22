# --- Method 1: The Beginner Loop (Imperative) ---
# Time: O(N) | Space: O(N) 
# Note: In older Python versions, string concatenation (+=) was O(N^2), 
# but modern Python optimizes it to O(N). Still, it's considered clunky.
def swap_case_loop(s):
    result = ""
    for char in s:
        if char.isupper():
            result += char.lower()
        elif char.islower():
            result += char.upper()
        else:
            result += char
    return result

# --- Method 2: God-Tier Generator Expression (Memory Optimized) ---
# Time: O(N) | Space: O(1) extra space!
def swap_case_generator(s):
    # at a time directly to the .join() method. Highly efficient for massive texts.
    return "".join(char.lower() if char.isupper() else char.upper() if char.islower() else char for char in s)

#--- Method 5: The Built-in Cheat Code (Production Grade) ---
# Time: O(N) | Space: O(N)
# Note: This is written in highly optimized C code under the hood. 
# It is the fastest possible way to do it in a real-world application.
def swap_case_builtin(s):
    return s.swapcase()
