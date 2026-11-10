---
name: neon-ledger-urban-fabric
description: "Règles de tissu urbain dense et de bâtiments voxel orientés pour Neon Ledger (Godot 4). Utiliser dès qu'on compose, densifie, génère ou contrôle les îlots et emprises bâties d'un quartier (masterplan, générateur procédural, greybox voxel), en particulier quand des rues ne sont pas alignées sur la grille du monde. Interdit les façades en escalier dues à la rastérisation d'emprises tournées et fixe des seuils de densité vérifiables. Complète neon-ledger-city-builder sans le remplacer."
---

# Neon Ledger — Urban Fabric (V0.3)

Ce skill fixe **comment le bâti remplit un quartier** : densité, alignement sur la rue, orientation des volumes. Le **workflow, les jalons humains et la protection des zones** restent ceux de `neon-ledger-city-builder` : lire son `SKILL.md` d'abord. Ici, rien ne dispense d'une validation de masterplan.

Origine : retour du 2026-11-10 sur le quartier test procédural, jugé « pas assez dense » avec des « bâtiments en escalier » parce que les emprises suivant des rues en biais étaient découpées en cellules de 1 m sur la grille du monde.

## Règle 1 — Jamais de façade en escalier

Un bâtiment n'est **jamais rastérisé sur la grille du monde**. Il est construit dans **son propre repère** (axe X le long de sa rue), puis placé par une transformation rigide (translation + rotation autour de Y).

- Emprise = rectangle, L, U ou assemblage de rectangles **dans le repère du bâtiment**. Pas d'emprise définie comme un ensemble de cellules du monde, pas de test « cellule dans le polygone » pour décider où poser des voxels.
- Le modèle voxel (VoxModel ou équivalent) est rempli en coordonnées locales entières ; le mesh est généré puis tourné d'un bloc. Les façades restent planes à tout angle.
- Seul ce qui touche le sol suit le terrain : le socle/plateforme descend jusqu'au point le plus bas de l'emprise transformée ; le plancher reste plat.
- Collision : celle du mesh transformé, ou une boîte orientée par volume. Jamais une collision par cellule du monde.
- Les rues, trottoirs et sols peuvent rester sur la grille d'altitude du monde (heightmap lisse) : seuls les volumes bâtis sont concernés.

**Contrôle automatique obligatoire** (test du projet) : pour chaque bâtiment, vérifier que son emprise est décrite en repère local par des rectangles et que l'angle du bâtiment vaut l'angle de sa rue de rattachement à 0,5° près. Un générateur qui produit une emprise par cellules du monde échoue le test.

## Règle 2 — Densité d'un tissu de ville, pas de pavillons isolés

Valeurs par défaut pour un quartier marchand/populaire ; l'utilisateur peut les changer, l'agent ne les baisse pas seul.

| Mesure | Défaut | Comment la mesurer |
| --- | --- | --- |
| Emprise bâtie / surface d'îlot (hors voirie et places) | ≥ 70 % | somme des emprises locales / aire des îlots |
| Front bâti continu le long des rues | ≥ 80 % de la longueur de façade d'îlot | segments de façade à ≤ 2 m de la limite de rue |
| Retrait façade / bord de trottoir | 0 à 2 m | distance perpendiculaire en repère local |
| Mitoyenneté | façades contiguës, joint ≤ 0,5 m ou partagé | distance entre emprises voisines du même îlot |
| Ruelles / passages entre îlots | 3 à 4 m de large | |
| Hauteurs | variées voisin à voisin (au moins 3 gabarits par îlot) | |
| Vides | réservés et nommés (place, placette, parvis, cour) | jamais un reste de découpe |

Un îlot se découpe en **parcelles étroites et profondes** perpendiculaires à la rue (largeur 6 à 14 m), pas en un seul gros volume posé au milieu. Les angles d'îlot reçoivent un bâtiment d'angle (L) qui tient les deux rues.

## Règle 3 — Carrefours et rues en biais

- Chaque parcelle est rattachée à **une** rue ; son repère suit cette rue. À un angle entre deux rues non parallèles, le bâtiment d'angle est un L dont chaque aile suit sa rue, ou un rectangle sur la rue principale avec un pan coupé.
- Le vide triangulaire qui reste au cœur d'un îlot en biais devient une cour nommée, jamais un escalier de voxels.
- Aucune emprise transformée ne déborde sur la chaussée, le trottoir ou une emprise voisine (test de recouvrement en polygones, pas en cellules).

## Règle 4 — La densité se compose depuis l'existant

Les seuils de la Règle 2 ne se remplissent jamais dans un rectangle libre. La première bande bâtie reprend l'orientation, les parcelles et les gabarits de la rue existante. Le tissu dense et les biais viennent ensuite. Voir `neon-ledger-city-builder` → `references/EXTENSIONS.md` § Intégration à l'existant.

## Livrables

- **TOUJOURS** : SVG vue de dessus + SVG vue de côté + dénivelé affiché (cotes aux nœuds, pentes %, profil du sol) + SVG de contexte avec la ville existante (repère monde), même pour une étude intermédiaire (règle de `neon-ledger-city-builder`).
- Masterplan (JSON + SVG via city-builder) montrant **les parcelles et leur repère**, avec le tableau de densité de la Règle 2 rempli par îlot.
- Test automatique : Règle 1 (emprise locale + angle), recouvrements, et chaque seuil chiffré de la Règle 2.
- En greybox : captures à hauteur de joueur dans une rue en biais, prouvant des façades planes.

## Pièges

- « Organique » ne veut pas dire « emprises par cellules » : l'irrégularité vient des rues, des retraits et des hauteurs, pas d'un contour pixelisé.
- Une marge de sécurité large entre rue et bâti (pour passer un test d'empiètement) détruit la densité : mesurer l'empiètement en polygones exacts plutôt qu'élargir la marge.
- Ne pas déclarer la densité atteinte sur la foi du SVG : la recalculer depuis les données du générateur.
