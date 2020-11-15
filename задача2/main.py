# функция, которая возвращает табулатуру аккордов соответственно их названиям
def turnChordsIntoTab(chords):
    # кладем кждый элемент в массив
    chordsArray = chords.split(' ')
    # начало табулатуры
    note_e = 'e|---'
    note_B = 'B|---'
    note_G = 'G|---'
    note_D = 'D|---'
    note_A = 'A|---'
    note_E = 'E|---'
    chord = ''

    # расписываем аккорды
    for i in range(len(chordsArray)):
        if chordsArray[i] == 'Am':
            note_e += '0---'
            note_B += '1---'
            note_G += '2---'
            note_D += '2---'
            note_A += '0---'
            note_E += '----'
            chord += 'Am  '

        if (chordsArray[i] == 'C'):
            note_e += '0---'
            note_B += '1---'
            note_G += '0---'
            note_D += '2---'
            note_A += '3---'
            note_E += '----'
            chord += 'C   '

        if (chordsArray[i] == 'D'):
            note_e += '2---'
            note_B += '3---'
            note_G += '2---'
            note_D += '0---'
            note_A += '----'
            note_E += '----'
            chord += 'D   '

        if (chordsArray[i] == 'G'):
            note_e += '3---'
            note_B += '0---'
            note_G += '0---'
            note_D += '0---'
            note_A += '2---'
            note_E += '3---'
            chord += 'G   '

    # конец табулатуры
    note_e += '|\n'
    note_B += '|\n'
    note_G += '|\n'
    note_D += '|\n'
    note_A += '|\n'
    note_E += '|\n'

    # возвращаем построенную табулатуру
    return note_e + note_B + note_G + note_D + note_A + note_E + '     ' + chord.strip()


print(turnChordsIntoTab('Am Am C C D D G G') ==
'e|---0---0---0---0---2---2---3---3---|\n' +
'B|---1---1---1---1---3---3---0---0---|\n' +
'G|---2---2---0---0---2---2---0---0---|\n' +
'D|---2---2---2---2---0---0---0---0---|\n' +
'A|---0---0---3---3-----------2---2---|\n' +
'E|---------------------------3---3---|\n' +
'     Am  Am  C   C   D   D   G   G')
