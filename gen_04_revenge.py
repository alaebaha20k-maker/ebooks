#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EBOOK 4/5 - Revenge Trading : Comment j'ai failli tout perdre"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
    Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether, PageBreak)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

NOIR=HexColor('#0A0A0A'); OR=HexColor('#C9A84C'); OR_PALE=HexColor('#FBF5E8')
OR_CLAIR=HexColor('#F5E6C8'); GRIS=HexColor('#4A4A4A'); GRIS_BG=HexColor('#F5F5F5')
PAGE_W,PAGE_H=A4; ML=MR=22*mm; MT=18*mm; MB=22*mm; CW=PAGE_W-ML-MR
TITLE="Revenge Trading : Comment j'ai failli tout perdre"

def S(n,**k):
    d=dict(fontName='Helvetica',fontSize=11,textColor=GRIS,leading=18.5,spaceAfter=8,alignment=TA_JUSTIFY)
    d.update(k); return ParagraphStyle(n,**d)

st={'body':S('b'),'bold':S('bd',fontName='Helvetica-Bold',textColor=NOIR,leading=18),
 'intro':S('i',fontSize=13,leading=22,spaceAfter=10),
 'h2':S('h2',fontName='Helvetica-Bold',fontSize=15,textColor=OR,leading=20,spaceBefore=16,spaceAfter=8),
 'dq':S('dq',fontName='Helvetica-Oblique',fontSize=12,textColor=OR_CLAIR,alignment=TA_CENTER,leading=20),
 'sn':S('sn',fontName='Helvetica-Bold',fontSize=32,textColor=OR,alignment=TA_CENTER,leading=38),
 'sl':S('sl',fontSize=8,textColor=GRIS,alignment=TA_CENTER,leading=12),
 'cb':S('cb',fontName='Helvetica-Bold',fontSize=9,textColor=OR,alignment=TA_CENTER,leading=14),
 'cn':S('cn',fontName='Helvetica-Bold',fontSize=13,textColor=OR_CLAIR,alignment=TA_CENTER,leading=18),
 't1':S('t1',fontName='Helvetica-Bold',fontSize=36,textColor=white,alignment=TA_CENTER,leading=44),
 't2':S('t2',fontName='Helvetica-Bold',fontSize=28,textColor=OR,alignment=TA_CENTER,leading=34),
 'cs':S('cs',fontSize=14,textColor=OR_CLAIR,alignment=TA_CENTER,leading=20),
 'ct':S('ct',fontSize=10,textColor=GRIS,alignment=TA_CENTER,leading=14),
 'cc':S('cc',fontSize=9,textColor=GRIS,alignment=TA_CENTER,leading=12),
 'cp':S('cp',fontName='Helvetica-Bold',fontSize=14,textColor=NOIR,alignment=TA_CENTER,leading=20,spaceAfter=8),
 'cb2':S('cb2',fontSize=10,textColor=GRIS,alignment=TA_CENTER,leading=16,spaceAfter=6),
 'tl':S('tl',fontName='Helvetica-Bold',fontSize=9,textColor=OR,leading=14),
 'tt':S('tt',fontName='Helvetica-Bold',fontSize=11,textColor=NOIR,leading=16),
 'ts':S('ts',fontSize=9,textColor=GRIS,leading=13,spaceAfter=6),
 'hl':S('hl',fontName='Helvetica-Bold',fontSize=9,textColor=OR,leading=14),
 'ht':S('ht',fontName='Helvetica-Bold',fontSize=22,textColor=NOIR,leading=28,spaceAfter=4),
 'hs':S('hs',fontSize=13,textColor=GRIS,leading=20,spaceAfter=12),
 'br':S('br',fontName='Helvetica-Bold',fontSize=14,textColor=OR,alignment=TA_CENTER,leading=20),
 'br2':S('br2',fontSize=10,textColor=GRIS,alignment=TA_CENTER,leading=16),
 'br3':S('br3',fontSize=10,textColor=OR,alignment=TA_CENTER,leading=16),
}

def footer(c,doc):
    c.saveState(); y=MB-8*mm
    c.setStrokeColor(GRIS); c.setLineWidth(0.3)
    c.line(ML,y+5*mm,PAGE_W-MR,y+5*mm)
    c.setFont('Helvetica',8); c.setFillColor(GRIS)
    c.drawString(ML,y,f"{TITLE}  ·  © TRADING ZONE")
    c.drawRightString(PAGE_W-MR,y,f"© TRADING ZONE  ·  {doc.page}"); c.restoreState()

def dq(t):
    tb=Table([[Paragraph(t,st['dq'])]],colWidths=[CW])
    tb.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),NOIR),('TOPPADDING',(0,0),(-1,-1),16),
        ('BOTTOMPADDING',(0,0),(-1,-1),16),('LEFTPADDING',(0,0),(-1,-1),22),('RIGHTPADDING',(0,0),(-1,-1),22)]))
    return KeepTogether([Spacer(1,8),tb,Spacer(1,8)])

def gb(items):
    t=Table([[Paragraph(i,st['body'])] for i in items],colWidths=[CW-32])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),OR_PALE),('BOX',(0,0),(-1,-1),2.5,OR),
        ('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),16),('RIGHTPADDING',(0,0),(-1,-1),16)]))
    return KeepTogether([Spacer(1,6),t,Spacer(1,6)])

def grb(items):
    inner=Table([[Paragraph(i,st['body'])] for i in items],colWidths=[CW-24])
    inner.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),GRIS_BG),('TOPPADDING',(0,0),(-1,-1),8),
        ('BOTTOMPADDING',(0,0),(-1,-1),8),('LEFTPADDING',(0,0),(-1,-1),16),('RIGHTPADDING',(0,0),(-1,-1),8)]))
    bar=Table([['']],colWidths=[3.5])
    bar.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),OR),('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
    combo=Table([[bar,inner]],colWidths=[3.5,CW-3.5])
    combo.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),0),
        ('BOTTOMPADDING',(0,0),(-1,-1),0),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0)]))
    return KeepTogether([Spacer(1,6),combo,Spacer(1,6)])

def sr(data):
    cw=CW/len(data)
    cells=[[Paragraph(v,st['sn']),Paragraph(l,st['sl'])] for v,l in data]
    t=Table([[Table([c],colWidths=[cw]) for c in cells]],colWidths=[cw]*len(data))
    t.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),4)]))
    hr=HRFlowable(width=CW,thickness=1,color=OR,spaceAfter=4)
    return KeepTogether([Spacer(1,6),hr,t,HRFlowable(width=CW,thickness=1,color=OR,spaceBefore=4),Spacer(1,6)])

def ch(lbl,title,sub):
    return KeepTogether([Paragraph(lbl,st['hl']),HRFlowable(width=CW,thickness=1.5,color=OR,spaceAfter=6),
        Paragraph(title,st['ht']),Paragraph(sub,st['hs'])])

def cover():
    rows=[[Paragraph('◆   COLLECTION LE CODE DU TRADER ÉLITE   ◆',st['cb'])],[Spacer(1,12)],
        [Paragraph('EBOOK 4 / 5',st['cn'])],[Spacer(1,20)],
        [Paragraph('REVENGE TRADING',st['t1'])],[Paragraph("Comment j'ai failli tout perdre", st['t2'])],
        [Paragraph('et comment l\'arrêter définitivement',st['t2'])],[Spacer(1,12)],
        [HRFlowable(width=70*mm,thickness=1.5,color=OR)],[Spacer(1,12)],
        [Paragraph('La psychologie derrière la spirale destructrice',st['cs'])],
        [Paragraph('et les 5 piliers pour en sortir pour de bon',st['cs'])],[Spacer(1,20)],
        [Paragraph('PSYCHOLOGIE DU TRADING · ÉDITION FRANÇAISE',st['ct'])],[Spacer(1,12)],
        [Paragraph('© TRADING ZONE — Tous droits réservés',st['cc'])]]
    t=Table(rows,colWidths=[170*mm])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),NOIR),('TOPPADDING',(0,0),(-1,-1),10),
        ('BOTTOMPADDING',(0,0),(-1,-1),10),('LEFTPADDING',(0,0),(-1,-1),20),
        ('RIGHTPADDING',(0,0),(-1,-1),20),('ALIGN',(0,0),(-1,-1),'CENTER')]))
    return [Spacer(1,25*mm),t]

def cpright():
    s=[Spacer(1,40*mm),Paragraph(TITLE,st['cp']),HRFlowable(width=80*mm,thickness=1,color=OR,spaceAfter=16)]
    for l in ['© 2024 TRADING ZONE — Tous droits réservés.',
        "Aucune partie ne peut être reproduite sans autorisation écrite.",'',
        'Auteur : TRADING ZONE — Édition numérique PDF','',
        "Avertissement : Cet ebook est destiné à un usage éducatif uniquement.",
        "Il ne constitue pas un conseil financier.",
        "Le trading comporte des risques importants.",'','www.tradingzone.fr']:
        s.append(Paragraph(l,st['cb2']))
    return s

def toc():
    s=[Spacer(1,10*mm),Paragraph('TABLE DES MATIÈRES',st['h2']),
       HRFlowable(width=CW,thickness=1,color=OR,spaceAfter=12)]
    for lbl,title,sub in [
        ('INTRODUCTION','La Spirale de Minuit','Ce que le revenge trading te coûte vraiment'),
        ('CHAPITRE 1','Anatomie d\'une Catastrophe','Comment une perte de 150€ devient 3 000€'),
        ('CHAPITRE 2','La Neurochimie de la Vengeance','Dopamine, cortisol et amygdale'),
        ('CHAPITRE 3','L\'Acceptation Radicale','Le premier pilier : changer ta relation à la perte'),
        ('CHAPITRE 4','Le Circuit Coupe-Feu','Les règles infranchissables qui te sauvent'),
        ('CHAPITRE 5','Le Changement d\'Identité','Devenir un gestionnaire de risques'),
        ('CONCLUSION','La Forteresse Mentale','5 piliers pour une liberté durable'),]:
        s+=[Paragraph(lbl,st['tl']),Paragraph(title,st['tt']),Paragraph(sub,st['ts']),Spacer(1,4)]
    return s

def content():
    P=lambda t:Paragraph(t,st['body'])
    PB=lambda t:Paragraph(t,st['bold'])
    H=lambda t:Paragraph(t,st['h2'])
    PI=lambda t:Paragraph(t,st['intro'])
    s=[]

    # INTRO
    s.append(ch('INTRODUCTION','La Spirale de Minuit','Ce que le revenge trading te coûte vraiment'))
    s.append(PI("Il est 23h un mardi soir. Votre écran scintille. Des chiffres rouges défilent. Encore. Vous fixez cette position qui saigne. Vous savez que vous devriez arrêter. Fermer. Éteindre tout. Mais vous ne pouvez pas. Pas encore. Parce que vous êtes en plein dans le revenge trading. Et cette fois, ça va vous coûter bien plus qu'une simple perte. Ça va vous coûter une partie de vous-même."))
    s.append(PI("Ce moment précis, cette montée d'adrénaline mêlée à la panique, cette voix intérieure qui vous hurle d'être raisonnable mais que vous ignorez, je le connais intimement. Je l'ai vécu. J'ai vu mon compte passer de 20 000 euros à moins de 5 000 en quelques semaines, uniquement à cause de cette pulsion incontrôlable de reprendre ce que le marché m'avait 'volé'."))
    s.append(sr([('78%','des traders particuliers abandonnent avant 1 an de rentabilité — à cause du revenge trading'),
                 ('2.5x','plus intense : la douleur d\'une perte vs le plaisir d\'un gain équivalent'),
                 ('90%','de réduction des pertes de revenge trading chez David en 4 semaines')]))
    s.append(dq('"Le revenge trading n\'est pas un manque de stratégie. C\'est un mécanisme de défense primaire de votre cerveau — une réaction primitive qui s\'active quand vous vous sentez attaqué par le marché."'))
    s.append(grb(["<b>PRIYA — 1 780€ EN UNE HEURE</b>",
        "Priya m'a envoyé un message à 3h du matin la semaine dernière. Elle venait de perdre 1 780 euros en une heure. Son trade initial, pourtant bien analysé, avait été stoppé pour une petite perte. Une perte de 120 euros. Gérable.",
        "Mais son ego n'a pas supporté cette humiliation. Il fallait récupérer. Il fallait prouver au marché qu'elle avait raison. Elle a multiplié la taille de ses positions par six. Elle a ignoré ses règles d'or. Et ce n'était pas la première fois.",
    ]))
    s.append(P("Combien de fois avez-vous dit 'plus jamais' après une session de revenge trading ? Ce cycle insidieux de promesse non tenue et de rupture ronge votre confiance. Il sape votre discipline jour après jour. La plupart des traders particuliers qui échouent ne le font pas à cause de mauvaises stratégies. Ils le font à cause de ce piège psychologique insidieux."))
    s.append(P("Le coût réel du revenge trading ne se limite jamais à l'argent que vous perdez. C'est aussi les heures incalculables de sommeil envolées, le stress chronique qui ronge vos relations personnelles, le poids écrasant de la culpabilité. C'est une érosion lente mais certaine de tout ce qui fait de vous un trader potentiellement confiant et performant."))

    # CH1
    s.append(ch('CHAPITRE 1','Anatomie d\'une Catastrophe','Comment une perte de 150€ devient 3 000€'))
    s.append(P("Imaginez ce scénario. Vous avez suivi votre plan à la lettre. Une configuration solide, une entrée précise, une gestion des risques impeccable. Pourtant, le marché décide d'aller contre vous. Votre stop loss est touché, et vous encaissez une perte de 150 euros. Rien d'énorme. Cela devrait être un non-événement. Mais quelque chose se déclenche en vous."))
    s.append(grb(["<b>NADIA — DU RECORD AU GOUFFRE</b>",
        "Nadia trade des actions depuis deux ans. Son compte avait atteint les 8 500 euros, un record dont elle était très fière. Un matin, après une nuit agitée, elle entre dans un trade un peu tôt sur un titre technologique.",
        "Le cours chute de 1,5%. Au lieu d'honorer son stop, elle le déplace mentalement. Une petite déviation 'juste pour voir si ça rebondit'. Le prix continue de descendre. Au lieu d'une perte de 170 euros, elle voit 350 euros de perte. La colère monte.",
        "Dans cet état de fureur contenue, la rationalité disparaît complètement. Elle a repéré un autre titre — une 'opportunité' qui semblait crier son nom. La configuration était douteuse, le volume faible. Elle le savait. Mais l'urgence de récupérer ses 350 euros était trop forte. Elle a doublé sa taille de position.",
        "Vingt minutes plus tard, son compte était en baisse de 1 100 euros pour la journée. Les 8 500 euros avaient fondu à 7 400 euros en moins de deux heures. Ce n'était plus une question de stratégie. C'était une spirale émotionnelle destructrice et auto-infligée.",
    ]))
    s.append(H("L'Aversion aux Pertes en Action"))
    s.append(P("C'est là que l'aversion aux pertes prend le dessus. Des études montrent que la douleur de perdre 100 euros est psychologiquement deux fois plus intense que le plaisir d'en gagner 100. Votre cerveau ne veut pas accepter cette perte. Il la perçoit comme une menace directe, une attaque personnelle. Une atteinte à votre identité de trader compétent."))
    s.append(P("Le revenge trading se nourrit de cette spirale vicieuse. Chaque perte due à un trade de vengeance renforce l'émotion négative. La frustration se mue en désespoir. Le doute de soi s'installe profondément, tel un poison. Et le cycle continue, car la seule solution que votre cerveau émotionnel perçoit est de trader encore plus. De prendre encore plus de risques."))
    s.append(grb(["<b>KHALIL — LE REVENGE TRADING DÉGUISÉ</b>",
        "Khalil, un day trader expérimenté, avait une stratégie rigoureuse pour les actions américaines. Un matin, deux de ses setups habituels n'ont pas fonctionné. Il était frustré, mais pas en colère, du moins en apparence.",
        "Il s'est dit : 'Ok, les actions ne sont pas claires. Je vais juste jeter un œil aux cryptos.' Son plan n'incluait absolument pas les cryptos ce jour-là. Il n'avait pas d'analyse claire, juste cette envie irrépressible de 'trouver' quelque chose.",
        "Il a pris une position démesurée sur Ethereum. Sans stop loss clair, sans vraie analyse. En 45 minutes, il avait perdu 4 800 euros. Ce n'était pas une 'meilleure opportunité'. C'était du revenge trading pur et simple, déguisé en flexibilité.",
    ]))
    s.append(H("Comment les Pros Traitent les Pertes"))
    s.append(P("Les traders professionnels abordent les pertes radicalement différemment. Pour eux, une perte fait partie du coût de faire des affaires. Ils la traitent comme une donnée statistique, pas comme une attaque personnelle. Si leur stop est touché, ils acceptent la perte, ferment la position, et se posent une question simple : 'Le plan a-t-il été exécuté correctement ?' Si oui, ils passent au trade suivant, sans émotion excessive."))

    # CH2
    s.append(ch('CHAPITRE 2','La Neurochimie de la Vengeance','Dopamine, cortisol et amygdale'))
    s.append(P("Quand vous subissez une perte, votre cerveau ne réagit pas logiquement. Il interprète cette perte comme une menace directe. Et face à une menace, notre cerveau reptilien se défend. Il cherche à restaurer l'équilibre, à prouver qu'il avait raison."))
    s.append(dq('"Votre amygdale, la partie de votre cerveau responsable des émotions primaires, prend le contrôle, reléguant le cortex préfrontal, siège de la logique, au second plan. C\'est le fameux détournement amygdalien."'))
    s.append(grb(["<b>SOFIA — LA CONFIGURATION IMAGINAIRE</b>",
        "Sofia avait un compte de 12 000 euros. Après une série de trois trades perdants consécutifs, elle avait perdu 800 euros. Un montant gérable. Mais son cerveau hurlait : 'Tu n'es pas stupide ! Prouve-le !'",
        "Elle a vu une configuration qui n'existait que dans son esprit — une sorte de mirage de vengeance. Elle a pris un trade sur une paire exotique qu'elle ne suivait jamais. Elle a mis 2 000 euros sur la ligne, plus de 16% de son capital. En 45 minutes, elle avait perdu 1 700 euros de plus.",
        "Elle n'essayait pas de gagner de l'argent. Elle essayait de se prouver qu'elle n'était pas un perdant. Cette quête de 'justice immédiate' est le piège le plus mortel du trading.",
    ]))
    s.append(H("La Boucle de Dopamine"))
    s.append(P("Ce qui est fascinant, c'est que la dopamine est aussi libérée quand nous cherchons à réparer une erreur. L'acte même d'entrer un nouvel ordre pour 'récupérer', même si c'est irréfléchi, procure une sensation de contrôle, une illusion de progrès. C'est comme le joueur qui perd au casino et double sa mise pour 'se refaire'. Il ne cherche pas à gagner, il cherche la décharge de dopamine."))
    s.append(P("C'est une danse dangereuse. La décharge d'adrénaline et de cortisol après une perte vous met dans un état de stress aigu. Votre capacité de raisonnement critique est réduite. Votre vision se rétrécit. Votre cerveau est en mode survie. Et le trading de vengeance est la réponse primitive à ce stress."))
    s.append(sr([('2x','plus intense : la douleur de perdre 100€ vs le plaisir d\'en gagner 100€'),
                 ('30%','de réduction de la capacité décisionnelle sous cortisol après une perte'),
                 ('82%','des traders se disent \'obligés\' de reprendre un trade après une perte significative')]))
    s.append(H("L'Impuissance Apprise"))
    s.append(P("Cette impuissance apprise est un piège redoutable. Vous avez tellement de fois cédé à l'impulsion que vous commencez à croire que vous n'avez aucun contrôle sur vous-même. Que c'est 'juste votre personnalité'. Mais ce n'est pas le cas. C'est un schéma comportemental, appris et renforcé par des cycles de récompense-punition, qui peut être désappris et remplacé."))

    # CH3
    s.append(ch('CHAPITRE 3','L\'Acceptation Radicale','Le premier pilier : changer ta relation à la perte'))
    s.append(P("Le premier pilier est ce que j'appelle l'Acceptation Radicale de la Perte. Cela semble contre-intuitif, n'est-ce pas ? La plupart des coachs vous diront de 'ne jamais abandonner'. Mais dans le trading, parfois, la meilleure bataille est celle que vous ne menez pas. L'Acceptation Radicale de la Perte n'est pas de la résignation. C'est une stratégie active."))
    s.append(P("C'est comprendre que chaque perte fait partie intégrante de votre modèle économique de trader. C'est un coût d'acquisition de profit. Pensez-y comme à une entreprise. Une entreprise paie des fournisseurs, des salaires. Ce sont des coûts. Les pertes sont vos coûts d'opérations."))
    s.append(grb(["<b>DAVID — 'CE N'EST PAS UN ÉCHEC, C'EST UNE DONNÉE'</b>",
        "David, un trader que j'ai coaché, avait une règle très simple. Chaque fois qu'il prenait une perte, il répétait à voix haute : 'Ce n'est pas un échec, c'est une donnée.' Ce simple mantra a transformé sa façon de voir les choses.",
        "Avant cela, David perdait en moyenne 1 500 euros par mois à cause du trading de vengeance. Après avoir intégré cette acceptation radicale, ses pertes moyennes dues à la vengeance sont tombées à moins de 150 euros par mois en l'espace de quatre semaines. Une réduction de 90%.",
        "Ce n'est pas parce qu'il était devenu un meilleur analyste technique. C'est parce qu'il avait changé sa relation émotionnelle à la perte — passant d'un combat personnel à une observation neutre des faits.",
    ]))
    s.append(H("La Pause des 5 Minutes"))
    s.append(P("Comment intégrer cette acceptation radicale ? Cela commence par la reconnaissance. Reconnaissez que la douleur de la perte est réelle. Ne la niez pas. Mais ne la laissez pas non plus dicter vos actions. Un exercice puissant : la 'Pause des 5 Minutes'. Après chaque trade perdant, vous vous déconnectez de votre plateforme pendant 5 minutes. Pas de regard sur les graphiques, pas de vérification de l'actualité."))
    s.append(gb(["<b>LE SCRIPT D'ACCEPTATION</b>",
        "Pendant vos 5 minutes, récitez l'une de ces phrases :",
        "◆  'Cette perte est un paiement pour ma formation'",
        "◆  'Cette perte était dans mon plan de risque'",
        "◆  'J'ai suivi mon plan, le résultat est une donnée'",
        "◆  'Le marché n'est pas mon ennemi. C'est simplement le marché.'",
        "L'objectif : court-circuiter le déclencheur de vengeance avant qu'il ne prenne le contrôle.",
    ]))

    # CH4
    s.append(ch('CHAPITRE 4','Le Circuit Coupe-Feu','Les règles infranchissables qui te sauvent'))
    s.append(P("Un autre outil crucial est le 'Circuit Coupe-Feu'. C'est une règle concrète, infranchissable, que vous mettez en place AVANT même d'ouvrir votre plateforme. La plupart des traders établissent des stop-loss, mais peu ont un stop-loss émotionnel ou un stop-loss de session. C'est une erreur colossale."))
    s.append(grb(["<b>MATEO — DE 70% PERDU À 35 000€</b>",
        "Mateo m'a contacté après avoir brûlé 70% de son compte en trois jours. Il avait une stratégie solide, mais chaque fois qu'il subissait deux pertes consécutives, une rage aveugle s'emparait de lui. Il doublait la taille de ses positions, ignorait ses propres signaux.",
        "J'ai travaillé avec Mateo pour mettre en place ce système. Sa première règle : 'Maximum deux pertes consécutives, puis arrêt immédiat pour la journée'. La deuxième : 'Si je perds plus de 2% de mon capital total en une seule journée, arrêt immédiat'. La troisième : 'Si je me sens frustré après un trade, je ferme tout pendant au moins une heure.'",
        "Au début, Mateo a lutté. Son instinct de vengeance était puissant. La première semaine, il a fermé sa plateforme trois fois après deux pertes. Mais il a tenu bon. Résultat : son compte est passé de 3 500 euros à 8 000 euros en trois mois — non pas grâce à des trades géniaux, mais grâce à l'élimination de la destruction auto-infligée.",
    ]))
    s.append(H("Le Circuit Coupe-Feu Complet"))
    s.append(gb(["<b>VOTRE CIRCUIT COUPE-FEU EN 3 RÈGLES</b>",
        "◆  Stop-Loss de Trade : % maximum de risque par trade (ex. 1% du capital)",
        "◆  Stop-Loss de Session : max 2-3 pertes consécutives ou X% de perte journalière → fermer la plateforme",
        "◆  Stop-Loss Émotionnel : si frustration, colère ou ennui excessif → arrêt immédiat",
        "",
        "Ces règles doivent être établies QUAND VOUS ÊTES CALME. Jamais au milieu de la tempête.",
    ]))
    s.append(grb(["<b>INGRID — LA MARCHE QUI A TOUT CHANGÉ</b>",
        "Ingrid travaillait à domicile. Sa station de trading était dans son salon. Après chaque perte, elle restait là, fixant l'écran. Son mentor lui a dit : 'Si tu perds, lève-toi. Quitte la pièce. Fais le tour du pâté de maisons pendant 30 minutes.'",
        "Le premier jour, après une perte frustrante de 300 euros, elle s'est forcée à sortir. Le simple fait de sentir le vent sur son visage a fait une différence colossale. La rage s'est estompée. Elle a réalisé que le trade de vengeance qu'elle était sur le point de prendre n'était basé sur rien de solide.",
        "Au fil du temps, cette pause de 30 minutes est devenue sacrée. Ses pertes ont diminué de 25% les mois suivants. Des études neurologiques montrent qu'une brève exposition à la nature réduit l'activité cérébrale liée à la rumination.",
    ]))

    # CH5
    s.append(ch('CHAPITRE 5','Le Changement d\'Identité','Devenir un gestionnaire de risques'))
    s.append(P("Pour arrêter le trading de vengeance, vous ne devez pas seulement changer ce que vous faites, mais qui vous êtes en tant que trader. Ce changement d'identité n'est pas quelque chose que vous décrétez du jour au lendemain. C'est quelque chose que vous construisez par vos actions répétées."))
    s.append(grb(["<b>SERGIO — DU 'TRADER REBELLE' AU GESTIONNAIRE DE RISQUE</b>",
        "Sergio se voyait comme un 'trader rebelle', celui qui 'défiait le marché'. Ce type d'identité est un terreau fertile pour le trading de vengeance. Quand le marché le mettait à l'épreuve, sa 'rébellion' se transformait en entêtement destructeur.",
        "Nous avons travaillé ensemble pour redéfinir son identité. Sergio a commencé à se voir comme un 'gestionnaire de risques stratégique'. Ce n'est pas un simple changement de mots. C'est un changement de perception profonde. Un gestionnaire de risques sait que les pertes sont inévitables. Il ne les craint pas. Il les gère.",
        "Ce changement d'identité a transformé ses résultats. Il a stabilisé son compte, puis commencé à progresser de manière constante. Il n'était pas devenu un génie du trading du jour au lendemain. Il était devenu un trader discipliné.",
    ]))
    s.append(H("Reconstruire l'Identité par l'Action"))
    s.append(P("Chaque fois que vous respectez votre Circuit Coupe-Feu après une perte, vous renforcez cette nouvelle identité. Chaque fois que vous prenez votre 'Pause des 5 Minutes', vous renforcez cette nouvelle identité. Chaque fois que vous affirmez votre nouveau rôle, vous devenez la personne qui ne fait pas de trading de vengeance, la personne qui est en contrôle."))
    s.append(gb(["<b>EXERCICE — LE JOURNAL D'IDENTITÉ (30 JOURS)</b>",
        "À la fin de chaque journée, écrivez trois phrases :",
        "◆  'Aujourd'hui, j'ai agi comme un gestionnaire de risques en [action précise].'",
        "◆  'La perte de [montant] sur le trade [X] était une donnée, pas un échec.'",
        "◆  'Je suis en train de construire une fondation solide, en agissant avec discipline.'",
        "",
        "Répétez cet exercice pendant 30 jours sans faute. Vous serez étonné de voir à quel point votre perception de vous-même change.",
    ]))
    s.append(grb(["<b>BRIANA — LE NOUVEAU VOCABULAIRE</b>",
        "Briana a adopté ce principe à la lettre. À chaque fois qu'on lui demandait ce qu'elle faisait, elle ne disait plus 'je suis trader', mais 'je suis une gestionnaire de risques qui utilise le trading comme un véhicule pour la croissance financière.'",
        "Ce simple changement de vocabulaire externe a renforcé son identité interne. Elle a commencé à prendre des décisions non pas en fonction de ce qu'une trader impulsive ferait, mais de ce qu'une gestionnaire de risque disciplinée ferait. Elle a découvert que la liberté en trading ne vient pas de la capacité à faire des gains énormes, mais de la maîtrise de soi face aux pertes.",
    ]))

    # CONCLUSION
    s.append(ch('CONCLUSION','La Forteresse Mentale','5 piliers pour une liberté durable'))
    s.append(P("La vraie bataille n'est pas contre le marché. Elle est contre vous-même. Contre ces impulsions primitives qui vous poussent à l'auto-sabotage. C'est un combat que l'on gagne pas à pas, trade après trade, décision après décision. En comprenant les mécanismes sous-jacents, en reconnaissant les déclencheurs, vous commencez à reprendre le contrôle."))
    s.append(P("La prochaine fois que vous subirez une perte, observez la montée de l'émotion. La frustration, la colère, le désir ardent de 'se refaire'. Ne réagissez pas immédiatement. Prenez cette pause. Récitez votre mantra. Et rappelez-vous que vous n'êtes plus le trader qui se laisse dicter par ses émotions. Vous êtes celui qui choisit l'action alignée avec son plan et son identité."))
    s.append(grb(["<b>LES 5 PILIERS DE VOTRE FORTERESSE</b>",
        "✓  Pilier 1 — Reconnaissance : identifier vos déclencheurs précis avec honnêteté",
        "✓  Pilier 2 — Pause Intentionnelle : 15 minutes minimum après chaque perte",
        "✓  Pilier 3 — Pré-définition Rigoureuse : règles écrites AVANT d'ouvrir la plateforme",
        "✓  Pilier 4 — Redéfinition de la Perte : 'coût d'apprentissage', jamais 'échec personnel'",
        "✓  Pilier 5 — Journal Détaillé : documenter l'état émotionnel, pas seulement le P&L",
    ]))
    s.append(gb(["<b>MES ENGAGEMENTS FINAUX</b>",
        "◆  Je définis mon Circuit Coupe-Feu avant chaque session, pas pendant",
        "◆  Après chaque perte, je prends la Pause des 5 Minutes sans exception",
        "◆  Je récite mon Script d'Acceptation pour recadrer chaque perte",
        "◆  Je me vois comme un gestionnaire de risques, pas comme un chasseur de profits",
        "◆  Je documente mes émotions dans mon journal autant que mes trades",
    ]))
    s.append(dq('"Au bout de ce chemin, il n\'y a pas seulement des profits plus constants. Il y a une liberté. Une liberté de l\'angoisse, du stress, de l\'auto-sabotage. Une liberté de trader avec clarté, avec confiance, et avec une sérénité que la plupart des traders ne connaîtront jamais."'))
    s.append(Spacer(1,16))
    s+=[Paragraph('TRADING ZONE',st['br']),Paragraph('Collection Le Code du Trader Élite — Ebook 4/5',st['br2']),Paragraph('www.tradingzone.fr',st['br3'])]
    return s

def build():
    out='04_Revenge_Trading_TRADING_ZONE.pdf'
    frame=Frame(ML,MB,CW,PAGE_H-MT-MB,id='main')
    tpl=PageTemplate(id='main',frames=[frame],onPage=footer)
    doc=BaseDocTemplate(out,pagesize=A4,pageTemplates=[tpl],leftMargin=ML,rightMargin=MR,topMargin=MT,bottomMargin=MB)
    story=cover()+[PageBreak()]+cpright()+[PageBreak()]+toc()+[PageBreak()]+content()
    doc.build(story); print(f"✓ {out} généré")

if __name__=='__main__': build()
