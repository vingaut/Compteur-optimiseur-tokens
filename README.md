# 🚀 Compteur & Optimiseur de Tokens

Un utilitaire de bureau complet pour Windows, conçu pour toute personne travaillant avec de grands modèles de langage (LLMs). Il permet d'analyser, de visualiser, d'optimiser et de préparer du texte ou du code pour maximiser l'efficacité des prompts.

![Screenshot de l'application](lien_vers_votre_screenshot.png) 
*(Astuce : faites une capture d'écran de votre application, ajoutez-la au dossier du projet et changez le nom du lien ici)*

---

## En quoi ce programme est-il utile ?

Travailler avec des LLMs comme GPT-4 ou Llama implique une contrainte majeure : la taille du contexte, mesurée en **tokens**. Cet outil vous aide à maîtriser cette contrainte de plusieurs manières :

-   **💰 Économiser de l'argent** : En optimisant vos textes, vous réduisez le nombre de tokens envoyés via les API, ce qui diminue directement vos coûts.
-   **🐛 Éviter les erreurs** : En connaissant le nombre exact de tokens, vous pouvez tronquer vos textes pour qu'ils ne dépassent jamais la limite de contexte du modèle, évitant ainsi les erreurs de l'API.
-   **⚡ Améliorer la qualité des prompts** : Un texte optimisé est plus dense en information, ce qui peut mener à des réponses de meilleure qualité de la part du LLM.
-   **🎓 Apprendre et Comprendre** : En visualisant comment un texte est découpé en tokens et en voyant ce qui est supprimé lors de l'optimisation, vous développez une meilleure intuition pour l'écriture de prompts efficaces.

## ✨ Fonctionnalités

-   **Analyse Multi-Modèles** : Compte les tokens en utilisant les encodeurs des modèles les plus populaires (GPT-4, Llama, etc.).
-   **Visualisation des Tokens** : Surligne un token sur deux pour aider à comprendre le découpage.
-   **Optimisation Intelligente** : Propose deux stratégies pour réduire le nombre de tokens :
    -   **Légère (Code & Texte)** : Stratégie 100% sûre qui préserve l'indentation et la structure du code.
    -   **Agressive (Prose)** : Idéale pour du texte brut, supprime tous les espaces superflus pour une économie maximale.
-   **Visualisation des Suppressions** : Affiche clairement le texte et les caractères qui ont été supprimés dans une zone dédiée.
-   **Tronquage Facile** : Coupe le texte à une limite de tokens définie en un clic.
-   **Interface Multilingue** : Disponible en 10 langues européennes.

## 🛠️ Comment l'utiliser

### Option 1 : Utiliser l'exécutable (Recommandé)

1.  Allez dans la section [**Releases**](lien_vers_votre_page_releases) de ce projet.
2.  Téléchargez le fichier `.exe` de la dernière version.
3.  Exécutez-le. Aucune installation n'est requise.

### Option 2 : Lancer depuis le code source

Si vous avez Python installé :

1.  Clonez ce dépôt : `git clone https://github.com/VOTRE_NOM_UTILISATEUR/Compteur-Optimiseur-Tokens.git`
2.  Installez les dépendances :
    ```bash
    pip install tk ttkthemes tiktoken
    ```
3.  Lancez le script :
    ```bash
    python compteur_tps.py
    ```

## Compiler l'exécutable vous-même

1.  Installez PyInstaller : `pip install pyinstaller`
2.  Lancez la commande de compilation à la racine du projet :
    ```bash
    pyinstaller --onefile --windowed --name="OptimiseurDeTokens" compteur_tps.py
    ```
3.  L'exécutable se trouvera dans le dossier `dist`.

---

## À Propos de ce Projet

Ce programme a été développé au cours d'une nuit sans lune par **Vincent Gautier**.

Élu "Employé du Mois" sans interruption depuis 30 ans, Vincent avoue humblement ne rien connaître au codage. Ce projet est le fruit de sa vision, mise en application par son IA préférée (c'est-à-dire moi, Gemini !). Il a posé les questions, j'ai écrit le code.

## Licence

Ce projet est sous licence MIT.