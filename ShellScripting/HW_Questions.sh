#Q.1)Create a script to read a name from command line. Check whether the name is of a file or directory.

echo "Enter the name of the file or directory"
read name

if [ -f $name ]
then
echo -e "It's the name of a file\n"
elif [ -d $name ]
then
echo -e "It's the name of a directory\n"
else
echo "No such file exist"
fi

#TO CHECK ERRORS

if [ $? -eq 0 ]
then
echo "Task Completed"
else
echo "Error"
fi
##################################################################################################################


#2. Create a script to read 3 names. Check how many names are of file and how many are of directories.

file=0
directory=0
for i in $1 $2 $3
do
if [ -f $i ]
then
echo "It is a file"
file=$(($file+1))
elif [ -d $i ]
then
echo "It is a directory"
directory=$(($directory +1))
else
echo "No such files or directories exist for arguement $i"
fi
done
echo -e "\nThere are $file files and $directory directories"
##################################################################################################################


#3. Create a script to print the total number of arguments passed at command line. If the
#arguments passed are > 3 then create a file with the name passed as 1st argument and a
#directory with the name passed as 2nd argument.

count=0
echo "Your entries are"

for i in $*
do
echo $i  
count=$(($count+1))
if [ $count -ge 3 ]
then
touch $1
mkdir $2
echo "A file $1 and a directory $2 is successfully created"
fi
done
##################################################################################################################


#4. Create a script to read 5 file names from the user. Count how many names start with"f".
echo "enter the file names"
read a b c d e f
count=0
for file in $a $b $c $d $e $f
do
case $file in
f*)count=$(($count+1));;
esac
done
echo "The name of $count files starts with f"
##################################################################################################################


#5. Create a script to read a directory path from command line. Count how many files arethere in this directory.

echo "The number of files in this directory is"
ls $1 | wc -l
##################################################################################################################


#6. Create a script to create a file in a directory. Ask the names of the file and directory from the user. 
#Do not create the file if it already exists or if the directory does notexists(also display an appropriate message).

echo "Enter the directory path"
read dir
echo "Enter the file name"
read file
#ls $dir|grep "$file"
if [ ! -d $dir ]
then
       echo "No such directories by the name $dir was found"
else
       if [ -f $file]
       then
       echo "A file by the name $file already exists"
       else
       touch $dir/$file
       echo "The file $file was successfully created in $dir directory"
       fi
fi

##################################################################################################################


#7. Create a script to count the number of files having read permission on them in a directory.

ls |for var in *
do
if [ -f $var -a -r $var ]
then
#a=$(($a + 1))
echo "The readable files are $var"
fi
done

#count=$(($count + 1))

##################################################################################################################


#8. Create a script to create two functions – one to create files and another to delete files.

creator()
{
	touch $*
}

exterminator()
{
	rm $*
}

exterminator $*

##################################################################################################################


#9. Create a script to create functions to
#a. Display long list of files – dir()
#b. Perform a search within a file – ser()
#If the 1st argument at command line is a directory name then a call to dir() should be made to display that directories content
#else if the name is of a file then call ser() to find if the pattern “help” exists in that file or not'

dir()
{
	echo "The files are"
	ls -l $1
}

ser()
{
	grep -w "help" $1
}

if [ -d $1 ]
then dir $1

elif  [ -f $1 ]
then ser $1
fi

##################################################################################################################


#9. Create a script that has a function to copy files. The first two arguments while running the script should be names of files to be copied and the third argument should be
#directory where the files are to be copied.

copy()
{
cp $1 $3
echo "$1 copied successfully to $3"
cp $2 $3
echo "$2 copied successfully to $3"
}
echo "the cla are $*"
copy $1 $2 $3

##################################################################################################################


#10. Create a script having a function which returns some value.

sum()
{
	value=$(($1+$2))
	echo $value
}

echo "The sum of $1 and $2 is $(sum $1 $2)"

##################################################################################################################


#11. Create multiple files with a single line.

touch f{1..1000)
touch apple{1..100}.txt


##################################################################################################################
