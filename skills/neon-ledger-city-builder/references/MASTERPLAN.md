# Masterplan 2D — méthode

1. Déterminer contraintes et usages : voies, livraisons, piétons, transitions, bâtiments, densité, identité et échelle de la zone.
2. Définir le zoning et le réseau de parcours **avant** de remplir la grille avec les bâtiments.
3. Tracer les points de vue à hauteur du joueur et les repères spatiaux; vérifier la visibilité sans se limiter au plan zénithal.
4. Déterminer les emprises réservées, bâties, reculs de façades, rapports de hauteurs, nombre d'étages et fonctions des rez-de-chaussée. Aucun bâtiment ne doit chevaucher la surface utile des voies.
5. Ne pas confondre largeur totale d'une rue et largeur piétonne utile (trottoirs, caniveaux, obstacles, étals).
6. Proposer des voies alternatives seulement si elles ont un intérêt de gameplay; aucun chiffre universel de densité ou de nombre de parcours n'est imposé.
7. Convertir le plan en JSON; valider; générer le SVG via script; comparer visuellement carte et tables. Seules les modifications JSON précèdent les nouveaux SVG.
8. Livrer carte avec titres, orientation, échelle, bâtiments identifiés, fonctions/hauteurs, circulation, spawn/sortie, POI, raccordements, limites et légende.
9. Fournir les anomalies restantes et la demande de validation. Ne jamais lancer la greybox avant accord.

### Acceptation

Un masterplan passe seulement si les emprises et liens sont cohérents, la lecture du SVG est suffisante pour que l'utilisateur décide et les arbitrages artistiques importants sont approuvés. Le validateur géométrique ne remplace pas cette lecture.
