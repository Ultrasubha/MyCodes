# Pipes
# Download "Harry Potter and the Goblet of fire" using CLI
wget https://raw.githubusercontent.com/bobdeng/owlreader/master/ERead/assets/books/Harry%20Potter%20and%20the%20Goblet%20of%20Fire.txt 
mv "Harry Potter and the Goblet of fire.txt" harry_potter.txt

# first 3 & last 10 lines 
head -3 harry_potter.txt
tail -10 harry_potter.txt

# Used to display occurrence of a word
grep -oi Harry harry_potter.txt |wc -l
grep -oi Ron harry_potter.txt |wc -l
grep -oi Hermione harry_potter.txt |wc -l
grep -oi Dumbledore harry_potter.txt |wc -l

# prints lines between 100 to 200
head -201 harry_potter.txt | tail -101

# How many unique words are present in the book? (need to do)
awk '{ for ( i=1; i<=NF; i++ ) { if ( NR==1 && !seen[$i]++ ) print $i }} END { print length(seen) }' harry_potter.txt

# Processes, ports
# List browser process IDs (PID) and parent process IDs (PPID):
pgrep -lf "chrome"

# Stop the browser application:
pkill -f "chrome"

# List the top 3 processes by CPU usage:
ps aux --sort=-%cpu | head -4

# List the top 3 processes by memory usage:
ps aux --sort=-%mem | head -4

# Start a Python HTTP server on port 8000:
python3 -m http.server 8000

# Stop the Python HTTP server (in another tab or terminal):
ctl + c

# Start a Python HTTP server on port 90:
python3 -m http.server 90

# Display all active connections and the corresponding TCP/UDP ports:
netstat -tulpn

# Find the PID of the process listening on port 5432:
lsof -i :5432

# Managing software:
# Install htop, vim, and nginx
sudo apt install htop vim nginx

# Uninstall nginx:
sudo apt remove --purge nginx

# Misc
# Find local ip address:
ifconfig

# Find the IP address of google.com:
nslookup google.com

# Check if the Internet is working using CLI:
ping google.com
