find . -type f \( -name "*.exe" -o -name "*.class" \) ! -path "./C#/*" -exec rm {} +
echo "Successfully Deleted all .exe and .class files"
