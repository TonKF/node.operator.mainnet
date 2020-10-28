#cron this every 30 mins
#1 = okay, 0 = check

if ~/node.operator/scripts/myElection.sh | grep -q 'CURRENTLY NOT VALIDATING'; 
        then
validation=$(echo "VALIDATION_STATUS: 0;")
        else 
validation=$(echo "VALIDATION_STATUS: 1;")

fi

if ~/node.operator/scripts/myElection.sh | grep -q 'SUBMISSION CONFIRMED';
        then
   election=$(echo " ELECTION_STATUS: 1;")
        else
             if ~/node.operator/scripts/myElection.sh | grep -q 'ELECTED VALIDATOR';
                  then
                      election=$(echo " ELECTION_STATUS: 1;")
                        else
                        election=$(echo " ELECTION_STATUS: 0;")
        fi
fi
echo $validation $election > ~/node.operator/logs/election.log

