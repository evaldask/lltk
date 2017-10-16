# -*- coding: utf-8 -*-

"""
Word stemmer that returns token for a given word
"""


class Stemmer(object):
    """
    Notes:
        Class to stem lithuanian words
        (more info about stemming: https://en.wikipedia.org/wiki/Stemming)
        Based on: https://github.com/tokenmill/snowball conservative.sbl

    Attributes:
        __step1_items: frozenset for items to remove in step1
        __step1_min: minimum key length in __step1_items frozenset
        __step1_max: maximum key length in __step1_items frozenset

        __step2_items: frozenset for items to remove in step2
        __step2_min: minimum key length in __step2_items frozenset
        __step2_max: maximum key length in __step2_items frozenset

    """

    def __init__(self):
        step1_items = [
            u'as',
            u'ias',
            u'is',
            u'ys',
            u'io',
            u'o',
            u'ui',
            u'iui',
            u'ą',
            u'ią',
            u'į',
            u'u',
            u'iu',
            u'e',
            u'yje',
            u'y',
            u'au',
            u'an',
            u'iai',
            u'ai',
            u'i',
            u'ių',
            u'ų',
            u'ių',
            u'ams',
            u'am',
            u'iams',
            u'iam',
            u'us',
            u'ius',
            u'ais',
            u'iais',
            u'uose',
            u'iuose',
            u'uos',
            u'iuos',
            u'uosna',
            u'iuosna',
            u'ysna',
            u'asis',
            u'aisi',
            u'osi',
            u'ųsi',
            u'uisi',
            u'ąsi',
            u'usi',
            u'usios',
            u'esi',
            u'uo',
            u'a',
            u'ia',
            u'os',
            u'ios',
            u'oj',
            u'oje',
            u'ioje',
            u'osna',
            u'iosna',
            u'om',
            u'oms',
            u'ioms',
            u'omis',
            u'iomis',
            u'ose',
            u'iose',
            u'on',
            u'ion',
            u'ė',
            u'ės',
            u'ei',
            u'ę',
            u'ėj',
            u'ėje',
            u'ėms',
            u'es',
            u'ėmis',
            u'ėse',
            u'ėsna',
            u'ėn',
            u'aus',
            u'iaus',
            u'umi',
            u'iumi',
            u'uje',
            u'iuje',
            u'iau',
            u'ūs',
            u'ums',
            u'umis',
            u'un',
            u'iun',
            u'ies',
            u'ens',
            u'enio',
            u'ers',
            u'eniui',
            u'eriai',
            u'enį',
            u'erį',
            u'imi',
            u'eniu',
            u'erimi',
            u'eria',
            u'enyje',
            u'eryje',
            u'ie',
            u'enie',
            u'erie',
            u'enys',
            u'erys',
            u'erų',
            u'ims',
            u'enims',
            u'erims',
            u'enis',
            u'imis',
            u'enimis',
            u'yse',
            u'enyse',
            u'eryse',
            u'iem',
            u'iems',
            u'ame',
            u'iame',
            u'uosi',
            u'iuosi',
            u'iesi',
            u'asi',
            u'iasi',
            u'amės',
            u'iamės',
            u'at',
            u'ate',
            u'iat',
            u'iate',
            u'atės',
            u'iatės',
            u'isi',
            u'im',
            u'imės',
            u'it',
            u'ite',
            u'ome',
            u'omės',
            u'ot',
            u'ote',
            u'otės',
            u'ėjo',
            u'ėjosi',
            u'otės',
            u'eisi',
            u'ėsi',
            u'ėm',
            u'ėme',
            u'ėmės',
            u'ėt',
            u'ėte',
            u'ėtės',
            u'ausi',
            u'omės',
            u'siu',
            u'siuosi',
            u'si',
            u'siesi',
            u's',
            u'ysis',
            u'sim',
            u'sime',
            u'sit',
            u'site',
            u'čiau',
            u'čiausi',
            u'tum',
            u'tumei',
            u'tumeis',
            u'tumeisi',
            u'tųsi',
            u'tumėm',
            u'tumėme',
            u'tumėmės',
            u'tute',
            u'tumėt',
            u'tumėte',
            u'tumėtės',
            u'k',
            u'ki',
            u'kimės',
            u'uoti',
            u'iuoti',
            u'auti',
            u'iauti',
            u'oti',
            u'ioti',
            u'ėti',
            u'yti',
            u'inti',
            u'inėti',
            u'enti',
            u'telėti',
            u'terėti',
            u'ti',
            u'ąs',
            u'iąs',
            u'įs',
            u'tųs',
            u'simės',
            u'sitės',
            u'kite'
        ]

        self.__step1_items = frozenset(step1_items)
        self.__step1_min = min(len(s) for s in step1_items)
        self.__step1_max = max(len(s) for s in step1_items)

        step2_items = [
            u'ing',
            u'išk',
            u'ėt',
            u'ot',
            u'uot',
            u'iuot',
            u'yt',
            u'iuk',
            u'iul',
            u'el',
            u'ėl',
            u'yl',
            u'učiuk',
            u'uliuk',
            u'utėait',
            u'ok',
            u'iok',
            u'sv',
            u'šv',
            u'zgan',
            u'op',
            u'iop',
            u'ain',
            u'ykšt',
            u'ykšč',
            u'esn',
            u'aus',
            u'iaus',
            u'ias',
            u'oj',
            u'ioj',
            u'aj',
            u'iaj',
            u'ąj',
            u'iąj',
            u'uoj',
            u'iuoj',
            u'iej',
            u'ųj',
            u'iųj',
            u'ies',
            u'uos',
            u'iuos',
            u'ais',
            u'iais',
            u'os',
            u'ios',
            u'ąs',
            u'iąs',
            u'dav',
            u'ant',
            u'iant',
            u'int',
            u'ėj',
            u'ę',
            u'ėję',
            u'ęs',
            u'siant',
            u'dam',
            u'auj',
            u'jam',
            u'iau',
            u'am'
        ]

        self.__step2_items = frozenset(step2_items)

        self.__step2_min = min(len(s) for s in step2_items)
        self.__step2_max = max(len(s) for s in step2_items)

    def __step1(self, word):
        """
        Notes:
            Removes endings in words
        Args:
            word: string element that contain single word

        Returns:
            word: word without ending or same word that was passed
        """
        for i in range(self.__step1_max, self.__step1_min, -1):
            if word[-i:] in self.__step1_items:
                return word[:-i]

        return word

    def __step2(self, word):
        """
        Notes:
            Removes suffixes in words
        Args:
            word: string element that contain single word

        Returns:
            word: word without suffix or same word that was passed
        """

        for i in range(self.__step2_max, self.__step2_min, -1):
            if word[-i:] in self.__step2_items:
                return word[:-i]

        return word

    def __replace(self, word, items):
        """
        Notes:
            If word contains element that equal tuple[0] in items array
            that element is replaced with tuple[1] value
        Args:
            word: string element thatis a word
            items: tuple array that contains in tuple[0] position element
            that needs to be replace, in tuple[1] position element to
            replace with.

        Returns:
            word: replaced or same word that was passed
        """

        for item in items:
            word = word.replace(item[0], item[1])

        return word

    def __fix_conflicts(self, word):
        """
        Notes:
            Fixes word endings
        Args:
            word: string element that contain single word

        Returns:
            word: word without suffix or same word that was passed
        """

        items = [
            (u'aite', u'aitė'),
            (u'aitės', u'aitė'),
            (u'uotės', u'uotė'),
            (u'uote', u'uotė'),
            (u'ėjime', u'ėjimas'),
            (u'esiu', u'esys'),
            (u'asius', u'asys'),
            (u'avime', u'avimas'),
            (u'ojime', u'ojimas'),
            (u'okatės', u'okatė'),
            (u'okate', u'okatė')
        ]
        return self.__replace(word, items)

    def __fix_chdz(self, word):
        """
        Notes:
            Fixed č / dž problem in word
        Args:
            word: string element that contain single word

        Returns:
            word: word without suffix or same word that was passed
        """

        items = [
            (u'č', u't'),
            (u'dž', u'd')
        ]
        return self.__replace(word, items)

    def __fix_gd(self, word):
        """
        Notes:
            Fixed gd problem in word
        Args:
            word: string element that contain single word

        Returns:
            word: word without suffix or same word that was passed
        """

        items = [
            (u'gd', u'g')
        ]
        return self.__replace(word, items)

    def stem(self, word):
        """
        Notes:
            Stems given word
        Args:
            word: string element that contain single word

        Returns:
            result: stemmed word. Result will always be shorter word or same
            word that was passed
        """

        result = self.__fix_conflicts(word)
        result = self.__step1(result)
        result = self.__fix_chdz(result)
        result = self.__step2(result)
        result = self.__fix_chdz(result)
        result = self.__fix_gd(result)
        return result
