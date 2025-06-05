## Challenge Description
You're a treasure hunter who found a locked vault! A file named `vault.zip` has been placed in your `/challenge` directory. Your goal is to unlock this vault and find the treasure (flag) inside!

#### Zip files
You may have noticed the `.zip` file extension. This file has been "zipped", or compressed.
"Zipping" files together is a way to gather them all and squish them together so they take up less space. There could be just one file, or several that have been zipped together.

To unzip a `.zip` file, you can use this command: `unzip filename.zip`

This will open up that zipped file, and give you the full information that was compressed inside. If you run `ls` after `unzip`, you should see some new files that weren't there before!

Unfortunately, this vault is locked with a password, in order to unzip it, you will need to find that password (you'll get a prompt to enter the password when you run `unzip`).

## Challenge Steps
1. Navigate to the `/challenge` directory, run `ls` to view all of the challenge files
2. Use `grep` to search the `vault_clue.txt` file for the *password* (For help with `grep`, check out the previous challenge, or go to the Linux Module -> "Find the password!")
3. Use the password you found to unzip `vault.zip`
4. You should now have a `vault.txt` file, in your `/challenge` directory. This file contains a temporary flag: `FLAG{...}` (use `cat` to view the flag)
5. Run `/challenge/verify` and enter the temporary flag from `vault.txt`, and you will receive your offical `pwn.college` flag!
