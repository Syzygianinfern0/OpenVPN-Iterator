#!/usr/bin/zsh
CREDS_FILE=$1
CONFIG_FILE=$2

if [ -f "$CONFIG_FILE" ]; then
    # When you directly give a config file (.ovpn)
    echo "Using config $CONFIG_FILE"
else
    # When you give a country ID number (https://api.nordvpn.com/v1/servers/countries)
    # For example
    #   India = 100
    #   Singapore = 195
    #   US = 228
    # Down the server configs from here https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip
    # and put it at ./ovpn
    echo "Getting best config for country id $CONFIG_FILE."
    CONFIG_FILE=$(curl --silent "https://api.nordvpn.com/v1/servers/recommendations?filters\[country_id\]=$CONFIG_FILE&limit=1" | jq --raw-output '.[].hostname')
    CONFIG_FILE=./ovpn/ovpn_udp/$CONFIG_FILE.udp.ovpn
    echo "Using config $CONFIG_FILE"
fi

while IFS= read -r line; do
    VPN_USER=${line%:*}
    VPN_PASSWORD=${line##*:}
    echo "####### $VPN_USER ####### $VPN_PASSWORD #######"
    sudo bash -c 'openvpn --auth-nocache --config '"$CONFIG_FILE"' --auth-user-pass <(echo -e "'"$VPN_USER"'\n'"$VPN_PASSWORD"'") --verb 0'
done <"$CREDS_FILE"
