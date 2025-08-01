def anagram_mi(kelime1, kelime2):
    return sorted(kelime1) == sorted(kelime2)

# Örnek kullanım
print(anagram_mi("listen", "silent"))  # True
print(anagram_mi("hello", "world"))    # False



from collections import Counter

def anagram_mi(kelime1, kelime2):
    return Counter(kelime1) == Counter(kelime2)

# Örnek kullanım
print(anagram_mi("listen", "silent"))  # True
print(anagram_mi("hello", "world"))    # False












def harf_sayisi(kelime):
    harfler = {}
    for harf in kelime:
        harfler[harf] = harfler.get(harf, 0) + 1
    return harfler

def anagram_mi(kelime1, kelime2):
    return harf_sayisi(kelime1) == harf_sayisi(kelime2)

# Örnek kullanım
print(anagram_mi("listen", "silent"))  # True
print(anagram_mi("python", "java"))    # False





anagram_mi = lambda k1, k2: sorted(k1) == sorted(k2)

print(anagram_mi("earth", "heart"))  # True
print(anagram_mi("hello", "python")) # False





kelime1 = "listen"
kelime2 = "silent"

anagram = sorted(kelime1) == sorted(kelime2)

print(anagram)  # Çıktı: True


kelime1 = "listen"
kelime2 = "silent"

harfler1 = {}
harfler2 = {}

for harf in kelime1:
    harfler1[harf] = harfler1.get(harf, 0) + 1

for harf in kelime2:
    harfler2[harf] = harfler2.get(harf, 0) + 1

anagram = harfler1 == harfler2

print(anagram)  # Çıktı: True






















































































































































