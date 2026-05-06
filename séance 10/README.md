![html](../assets/html.png) ![css](../assets/css.png) ![js](../assets/js.png)  ![php](../assets/php.png) 
# séance 10

1. [code(Sic.)](./code(Sic)/) (html et css)
2. [pipo](./popipopipopipo/) (php)

# dépendances

```command prompt (admin)
mklink "C:\xampp\htdocs\NAME.php" "C:\PATH\TO\SOURCE.php"
```

- [PHP](https://www.php.net/)
- [XAMPP](https://www.apachefriends.org/fr/index.html)

## configurer XAMPP

> [!IMPORTANT]
> si le bouton `start` fonctionne sans rien faire, configurer XAMPP n'est *pas nécessaire*.

1. cliquer sur `config` de `Apache`
2. cliquer sur `httpd.conf`
3. chercher `80`
4. remplacer `Listen 80` par `Listen 82`
5. cliquer sur `suivant`
6. changer `Servername localhost:80` en `Servername localhost:82`
7. sauvegarder
8. refaite la première étape et cliquer sur `httpd-ssl.conf`
9. changer `Listen 443` en `Listen 4433`
10. sauvegarder et essayer de démarrer `Apache`