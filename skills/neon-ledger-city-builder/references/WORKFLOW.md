# Workflow humain / agent

## Phase 0 — cadrage

Produire une fiche courte : `Brief`, `Exigences imposées`, `Hypothèses proposées`, `Questions majeures`, `Contraintes existantes`, `Risques`. Chaque question importante doit comporter une suggestion par défaut explicitement non approuvée, et sa justification. Ne pas demander des choix secondaires déjà résolubles par l'urbanisme courant.

Exemple : « Trois tours demandées : conserve-t-on leurs hauteurs semblables ? Proposition : hiérarchie 140/165/185 m pour une skyline lisible (à confirmer); option symétrique possible. » Les chiffres sont des suggestions contextuelles, pas des exigences du Skill.

L'utilisateur approuve ou corrige le cahier des charges. Enregistrer une synthèse textuelle de la décision, la date et les contraintes; ne pas fabriquer d'approbation.

## Phase 1 — masterplan

Analyser registre, zones voisines, topographie, réseau, usages et échelle TPP. **Avant de dessiner les emprises**, concevoir la morphologie : histoire des formes, hiérarchie boulevard/seuils/lieux/ruelles, sous-espaces, fonctions des vides, séquences d'exploration à hauteur humaine et conflits d'accès. Une grille répétitive peut être pertinente si demandée, mais pas être le défaut automatique. Dessiner ensuite sur données métriques, auditer et rendre le SVG depuis le JSON. **Faire obligatoirement la Design Quality Review distincte des contrôles géométriques** (references/MASTERPLAN.md + templates/masterplan-design-review.md). Un quadrillage générique, une symétrie non voulue, un marché artificiellement centré ou des parcours monotones contraires au brief doivent être corrigés avant de demander APPROUVER_MASTERPLAN. Présenter un lien SVG ouvrable et les arbitrages. Ne pas commencer de greybox ni promettre un test TPP réel avant phase 2.

## Phase 2 — greybox

L'approbation du masterplan est obligatoire. Ajouter uniquement la zone de travail, sans modifier les zones gelées. Vérifier scène réellement chargée, coordonnées, emprises, hauteurs, collisions, caméra joueur et plusieurs cheminements. Captures: orthographique, spawn, points de jonction, intersections, place/repère, sortie. Consigner les mesures, les tests non réalisés et leurs conséquences.

## Phase 3 — DA et assets (V0.4 : 100 % des essentiels avant habillage)

Avec la greybox approuvée, recueillir si nécessaire les préférences artistiques non précisées; proposer des alternatives argumentées. Créer un style guide local, un plan d'habillage et un inventaire des assets (disponibles, gratuits à sourcer, uniques à créer), plus licence, budget de détails et plan de visibilité. Validation spécifique des téléchargements / écritures externes. **Bloquant :** décomposer la zone en sous-zones fonctionnelles et étudier les références. Pour chaque besoin prioritaire, enregistrer FIT/ADAPT/REJECT/MISSING/PLACEHOLDER avec raison et couverture. Chercher activement des alternatives gratuites si les modèles locaux sont inadaptés, ou proposer la création via neon-ledger-environment sans l'exécuter automatiquement. **L'objectif est 100 % des besoins essentiels du périmètre approuvé : 50/50 pour Faubourg des Traverses.** Un rapport 15/50 déclenche une nouvelle boucle active d'approvisionnement, pas une fin de phase. Poursuivre le sourcing pour chaque manque, ou rédiger les briefs de création et demander leur exécution. Distinguer solutions identifiées et ressources réellement prêtes/importées/vérifiées. Demander les autorisations et rester en phase 3 jusqu'à couverture N/N réelle. Ne jamais compter un modèle non téléchargé ou un brief comme prêt. Si des actions sont impossibles sans accord, présenter les choix et indiquer BLOCKED. Manques essentiels non résolus = demander un arbitrage avant habillage. La liste d'assets est un plan avant le placement. Voir SET_DRESSING.md, ASSETS_NOTION.md et ASSET_COVERAGE_100.md.

## Phase 4 — habillage (V0.2 : contrôle visuel itératif)

Travail par sous-zones et couches: masses architecturales, entrées/façades, signalétique, traces d'activité, mobilier, lumière, finition. Captures réelles au niveau du joueur, vérifications de dégagement, cohérence d'usage et de styles, budget GPU. Contrôler chaque sous-zone, ses couches fonctionnelles et ses surfaces calmes. Prendre 3–5 hero views à des caméras reproductibles + vue globale, comparer avant/après, classer BLOCKER/MAJOR/MINOR et corriger localement. Utiliser templates/dressing-report.md. Si les captures Godot ne sont pas disponibles, signaler NOT_TESTED et bloquer le gate; ne pas annoncer un résultat final. Itérer localement puis soumettre les vues et la liste de nouvelles ressources. Ne pas construire une scène « belle » au détriment de l'échelle et des accès.

## Phase 5 — gel

Après approbation explicite de phase 4, consigner l'empreinte du masterplan, l'identifiant et le statut `locked` dans le registre, associer les preuves de validation, les chemins de fichiers et les décisions. Une extension ne doit pas changer silencieusement le gel précédent.

## Règles universelles

- Un jalon humain ne peut pas être satisfait par l'agent en écrivant « approuvé » dans un fichier.
- Toute modification majeure du contrat d'une phase validée exige retour à cette phase et nouvel accord.
- À la reprise : identifier le dernier jalon approuvé et les changements intervenus depuis; signaler les changements hors bande.
- Autorisation de franchir une phase ≠ autorisation de télécharger des assets, d'écrire dans Notion, de créer une branche Git ou de modifier une zone protégée.
- Ne pas inventer d'images, de screenshots ou de résultats de test.

## Cas : refonte d'une zone déjà approuvée (V2 → V3)

1. Obtenir l'autorisation explicite et locale de modifier la zone ; fixer ce qui reste imposé (raccords, coordonnées des connecteurs).
2. Archiver l'ancienne version dans `versions/<v>/` (masterplan, scène, tests propres à cette version) ; ne rien supprimer.
3. Déplacer les tests spécifiques à l'ancienne géométrie ; adapter ceux qui dépendent de la scène (nombre de bâtiments, chemins de nœuds).
4. Rejouer les phases 0 à 2 avec leurs jalons ; recorriger le registre (`status`) seulement après chaque approbation.
5. Une demande de retrait ou de déplacement d'un objet après approbation (par exemple un bâtiment isolé) est notée dans `decisions.md` avec la date, et les SVG, captures et compteurs de tests sont régénérés.
