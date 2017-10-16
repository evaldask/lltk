# -*- coding: utf-8 -*-

"""
Sentence splitter splits given text into sentences
"""

import re


class SentenceSplitter(object):
    """
    Notes:
        Splits given text into sentences

    Attributes:
        __sentence_enders: regex for sentence splitting
    """

    __sentence_enders = None

    def __init__(self):
        self.__sentence_enders = re.compile(r"""
        # Split sentences on whitespace between them.
        (?:               # Group for two positive lookbehinds.
            (?<=[.!?])      # Either an end of sentence punct,
        | (?<=[.!?]['"])  # or end of sentence punct and quote.
        )                 # End group of two positive lookbehinds.
            (?<!  dr\.   )
            (?<!  a\.a\.   )
            (?<!  akt\.   )
            (?<!  al\.   )
            (?<!  angl\.   )
            (?<!  ang\.   )
            (?<!  apskr\.   )
            (?<!  apsk\.   )
            (?<!  aps\.   )
            (?<!  aps\./min\.   )
            (?<!  arch\.   )
            (?<!  ar\.   )
            (?<!  atkov\.   )
            (?<!  atk\.   )
            (?<!  aut\.   )
            (?<!  bal\.   )
            (?<!  baud\.   )
            (?<!  blk\.   )
            (?<!  blok\.   )
            (?<!  buv\.   )
            (?<!  cd\.   )
            (?<!  ch\.   )
            (?<!  cm\.   )
            (?<!  corp\.   )
            (?<!  dab\.   )
            (?<!  deš\.   )
            (?<!  diz\.   )
            (?<!  doc\.   )
            (?<!  dokt\.   )
            (?<!  dol\.   )
            (?<!  dr\.   )
            (?<!  dž\.   )
            (?<!  dvit\.   )
            (?<!  el\.   )
            (?<!  etc\.   )
            (?<!  feat\.   )
            (?<!  gen\.   )
            (?<!  gim\.   )
            (?<!  gr\.   )
            (?<!  gv\.   )
            (?<!  gyv\.   )
            (?<!  habil\.   )
            (?<!  išprov\.   )
            (?<!  išpr\.   )
            (?<!  isp\.   )
            (?<!  jr\.   )
            (?<!  kab\.   )
            (?<!  kam\.   )
            (?<!  kap\.   )
            (?<!  ketv\.   )
            (?<!  kg\.   )
            (?<!  klaid\.   )
            (?<!  klas\.   )
            (?<!  kld\.   )
            (?<!  kl\.   )
            (?<!  km\.   )
            (?<!  km/val\.   )
            (?<!  komp\.   )
            (?<!  kt\.   )
            (?<!  kub\.   )
            (?<!  kun\.   )
            (?<!  kv\.   )
            (?<!  liet\.   )
            (?<!  lot\.   )
            (?<!  lsp\.   )
            (?<!  ltn\.   )
            (?<!  Lt\.   )
            (?<!  Lt/kub\.   )
            (?<!  maks\.   )
            (?<!  med\.   )
            (?<!  mėn\.   )
            (?<!  met\.   )
            (?<!  min\.   )
            (?<!  mln\.   )
            (?<!  mlrd\.   )
            (?<!  mm\.   )
            (?<!  mob\.   )
            (?<!  mong\.   )
            (?<!  mr\.   )
            (?<!  mrs\.   )
            (?<!  m/sek\.   )
            (?<!  naud\.   )
            (?<!  no\.   )
            (?<!  npr\.   )
            (?<!  nr\.   )
            (?<!  nuotr\.   )
            (?<!  op\.   )
            (?<!  pab\.   )
            (?<!  pan\.   )
            (?<!  past\.   )
            (?<!  pav\.   )
            (?<!  perdav\.   )
            (?<!  perd\.   )
            (?<!  pers\.   )
            (?<!  per\.   )
            (?<!  pil\.   )
            (?<!  plg\.   )
            (?<!  pl\.   )
            (?<!  por\.   )
            (?<!  praž\.   )
            (?<!  proc\.   )
            (?<!  prof\.   )
            (?<!  prom\.   )
            (?<!  pr\.   )
            (?<!  p\.s\.   )
            (?<!  pusm\.   )
            (?<!  pvz\.   )
            (?<!  raj\.   )
            (?<!  red\.   )
            (?<!  rez\.   )
            (?<!  rež\.   )
            (?<!  rus\.   )
            (?<!  saviv\.   )
            (?<!  sav\.   )
            (?<!  sek\.   )
            (?<!  sen\.   )
            (?<!  sh\.   )
            (?<!  skg\.   )
            (?<!  spec\.   )
            (?<!  sportin\.   )
            (?<!  srd\.   )
            (?<!  str\.   )
            (?<!  \sst\.   )
            (?<!  švc\.   )
            (?<!  šv\.   )
            (?<!  tel\.   )
            (?<!  tikr\.   )
            (?<!  trit\.   )
            (?<!  tritaŠk\.   )
            (?<!  trln\.   )
            (?<!  tšk\.   )
            (?<!  t\.t\.   )
            (?<!  tūks\.   )
            (?<!  tūkst\.   )
            (?<!  t\.y\.   )
            (?<!  užs\.   )
            (?<!  val\.   )
            (?<!  vert\.   )
            (?<!  vid\.   )
            (?<!  vnt\.   )
            (?<!  vok\.   )
            (?<!  vyr\.   )
            (?<!  žr\.   )
        \s+               # Split on whitespace between sentences.
        """, re.IGNORECASE | re.VERBOSE)

    def split(self, text):
        """
        Notes:
            Splits given text into sentences
        Args:
            text: string element that contain sentences

        Returns:
            results: array of sentences from splitted text
        """

        sentence_list = self.__sentence_enders.split(text)

        results = []
        is_quote = False
        add_next = False
        for sentence in sentence_list:
            if is_quote or add_next:
                results[-1] += ' ' + sentence
                add_next = False
            else:
                results.append(sentence)

            words = sentence.split(' ')

            # uncomment for keeping quote in same sentence.
            # NOTE: does not work perfectly
            # contains = sentence.count('"') + sentence.count("'")
            # if contains % 2 == 1:
            #    is_quote = not is_quote

            if len(words[-1].replace(' ', '').replace('.', '')) == 1:
                add_next = True

        return results
