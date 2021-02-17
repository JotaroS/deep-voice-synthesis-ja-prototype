import MeCab
from pykakasi import kakasi
import jaconv

kakasi = kakasi()
kakasi.setMode('K', 'a')
me = MeCab.Tagger ()
conv = kakasi.getConverter()

def convert_romaji(txt):
  arrays = [i[1] if len(i[1]) > 0 else i[0] for i in [t.split("\t") for t in me.parse(txt).split("\n")] if len(i) > 2]
  return " ".join([jaconv.hira2kata(a) for a in arrays if a is not None]).replace("、", ",").replace("。", ".")


def japanese_alphabet(jpn_text):
    kana = convert_romaji(jpn_text)
    kana = conv.do(kana)
    return kana

print(japanese_alphabet("こんにちは、今日はいい天気です。"))