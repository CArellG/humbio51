assignment=$1
mkdir /submissions/$assignment
for user in `ls /home`
do
    mkdir /submissions/$assignment/$user
    chown $user:$user /submissions/$assignment/$user
    chmod -R 770 /submissions/$assignment/$user
done
