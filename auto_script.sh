cd "D:\WORKING\my_git\python_scripts"
git add --all
git commit -m "Test Readme change"
# git commit -m "`date`"
echo ""
echo "***************************************"
echo "Information: "
echo "Pushing to remote, Please wait ....."
# showing remote
git remote -v
echo "***************************************"
echo ""
git push
echo ""
echo "                  SUCCESS                  "
# 5 seconds sleep
sleep 5s