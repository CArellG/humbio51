assignment=$1
mkdir /submissions/$assignment
for user in `ls /home`
do
    mkdir /submissions/$assignment/$user
    chown $user:$user /submissions/$assignment/$user
    chmod -R 770 /submissions/$assignment/$user
done
root@grading-server:/opt# cat close_assignment.sh 
assignment=$1
chown -R root:sudo /submissions/$assignment
chmod -R g+w /submissions/$assignment
