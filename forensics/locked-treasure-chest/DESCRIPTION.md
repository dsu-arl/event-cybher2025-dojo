You found a digital treasure chest (digital_treasure.zip) hiding another zip file. The flag is contained within the (treasure.zip). Unzip it to check its contents, but the real secret might be in the zip file’s metadata. Use zipinfo to find the flag, which starts with FLAG{.

Remember when unzipping a file use this command unzip /challenge/digital_treasure.zip /home/hacker

Do not unzip the treasure.zip. You will manipulate the metadata of the file and not get the correct flag.

Hint: Unzip with unzip digital_treasure.zip, but try zipinfo -h if you need help looking for the correct command operation. The zipinfo -h will display the help pages for more information about other ways to use zipinfo.

The files that you will be working on are in the /challenge directory.
