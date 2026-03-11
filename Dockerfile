# Käytetään kevyttä Nginx-pohjaa
FROM nginx:alpine

# Kopioidaan projektisi index.html Nginxin oletushakemistoon
COPY index.html /usr/share/nginx/html/index.html

# Paljastetaan portti 80
EXPOSE 80