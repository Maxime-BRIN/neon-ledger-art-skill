# Synchronisation des assets vers Notion — étape obligatoire

## Cible officielle
- Base : **⛩️ Assets Neon Ledger**
- URL : https://app.notion.com/p/ns-group/5dc0caa5658e48499bb87bcf0d9be012
- Data source observée le 2026-11-03 : `collection://2539d081-70cb-463a-b04e-7021ca993c8f`
- **Toujours relire le schéma vivant avant modification** : noms et options peuvent évoluer.

## Origine des assets récupérés ou adaptés
- Renseigner le créateur original et la page de l'asset précis, ainsi que la chaîne de modifications éventuelles ; ne pas attribuer l'œuvre originale à l'IA.
- Conserver la preuve de licence consultée, l'URL et la date de vérification ; noter les obligations d'attribution, la provenance des textures, les restrictions de redistribution et les modifications.
- N'importer dans le dépôt public que les fichiers autorisés. La gratuité d'accès ne signifie pas permission de redistribution.
- Ne cocher `Licence vérifiée` que lorsque la licence de **cet asset précis** et ses conditions sont documentées ; ne jamais supposer que toute une plateforme est CC0.
- Pour un asset existant déjà enregistré, enrichir la fiche sans doublon. Si l'image preview de source est soumise à restrictions, privilégier un rendu propre autorisé.

## Algorithme idempotent
1. Avant une création, rechercher dans la BDD les entrées correspondant à l'asset par **Nom**, chemin, source/lien et éventuel identifiant stable. Vérifier visuellement les homonymes.
2. Mettre à jour l'entrée existante ; ne créer une fiche que si aucun asset correspondant n'existe.
3. Une fiche par **asset réutilisable distinct** (pas une fiche par capture, rendu ou variante cosmétique). Créer des fiches séparées pour des variantes réellement autonomes si cela aide l'inventaire.
4. Remplir les champs connus sans écraser des données préexistantes plus fiables. Ne jamais renseigner au hasard une option ou une licence.
5. Produire une image représentative de l'asset. À la phase concept : concept IA **étiqueté comme tel**. À la phase 2 et 3 : vraie capture/rendu du mesh, si disponible.
6. Joindre l'image à la propriété **`Aperçu`** (type fichier) et **ajouter une seule image représentative dans le contenu de la page**, avec une légende utile. Important : la galerie Notion peut utiliser **Aperçu de la carte = Contenu** ; dans ce cas la propriété seule ne garantit pas une vignette. Ne pas multiplier les images dans la page.
7. Vérifier la fiche via une relecture Notion après écriture, y compris **image visible**, lien, statut et licence. Si la vue galerie n'est pas vérifiable par l'API, le signaler sans prétendre l'avoir contrôlée.
8. Rapporter l'URL et le résultat des écritures. Si l'accès Notion/stockage d'image manque, conserver l'image exportée, noter **BLOCKED** et ne pas simuler une synchronisation.

## Correspondance des propriétés constatées
| Propriété | Consigne |
|---|---|
| `Nom` | Nom unique, descriptif, stable |
| `Aperçu` | Fichier image généré et accessible |
| `Catégorie` | Option du schéma (Architecture, Mobilier urbain, Voirie & infrastructure, etc.) |
| `Type` | `Modèle 3D` ou autre option réelle correspondant à l'asset |
| `Usage` | Fonction gameplay et contexte |
| `Chemin projet` | Chemin réel du fichier source/export dans le jeu, sinon vide |
| `Lien` | Lien réel et pérenne vers la source, asset ou dépôt, sinon vide |
| `Auteur` | Créateur réel ou chaîne de génération documentée |
| `Source` | Sélectionner **uniquement** une option existante pertinente ; ne pas attribuer une source externe à un asset généré localement |
| `Statut` | `Nouvel asset` pendant la création ; `Intégré` seulement après contrôle en jeu ; autres statuts selon constat |
| `Contrôle technique` | `À vérifier`, `Conforme`, `Problème`, `Non applicable`, selon tests réellement réalisés |
| `Licence` | Choisir uniquement une option prouvée et applicable ; sinon laisser vide et expliquer |
| `Licence vérifiée` | Cocher uniquement avec preuve de licence ; une création IA ne doit pas être présentée arbitrairement comme CC0 |
| `Décision / remarques` | Zone, phase 1/2/3, état d'approbation, chemin image, format, dimensions, limites et liens de validation |
| `Priorité`, `Phase du jeu` | Conserver ou renseigner seulement si cohérent avec les décisions de production |

## Qualité du visuel
- Image lisible en galerie, cadrage net et centrage sur **un seul asset** ; éviter planches composées si fiche unitaire.
- Distinguer `Concept IA (non modélisé)`, `Rendu Blender` et `Capture Godot`.
- Ne jamais inventer de screenshot Godot, utiliser une génération d'image comme preuve de maillage ou déclarer un asset intégré sur une simple exportation GLB.
- Garder l'original dans le pipeline de production ; l'aperçu Notion n'est qu'un média de consultation.

## Échec partiel
L'asset et le rapport peuvent être livrés même si Notion échoue, mais marquer la **synchronisation Notion non terminée**, avec raison et données à reprendre. Ne pas bloquer silencieusement la production ; ne jamais créer de doublons lors d'une nouvelle tentative.
