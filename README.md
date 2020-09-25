# node.operator.mainnet

      mv node.operator.mainnet node.operator
    cd node.operator/scripts && . ~/node.operator/configs/env.sh main
    chmod +x -R ${NODE_OPERATOR_SCRIPTS_DIR}
    cd ~/node.operator/configs
    cat bashrc.config > ~/.bashrc && source ~/.bashrc
    crontab ~/node.operator/configs/crontab

# python and crontab setup for election alarm

      sudo apt install -y python && sudo apt update && sudo apt install -y python-pip && sudo pip install gspread && sudo pip install --upgrade oauth2client && sudo pip install psutil && pip uninstall python-telegram-bot; pip uninstall telegram; pip uninstall telegram-bot; pip install telegram-bot && (crontab -l ; echo "*/30 * * * * python ~/node.operator/monitor/checkElection.sh")| crontab - && (crontab -l ; echo "* * * * * python ~/node.operator/monitor/alarm.py")| crontab - && chmod +x -R ~/node.operator
      

# node.operator

These scripts are created to help node operators. All the paths used are the default locations of https://github.com/tonlabs/main.ton.dev.

1. INITIAL INSTALL

Install dependencies and download/setup repo
	
	sudo apt install -y git && cd && rm -rf ~/node.operator && git clone https://github.com/kevintmax/node.operator.mainnet.git && chmod +x -R ~/node.operator.mainnet/scripts && mv ~/node.operator.mainnet ~/node.operator && cat ~/node.operator/configs/bashrc.config > ~/.bashrc && source ~/.bashrc && sudo apt install bc && cd ~/node.operator/scripts && . ~/node.operator/configs/env.sh

Import crontab after completion of sync

	crontab ~/node.operator/configs/crontab.config

2. UPDATE

Update and import crontab
	
	

Update but NOT import crontab
	
	
