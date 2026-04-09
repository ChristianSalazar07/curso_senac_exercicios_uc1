import calculos as calc
import caes
print(calc.media_ponderada([3,4,5],[5,2,8]))
meuCao = caes.Poodle(30, "Branco")
meuOutroCao = caes.Cao(20, "Shitzu")
meuGolden = caes.Golden(30, "Dourado, sla")
print(meuCao)
print(meuOutroCao)
print(meuGolden)
meuOutroCao.latir()
meuGolden.latir()
meuGolden.sentar()
meuCao.latir()
meuCao.sentar()