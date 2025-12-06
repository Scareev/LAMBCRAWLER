import time
import random

#LAMB // ZERAR JOGO
lamb = 4000
main = True

#RNG 
chance = 0
durabilidade = 0
limite = 5

#RENDA INICIAL
dinheiro = 0

#PICARETAS
permitirMinerar = True
picaretas = ['Picareta de Ferro', 'Picareta de Ouro', 'Picareta de Diamante', 'Picareta de Void']
picareta_de_ferroPreço = 0
picareta_de_ouroPreço = 50
picareta_de_diamantePreço = 350
picareta_de_voidPreço = 1000

#MINÉRIOS
ironOre = 0
goldOre = 0
diamondOre = 0
voidOre = 0

#INVENTÁRIO
inventario = [picaretas[0]]

#LEVEL-UP
level = 1

#SISTEMA DE CAÇA
meuHP, meuHPTotal = 100, 100
meuDano = 0
critChance = 0
XP = 0
XPTotal = 10

#POOL DE INIMIGOS
#Para cada inimigo, é proporcional ao seu index, exemplo: todos os indexes 0 são atribuidos ao slime, indexes 1 ao zumbi, e assim vai.
mobs = {
  "monstBoolean":       True,
  "monstName":          ["Slime", "Zumbi", "Earth Golem"],
  "monstHP":            [50, 70, 120],
  "monstHPTotal":       [50, 70, 120],
  "monstATK":           [20, 25, 50],
  "monstLevel":         [0, 1, 2],
  "monstXPDropRate":    [[5, 10], [10, 25], [25, 75]]
}

#DROPS
drops = {
    "itemName":         ["Geleia", "Carne Podre", "Rocha Mística"],
    "itemValue":        [50, 20, 250],
    "itemRarity":       [0, 0, 1]
}
itemGel = 'Geleia'
itemCarne = 'Carne Podre'

#ITENS CRAFTAVEIS
craftables = ['Cosmetic', 'Elixir']


def minerar():
    global dinheiro, chance, ironOre, goldOre, diamondOre, voidOre, durabilidade, permitirMinerar
    if permitirMinerar == True:
        durabilidade += 1
        chance = random.randint(1, 100)
        ironOre = random.randint(2, 5)
        goldOre = random.randint(10, 30)
        diamondOre = random.randint(30, 50)
        voidOre = random.randint(1000, 4000)
        time.sleep(0.1)
        print('Minerando.')
        time.sleep(0.1)
        print('Minerando..')
        time.sleep(0.1)
        print('Minerando...')
        time.sleep(0.1)
        print('')
        print('')
        print('')
        print('')
        if durabilidade < limite:
            if chance >= 10 and chance <= 50:
                dinheiro = dinheiro + ironOre
                print('')
                print(f'Você minerou \033[90mFERRO!\033[0m ele vale: {ironOre} moedas.')
                print('')
            elif chance >= 40 and chance <= 60:
                dinheiro = dinheiro + goldOre
                print('')
                print(f'Você minerou \033[93mOURO!\033[0m ele vale: {goldOre} moedas.')
                print('')
            elif chance >= 70 and chance <= 90:
                dinheiro = dinheiro + diamondOre
                print('')
                print(f'Você minerou \033[96mDIAMANTE!\033[0m ele vale: {diamondOre} moedas.')
                print('')
            elif chance >= 91 and chance <= 100:
                dinheiro = dinheiro + voidOre
                print('')
                print(f'Você minerou \033[32m\033[1mO VOID!\033[0m ele vale: {voidOre} moedas.')
                print('')
            else:
                print('')
                print(f'Você não achou nada...')
                print('')
            print(f'DURABILIDADE: {durabilidade} de {limite}')
        else:
            permitirMinerar = False
            inventario.remove(inventario[0])
            print(f'DURABILIDADE: {durabilidade} de {limite}')
            print('')
            fastColorInsert('Sua picareta quebrou! Compre outra picareta para continuar minerando.', 'vermelho')
            print('')

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
    print(f'\033[91mBATALHA ENCONTRADA!\033[0m: {enemyName} LEVEL: {enemyLevel}')
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
    global dinheiro, level, critChance, itemGel, itemCarne, main, XP
    global enemy, enemyHP, enemyATK, enemyName, enemyHPTotal
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
            print(f'Seu HP atual: {meuHP} / {meuHPTotal} <-- \033[91m{danoInimigo}\033[0m DANO RECEBIDO')
            print(f'HP do {enemyName}: {enemyHP} / {enemyHPTotal} <-- \033[91m{meuDano}\033[0m DANO DADO')
            print('-=-=-')
            if meuHP <= 0:
                main = False
                meuHP *= (-1)
                print('VOCÊ MORREU!')
                break
            if enemyHP <= 0:
                print('\033[92mVOCÊ VENCEU!\033[0m')
                dropSys()
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

def dropSys():
    global inventario, dinheiro
    global enemyName
    global itemCarne, itemGel
    dinheiroGanho = random.randint(50, 100)
    if enemyName == 'slime':
        dinheiro += dinheiroGanho
        inventario.append(itemGel)
        print(f'Você ganhou: {itemGel}!')
        print(f'Você ganhou: {dinheiroGanho} moedas!')
    elif enemyName == 'zumbi':
        dinheiroGanho = random.randint(50, 100)
        dinheiro += dinheiroGanho
        inventario.append(itemCarne)
        print(f'Você ganhou: {itemCarne}!')
        print(f'Você ganhou: {dinheiroGanho} moedas!')

def inv():
    global itemGel
    print('')
    print('Seus itens:')
    print(inventario)        
    print('')

def levelUp():   
    global meuHP, meuHPTotal, XP, XPTotal, level
    while XP >= XPTotal:
        level += 1
        meuHP += 160
        meuHPTotal = meuHP
        print('')
        fastColorInsert('VOCÊ SUBIU DE NÍVEL!', 'verde')
        print(f'Seu HP Subiu!: {meuHP}')
        print('')
        XP -= XPTotal
        XPTotal = int(XPTotal * 1.5) # Aumenta o custo do próximo nível em 50%
        print(f'XP necessário para o próximo nível: {XPTotal}')

def shop():
    global dinheiro, lamb, main, inventario, picaretas
    print('')
    print(('-=-' * 5) + 'Loja do Seu Bananal!' + ('-=-' * 5))
    print(f'SEU DINHEIRO ATUAL: ', end='') # end='' impede o print de pular linha
    fastColorInsert(f'{dinheiro} MOEDAS.', 'amarelo')
    print('')
    print('Produtos disponiveis:')
    print('0: LAMB: 4000 MOEDAS') 

    if picaretas[3] not in inventario: # Picareta de Void
        print(f'1: {picaretas[3]} - 1000 MOEDAS')
    if picaretas[1] not in inventario: # Picareta de Ouro
        print(f'2: {picaretas[1]} - 50 MOEDAS') 

    print('')
    comprar = input('COMPRAR: ').lower()

    if comprar == "0" and dinheiro >= lamb:
        print('você ZEROU O JOGO!')
        main = False
    elif comprar == "1" or comprar == "2":
        comprar_picareta(comprar)
    else:
        print('')
        fastColorInsert('Opção inválida ou dinheiro insuficiente.', 'vermelho')
        print('')

def comprar_picareta(id_da_picareta):
    global dinheiro, limite, permitirMinerar, inventario, picaretas

    #PICARETA DE VOID
    if id_da_picareta == "1":
        if picaretas[3] not in inventario:
            if dinheiro >= 1000:
                dinheiro -= 1000
                limite += 100
                permitirMinerar = True
                inventario.append(picaretas[3])
                print(f'\n\033[92mVocê comprou a {picaretas[3]}!\033[0m')
            else:
                fastColorInsert('Sem dinheiro.', 'vermelho')
        else:
            fastColorInsert('Você já possui este item!', 'verde')
 
    elif id_da_picareta == "2":
        if picaretas[1] not in inventario:
            if dinheiro >= 50:
                dinheiro -= 50
                limite += 30
                permitirMinerar = True
                inventario.append(picaretas[1])
                print(f'\n\033[92mVocê comprou a {picaretas[1]}!\033[0m')
            else:
                fastColorInsert('Sem dinheiro.', 'vermelho')
        else:
            fastColorInsert('Você já possui este item!', 'verde')

def craft():
    global inventario, itemGel, picaretas, craftables
    print('')
    print('')
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
        craftItems(escolha_craft)
    except ValueError:
        print('')
        fastColorInsert('Comando inválido. Digite apenas o NÚMERO do item. (Ex: 1 ou 2)', 'vermelho')
        print('')

def craftItemsAppender(index):
    if index >= 0:
        inventario.append(craftables[index])
        print('')
        print(f'VOCÊ CRAFTOU: {craftables[index]}!')
        print('')
    else:
        print('')
        fastColorInsert('Item não existe.', 'vermelho')
        print('')

def craftItems(index):
    global inventario, craftables
    global picaretas
    global itemGel, itemCarne
    if index == 1 and picaretas[1] in inventario and itemGel in inventario:
        craftItemsAppender(0)
        inventario.remove(itemGel)
        inventario.remove(picaretas[1])
    elif index == 2 and itemCarne in inventario and itemGel in inventario:
        craftItemsAppender(1)
        inventario.remove(itemGel)
        inventario.remove(itemCarne)
    else:
        print('')
        fastColorInsert('Você não tem os itens necessários!', 'vermelho')
        print('')

def help():
    print('')
    print('para zerar o jogo, você precisa comprar o LAMB!')
    print('se sua picareta quebrar, você pode comprar mais picaretas para mais durabilidade!')
    print('')
      
def changeLog():
    print('')
    print(('-=-'*5) + 'CHANGELOG:' + ('-=-'*5))
    print('')
    print('~ Remake do sistema de Crafting.')
    print('+ Zumbi na pool de Caçar.')
    print('+ Itens: Cosmetic e Elixir adicionados.')
    print('+ fastColorInsert(texto, cor): Função automática de colorir texto no terminal')
    print('+ Adição deste changelog :)')
    print('')

def menu():
    global dinheiro, meuHP, XP, XPTotal
    print(('-=-' * 5) + 'LambCrawler 1.2' + ('-=-' * 5))
    print(f'SEU DINHEIRO ATUAL: \033[93m{dinheiro}\033[0m')
    print(f'SEU HP ATUAL: \033[92m {meuHP}\033[0m')
    print(f'SEU XP ATUAL: \033[96m {XP} / {XPTotal}\033[0m \033[96m(Level {level})\033[0m')
    print('Ações: (m)MINERAR, (c)CAÇAR, (s)SHOP, (h)HELP, (i)INV, (craft)CRAFT', '(cl)CHANGELOG')
    print('-=-' * 15)
    escolha(input('AÇÃO: ').lower())

def fastColorInsert(texto, cor):
   if cor == 'amarelo':
        print('\033[93m' + texto + '\033[0m')
   elif cor == 'vermelho':
        print('\033[91m' + texto + '\033[0m')
   elif cor == 'verde':
        print('\033[92m' + texto + '\033[0m')

#LOOP PRINCIPAL
def escolha(action):
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
        craft()
    elif action == "cl":
        changeLog()
    else:
        print('')
        fastColorInsert('Comando Inválido.', 'vermelho')
        print('')

while main:
    menu()