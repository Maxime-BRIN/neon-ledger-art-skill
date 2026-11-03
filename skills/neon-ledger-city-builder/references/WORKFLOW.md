# Workflow humain / agent

## Phase 0 — cadrage

Produire une fiche courte : `Brief`, `Exigences imposées`, `Hypothèses proposées`, `Questions majeures`, `Contraintes existantes`, `Risques`. Chaque question importante doit comporter une suggestion par défaut explicitement non approuvée, et sa justification. Ne pas demander des choix secondaires déjà résolubles par l'urbanisme courant.

Exemple : « Trois tours demandées : conserve-t-on leurs hauteurs semblables ? Proposition : hiérarchie 140/165/185 m pour une skyline lisible (à confirmer); option symétrique possible. » Les chiffres sont des suggestions contextuelles, pas des exigences du Skill.

L'utilisateur approuve ou corrige le cahier des charges. Enregistrer une synthèse textuelle de la décision, la date et les contraintes; ne pas fabriquer d'approbation.

## Phase 1 — masterplan

Analyser registre, zones voisines, topographie, route réseau, usage, échelle TPP. Dessiner sur données métriques, auditer puis rendre SVG depuis JSON. Livrer plan lisible et table des emprises. Corriger toutes les violations bloquantes avant de solliciter la validation. Ne jamais faire passer l'imprécision d'une esquisse pour une erreur de caméra.

## Phase 2 — greybox

L'approbation du masterplan est obligatoire. Ajouter uniquement la zone de travail, sans modifier les zones gelées. Vérifier scène réellement chargée, coordonnées, emprises, hauteurs, collisions, caméra joueur et plusieurs cheminements. Captures: orthographique, spawn, points de jonction, intersections, place/repère, sortie. Consigner les mesures, les tests non réalisés et leurs conséquences.

## Phase 3 — DA et assets

Avec la greybox approuvée, recueillir si nécessaire les préférences artistiques non précisées; proposer des alternatives argumentées. Créer un style guide local, un plan d'habillage et un inventaire des assets (disponibles, gratuits à sourcer, uniques à créer), plus licence, budget de détails et plan de visibilité. Validation spécifique des téléchargements / écritures externes. La liste d'assets est un plan avant le placement.

## Phase 4 — habillage

Travail par sous-zones et couches: masses architecturales, entrées/façades, signalétique, traces d'activité, mobilier, lumière, finition. Captures réelles au niveau du joueur, vérifications de dégagement, cohérence d'usage et de styles, budget GPU. Itérer localement puis soumettre les vues et la liste de nouvelles ressources. Ne pas construire une scène « belle » au détriment de l'échelle et des accès.

## Phase 5 — gel

Après approbation explicite de phase 4, consigner l'empreinte du masterplan, l'identifiant et le statut `locked` dans le registre, associer les preuves de validation, les chemins de fichiers et les décisions. Une extension ne doit pas changer silencieusement le gel précédent.

## Règles universelles

- Un jalon humain ne peut pas être satisfait par l'agent en écrivant « approuvé » dans un fichier.
- Toute modification majeure du contrat d'une phase validée exige retour à cette phase et nouvel accord.
- À la reprise : identifier le dernier jalon approuvé et les changements intervenus depuis; signaler les changements hors bande.
- Autorisation de franchir une phase ≠ autorisation de télécharger des assets, d'écrire dans Notion, de créer une branche Git ou de modifier une zone protégée.
- Ne pas inventer d'images, de screenshots ou de résultats de test.
