kinas = 'kinas'
claim = int(input('kaç adet claim var:'))
toprak = claim*485
piston = claim*200
deniz_feneri = claim*305
print(toprak,'adet toprak')
print(piston,'adet piston')
print(deniz_feneri,'adet deniz feneri')
print('----------------------------')
bool = input('fiyat hesaplamak ister misiniz:(evet/hayir)')
if bool == 'evet':
    toprak_fiyati = int(input('toprakin güncel tane fiyatini giriniz:'))
    piston_fiyati = int(input('pistonun güncel tane fiyatini giriniz:'))
    deniz_feneri_fiyati = int(input('deniz fenerinin güncel tane fiyatini giriniz:'))
print('----------------------------')
print('toprağin toplam tutari',toprak_fiyati*toprak,kinas)
print('pistonun toplam tutari',piston_fiyati*piston,kinas)
print('deniz fenerinin toplam tutari',deniz_feneri_fiyati*deniz_feneri,kinas)
print('total olarak:',(toprak_fiyati*toprak+piston_fiyati*piston+deniz_feneri_fiyati*deniz_feneri),kinas)
