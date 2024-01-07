### **Linux Commands Cheat Sheet:**

**1. File and Directory Operations:**

   - **List Files and Directories:**
     ```bash
     ls
     ```
   - **Change Directory:**
     ```bash
     cd directory
     ```
   - **Copy Files/Directories:**
     ```bash
     cp source destination
     ```
   - **Move/Rename Files:**
     ```bash
     mv oldname newname
     ```
   - **Remove/Delete Files:**
     ```bash
     rm filename
     ```

**2. File Viewing and Editing:**

   - **View File Contents:**
     ```bash
     cat filename
     ```
   - **Display Text Page by Page:**
     ```bash
     less filename
     ```
   - **Edit File:**
     ```bash
     nano filename
     ```
   - **Search for Text in Files:**
     ```bash
     grep pattern filename
     ```

**3. File Permissions:**

   - **Change File Permissions:**
     ```bash
     chmod permissions filename
     ```
   - **Change File Owner:**
     ```bash
     chown user:group filename
     ```

**4. File Compression and Archiving:**

   - **Compress Files:**
     ```bash
     gzip filename
     ```
   - **Decompress Files:**
     ```bash
     gunzip filename.gz
     ```
   - **Create Tar Archive:**
     ```bash
     tar -cvf archive.tar files
     ```
   - **Extract Tar Archive:**
     ```bash
     tar -xvf archive.tar
     ```

**5. Process Management:**

   - **List Running Processes:**
     ```bash
     ps
     ```
   - **Kill a Process:**
     ```bash
     kill process_id
     ```
   - **Check System Resources Usage:**
     ```bash
     top
     ```
   - **Run a Process in the Background:**
     ```bash
     command &
     ```

**6. System Information:**

   - **Display System Information:**
     ```bash
     uname -a
     ```
   - **Check Disk Space:**
     ```bash
     df -h
     ```
   - **Check Memory Usage:**
     ```bash
     free -h
     ```

**7. Networking:**

   - **Check Network Connectivity:**
     ```bash
     ping host
     ```
   - **Check Open Ports:**
     ```bash
     netstat -lntu
     ```
   - **Transfer Files Over SSH:**
     ```bash
     scp localfile user@remote:/path
     ```

**8. Users and Groups:**

   - **Display Logged-In Users:**
     ```bash
     who
     ```
   - **Add a User:**
     ```bash
     adduser username
     ```
   - **Change User Password:**
     ```bash
     passwd username
     ```

**9. Package Management:**

   - **Update Package Lists:**
     ```bash
     sudo apt update
     ```
   - **Install Package:**
     ```bash
     sudo apt install package
     ```
   - **Remove Package:**
     ```bash
     sudo apt remove package
     ```

**10. Miscellaneous:**

   - **Find Files by Name:**
     ```bash
     find /path -name filename
     ```
   - **Create Symbolic Link:**
     ```bash
     ln -s source link
     ```
   - **Show System Logs:**
     ```bash
     journalctl
     ```

**11. Advanced Commands:**

   - **I/O Redirection:**
     - Redirect input and output streams.
     ```bash
     command > output.txt
     command < input.txt
     ```
   - **Pipeline Commands:**
     - Pass output of one command as input to another.
     ```bash
     command1 | command2
     ```
   - **Environment Variables:**
     ```bash
     export VAR=value
     echo $VAR
     ```

