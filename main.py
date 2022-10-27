import random

breakfastList = [
    'Owsianka z orzechami włoskimi i daktylami',
    'Burger śniadaniowy z bekonem i jajkiem sadzonym',
    'Jajecznica z szynką',
    'Jajka sadzone z bekonem i fasolką',
    'Biszkopt z jabłkami',
    'Owsianka z jabłkami, płatkami migdałów i miodem',
    'Omlet twarogowo-owsiany z owocami',
    'Kanapki z serem i warzywami',
    'Owsianka snickers',
    'Parówki z chlebem i ketchupem',
    'Grysik z owocami',
    'Omlet w tortilli z serem i warzywami',
    'Szakszuka',
    'Kanapki z twarogiem i szczypiorkiem',
    'Tosty francuskie z czekoladą',
    'Tosty francuskie z jabłkami i konfiturą a\'la Gordom Ramsay'
    ]

lunchList = [
    'Bułka z szynką i pomidorem, jogurt',
    'Bułka z serem i warzywami, banan',
    'Koktajl białkowy z bananem i masłem orzechowym, jabłko',
    'Jogurt proteinowy, baton proteinowy, dwie pomarańcze',
    'Tortilla z bieluchem, warzywami i szynką',
    'Czekoladowo-wiśniowy koktajl na skyrze',
    'Kefir, banan, pomarańcze',
    'Serek wiejski z warzywami i chlebem',
    'Skyr z czekoladą, roczynkami i bananem',
    'Jogurt naturalny z płatkami owsianymi i migdałami',
    'Skyr z kiwi i orzechami',
    'Skyr pitny, baton proteinowy, banan',
    'Jogurt z płatkami owsianymi i truskawkami',
    'Kefir, banan, baton proteinowy'
    ]

dinnerList = [
    'Spaghetti bolognese',
    'Butter chicken',
    'Kurczak w tortilli z sosem czosnkowym i warzywami',
    'Kurczak w tortilli z sosem musztardowym i warzywami',
    'Dietetyczne burgery',
    'Pizza',
    'Makaron z kurczakiem, szpinakiem i pesto',
    'Makaron z bekonem, szpinakiem, serem feta i pomidorkami',
    'Fasolka szparagowa z kaszą i jajkiem sadzonym',
    'Pieczone mielone z ziemniakami i kapustą',
    'Kotlety z kurzaka z ziemniakami i surówką',
    'Pulpety w sosie pomidorowym z ryżem',
    'Leczo',
    'Pita z soem czosnkowym, gyrosem i surówką',
    ]

supperList = [
    'Tosty z mozarellą i oliwkami',
    'Naleśniki z frużeliną',
    'Gofry z frużeliną',
    'Sałatka z mozarellą i oliwkami',
    'Hummus ze słupkami warzyw',
    'Quesadilla wege',
    'Grzanki z cebulą, serem i oliwkami',
    'Kanapka z serem feta i pomidorem',
    'Naleśniki z bananami i czekoladą',
    'Panini z szynką, serem i suszonymi pomidorami',
    'Grzanki z ricottą, rukolą i szynką szwarcwaldzką',
    'Kanapki z pastą jajeczną i szczypiorkiem',
    'Mini zapiekanki warzywno, serowo, jajeczne'
    ]

def pickRandomMeal(whichMealList):
    return(str(whichMealList[random.randint(0,(len(whichMealList)-1))]))

def generateMenuForDay(dayNum):
    menuForDay = '\nŚniadanie : '+(pickRandomMeal(breakfastList))+'\nDrugie śniadanie : '+(pickRandomMeal(lunchList))+'\nObiad : '+(pickRandomMeal(dinnerList))+'\nKolacja : '+(pickRandomMeal(supperList))+'\n\n'
    return ('Dzień '+str(dayNum)+' :'+menuForDay)

def generateFullMenu():
    fullMenu = 'Oto jadłospis na '+str(amountOfDays)+' dni:\n\n'
    for i in range(amountOfDays):
        fullMenu = fullMenu + (generateMenuForDay(i+1))
        i = i + 1
    return fullMenu

def yesOrNo(questionToConfirm):
    while True:
        yesNoInput = input(questionToConfirm)
        try:
            str(yesNoInput)
        except:
            continue
        yesNoInput = yesNoInput.upper()
        if yesNoInput == 'T':
            return True
        if yesNoInput == 'N':
            return False

while True:
    amountOfDays = input('Na ile dni chcesz przygotować jadłospis? (Poradzę sobie najwyżej z 14) : ')
    errorFlag = False
    try:
        amountOfDays = int(amountOfDays)
    except:
        errorFlag = True
    if errorFlag == True:
        print('Nieprawidłowa ilość dni. Podaj wartość numeryczną.')
        continue
    if amountOfDays <= 0:
        print('Nie mogę przygotować jadłospisu na ujemną lub zerową ilośc dni. Podaj prawidłową wartość.')
    elif amountOfDays > 14:
        print('Nie przygotuję jadłospisu aż na tyle dni. Podaj wartość z zakresu 1-14')
    if amountOfDays > 0 and amountOfDays <= 14 and errorFlag == False:
        break

while True:
    menuForUser = generateFullMenu()
    print(menuForUser)
    if yesOrNo('Czy podoba Ci się to menu? (T/N) : '):
        break