# Plausible Analytics

To Deploy:

1. git clone https://github.com/mattbr0wn/plausible.git
2. copy .env into plausible/.env
3. copy Caddyfile into caddy/Caddyfile.plausible
4. add `./Caddyfile.plausible:/etc/caddy/Caddyfile.plausible` to caddy/docker-compose
5. add `import Caddyfile.plausible` to caddy/Caddyfile
6. stop caddy
7. run `sudo docker compose -f ./plausible/docker-compose.yaml -f ./caddy/docker-compose.yaml up -d --build`
