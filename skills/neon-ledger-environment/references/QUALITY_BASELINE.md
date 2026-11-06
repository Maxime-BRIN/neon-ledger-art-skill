# Plancher de qualité visuelle — V1.7

## Pourquoi
Les kits K01–K04 du Faubourg V3 ont été livrés « prêts » (licence, import, cotes) alors que leurs rendus étaient des volumes à couleurs unies, 36 triangles pour un mur, sans texture : très en dessous de B18. Cause : le skill ne fixait de barre visuelle que par rapport à un concept approuvé (B18 en avait un, itéré V1 → V2 avec validation humaine). Sans concept, rien n'imposait de niveau, et `GEOMETRY_PASS` suffisait. Un kit modulaire n'est pas exempté de qualité sous prétexte qu'il est « structurel ».

## Règle
Tout asset, module ou kit livré doit atteindre le **niveau de l'asset de référence approuvé du projet** (Neon Ledger : B18, `docs/production/k01/b18_art_v2/` et `b18_material_ab/`), même sans concept dédié. Sans cela : `VISUAL_INCOMPLETE`, jamais « prêt ».

## Plancher (mesurable)
1. **Aucun aplat de couleur** : chaque surface a un matériau PBR (BaseColor + Roughness + Normal OpenGL), densité d'au moins 512 px/m sur les surfaces vues de près, matières locales du dépôt (Concrete034, PaintedMetal004…).
2. **Géométrie réelle** pour joints, biseaux, cadres, ferrures, fixations, caissons ; pas de boîte à 12 triangles.
3. **Usure causale** (reprises, humidité de pied, coulures sous fixations, abrasion sur arêtes), masques fins et irréguliers : des taches grosses et contrastées font effet granito et ne passent pas.
4. **Habillage de la famille** : accessoires, ferrures, signalétique abstraite, réseaux attachés selon la matrice de fidélité.
5. **Rendu Godot réel** de nuit ET en lumière neutre, à côté de la référence (même caméra) ; contrôle gros plan à 1,7 m. Les budgets (triangles, mémoire) sont mesurés et annoncés, pas utilisés pour justifier des aplats.
6. **Les chiffres ne prouvent rien** : cotes, import, nombre de modules et licences ne valent jamais « prêt » seuls ; la capture comparée à la référence décide.

## Méthode
- Lire d'abord les sources de l'asset de référence (production.md, scripts de matières) et les réutiliser.
- Produire UN témoin, le valider visuellement contre la référence, puis seulement décliner (palette, variantes). Jamais décliner avant validation du témoin.
- Les shaders et effets Godot (grime à l'échelle monde, SSR, SDFGI) font partie du niveau B18 : un GLB cuit seul ne suffit pas à l'atteindre, le prévoir (matériaux `.tres` / shader) dès le départ.
- Chaque écart restant est listé (BLOCKER / MAJOR / MINOR) ; ne pas déclarer le niveau atteint sans comparaison côte à côte.
