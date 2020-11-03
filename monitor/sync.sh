
#!/bin/bash

username=$(whoami)
hostname=$(hostname -s)

SYNC=$(~/*.ton.dev/scripts/check_node_sync_status.sh | grep TIME_DIFF | awk '{print $4}')

if [ "$SYNC" -lt -100 ]; then
  SYNC_STATUS=$(echo SYNC_STATUS=0;)
  if ["$SYNC" -gt 0]; then
    SYNC_STATUS=$(echo SYNC_STATUS=0;)
      if [ $SYNC -lt 0 ] &&  [ $TIME -gt -100 ]; then
        SYNC_STATUS=$(echo SYNC_STATUS=1;)
          else
           SYNC_STATUS=$(echo SYNC_STATUS=0;)
           
 fi
          
        
