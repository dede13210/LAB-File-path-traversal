# LAB-File-path-traversal

Pour mancer docker.
```
docker build -t my-flask-app .

docker run -p 5000:5000 my-flask-app
```

Vous pouvez visiter l'image fournit par l'api ici http://127.0.0.1:5000/image?filename=example.jpg

Le but de ce lab est d'accéder à un image se trouvant dans le dossier racine de l'application nommé secret.jpg

<details>
  <summary>Cliquer ici pour révéler la solution</summary>
  http://127.0.0.1:5000/image?filename=../../../secret.jpg
</details>