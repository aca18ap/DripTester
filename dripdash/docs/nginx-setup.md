# Nginx Proxy Setup

We recommend against running DripDash with `sudo` in order to bind to port 80, instead run on `PORT=8000` (default for production) and use Nginx to proxy your server.

## Installing Nginx

```bash
sudo apt-get install nginx
```

Create a new file  `/etc/nginx/site-available/dripdash.conf` with the following content:

```nginx
server {
    server_name *.yourdomain.com yourdomain.com;
    listen 80;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

To enable this configuration, we create a symlink to `sites-enabled`, and remove the default link.

```bash
ln -s /etc/nginx/sites-available/dripdash.conf /etc/nginx/sites-enabled/dripdash.conf
rm /etc/nginx/sites-enabled/default
```

Finally restart Nginx.

```bash
sudo service nginx restart
```

If everything has gone according to plan, this command won't return anything.

## Configuring DripDash

Ensure DripDash is running with `npm run production`.

Open up your browser and navigate to `yourdomain.com` (no port) and you should see DripDash running. This means Nginx is working as a proxy, as intended.

## Enabling SSL

To allow secure connections to DripDash we need a certificate granted by a Certificate Authority (CA). We're going to use `certbot` to obtain a certificate from Let's Encrypt, a free CA.

### Getting a certificate with `certbot`

```bash
sudo apt-get install certbot python-certbot-nginx
```

Once `certbot` is installed, check Nginx is running and DripDash is still accessible over HTTP (port 80). Ensure port 443 is also open, ready to receive HTTPS connections.

```bash
sudo certbot --nginx
```

Follow the instructions given to you by `certbot` and it'll handle everything else. (how kind!)

Finally, check your configuration still looks good, and restart Nginx one last time.

```bash
cat /etc/nginx/sites-available/dripdash.conf

# check the configuration looks good then restart Nginx.
sudo service nginx restart
```

### Checking it works

Navigate to DripDash in your browser. You may see it still loads over HTTP, in which case you'll need to clear your cache. Once you see the padlock, you know it's working!  🎉