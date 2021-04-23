"""
    Localisation Cameroon
    By Yameni Bakam Gleen Karel
    Last edited: 23.04.2021
"""

import numpy as np


def dataset():
    regions = ['Extrême-Nord', 'Nord', 'Adamaoua', 'Centre', 'Est', 'Littoral', 'Ouest', 'Nord-Ouest', 'Sud-ouest',
               'Sud']
    divisions = {
        'Extrême-Nord': ['Diamaré', 'Logone-et-Chari', 'Mayo-Danay', 'Mayo-Kani', 'Mayo-Sava', 'Mayo-Tsanaga'],
        'Nord': ['Bénoué', 'Faro', 'Mayo-Louti', 'Mayo-Rey'],
        'Adamaoua': ['Djérem', 'Faro-et-Déo', 'Mayo-Banyo', 'Mbéré', 'Vina'],
        'Centre': ['Haute-Sanaga', 'Lekié', 'Mbam-et-Inoubou', 'Mbam-et-Kim', 'Méfou-et-Afamba', 'Méfou-et-Akono',
                   'Mfoundi', 'Nyong-et-Kellé', 'Nyong-et-Mfoumou', 'Nyong-et-So’o'],
        'Est': ['Boumba-et-Ngoko', 'Haut-Nyong', 'Kadey', 'Lom-et-Djérem'],
        'Littoral': ['Moungo', 'Nkam', 'Sanaga-Maritime', 'Wouri'],
        'Ouest': ['Bamboutos', 'Haut-Nkam', 'Hauts-Plateaux', 'Koung-Khi', 'Menoua', 'Mifi', 'Ndé', 'Noun'],
        'Nord-Ouest': ['Boyo', 'Bui', 'Donga-Mantung', 'Menchum', 'Mezam', 'Momo', 'Ngo-Ketunjia'],
        'Sud-ouest': ['Fako', 'Koupé-Manengouba', 'Lebialem', 'Manyu', 'Meme', 'Ndian'],
        'Sud': ['Dja-et-Lobo', 'Mvila', 'Océan', 'Vallée-du-Ntem']
    }
    sub_divisions = {
        #Extreme Nord 1
        'Diamaré': ['Bogo', 'Dargala', 'Gazawa', 'Maroua Ier', 'Maroua IIe', 'Maroua IIIe', 'Meri', 'Ndoukoula',
                    'Petté'],
        'Logone-et-Chari': ['Blangoua', 'Darak', 'Fotokol', 'Goulfey', 'Hile-Alifa', 'Kousséri', 'Logone-Birni',
                            'Makary', 'Waza', 'Zina'],
        'Mayo-Danay': ['Datcheka', 'Gobo', 'Guémé', 'Guéré', 'Kai-Kai', 'Kalfou', 'Kar-Hay', 'Maga', 'Tchatibali',
                       'Wina', 'Yagoua'],
        'Mayo-Kani': ['Dziguilao', 'Guidiguis', 'Kaélé', 'Mindif', 'Moulvoudaye', 'Moutourwa', 'Touloum'],
        'Mayo-Sava': ['Kolofata', 'Mora', 'Tokombéré'],
        'Mayo-Tsanaga': ['Bourrha', 'Hina', 'Koza', 'Mogodé', 'Mokolo', 'Mozogo', 'Soulédé-Roua'],

        #Nord 2
        'Bénoué': ['Barndaké', 'Bashéo', 'Bibemi', 'Dembo', 'Garoua Ier', 'Garoua IIe', 'Garoua IIIe', 'Gashiga',
                   'Lagdo', 'Ngong', 'Pitoa', 'Touroua'],
        'Faro': ['Beka', 'Poli'],
        'Mayo-Louti': ['Figuil', 'Guider', 'Mayo-Oulo'],
        'Mayo-Rey': ['Madingring', 'Rey-Bouba', 'Tcholliré', 'Touboro'],

        #Adamaoua 3
        'Djérem': ['Ngaoundal', 'Tibati'],
        'Faro-et-Déo': ['Galim-Tignère', 'Kontcha', 'Mayo-Baléo', 'Tignère'],
        'Mayo-Banyo': ['Bankim', 'Banyo', 'Mayo-Darlé'],
        'Mbéré': ['Dir', 'Djohong', 'Meiganga', 'Ngaoui'],
        'Vina': ['Belel', 'Mbe', 'Nganha', 'Ngaoundéré Ier', 'Ngaoundéré IIe', 'Ngaoundéré IIIe', 'Nyambaka', 'Martap',
                 'Ngan-Ha'],

        #Centre 4
        'Haute-Sanaga': ['Bibey', 'Lembe-Yezoum', 'Mbandjock', 'Minta', 'Nanga-Eboko', 'Nkoteng', 'Nsem'],
        'Lekié': ['Batchenga','Ebebda','Elig-Mfomo','Evodoula','Lobo','Monatélé','Obala','Okola','Sa’a'],
        'Mbam-et-Inoubou': ['Bafia', 'Bokito', 'Deuk', 'Kiiki', 'Kon-Yambetta', 'Makénéné', 'Ndikiniméki', 'Nitoukou',
                            'Ombessa'],
        'Mbam-et-Kim': ['Mbangassina', 'Ngambè-Tikar', 'Ngoro', 'Ntui', 'Yoko'],
        'Méfou-et-Afamba': ['Afanloum', 'Awaé', 'Edzendouan', 'Esse', 'Mfou', 'Nkolafamba', 'Olanguina', 'Soa'],
        'Méfou-et-Akono': ['Akono', 'Bikok', 'Mbankomo', 'Ngoumou'],
        'Mfoundi': ['Yaoundé 1 (Nlongkak)', 'Yaoundé 2 (Tsinga)', 'Yaoundé (Efoulan)',
                    'Yaoundé 4 (Kondengui - Lycée de minkan)', 'Yaoundé 5 (nkolmesseng)',
                    'Yaoundé 6 (Biyem-Assi)', 'Yaoundé 7 (Nkolbisson)'],
        'Nyong-et-Kellé': ['Biyouha', 'Bondjock', 'Bot-Makak', 'Dibang', 'Éséka', 'Makak', 'Matomb', 'Messondo',
                           'Ngog-Mapubi','Ngui-Bassal'],
        'Nyong-et-Mfoumou': ['Akonolinga', 'Ayos', 'Endom', 'Kobdombo', 'Mengang'],
        'Nyong-et-So’o': ['Akoeman', 'Dzeng', 'Mbalmayo', 'Mengueme', 'Ngomedzap', 'Nkolmetet'],

        #Est 5
        'Boumba-et-Ngoko': ['Gari-Gombo', 'Moloundou', 'Salapoumbé', 'Yokadouma'],
        'Haut-Nyong': ['Abong-Mbang' ,'Angossas' ,'Atok' ,'Dimako' ,'Doumaintang' ,'Doumé' ,'Lomié' ,'Mboma' ,
                       'Messamena' ,'Messok' ,'Mindourou' ,'Ngoyla' ,'Nguelemendouka', 'Somalomo'],
        'Kadey': ['Batouri', 'Kentzou', 'Kette', 'Mbang', 'Ndelele', 'Nguelebok', 'Ouli'],
        'Lom-et-Djérem': ['Bélabo', 'Bertoua Ier', 'Bertoua IIe', 'Bétaré-Oya', 'Diang', 'Garoua-Boulaï', 'Mandjou',
                          'Ngoura'],

        #Littoral 6
        'Moungo': ['Baré-Bakem', 'Bonaléa (Souza)', 'Dibombari', 'Loum', 'Manjo', 'Mbanga', 'Melong', 'Mombo',
                   'Njombe-Penja (Penja)', 'Nkongsamba 1er (Nkongsamba)', 'Nkongsamba 2e (Ekangté Mbeng)',
                   'Nkongsamba 3e (Nkongsamba)','Eboné'],
        'Nkam': ['Nkondjock', 'Nord Makombé', 'Yabassi', 'Yingui'],
        'Sanaga-Maritime': ['Dibamba', 'Dizangué', 'Édéa Ier (Pongo)', 'Édéa IIe (Ékité)', 'Massock-Songloulou',
                            'Mouanko', 'Ndom', 'Ngambe', 'Ngwei', 'Nyanon', 'Pouma'],
        'Wouri': ['Douala I (Bonanjo)', 'Douala II (New Bell)', 'Douala III (Logbaba)', 'Douala IV (Bonassama)',
                  'Douala V (Kotto)', 'Douala VI (Manoka)'],

        #Ouest 7
        'Bamboutos': ['Babadjou', 'Batcham', 'Galim', 'Mbouda'],
        'Haut-Nkam': ['Bafang', 'Bakou', 'Bana', 'Bandja', 'Banka', 'Banwa', 'Kékem'],
        'Hauts-Plateaux': ['Baham', 'Bamendjou', 'Bangou', 'Batié'],
        'Koung-Khi': ['Bayangam', 'Demdeng', 'Petté-Bandjoun'],
        'Menoua': ['Dschang', 'Fokoué', 'Fongo-Tongo', 'Nkong-Zem', 'Penka-Michel', 'Santchou'],
        'Mifi': ['Bafoussam Ier', 'Bafoussam IIe', 'Bafoussam IIIe'],
        'Ndé': ['Bangangté', 'Bassamba', 'Bazou', 'Tonga'],
        'Noun': ['Bangourain', 'Foumban', 'Foumbot', 'Kouoptamo', 'Koutaba', 'Magba', 'Malentouen', 'Massangam',
                 'Njimom'],

        #Nord-Ouest 8
        'Boyo': ['Belo', 'Fonfuka', 'Fundong', 'Njinikom'],
        'Bui': ['Elak-Oku', 'Jakiri', 'Kumbo', 'Mbiame', 'Nkum', 'Nkor'],
        'Donga-Mantung': ['Ako', 'Misaje', 'Ndu', 'Nkambé', 'Nwa'],
        'Menchum': ['Benakuma', 'Furu-Awa', 'Wum', 'Zhoa'],
        'Mezam': ['Bafut', 'Bali', 'Bamenda Ier', 'Bamenda IIe', 'Bamenda IIIe' ,'Santa', 'Tubah'],
        'Momo': ['Andek', 'Batibo', 'Mbengwi', 'Njikwa', 'Widikum-Boffe'],
        'Ngo-Ketunjia': ['Babessi', 'Balikumbat', 'Ndop'],

        #Sud-Ouest 9
        'Fako': ['Buéa', 'Limbé Ier', 'Limbé IIe', 'Limbé IIIe', 'Muyuka', 'Tiko', 'West Coast'],
        'Koupé-Manengouba': ['Bangem', 'Nguti', 'Tombel'],
        'Lebialem': ['Alou', 'Menji', 'Wabane'],
        'Manyu': ['Akwaya', 'Eyumodjock', 'Mamfé', 'Tinto'],
        'Meme': ['Konye', 'Kumba Ier', 'Kumba IIe', 'Kumba IIIe', 'Mbonge'],
        'Ndian': ['Bamusso', 'Dikome-Balue', 'Ekondo-Titi', 'Idabato', 'Isanguele', 'Kombo-Abedimo', 'Kombo-Idinti',
                  'Mundemba', 'Toko'],

        #Sud 10
        'Dja-et-Lobo': ['Bengbis', 'Djoum', 'Meyomessala', 'Meyomessi', 'Mintom', 'Oveng', 'Sangmélima', 'Zoétélé'],
        'Mvila': ['Biwong-Bane', 'Biwong-Bulu', 'Ebolowa Ier', 'Ebolowa IIe', 'Efoulan', 'Mengong', 'Mvangan',
                  'Ngoulemakong'],
        'Océan': ['Akom II', 'Bipindi', 'Campo', 'Kribi Ier', 'Kribi IIe', 'Lokoundjé', 'Lolodorf', 'Mvengue', 'Niete'],
        'Vallée-du-Ntem': ['Ambam', 'Kyé-Ossi', 'Ma’an', 'Olamze']
    }
    return regions, divisions, sub_divisions


def search(regions, divisions, sub_divisions, name):

    for region in regions:
        if region.lower() == name.lower():
            return True, False, False, None, region

    for region in divisions:
        for division in divisions[region]:
            if division.lower() == name.lower():
                return  False, True, False, region, division

    for division in sub_divisions:
        for sub_division in sub_divisions[division]:
            if sub_division.lower() == name.lower():
                return False, False, True, division, sub_division

    return False, False, False, None, name

def word_recognitrion(regions, divisions, sub_divisions, name):
    possible = []

    for region in regions:
        if int(len(name)*(0.65)) < len(region) and len(region) - len(name) > -3:
            variable = algorithm(region, name)
            if variable:
                possible.append(variable)

    for region in divisions:
        for division in divisions[region]:
            if int(len(name) * (0.65)) < len(division) and len(division) - len(name) > -3:
                variable = algorithm(division, name)
                if variable:
                    possible.append(variable)

    for division in sub_divisions:
        for sub_division in sub_divisions[division]:
            if len(sub_division) - len(name) > -3:
                variable = algorithm(sub_division, name)
                if variable:
                    possible.append(variable)

    return possible


def algorithm(word, name):

    j = -1
    if len(word) >= len(name):
        #print(name, word)
        for letter in name:
            j += 1
            order = 0
            i = -1
            if j > len(name):
                break
            for element in word:
                i += 1
                if letter.lower() == element.lower():
                    order = 1
                    for x in range(j + 1, len(name)):
                        #print(i, x, j)
                        if i + x-j == len(word):
                            break
                        if name[x].lower() == word[i + x-j].lower():
                            #print(x, i+x-j)
                            order += 1

            if int(len(name) * (0.70)) < order:
                return word


    if word[0].lower() != name[0].lower():
        return []

    evalution = 0
    for letter in name:
        for element in word:
            if letter.lower() == element.lower():
                evalution += 1
                break
    if int(len(word)*(0.70)) < evalution:
        return word

    return []


def main():

    regions, divisions, sub_divisions = dataset()

    status = True

    while status:

        name = input("Enter a Region/Division/Sub-Division: ")
        if name =='0':
            status = False

        reg, div, sub, nom, name= search(regions, divisions, sub_divisions, name)

        if reg == div == sub:
            print('Name not define')
            possible = word_recognitrion(regions, divisions, sub_divisions, name)
            if possible:
                print('did you mean:')
                for element in possible:
                    print(element)

        if reg:
            print('Region' + ':' + name)
            print('Divisions in ' + name + ' (' + str(len(divisions[name])) + ')' + ':')
            for division in divisions[name]:
                print('-' + division)
            print('\n\n')


        elif div:
            print('Division' + ':' + name)
            print('Region' + ':' + nom)
            print('Sub-Divisions in ' + name + ' (' + str(len(sub_divisions[name])) + ')' + ':')
            for sub_division in sub_divisions[name]:
                print('-' + sub_division)
            print('\n\n')


        elif sub:
            print('Sub-Division' + ':' + name)
            print('Division' + ':' + nom)
            _, _, _, n, name = search(regions, divisions, sub_divisions, nom)
            print('Region' + ':' + n)
            print('\n\n')
    """
    sum = 0
    for division in divisions:
        sum = sum + len(divisions[division])
        print(division)
        print(sum)
    sum = 0
    print('\n\n')
    for sub_division in sub_divisions:
        sum = sum + len(sub_divisions[sub_division])
        print(sub_division)
        print(sum)
    """

main()
