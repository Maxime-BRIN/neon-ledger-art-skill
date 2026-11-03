# ASSET_SOURCING — Rechercher avant de créer

## Objectif et ordre obligatoire
Éviter de reconstruire des objets 3D courants déjà disponibles. Cette étape précède le routage des images et les trois missions artistiques ; elle s'applique aux props, infrastructures, kits et autres modèles 3D. Les images IA restent pertinentes **uniquement si la création originale a été choisie**, ou sur demande expresse de concept art. Ne jamais inventer un résultat de recherche.

## Procédure concise
1. **Interne** : rechercher par nom, synonymes, famille et usage dans les dossiers du projet, les fichiers validés, la documentation et la BDD Notion « ⛩️ Assets Neon Ledger » si accessibles. Vérifier variantes existantes, statut et absence de doublon.
2. **Externe** : chercher 1 à 3 candidats pertinents sur des catalogues d'assets, en priorité les bibliothèques à licence permissive (Poly Haven, Kenney, Quaternius), puis d'autres catalogues (Fab, Sketchfab, etc.) avec contrôle **par asset**. Vérifier que le téléchargement et l'usage commercial sont permis ; ne pas confondre page de résultats, aperçu et fichier 3D accessible.
3. **Vérification individuelle** : relever URL directe de la fiche, auteur, licence exacte et preuve consultable, attribution, modifications, redistribution, dépendances de textures, formats, dimensions, polycount si connu, qualité PBR, proportions, compatibilité Godot (testée ou non), et éventuel coût d'adaptation.
4. **Décision** : comparer RÉUTILISER (asset conforme), ADAPTER (asset proche et amélioration limitée), CRÉER (aucun candidat satisfaisant, licence incompatible, adaptation plus coûteuse ou identité artistique spécifique). Ne pas utiliser la création comme option par défaut.
5. **Présentation** : recommander une voie en deux à cinq lignes par asset avec liens et limites ; obtenir l'accord requis avant les écritures dans le projet. Ne télécharger qu'après choix, sans aspirer massivement des packs.

## Vérifications essentielles
- **Juridique** : « gratuit » n'est pas une licence. Vérifier *l'asset exact*, pas seulement la plateforme : CC0, CC BY, licence Standard, restrictions éventuelles. Vérifier usage dans un jeu commercial, droit de modification, attribution, distribution dans le jeu vs redistribution brute dans un dépôt GitHub public. Respecter licences de textures et éléments intégrés. Une licence non établie = **non vérifiée**, asset non incorporé.
- **Artistique** : silhouette, proportions, matérialité, état d'entretien, cohérence du quartier, lisibilité 2–15 m ; ne pas ajouter automatiquement néons et salissures.
- **Technique** : géométrie réelle (pas un mesh cachant un blockout), textures PBR présentes, pivot, échelle, axes, UV, nombre de matériaux, LOD/collisions selon usage, performance Godot à mesurer, format glTF/GLB ou conversion plausible.
- **Économie** : estimer récupération + adaptation + vérification contre conception + modélisation + PBR + vérification. Un asset gratuit trop lourd ou sans preuve peut coûter plus qu'une création.

## Voies de production
### RÉUTILISER
Conserver l'original, documenter sa provenance, adapter seulement l'import (si requis), contrôler dans Blender/Godot et intégrer via gates pertinentes. Ne pas générer de concept ou refaire sa géométrie inutilement.

### ADAPTER
Conserver une source originale non écrasée, décrire les changements minimum (matériaux, vieillissement motivé, optimisation, raccords, petits éléments distinctifs). Les changements visuels de DA sont approuvés avant modification. Vérifier droit de modification et redistribution.

### CRÉER
Justifier l'absence de candidat convenable et reprendre le routage image fournie → concept IA si générateur disponible → brief textuel si indisponible, avec approbation de phase 1, puis modélisation et PBR.

## Livrable minimal — tableau de décision
| Asset | Existant projet | Candidat externe + URL | Licence prouvée | Effort d'adaptation | Décision | Prochaine validation |
|---|---|---|---|---|---|---|

Si outils de recherche, sources ou fichiers du projet sont inaccessibles, afficher **NOT_TESTED** avec limites. Ne jamais affirmer qu'aucun asset n'existe après une recherche non effectuée.

## Idempotence et catalogue
Appliquer `NOTION_ASSET_CATALOG.md`. Une fiche par asset réutilisable, pas par capture ; pas de doublons ; vrai aperçu du mesh quand disponible ; auteur réel et provenance ; statut `Intégré` uniquement après test Godot. Ne jamais attribuer automatiquement CC0 à une création IA.
