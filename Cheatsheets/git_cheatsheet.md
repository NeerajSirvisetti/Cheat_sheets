# Git Cheat sheet

## Setting up SSH access for github
To set up SSH access for Git, follow these steps:

1. **Generate SSH Key Pair:**
   Run the following command to generate an SSH key pair:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
   ```
   - Replace "your.email@example.com" with your actual email. Press Enter to accept the default file location and set a passphrase if desired.
   - -t rsa: Specifies the type of key to create, in this case, RSA.
   - -b 4096: Sets the number of bits in the key. A higher bit length generally provides better security.
   - -C "your.email@example.com": Adds a comment to help identify the key, usually your email address. It's optional but useful for distinguishing keys if you have multiple.

3. **Start SSH Agent:**
   If not already running, start the SSH agent:
   ```bash
   eval "$(ssh-agent -s)"
   ```

4. **Add SSH Private Key to SSH Agent:**
   ```bash
   ssh-add ~/.ssh/id_rsa
   ```
   If you used a different file name or location, adjust accordingly.

5. **Copy SSH Public Key to Clipboard:**
   ```bash
   cat ~/.ssh/id_rsa.pub | pbcopy   # For macOS
   cat ~/.ssh/id_rsa.pub | xclip -selection clipboard   # For Linux
   ```

6. **Add SSH Key to GitHub (or other Git hosting service):**
   - Go to your GitHub account settings.
   - Select "SSH and GPG keys."
   - Click "New SSH key" or "Add SSH key."
   - Paste your public key.

7. **Test SSH Connection:**
   ```bash
   ssh -T git@github.com
   ```
   Confirm that you see a message indicating successful authentication.

Now, your SSH key is set up, and you can use Git over SSH without entering your username and password each time.

Remember to adapt these steps if you're using a different Git hosting service. 

## Initializing a connection from your local repo to new repo in Github

1. **Create a New Repository on GitHub:**
   - Go to GitHub and create a new repository.
   - Optionally, initialize the repository with a README file.

2. **Open Terminal:**
   - Navigate to the local directory where you want to initialize your Git repository.

3. **Initialize Git:**
   ```bash
   git init
   ```

4. **Add a Remote Origin:**
   ```bash
   git remote add origin <repository_url>
   ```
   Replace `<repository_url>` with the URL of the repository you created on GitHub.

5. **Check Remote URL:**
   ```bash
   git remote -v
   ```
   Confirm that the remote URL is set correctly.

6. **Add Files and Commit:**
   ```bash
   git add .
   git commit -m "Initial commit"
   ```

7. **Push to GitHub:**
   ```bash
   git push -u origin master
   ```
   This assumes your default branch is named "master." If it's different, replace "master" with your branch name.

Now, your local repository is connected to the remote repository on GitHub, and your initial commit has been pushed.

Remember to replace `<repository_url>` with your actual GitHub repository URL. 

## Git configuration commands

To set up some basic configurations for Git, you can use the following commands:

1. **Set Your Name:**
   ```bash
   git config --global user.name "Your Name"
   ```
   Replace "Your Name" with your actual name.

2. **Set Your Email:**
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   Replace "your.email@example.com" with your actual email.

3. **Set Default Editor (Optional):**
   ```bash
   git config --global core.editor "your_preferred_text_editor"
   ```
   Replace "your_preferred_text_editor" with the text editor you prefer to use for commit messages. For example, "nano," "vim," or "code" for Visual Studio Code.

4. **Set Default Branch Name (Optional, if not using "master"):**
   ```bash
   git config --global init.defaultBranch "main"
   ```
   Replace "main" with your desired default branch name.

5. **Configure Credential Helper for Caching (Optional):**
   ```bash
   git config --global credential.helper cache
   ```
   This helps Git remember your credentials for a certain period.

6. **Configure Global Ignore (Optional):**
   ```bash
   git config --global core.excludesfile '~/.gitignore_global'
   ```
   Create a global gitignore file (e.g., `~/.gitignore_global`) to specify patterns for files that Git should ignore globally.

These commands set up basic configurations, making your Git experience more personalized. 

## Basic daily usage commands

**Clone a Repository:**
```bash
git clone <repository_url>
```

**Add a Remote Origin:**
```bash
git remote add origin <repository_url>
```

**Create a New Branch:**
```bash
git branch <branch_name>
git checkout -b <branch_name>
```

**Switch Branches:**
```bash
git checkout <branch_name>
```

**Stage Changes:**
```bash
git add <file_name>
```

**Commit Changes:**
```bash
git commit -m "Your commit message"
```

**Push Changes to GitHub:**
```bash
git push origin <branch_name>
```

**Pull Changes from GitHub:**
```bash
git pull origin <branch_name>
```

**Merge Branches:**
```bash
git checkout <base_branch>
git merge <feature_branch>
```

**View Branches:**
```bash
git branch
```

**View Remote Repositories:**
```bash
git remote -v
```

**Undo Changes (before committing):**
```bash
git checkout -- <file_name>
```

**Undo Commit (local only):**
```bash
git reset HEAD~1
```

Remember to replace `<repository_url>`, `<branch_name>`, and `<file_name>` with the appropriate values for your project.
