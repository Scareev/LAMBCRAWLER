import time
import random

#ZERAR JOGO
main = True

#RNG 
chance = 0

#SHOP

item_quantity = [1, 3]
craft_quantity = [1, 2]

#RENDA INICIAL
dinheiro = 10000

#PICARETAS
permitirMinerar = True

picaretas = {
    "names":            ['Picareta de Ferro', 'Picareta de Ouro', 'Picareta de Diamante', 'Picareta de Void'],
    "prices":           [0, 50, 350, 1000],
    "limits":           [5],
    "durability":       [0, 35, 65, 250]
} 

#MINÉRIOS
ores = {
    "iron_ore":         0,
    "gold_ore":         0,
    "diamond_ore":      0,
    "void_ore":         0,
}

ores_value = {
    "iron_ore_value":         0,
    "gold_ore_value":         0,
    "diamond_ore_value":      0,
    "void_ore_value":         0,
}


#INVENTÁRIO
inventario = {
    "items":              [picaretas["names"][0], "Scrap", "Scrap"]
}

#LEVEL-UP
level = 1

#SISTEMA DE CAÇA
meuHP, meuHPTotal = 100, 100
meuDano = 0
critChance = 0
XP, XPTotal = 0, 10

#POOL DE INIMIGOS
#Para cada inimigo, é proporcional ao seu index, exemplo: todos os indexes 0 são atribuidos ao slime, indexes 1 ao zumbi, e assim vai.
mobs = {
    "monstBoolean":       True,
    "monstName":          ["Slime", "Zumbi", "Earth Golem"],
    "monstHP":            [50, 70, 120],
    "monstHPTotal":       [50, 70, 120],
    "monstATK":           [20, 25, 50],
    "monstLevel":         [0, 1, 2],
    "monstXPDropRate":    [[2, 5], [5, 10], [10, 20]],
    "monstCash":          [[25, 50], [50, 100], [100, 200]]
}

#DROPS
drops = {
    "itemName":           ["Geleia", "Carne Podre", "Rocha Mística"],
    "itemValue":          [50, 20, 250],
    "itemRarity":         [0, 0, 1]
}

#ITENS CRAFTAVEIS
craftables = ['Cosmetic', 'Elixir']


def minerar():
    global dinheiro, chance, permitirMinerar, picaretas, ores, ores_value
    if permitirMinerar == True:
        picaretas['durability'][0] += 1
        chance = random.randint(1, 100)
        ores_value['iron_ore_value'] = random.randint(2, 5)
        ores_value['gold_ore_value'] = random.randint(10, 30)
        ores_value['diamond_ore_value'] = random.randint(30, 50)
        ores_value['void_ore_value'] = random.randint(1000, 4000)
        time.sleep(0.1)
        print('Minerando.')
        time.sleep(0.1)
        print('Minerando..')
        time.sleep(0.1)
        print('Minerando...')
        time.sleep(0.1)
        print('')
        print('')
        if picaretas['durability'][0] < picaretas['limits'][0]:
            if chance >= 10 and chance <= 50:
                dinheiro += ores_value['iron_ore_value']
                print('')
                print('Você minerou ' + fastColorInsert('FERRO!', 'preto') + f' ele vale: {ores_value["iron_ore_value"]} moedas.')
                print('')
            elif chance >= 40 and chance <= 60:
                dinheiro += ores_value['gold_ore_value']
                print('')
                print('Você minerou ' + fastColorInsert('OURO!', 'amarelo') + f' ele vale: {ores_value["gold_ore_value"]} moedas.')
                print('')
            elif chance >= 70 and chance <= 90:
                dinheiro += ores_value['diamond_ore_value']
                print('')
                print('Você minerou ' + fastColorInsert('DIAMANTE!', 'ciano') + f' ele vale: {ores_value["diamond_ore_value"]} moedas.')
                print('')
            elif chance >= 91 and chance <= 100:
                dinheiro += ores_value['void_ore_value']
                print('')
                print('Você minerou ' + fastColorInsert('VOIDITA!', 'verde') + f' ele vale: {ores_value["void_ore_value"]} moedas.')
                print('')
            else:
                print('')
                print(fastColorInsert(f'Você não achou nada...', 'cinza'))
                print('')
            print(f'DURABILIDADE: {picaretas['durability'][0]} de {picaretas["limits"][0]}')
        else:
            print(f'DURABILIDADE: {picaretas['durability'][0]} de {picaretas["limits"][0]}')
            print('')
            print(fastColorInsert('Sua picareta quebrou! Compre outra picareta para continuar minerando.', 'vermelho'))
            print('')
            permitirMinerar = False
            inventario['items'].remove(inventario['items'][0])

def enemyPool(enemyPoolValue):
    global enemy, enemyHP, enemyATK, enemyHPTotal, enemyName, enemyLevel
    global mobs
    enemyName = mobs["monstName"][enemyPoolValue]
    enemy = mobs["monstBoolean"]
    enemyHP = mobs["monstHP"][enemyPoolValue]
    enemyATK = mobs["monstATK"][enemyPoolValue]
    enemyHPTotal = mobs["monstHPTotal"][enemyPoolValue]
    enemyLevel = mobs["monstLevel"][0]
    print('')
    print(fastColorInsert('BATALHA ENCONTRADA! ','vermelho') + f'{enemyName} LEVEL: {enemyLevel}')
    print('')
    combatSys(enemyPoolValue)

def caçar():
    global monstChance
    monstChance = random.randint(0,2)
    print('Procurando monstro.')
    time.sleep(0.2)
    print('Procurando monstro..')
    time.sleep(0.2)
    print('Procurando monstro...')
    time.sleep(0.2)
    enemyPool(monstChance)

def combatSys(enemyIndex):
    global dinheiro, level, critChance, main, XP
    global enemy, enemyHP, enemyATK, enemyHPTotal, enemyName, enemyLevel
    global meuHP, meuDano, meuHPTotal
    while enemyHP > 0:
        meuDano = random.randint(40, 50)
        danoInimigo = random.randint(0, enemyATK) # Variável para ser o dano do inimigo num range aleatório de 0 até seu dano MAX.
        atacar = input('Digite "A" para ATACAR: ').lower()
        if atacar == "a":
            enemyHP = enemyHP - meuDano
            meuHP = meuHP - (danoInimigo)
            print('-=-=-') 
            print('Você ataca o inimigo!')
            time.sleep(0.2)
            print('POW!')
            time.sleep(0.2)
            print('ARGH!!!')
            time.sleep(0.5)
            print('UGH!')
            print('')     
            print(f'Seu HP atual: {meuHP} / {meuHPTotal} <-- ' + fastColorInsert(danoInimigo, 'vermelho') + ' DANO RECEBIDO')
            print(f'HP do {enemyName}: {enemyHP} / {enemyHPTotal} <-- ' + fastColorInsert(meuDano, 'vermelho') + ' DANO DADO')
            print('-=-=-')
            if meuHP <= 0:
                main = False
                meuHP *= (-1)
                print('VOCÊ MORREU!')
                break
            if enemyHP <= 0:
                print('\033[92mVOCÊ VENCEU!\033[0m')
                dropSys(enemyIndex)
                XPSys(enemyIndex)
                levelUp()
                enemy = False
                enemyHPTotal = 0
                enemyHP = 0 
                enemyName = ''
                print('')
                break

def XPSys(enemyXPValue):
    global mobs
    global XP
    XPGanho = random.randint(mobs["monstXPDropRate"][enemyXPValue][0], mobs["monstXPDropRate"][enemyXPValue][1])
    XP += XPGanho
    print(f'Você ganhou: {XPGanho} de XP!')

def dropSys(enemyDrop):
    global inventario, dinheiro
    global drops, mobs
    dinheiroGanho = random.randint(mobs['monstCash'][enemyDrop][0], mobs['monstCash'][enemyDrop][1])
    dinheiro += dinheiroGanho
    inventario['items'].append(drops['itemName'][enemyDrop])
    print(f'Você ganhou: {drops['itemName'][enemyDrop]}!')
    print(f'Você ganhou: {dinheiroGanho} moedas!')

def inv():
    print('')
    print('')
    print('Seus itens:')
    print(inventario["items"])        
    print('')

def levelUp():   
    global meuHP, meuHPTotal, XP, XPTotal, level
    while XP >= XPTotal:
        level += 1
        meuHP += 160
        meuHPTotal = meuHP
        print('')
        print(fastColorInsert('VOCÊ SUBIU DE NÍVEL!', 'verde'))
        print(f'Seu HP Subiu!: {meuHP}')
        print('')
        XP -= XPTotal
        XPTotal = int(XPTotal * 1.5) # Aumenta o custo do próximo nível em 15%
        print(f'XP necessário para o próximo nível: {XPTotal}')

def shop():
    global dinheiro, main, inventario, picaretas
    print('')
    print(('-=-' * 5) + 'Loja do Seu Bananal!' + ('-=-' * 5))
    print(f'SEU DINHEIRO ATUAL: ', end='')
    print(fastColorInsert(f'{dinheiro} MOEDAS.', 'amarelo'))
    print('')
    if picaretas["names"][1] not in inventario['items']: # Picareta de Ouro
        print(f'1: {picaretas["names"][1]} - 50 MOEDAS') 
    else:
        print('Já comprado!')
    if picaretas["names"][2] not in inventario['items']: # Picareta de Diamante
        print(f'2: {picaretas["names"][2]} - 350 MOEDAS') 
    else:
        print('Já comprado!')
    if picaretas["names"][3] not in inventario['items']: # Picareta de Ouro
        print(f'3: {picaretas["names"][3]} - 1000 MOEDAS') 
    else:
        print('Já comprado!')
    print('')
    try:
        compra = int(input('COMPRAR: ').lower())
        comprar(compra)
    except ValueError:
        print('')
        print(fastColorInsert('Comando errado.', 'vermelho'))
        print('')

def comprar(index):
    global main, dinheiro, item_quantity, permitirMinerar, inventario, picaretas
    if index >= item_quantity[0] and index <= item_quantity[-1]:
        if (picaretas['names'][index] not in inventario['items']) and (dinheiro >= picaretas['prices'][index]):
            dinheiro -= picaretas['prices'][index]
            picaretas['limits'][0] += picaretas['durability'][index]
            permitirMinerar = True
            inventario['items'].append(picaretas['names'][index])
            print(fastColorInsert(f'Você comprou a {picaretas['names'][index]}!', 'verde'))
        else:
            print('')
            print(fastColorInsert('Sem dinheiro.', 'vermelho'))
            print('')
    else:
        print('')
        print(fastColorInsert('Item não existe.', 'vermelho'))
        print('')

def craftmenu():
    global inventario, picaretas, craftables
    print('')
    print('')
    print('---' * 10)
    print('Para craftar o item, digite o NÚMERO dele.')
    print('')
    print('1: Geleia + Picareta de Ouro = Cosmetic')
    print('2: Geleia + Carne Podre = Elixir')
    print('---' * 10)
    try:
        escolha_craft = int(input('QUAL ITEM CRAFTAR: '))
        craft(escolha_craft)
    except ValueError:
        print('')
        print(fastColorInsert('Comando inválido. Digite apenas o NÚMERO do item. (Ex: 1 ou 2)', 'vermelho'))
        print('')

def craft(index):
    global inventario
    if index >= craft_quantity[0] and index <= craft_quantity[-1]:
        inventario['items'].append(craftables[index-1])
        print('')
        print(f'VOCÊ CRAFTOU: {craftables[index-1]}!')
        print('')
    else:
        print('')
        print(fastColorInsert('Item não existe.', 'vermelho'))
        print('')

def help():
    print('')
    print('digite "SAIR" para encerrar o jogo.')
    print('se sua picareta quebrar, você pode comprar mais picaretas para mais durabilidade!')
    print('')

def menu():
    global dinheiro, meuHP, XP, XPTotal
    print(('-=-' * 5) + 'LambCrawler 1.2.3.1' + ('-=-' * 5))
    print(f'SEU DINHEIRO ATUAL: {fastColorInsert(dinheiro, "amarelo")}')
    print(f'SEU HP ATUAL: {fastColorInsert(meuHP, "verde")}')
    print(f'SEU XP ATUAL: {fastColorInsert(f"{XP} / {XPTotal}", "ciano")} {fastColorInsert(f"(Level {level})", "ciano")}')
    print('Ações: (m)MINERAR, (c)CAÇAR, (s)SHOP, (h)HELP, (i)INV, (craft)CRAFT')
    print('-=-' * 15)
    escolha(input('AÇÃO: ').lower())

def fastColorInsert(texto, cor):
    texto = str(texto)
    cor = cor.lower()
    if cor == 'amarelo':
        return '\033[93m' + texto + '\033[0m'
    elif cor == 'vermelho':
        return '\033[91m' + texto + '\033[0m'
    elif cor == 'verde':
        return '\033[92m' + texto + '\033[0m'
    elif cor == 'azul':
        return '\033[94m' + texto + '\033[0m'
    elif cor == 'magenta' or cor == 'roxo':
        return '\033[95m' + texto + '\033[0m'
    elif cor == 'ciano':
        return '\033[96m' + texto + '\033[0m'
    elif cor == 'branco' or cor == 'cinza':
        return '\033[97m' + texto + '\033[0m'
    elif cor == 'preto':
        return '\033[90m' + texto + '\033[0m'
    else:
        return texto

#LOOP PRINCIPAL
def escolha(action):
    global main
    if action == "m":
        minerar()
    elif action == "s":
        shop()
    elif action == "c":
        caçar()
    elif action == "h":
        help()
    elif action == "i":
        inv()
    elif action == "craft":
        craftmenu()
    elif action == "sair":
        print('')
        print('Obrigado por jogar!')
        print('')
        main = False
    else:
        print('')
        fastColorInsert('Comando Inválido.', 'vermelho')
        print('')

while main:
    menu()