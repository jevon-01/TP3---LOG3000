# Dossier Templates

Ce dossier contient les modèles HTML (templates) de l'application Jinja2 pour Flask.

## 📄 Fichiers

### `index.html`
Le template principal qui affiche l'interface de la calculatrice web.

#### Structure
- **Formulaire POST** : Envoie l'expression saisie au serveur Flask pour évaluation
- **Champ d'affichage** : Affiche le résultat du calcul (lecture seule)
- **Grille de boutons** : Contient les chiffres (0-9), les opérateurs (+, -, *, /), un bouton clair (C) et le bouton égal (=)
- **Fonctions JavaScript** :
  - `appendToDisplay(value)` : Ajoute une valeur au champ d'affichage
  - `clearDisplay()` : Efface le contenu du champ d'affichage

#### Liaison au CSS
```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```
Utilise la fonction Jinja2 `url_for()` pour générer le chemin correct vers le fichier CSS.

## 🔗 Interaction avec l'application

Le template communique avec l'application Flask (`app.py`) :
1. **GET** : Affiche la calculatrice vide au chargement
2. **POST** : Envoie l'expression saisie et reçoit le résultat

Le résultat est affiché dans le champ `display` via la variable `{{ result }}`.

## 📝 Notes

- Les templates utilisent la syntaxe **Jinja2** (variables entre `{{ }}`)
- Les fonctions JavaScript gèrent l'interface client
- Le serveur Flask valide et évalue les expressions

## ✏️ Modification

Pour ajouter des éléments ou modifier le design :
1. Éditez le fichier `index.html`
2. Mettez à jour `static/style.css` pour les changements de style
3. Ajoutez des fonctions JavaScript si nécessaire
