# node.operator

These scripts are created to help node operators. All the paths used are the default locations of https://github.com/tonlabs/main.ton.dev.

1. INITIAL INSTALL

Install dependencies and download/setup repo
	
	sudo apt-get update && sudo apt install -y git && cd && rm -rf ~/node.operator && git clone https://github.com/kevintmax/node.operator.mainnet.git && chmod +x -R ~/node.operator.mainnet/ && mv ~/node.operator.mainnet ~/node.operator && cat ~/node.operator/configs/bashrc.config > ~/.bashrc && source ~/.bashrc && sudo apt install bc && cd ~/node.operator/configs && . ./env.sh && cd ~/node.operator/scripts && ./validatorBuild.sh


Import crontab

	crontab ~/node.operator/configs/crontab.config

2. UPDATE

Update and import crontab
	
	

Update but NOT import crontab
