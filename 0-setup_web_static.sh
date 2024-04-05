#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

if ! command -v nginx &> /dev/null
then
	sudo apt update
	sudo apt install -y nginx
fi

sudo mkdir -p /data/web_static/{releases/test,shared}

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R pascal_pc:pascal_pc /data

config_content=$(cat <<EOF
server {
listen 80;
listen [::]:80;

server_name _;

location /hbnb_static {
alias /data/web_static/current/;
}
}
EOF
)

echo "$config_content" | sudo tee /etc/nginx/sites-available/default > /dev/null

sudo systemctl restart nginx

exit 0
