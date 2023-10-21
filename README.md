# Collabothon2023
## How to run it?

1. `docker build -t app .`
2. `docker run --name app_container -p 80:80 -v ~/.config:/root/.config app`
3. Go to http://0.0.0.0:80
