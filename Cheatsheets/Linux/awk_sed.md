### **AWK and SED Commands Cheat Sheet:**

**1. AWK:**

   - **Basic Structure:**
     ```awk
     pattern { action }
     ```
   - **Print Specific Columns:**
     ```bash
     awk '{print $1, $3}' filename
     ```
   - **Conditional Statements:**
     ```awk
     awk '{if ($3 > 50) print $1, $3}' filename
     ```
   - **Built-in Variables:**
     - `NF`: Number of fields in a line.
     - `NR`: Number of records (lines).
     - `FS`: Field separator.
     ```bash
     awk '{print NR, NF, $0}' filename
     ```
   - **Pattern Matching:**
     ```awk
     awk '/pattern/ {print $2}' filename
     ```
   - **Mathematical Operations:**
     ```awk
     awk '{total += $3} END {print "Average: ", total/NR}' filename
     ```

**2. SED:**

   - **Basic Structure:**
     ```bash
     sed 's/pattern/replacement/' filename
     ```
   - **In-Place Editing:**
     ```bash
     sed -i 's/pattern/replacement/' filename
     ```
   - **Print Specific Lines:**
     ```bash
     sed -n '10,20p' filename
     ```
   - **Delete Lines:**
     ```bash
     sed '5,10d' filename
     ```
   - **Substitute and Replace:**
     ```bash
     sed 's/foo/bar/g' filename
     ```
   - **Insert and Append:**
     ```bash
     sed '3i\New Line' filename
     sed '$a\End of File' filename
     ```
   - **Conditional Execution:**
     ```bash
     sed '/pattern/ {s/foo/bar/; s/123/456/}' filename
     ```
   - **Delete Lines Matching Pattern:**
     ```bash
     sed '/pattern/d' filename
     ```
   - **Hold and Pattern Buffers:**
     ```bash
     sed -n '/pattern/{p; h}; $ {x; p}' filename
     ```

**3. AWK and SED Together:**

   - **Use AWK Output in SED:**
     ```bash
     awk '{print $2}' filename | sed 's/foo/bar/'
     ```
   - **Use SED Output in AWK:**
     ```bash
     sed 's/pattern/replacement/' filename | awk '{print $1}'
     ```

**4. Advanced Usage:**

   - **AWK Script File:**
     - Create a separate AWK script file.
     ```awk
     # script.awk
     {print $1, $3}
     ```
     ```bash
     awk -f script.awk filename
     ```
   - **SED Multiple Operations:**
     ```bash
     sed -e 's/pattern1/replacement1/' -e 's/pattern2/replacement2/' filename
     ```

