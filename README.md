# TP3 --- LOG3000 Application Calculatrice Web
- Équipe : 11
- Membres : Jeremy Vong, Tan-Tommy Rin, Alexie Lalonde-Legault


## Description

Une application calculatrice simple basée sur Flask, créée pour un projet de cours (LOG3000).  
L’application accepte des expressions arithmétiques de base via un formulaire web et les évalue en utilisant des opérateurs personnalisés. Elle inclut également une petite suite de tests pour valider les fonctionnalités principales.

---

## 📋 Fonctionnalités

- Prend en charge l’addition, la soustraction, la multiplication et la division entière
- Validation de base de l’expression et des opérandes numériques
- Interface HTML simple pour la calculatrice
- Tests unitaires pour la logique de calcul et les fonctions d’opérateurs

---

## 🛠️ Prérequis

- Python 3.10 ou version ultérieure
- `pip` pour installer les dépendances

Les dépendances sont listées dans `requirements.txt` :

```text
Flask
pytest
``` 

Installez-les avec :

```bash
pip install -r requirements.txt
```

---

## 🚀 Exécution de l’application

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/jevon-01/TP3---LOG3000.git
    cd TP3---LOG3000
    ```

2. (Optionnel) Créez et activez un environnement virtuel :
    ```bash
    python -m venv venv
    venv\Scripts\activate    # Windows
    source venv/bin/activate   # macOS / Linux
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Démarrez le serveur Flask :
    ```bash
    python app.py
    ```

5. Ouvrez votre navigateur et rendez-vous à `http://127.0.0.1:5000/` pour voir la calculatrice.

---

## 🧪 Tests

Des tests unitaires simples se trouvent dans le répertoire `tests/`. Ils couvrent actuellement le module `operators` et la logique principale `calculate`.

Exécutez les tests avec pytest :

```bash
pip install pytest            # si ce n’est pas déjà installé
pytest
```

Ajoutez des tests supplémentaires en modifiant ou en développant les fichiers dans `tests/`.

---

## 📝 Structure du projet

```
app.py                # Application Flask et logique de calcul
operators.py          # Fonctions d’opérateurs arithmétiques
static/               # Ressources statiques (CSS)
templates/            # Modèles HTML pour l’interface web
tests/                # Squelettes de tests unitaires
README.md             # Cette documentation
requirements.txt      # Dépendances Python
```

---

## 💡 Remarques et améliorations

- Les fonctions `operators`:
- L'addition est `a + b`
- La soustraction devrait être `a - b`
- La multiplication devrait être `a * b`
- La division devrait utiliser la division (`/`)
- La gestion des entrées n’autorise qu’un seul opérateur et suppose des opérandes numériques décimales.

Les améliorations futures pourraient inclure :

- Prise en charge des parenthèses et de l’ordre des opérations
- Division flottante
- Amélioration du design frontend et interface JavaScript
- Messages d’erreur et validation avancée