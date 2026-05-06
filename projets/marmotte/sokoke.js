const jeu = {
  0: {
    t: "_w4x.2",
    c: [
      {
        get t() {
          return badEnding9 ? "Oubliez mes salutations..." : "Bonjour"
        },
        next: 1,
      },
    ],
    music: null,
  },
  1: {
    t: "Pour une expérience complète, montez le volume à environ 35%.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "Non merci, je fais sans", next: 3 },
    ],
  },
  2: {
    t: "Voudriez-vous bien vérifier cela ?",
    c: [
      { t: "Oui", next: 7 },
      {
        t: "Non merci",
        action: (button) => {
          deplacerBouton(button)
          return false
        },
      },
    ],
  },
  3: {
    t: "Pour une expérience complète, montez le volume à environ 35%.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "Vous êtes sûr de vous ?", next: 4 },
    ],
  },
  4: {
    t: "Pour une expérience complète, montez le volume à environ 35%.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "Vraiment sûr ??", next: 5 },
    ],
  },
  5: {
    t: "Pour une expérience complète, montez le volume à environ 35%.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "VRAIMENT SÛR ?", next: 6 },
    ],
  },
  6: {
    t: "Pour une expérience complète, montez le volume à environ 35%.",
    c: [{ t: "J'ai augmenté le son", next: 2 }],
  },
  7: {
    t: "Quel animal produit ce son ?",
    audio: "meu.mp3",
    audioVolume: 0.35,
    c: [
      { t: "Un chat", next: 9 },
      { t: "Un orang-outan", next: 9 },
      { t: "Un canard", next: 9 },
      { t: "Une vache", next: 8 },
      { t: "Un mammouth", next: 9 },
    ],
  },
  8: {
    t: "Merci pour votre confiance.",
    music: "intro",
    bg: "#c4c4c4",
    boxbg: "#c6c6c6d8",
    border: "#c4c4c4",
    c: [{ t: "Avec plaisir", next: 10 }],
  },
  9: {
    t: "Vous mentez ?",
    c: [
      { t: "Oui", next: 3 },
      {
        t: "Non",
        next: 0,
        action: () => {
          badEnding9 = true
        },
      },
    ],
  },
  10: {
    t: "Bienvenue dans _w4x.2",
    c: [{ t: "Bien", next: 13 }],
  },
  13: {
    t: "Vos réponses sont enregistrées",
    c: [
      { t: "Entendu", next: 18 },
      { t: "Et mes données ?", next: 16 },
    ],
  },
  12: {
    t: "これは現実じゃない。最初から存在していなかった。",
    c: [{ t: "???", next: 20 }],
    bg: "#59283e",
    border: "#ffc9c5",
    boxbg: "#b94562bd",
    music: "yume",
    // url: "./..png",
  },
  16: {
    t: "Vos données sont sécurisées et stockées sur les serveurs de la société hubiC, fournie par ██████.",
    c: [
      { t: "Compris", next: 18 },
      { t: "Cela me semble sûr", next: 18 },
      { t: "Et le RGPD ?", next: 17 },
    ],
  },
  17: {
    t: "Aucune loi n'est en vigueur à ██████.",
    bg: "#7c7c7c",
    boxbg: "#535353d8",
    border: "#c4c4c4",
    c: [{ t: "Ah...", next: 18 }],
    music: "vie_privee",
  },
  18: {
    t: "Merci pour votre compréhension. _w4x.2 peut à présent commencer.",
  },
  19: {
    t: "Vous avez trois choix.",
    c: [
      { t: "1", next: 100 },
      { t: "2", next: 300 },
      { t: "3", next: 12 },
    ],
  },
  20: {
    t: "Vous avez 2 c̵̨̧̢̨̧̤͖̤͇̤͕̜̝̱̦̹͈̝̭͍͉͚̟͓͍̘̪̮̬̟͔̮͇̳̩̯͍͖̲͎͙̩͆̈́̉̔̌̈̇̐͒͛̍̔̈̅̌̿̈̊͋̏͛͊͆̓͑͊͘͜͜ͅh̶̨̢̺̰͉̪̟̬̟̺͉̤̮̣̱̳̗̦̱͓̘̹͓̘͔̞̱̱͙̫͖̺͓̟̲͙͎̱̘̺͎̝̺̻̜̳̫̰͇̹̼̭̏̔̽̎́̽̈́̽̑̊̅̿̑̓̋̊̐̏͑͋͐̏͆̾́̇̅͘͜͝͝͝ͅͅǫ̸̨̧̨̧̢̢̧̢̡̛͖͖̦̯͈̫̦͙̰͎͈̰̤̟̰̥̫̝̫͈̥̬̩̹̝̬̦̜̙̜̞̠͈̲̜͚̟̳̪̼̱̮̥͓͉͉̭̬̪̯͕̖͖̠̖͎͚̞̇̐͒̑̎̀̑̎̓̄̄́̐͗̓͌̄̀̋̉̑̾̃̀͌̄̄͗͐̾̀̈̊͛̃̓̐̓͌͋͌́̆̔̈͐̐͗̊́̈́̒̈́͂̍̅̇̓̎͒͘̕̚͘͘̚̚͜͜͜͠͠͝͝͠͝͠͠͝ͅͅi̴̡̧̡̢̡̛̲͔͍̗̮̺͇͕̟̹̭̮̦̗̘̱͉̩͍̻̥͚̮̳̱̭̣̙͓̲̺͍͙̪̠̫̼͇̼̹͎̞͎̤̼͉̪̫̰̫̭̾̾͑̈́̈͛̐̍̾̋͐̃̒̊̋͆̿̿͊̿̇̃̑͑̈̒͘̚͜͜͜͝͠ẋ̵̨̧̨̧̘̺̞̹̞̻̭̗̣̫͍̳̜̠͙͎̩͉̹͚̞̻̰̹̬̖̳̯̼͈̝̰̠̥̦̱͉̩͉̝͈̯̥̲̲̲̫̳̘̜͇̖̥̙̝̻̬̙̘̦̬̊́͜͝ͅ.",
    c: [
      { t: "1", next: 100 },
      { t: "2", next: 300 },
    ],
  },
  21: {
    t: "Vous avez 1 choix",
    c: [{ t: "2", next: 300 }],
  },
  22: {
    t: "Vous avez 1 choix",
    c: [{ t: "1", next: 100 }],
  },
  100: {
    t: "Bienvenue dans le Scénario 1 ! Avant de commencer nous vous demanderons de bien vouloir confirmer que vous n'êtes pas un robot.",
    c: [
      {
        t: "Très bien allons-y.",
        next: 101,
      },
    ],
  },
  101: {
    t: "Indiquez le nombre d'images présentant une voiture.",
    c: [
      { t: "Deux", next: 103 },
      { t: "Quatre je crois", next: 103 },
      { t: "Heu... je n'en vois aucune", next: 103 },
      { t: "J'en ai ras le cul de ces tests !", next: 102 },
    ],
    bg: "#c4c4c4",
    boxbg: "#c6c6c6d8",
    border: "#c4c4c4",
    music: "yume",
    img: "je_ne_suis_pas_un_robot.png",
  },
  102: {
    t: "On s'en fiche",
    c: [
      {
        t: "Sympa",
        next: 101,
      },
    ],
  },
  103: {
    t: "Nous vous remercions de votre confirmation en tant qu'IA. Le scénario peut commencer.",
    c: [
      {
        t: "Ouais c'est ça",
        next: 104,
      },
    ],
  },
  104: {
    t: "Vous vous trouvez sur un chemin dans une forêt (début par défaut), vous décidez :",
    c: [
      { t: "D'aller à gauche", next: 105 },
      { t: "De revenir sur vos pas", next: 106 },
      { t: "D'avancer", next: 108 },
      { t: "D'aller à droite (même si je peux vous dire que c'est une mauvaise idée)", next: 107 },
    ],
    url: "foret.jpg",
    music: "oiseau",
  },
  105: {
    t: "Mouaih une impasse, rien à voir par là",
    c: [
      {
        t: "Faire demi-tour",
        next: 104,
      },
    ],
    url: "foret.jpg",
  },
  106: {
    t: "Hop pop pop on a pas encore construit cette partie de la map, vous n'êtes pas censé être là...",
    c: [
      {
        t: "C'est pas ma faute si votre jeu est buggé",
        next: 104,
      },
    ],
    url: "construction.png",
  },
  107: {
    t: "Vous n'aviez pas vu le ravin et vous vous précipitez dedans : vous êtes mort ",
    c: [
      {
        t: "Je vous avez prévenu ",
        next: 104,
      },
    ],
    url: "ravin.jpg",
  },
  108: {
    t: "(Pff quel choix basique, mais le bon il semblerait) Vous continuez votre périple dans la forêt quand soudainement vous tombez sur un chat fumant ... de l'herbe à chat. ",
    c: [
      {
        t: "Euh...",
        next: 109,
      },
    ],
    url: "foretchat.jpg",
  },
  109: {
    t: "Bonjour jeune entrepreneur",
    c: [
      {
        t: "Vous vous demandez si vous ne fumeriez pas un peu vous aussi.",
        next: 110,
      },
    ],
    url: "foretchat.jpg",
    audio: "meow.mp3",
  },
  110: {
    t: "Le chat vous regarde et tout à coup vous tend sa patte :",
    c: [
      { t: "Vous la prenez sans réfléchir (la patte) : Après tout que pourrait-il arriver ?", next: 112 },
      { t: "Vous n'êtes pas fou, vous gardez vos distances ", next: 111 },
    ],
    url: "foretchat.jpg",
  },
  111: {
    t: "Le chat vous regarde et retend sa patte, en ne vous laissant pas le temps cette fois-ci de vous écartez, il attrape votre main.",
    c: [
      {
        t: "Mais c'était une fausse question à choix multiple !",
        next: 112,
      },
    ],
    url: "foretchat.jpg",
  },
  112: {
    t: "Tout devient flou autour de vous et vous vous sentez transporté, finalement vos alentours se stabilisent et vous vous rendez compte que vous vous êtes téléporté... Mais horreur vous reconnaissez l'endroit !",
    c: [
      {
        t: "Qu'est-ce qu'il y a, je suis où, bon sang ???",
        next: 113,
      },
    ],
    bg: "#c4c4c4",
    boxbg: "#c6c6c6d8",
    border: "#c4c4c4",
    music: null,
    audio: "téléporte.mp3",
  },
  113: {
    t: "Zut, patacrote, (le reste est censuré), s'exclame le chat, qui vous a, semble-t-il accompagné. Je nous ai transporté au mauvais endroit ! Nous sommes dans un lieu terrible... Nous sommes au Lycée Jean Mermoz. Et il semblerait que le portail soit fermé...",
    c: [
      {
        t: "Super et j'imagine que c'est moi qui vait devoir trouver un moyen de nous sortir d'ici, hein ?",
        next: 114,
      },
    ],
    url: "lycéechat.png",
    music: "crowd",
    audio: "meow.mp3",
  },
  114: {
    t: "Oui c'est ça, comment avez-vous deviné ? ",
    c: [
      {
        t: "Vous grommelez mais ne rajoutez rien (vous êtes un peu une petite victime) ",
        next: 115,
      },
    ],
    alert: "Nouvelle mission  : Trouver un moyen de vous échapper du Lycée Jean Mermoz",
    url: "lycéechat.png",
    audio: "meow.mp3",
  },
  115: {
    t: "Bon, il semblerait que nous devions activer le mécanisme permettant l'ouverture du portail, or celui-ci se trouve derrière cette porte... qui est malheureusement fermée à clé. Donc il faut que nous trouvions cette clé ! ",
    c: [
      {
        t: "A vous entendre parler on dirai que vous faites ça tous les jours ",
        next: 116,
      },
    ],
    url: "lycéechat.png",
    audio: "meow.mp3",
  },
  116: {
    //Si le bouton porte bleue et le bouton porte jaune ont tous les deux été pressé alors rendre scénario 121, plutôt que 120
    t: "Très bien vous voilà donc bloqué avec ce chat pas très net, mais pas de soucis vous allez vous en sortir. Vous vous trouvez en face de trois portes : ",
    c: [
      {
        t: "Vous essayer la porte bleue",
        action: () => {
          porteb = true
        },
        next: 117,
      },
      {
        t: "Vous essayez la porte jaune",
        action: () => {
          portej = true
        },
        next: 118,
      },
      {
        t: "Vous essayez la porte pas peinte",
        action: () => {
          if (porteb && portej) {
            choix(121)
          } else {
            choix(120)
          }
          return false
        },
      },
      { t: "Pourquoi entendons nous des gens discuter en fond alors que le lycée est complètement désert ?", next: 119 },
    ],
    url: "lycée.jpg",
  },
  117: {
    t: "Quelque chose semble bloquer la porte de l'intérieur",
    c: [
      {
        t: "Je me demande bien ce que c'est",
        next: 116,
      },
    ],
    url: "lycée.jpg",
  },
  118: {
    t: "Celle-ci est fermée à clé",
    c: [
      {
        t: "Bon bah pas par là du coup",
        next: 116,
      },
    ],
    url: "lycée.jpg",
  },
  119: {
    t: "Vous croyez vraiment obtenir une réponse à cette question ?",
    c: [
      {
        t: "Peu importe, je ne choisi même pas vraiment ce que je réponds ...",
        next: 116,
      },
    ],
    url: "lycée.jpg",
  },
  120: {
    t: "Celle-ci s'ouvre.",
    c: [
      {
        t: "Parfait",
        next: 122,
      },
    ],
    url: "lycée.jpg",
  },
  121: {
    t: "Celle-ci s'ouvre.",
    c: [
      {
        t: "C'est quoi toutes ces portes barricadées sérieux ?!!",
        next: 122,
      },
    ],
    url: "lycée.jpg",
  },
  122: {
    t: "Vous entrez dans un local technique, vous y trouvez une clé et un aspirateur.",
    c: [
      {
        t: "Vous prenez la clé et l'aspirateur",
        next: 123,
      },
    ],
    url: "lycée.jpg",
  },
  123: {
    t: "Vous êtes de retour dans le couloir",
    c: [
      { t: "Porte jaune : vérouillée ", next: 126 },
      { t: "Porte bleue condamnée de l'intérieur ", next: 124 },
    ],
    audio: "zelda.mp3",
    url: "lycée.jpg",
  },
  143: {
    t: "Vous êtes de retour dans le couloir",
    c: [
      { t: "Porte jaune : vérouillée ", next: 126 },
      { t: "Porte bleue condamnée de l'intérieur ", next: 124 },
    ],
    url: "lycée.jpg",
  },
  124: {
    t: "Vous utilisez",
    c: [
      { t: "Clé", next: 125 },
      { t: "Aspirateur", next: 125 },
    ],
    url: "lycée.jpg",
  },
  125: {
    t: "Cela ne fonctionne pas, logique...",
    c: [
      {
        t: "Oui bon ça va, j'essaie juste de faire le tour de tout les recoins du jeu.",
        next: 143,
      },
    ],
    url: "lycée.jpg",
  },
  126: {
    t: "Vous utilisez",
    c: [
      { t: "Clé", next: 127 },
      { t: "Aspirateur", next: 128 },
    ],
    url: "lycée.jpg",
  },
  127: {
    t: "Utilisez une clé pour déverouiller une porte ?? Ridicule.",
    c: [
      {
        t: "Vous êtes des malins vous.",
        next: 143,
      },
    ],
    url: "lycée.jpg",
  },
  128: {
    t: "Grâce à votre super aspirateur vous réussissez à faire bouger le loquet assez pour déverouiller la porte. Celle-ci s'ouvre ! ",
    c: [
      {
        t: "...",
        next: 129,
      },
    ],
    url: "lycée.jpg",
  },
  129: {
    t: "Vous entrez dans une salle de cours assez banale, se nommant apparament la B101. Vous y découvrez une autre porte menant vers la salle d'à-côté, vérouillée par un cadenas à 3 chiffres. Vous trouvez aussi une lettre rédigée dans une magnifique italique posée sur une table. ",
    c: [
      { t: "Regarder la lettre rédigée dans une magnifique italique", next: 130 },
      { t: "Essayer de déverrouiller le cadenas ", next: 131 },
    ],
    url: "lycée.jpg",
  },
  130: {
    c: [
      {
        t: "Je vois",
        next: 129,
      },
    ],
    img: "lettre.png",
  },
  131: {
    t: "Un cadenas à 3 chiffres bloque la porte.",
    c: [
      {
        t: "Entrer le code",
        action: () => {
          const code = prompt("Entrez le code à 3 chiffres :")
          const clean = code.trim()

          if (clean.length !== 3) {
            alert("C'est un cadenas à 3 chiffres… pas plus, pas moins.")
            return false
          }

          if (code === "100") {
            choix(133)
          } else {
            alert("Bouh loser, c'est pas ça")
            return false
          }

          return false
        },
      },
      {t: "Retourner en arrière.", next: 129,},
    ],
  },
  133: {
    t: "La porte s'ouvre dans un grincement. Vous entrez dans une nouvelle salle de cours, posez bien en évidence sur la table se trouve une clé annoté : clé de la guérite possédant le mécanisme d'ouverture du portail du Lycée Jean Mermoz. ",
    c: [
      {
        t: "Enfin ! Vous la prenez ",
        next: 134,
      },
    ],
    audio: "zelda.mp3",
    url: "lycée.jpg",
  },
  134: {
    t: "Vous réalisez vous trouvez dans la salle à la porte bleue qui était condamné de l'intérieur. Celle-ci est en effet bloquez par une bouteille d'eau en plastique. ",
    c: [
      {
        t: "Et bien je comprends mieux pourquoi je n'arrivai pas à entrer avant",
        next: 135,
      },
    ],
    url: "lycée.jpg",
  },
  135: {
    t: "Vous tentez de bouger la bouteille en plastique. Mince, vous n'avez plus assez d'energie pour effectuer cette action. Mais pas de souci, vous pouvez en regagner en visionnant cette publicité :",
    c: [
      {
        t: "Pub",
        action: () => {
          lancerVideo("Pub.mp4")
          return false
        },
      },
    ],
    url: "lycée.jpg",
  },
  137: {
    t: "Vous pouvez enfin déplacer la bouteille et revenir dans le couloir.",
    c: [
      {
        t: "Mais attendez une seconde pourquoi je ne suis pas juste revenu sur mes pas ? ",
        next: 138,
      },
    ],
    url: "lycée.jpg",
  },
  138: {
    t: "Vous retournez près du portail et retrouvez le chat, qui n'avait pas bougé depuis votre arrivée ",
    c: [
      {
        t: "J'ai la clé, et ce n'est pas grâce à toi ",
        next: 139,
      },
    ],
    url: "lycéechat.png",
  },
  139: {
    t: "Formidable, passe la moi, je m'occupe du reste.",
    c: [
      {
        t: "Quelle générosité ",
        next: 140,
      },
    ],
    url: "lycéechat.png",
    audio: "meow.mp3",
  },
  140: {
    t: "Le chat ouvre la guérite et actionne l'ouverture du portail, finalement vous êtes libre !!",
    c: [
      {
        t: "Oui oui, voyons pour combien de temps",
        next: 141,
      },
    ],
    url: "lycéechat.png",
  },
  141: {
    t: "Alors que vous vous éloigné, le chat vous rappelle : Attendez jeune entrepreneur, vous n'avez pas tirer de leçon de cette aventure ? Alors dite-moi qu'elle est la morale de l'histoire ?",
    c: [
      { t: "D'éviter au plus possible le Lycée Jean Mermoz ? ", next: 142 },
      { t: "De ne jamais m'approcher d'un chat fumant dans un bois ? ", next: 142 },
      { t: "De ne pas jouer à un jeu programmé par 3 adolescents ? ", next: 142 },
    ],
    alert: "Mission accomplie : Vous vous êtes échappé du Lycée Jean Mermoz !",
    url: "lycéechat.png",
    audio: "meow.mp3",
  },
  142: {
    t: "Mais non, vous n'y êtes pas du tout. La conclusion est que peu importe la situation, le pouvoir de l'amitié triomphe toujours !",
    c: [
      {
        t: "Vous vous éloigné en courant ",
        next: 143,
      },
    ],
    url: "lycéechat.png",
    audio: "meow.mp3",
  },
  143: {
    //! fin 1
    t: "Bravo vous avez survécu au Scénario 1 !",
    get c() {
      return [
        {
          t: "Merci",
          action: () => {
            end1 = true
          },
          next: end1 && end2 ? 1000 : 21,
        },
      ]
    },
    alert: "Accomplissement : Le chat fumant semble avoir dévellopé des sentiments pour vous.",
  },

  300: {
    t: "Bienvenue dans la forêt...(Votre objectif : Ne pas mourir)",
    c: [
      { t: "Vous criez à l'aide", next: 301 },
      { t: "Vous marchez sans bruit", next: 302 },
    ],
    music: "foret",
    bg: "#3B4D37",
    boxbg: "#4B573E",
    border: "#3E4031"
  },

  301: {
    t: "Vous êtes mort (Mangé par un ours qui vous a entendu).",
    c: [
      { t: "Recommencer", next: 300 },
      { t: "Recommencer", next: 300 },
      { t: "Recommencer", next: 300 },
      { t: "Recommencer", next: 300 },
    ],
    audio: "meurt.mp3",
  },

  302: {
    t: "Vous avancez bien joué. Vous trouvez un sac par terre...",
    c: [
      { t: "Ouvrir", next: 303 },
      { t: "Ignorer calmement", next: 304 },
      { t: "Explorer plus loin dans la forêt", next: 330 },
    ],
  },

  303: {
    t: "Dedns il y a une lampe torche et un sandwich",
    c: [
      { t: "Manger le sandwich", next: 305 },
      { t: "Jeter le sandwich", next: 306 },
    ],
  },

  304: {
    t: "Vous marchez encore et encore...",
    c: [{ t: "Et donc ?", next: 307 }],
  },

  307: {
    t: "Bah et donc vous tournez en rond (n'allez jamais en fôret, vous êtes nul en survie).",
    c: [{ t: "Prendre le compliment et recommencer", next: 300 }],
  },

  305: {
    t: "Vous avez fini en décomposition car le sandwich était toxique.",
    c: [{ t: "Recommencer", next: 300 }],
    audio: "meurt.mp3",
  },

  306: {
    t: "Bien joué, maitenant grâce à la lampe vous voyez un panneau sortie enfin !!",
    c: [
      { t: "Y aller", next: 308 },
      { t: "Partir a l'opposé", next: 309 },
    ],
  },

  308: {
    t: "un PANNEAU ??? dans la forêt..?? C'était un piège vous êtes mort... ",
    c: [{ t: "Recommencer", next: 300 }],
    audio: "meurt.mp3",
  },

  309: {
    t: "Bien joué il fallait réflechir... Maintenant vous entendez de l'eau...",
    c: [
      { t: "Y aller", next: 310 },
      { t: "Attendre", next: 311 },
    ],
    music: "riviere",
  },

  310: {
    t: "Vous devez traverser la rivière avant de pouvoir sortir",
    c: [
      { t: "Traverser à la nage", next: 312 },
      { t: "Traverser sur le pont", next: 313 },
    ],
    music: "riviere",
    bg: "#ADCACA",
    boxbg: "#6BBFBF",
    border: "#244040"
  },

  311: {
    t: "Et vous attendez quoi on peut savoir ?",
    c: [{ t: "Vous êtes mort d'ennuie, vous recommencez... encore", next: 300 }],
    audio: "meurt.mp3",
  },

  312: {
    t: "Vous vous êtes noyé. Bravo",
    c: [{ t: "Recommencer", next: 300 }],
    audio: "meurt.mp3",
  },

  313: {
    //! fin 2
    t: "Le pont est solide vous êtes sauvé en arrivant de l'autre coté",
    get c() {
      return [
        {
          t: "BRAVO vous avez enfin terminé ce jeu",
          action: () => {
            end2 = true
          },
          next: end1 && end2 ? 1000 : 22,
        },
      ]
    },
  },

  330: {
    t: "Vous vous enfoncez plus profondément dans la forêt... l'ambiance devient inquiétante.",
    c: [
      { t: "Continuer", next: 331 },
      { t: "Faire demi-tour", next: 302 },
    ],
  },

  331: {
    t: "Vous trouvez un vieux campement abandonné.",
    c: [
      { t: "Fouiller", next: 332 },
      { t: "Ne pas toucher", next: 333 },
    ],
  },

  332: {
    t: "Vous trouvez un couteau rouillé et une bouteille étrange.",
    c: [
      { t: "Boire", next: 334 },
      { t: "Garder le couteau", next: 335 },
    ],
  },

  334: {
    t: "La bouteille était toxique... mauvaise idée.",
    c: [{ t: "Recommencer", next: 300 }],
    audio: "meurt.mp3",
  },

  333: {
    t: "Vous entendez un bruit derrière vous...",
    c: [
      { t: "Se retourner", next: 336 },
      { t: "Courir", next: 337 },
    ],
  },

  336: {
    t: "Trop tard. Quelque chose vous attrape... vous êtes mort.",
    c: [{ t: "Recommencer", next: 300 }],
    audio: "meurt.mp3",
  },

  337: {
    t: "Vous courez et tombez sur une clairière.",
    c: [
      { t: "Traverser", next: 338 },
      { t: "Contourner", next: 339 },
    ],
  },

  338: {
    t: "Un piège caché au sol... vous êtes mort.",
    c: [{ t: "Recommencer", next: 300 }],
    audio: "meurt.mp3",
  },

  339: {
    t: "Vous contournez et trouvez... la rivière !",
    c: [{ t: "Continuer", next: 310 }], // rejoint ton chemin existant
    music: "riviere",
    bg: "#ADCACA",
    boxbg: "#6BBFBF",
    border: "#244040"
  },

  335: {
    t: "Avec le couteau, vous vous sentez plus en sécurité.",
    c: [{ t: "Continuer", next: 333 }],
  },
  1000: {
    t: "",
    c: [{ t: "Recommencer", next: 1 }],
    bg: "transparent",
    border: "transparent",
    boxbg: "transparent",
    url: "akinator_p.png",
    music: "victoire",
  },
}
let porteb = false
let portej = false

let scenarioActuel = 0
let badEnding9 = false
let end1 = false
let end2 = false

const musiques = {
  intro: { src: "for_the_fans.mp3", volume: 0.05 },
  yume: { src: "きえない_きずあと.mp3", volume: 0.05 },
  vie_privee: { src: "どこかへつづくもり〜森の世界〜.mp3", volume: 0.1 },
  oiseau: { src: "zosiaux.mp3", volume: 0.1 },
  crowd: { src: "gens_fond.mp3", volume: 0.5 },
  foret: { src: "foret.mp3", volume: 0.5 },
  riviere: { src: "riviere.mp3", volume: 0.4 },
  victoire: { src: "petit yodé et l'enfant siro - victoire.mp3", volume: 0.6 },
}

const lecteurMusique = new Audio()
lecteurMusique.loop = true

let musiqueCourante = null
let audioDebloque = false
let progressionInterval = null
let progressionValeur = 0
const volumeEffetsDefaut = 0.35

function changerFond(couleur) {
  document.documentElement.style.setProperty("--bodybg", couleur)
}

function changerBordure(couleur) {
  document.documentElement.style.setProperty("--border", couleur)
}

function changerFondBoite(couleur) {
  document.documentElement.style.setProperty("--boxbg", couleur)
}

function changerFondImage(urll) {
  document.documentElement.style.setProperty("--defaulturl", `url("${urll}")`)
}

function debloquerAudio() {
  if (audioDebloque) return
  audioDebloque = true
}

function jouerMusique(id) {
  if (!id) return
  if (musiqueCourante === id) return

  const piste = musiques[id]
  if (!piste) return

  musiqueCourante = id
  lecteurMusique.src = piste.src
  lecteurMusique.volume = piste.volume ?? 0.2
  lecteurMusique.play().catch(() => {
    audioDebloque = false
  })
}

function deplacerBouton(button) {
  button.style.position = "fixed"
  button.style.left = Math.random() * 80 + "vw"
  button.style.top = Math.random() * 80 + "vh"
}

function reinitialiserProgression() {
  if (progressionInterval) {
    clearInterval(progressionInterval)
    progressionInterval = null
  }

  progressionValeur = 0
  const barre = document.getElementById("bar")
  const container = document.getElementById("progressContainer")

  if (barre) {
    barre.style.width = "0%"
  }

  if (container) {
    container.style.display = "none"
    container.setAttribute("aria-hidden", "true")
  }
}

function demarrerProgressionScenario18() {
  const barre = document.getElementById("bar")
  const container = document.getElementById("progressContainer")
  if (!barre || !container) return

  if (progressionInterval) return

  container.style.display = "flex"
  container.setAttribute("aria-hidden", "false")
  barre.style.width = "0%"
  progressionValeur = 0

  progressionInterval = setInterval(() => {
    progressionValeur += 25

    if (progressionValeur >= 100) {
      progressionValeur = 100
      barre.style.width = `${progressionValeur}%`
      clearInterval(progressionInterval)
      progressionInterval = null
      choix(19)
      return
    }

    barre.style.width = `${progressionValeur}%`
  }, 1500)
}

function afficherScenario() {
  const scenario = jeu[scenarioActuel]
  const storyDiv = document.getElementById("story")
  const buttonsDiv = document.querySelector(".buttons")

  storyDiv.innerHTML = ""

  const texte = document.createElement("h1")
  texte.textContent = scenario.t
  storyDiv.appendChild(texte)

  if (scenario.img) {
    const image = document.createElement("img")
    image.src = scenario.img
    storyDiv.appendChild(image)
  }
  buttonsDiv.innerHTML = ""

  if (scenario.alert) {
    alert(scenario.alert)
  }

  // Si un changement de fond existe
  if (scenario.bg) {
    changerFond(scenario.bg)
  }

  if (scenario.border) {
    changerBordure(scenario.border)
  }

  if (scenario.boxbg) {
    changerFondBoite(scenario.boxbg)
  }

  if (scenario.url) {
    changerFondImage(scenario.url)
  } else {
    document.documentElement.style.setProperty("--defaulturl", "none")
  }

  // Si un son existe
  if (scenario.audio) {
    const audio = new Audio(scenario.audio)
    audio.volume = scenario.audioVolume ?? volumeEffetsDefaut
    audio.play()
  }

  // Si une musique existe
  if (scenario.music) {
    jouerMusique(scenario.music)
  }

  if (scenarioActuel === 18) {
    demarrerProgressionScenario18()
  } else {
    reinitialiserProgression()
  }

  ;(scenario.c ?? []).forEach((choixOption, index) => {
    const button = document.createElement("button")
    button.id = "btn" + (index + 1) // Simplicité pour sélectionner un bouton en CSS
    button.textContent = choixOption.t

    if (scenarioActuel === 1000 && index === 0) {
      button.style.position = "fixed"
      button.style.left = "1016px"
      button.style.top = "322px"
      button.style.transform = "translate(-50%, -50%)"
      button.style.margin = "0"
      button.style.paddingLeft = "10px"
      button.style.paddingRight = "30px"
      button.style.backgroundColor = "transparent"
      button.style.borderColor = "transparent"
      button.style.color = "transparent"
      button.style.boxShadow = "none"
      button.style.opacity = "0"
    }

    button.onclick = () => {
      if (scenarioActuel === 1000 && index === 0) {
        window.location.reload()
        return
      }

      debloquerAudio()

      const continuer = choixOption.action ? choixOption.action(button) : true
      if (continuer !== false) {
        let next = choixOption.next
        // Calculer dynamiquement après l'action pour 143 et 313
        if ((scenarioActuel === 143 || scenarioActuel === 313) && end1 && end2) {
          next = 1000
        }
        choix(next)
      }
    }
    buttonsDiv.appendChild(button)
  })
}

function choix(numeroScenario) {
  scenarioActuel = numeroScenario
  afficherScenario()
}

function lancerVideo(src) {
  const storyDiv = document.getElementById("story")
  const buttonsDiv = document.querySelector(".buttons")

  storyDiv.innerHTML = ""
  buttonsDiv.innerHTML = ""

  const video = document.createElement("video")
  video.src = src
  video.autoplay = true
  video.controls = false
  video.style.maxWidth = "100%"

  storyDiv.appendChild(video)

  video.addEventListener("ended", () => {
    choix(137)
  })
}

// Initialiser le jeu au chargement
window.onload = afficherScenario
