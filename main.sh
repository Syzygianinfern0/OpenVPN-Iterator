#!/usr/bin/zsh
CREDS_FILE=$1
CONFIG_FILE=$2

while IFS= read -r line; do
    VPN_USER=${line%:*}
    VPN_PASSWORD=${line##*:}
    echo "####### $VPN_USER ####### $VPN_PASSWORD #######"
    sudo bash -c 'openvpn --auth-nocache --config '"$CONFIG_FILE"' --auth-user-pass <(echo -e "'"$VPN_USER"'\n'"$VPN_PASSWORD"'") --verb 0'
done <"$CREDS_FILE"
