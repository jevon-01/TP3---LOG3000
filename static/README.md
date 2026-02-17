# Dossier Static

Ce dossier contient toutes les ressources statiques de l'application (fichiers CSS, JavaScript, images, etc.).

## 📁 Contenu

### `style.css`
Feuille de style CSS principale pour l'interface de la calculatrice web. Contient les règles de mise en page et de styling pour une meilleure expérience utilisateur.

## 📝 Notes

- Les fichiers CSS et JavaScript dans ce dossier sont servis directement par Flask
- Assurez-vous que tous les fichiers statiques sont correctement référencés dans les templates HTML
- Pour ajouter de nouvelles ressources, créez des fichiers dans ce répertoire et référencez-les depuis `templates/index.html`

## 🔗 Utilisation

Les fichiers statiques sont accessibles à partir du navigateur via des chemins relatifs comme :
```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

Cela garantit que les chemins sont corrects peu importe l'URL de base de l'application.
