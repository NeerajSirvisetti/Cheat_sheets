### **Shell Scripting Cheat Sheet:**

**1. Basics:**
   - **Shebang Line:**
     - Specify the shell to use.
     ```bash
     #!/bin/bash
     ```
   - **Printing:**
     - Display information to the console.
     ```bash
     echo "Hello, Shell!"
     ```
   - **Taking Inputs:**
     - Receive user input.
     ```bash
     read -p "Enter something: " userInput
     ```

**2. Variables:**
   - **Variable Declaration:**
     - Variables are untyped.
     ```bash
     myVar="Hello, Shell!"
     ```
   - **Variable Substitution:**
     - Substitute variable values in strings.
     ```bash
     echo "Value: $myVar"
     ```

**3. Control Flow:**
   - **For Loops:**
     - Iterate over a range of values.
     ```bash
     for i in {0..4}; do
         # code block
     done
     ```
   - **If-Else Statements:**
     ```bash
     if [ condition ]; then
         # code block
     elif [ anotherCondition ]; then
         # code block
     else
         # code block
     fi
     ```

**4. Functions:**
   - **Defining Functions:**
     - Encapsulate reusable code.
     ```bash
     myFunction() {
         # code block
         return $result
     }
     ```

**5. Arrays:**
   - **Array Declaration:**
     ```bash
     myArray=("value1" "value2" "value3")
     ```
   - **Array Operations:**
     ```bash
     # Length
     length=${#myArray[@]}

     # Accessing elements
     element=${myArray[1]}

     # Iterating over elements
     for item in "${myArray[@]}"; do
         # code block
     done
     ```

**6. File Handling:**
   - **Reading from a File:**
     ```bash
     while IFS= read -r line; do
         # code block
     done < "file.txt"
     ```
   - **Writing to a File:**
     ```bash
     echo "Hello, Shell!" > "new_file.txt"
     ```

**7. String Manipulation:**
   - **String Concatenation:**
     ```bash
     string1="Hello, "
     string2="Shell!"
     concatenated="$string1$string2"
     ```
   - **Substring:**
     ```bash
     substring=${myString:7:5}
     ```

**8. Conditional Statements:**
   - **Logical Operators:**
     ```bash
     # AND
     if [ condition1 ] && [ condition2 ]; then
         # code block
     fi

     # OR
     if [ condition1 ] || [ condition2 ]; then
         # code block
     fi
     ```

**9. Case Statements:**
   ```bash
   case "$variable" in
     "value1")
         # code block
         ;;
     "value2")
         # code block
         ;;
     *)
         # default code block
         ;;
   esac
   ```

**10. Exit Status:**
   - **Checking Exit Status:**
     ```bash
     if [ $? -eq 0 ]; then
         # success code block
     else
         # failure code block
     fi
     ```

**11. Command Substitution:**
   ```bash
   result=$(command)
   ```

**12. Pipes and Redirection:**
   ```bash
   # Pipe output to another command
   command1 | command2

   # Redirect output to a file
   command > output.txt
   ```

**13. Arithmetic Operations:**
   ```bash
   result=$((5 + 3))
   ```

**14. Comments:**
   ```bash
   # This is a comment
   ```

**15. Conditional Execution:**
   ```bash
   # Execute command2 only if command1 succeeds
   command1 && command2

   # Execute command2 only if command1 fails
   command1 || command2
   ```

