# Usar la imagen base de Alpine con Nginx
FROM nginx:alpine

# Copiar el archivo HTML al directorio predeterminado de Nginx
COPY index.html /usr/share/nginx/html/

# Exponer el puerto 80
EXPOSE 80

# Iniciar Nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]
