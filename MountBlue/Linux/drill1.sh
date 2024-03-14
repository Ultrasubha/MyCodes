#Create the following directory structure
mkdir hello
cd hello
mkdir -p one/two/three/four five/six/seven
cd one
touch a.txt b.txt
touch two/d.txt
touch two/three/e.txt
touch two/three/four/access.log

# Add the following content to a.txt
echo "Unix is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, development starting in the 1970s at the Bell Labs research center by Ken Thompson, Dennis Ritchie, and others" > a.txt

cd .. ; cd ..

#Delete all the files having the .log extension
find . -name "*.txt" -type f -delete

#Delete the directory named five
rm -rf hello/five

#Rename the one directory to uno
mv hello/one hello/uno

#Move a.txt to the two directory
mv hello/uno/a.txt hello/uno/two
