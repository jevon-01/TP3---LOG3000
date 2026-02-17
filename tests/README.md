# Dossier Tests

Ce dossier contient la suite de tests unitaires pour l'application calculatrice.

## 🧪 Fichiers de test

### `test_operators.py`
Tests unitaires pour les fonctions d'opérateurs dans `operators.py`.

**Fonctions à tester :**
- `add(a, b)` - Addition
- `subtract(a, b)` - Soustraction
- `multiply(a, b)` - Multiplication
- `divide(a, b)` - Division

### `test_app.py`
Tests unitaires pour l'application Flask dans `app.py`.

**Fonctions à tester :**
- `calculate(expr)` - Fonction de calcul d'expression
- `index()` - Route principale GET et POST

## 🚀 Exécution des tests

### Installation de pytest
```bash
pip install pytest
```

### Lancer tous les tests
```bash
pytest
```

### Lancer un fichier de test spécifique
```bash
pytest tests/test_operators.py
pytest tests/test_app.py
```

## 📋 Bonnes pratiques

- **Nommez clairement les tests** : utiliser `test_` comme préfixe
- **Un test = une assertion** : chaque test doit vérifier une chose spécifique
- **Isolez les tests** : les tests ne doivent pas dépendre les uns des autres
- **Testez les cas limites** : valeurs nulles, négatives, très grandes, etc.
- **Documentez les cas particuliers** : ajouter des commentaires pour les comportements inhabituels


## 📝 Notes

- Les fichiers de test sont actuellement des squelettes vides
- Complétez-les avec des cas de test réels
- Assurez-vous de tester tous les chemins d'exécution
