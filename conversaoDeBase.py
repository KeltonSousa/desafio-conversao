while(True):   
    print('''\n Qual base desejas converter:
    1 - DECIMAL
    2 - BINARIA
    3 - OCTAL
    4 - HEXADECIMAL 
    5 - SAIR\n''')



    base = int(input('\n Digite sua opção: '))
    if base == 1:
        deci = int(input('\n Digite o numero em decimal desejado:'))
        print(' \n------------------------------------')
        print(' {} convertido para binario eh {}' .format(deci, bin(deci)[2:]))
        print(' {} convertido para octal eh {}' .format(deci, oct(deci)[2:]))
        print(' {} convertido para hexadecimal eh {}' .format(deci, hex(deci)[2:]))
        print(' ------------------------------------')

    elif base == 2:
        bin = int(input('\n Digite o numero em binario desejado:'))
        binToDec = str(bin)
        if all (c in '01' for c in binToDec):
            binNum = int(binToDec, 2)
            print(' \n------------------------------------')
            print(' {} convertido para decimal eh {}' .format(bin, int(binToDec, 2)))
            print(' {} convertido para octal eh {}' .format(bin, oct(binNum)[2:]))
            print(' {} convertido para hexadecimal eh {}' .format(bin, hex(binNum)[2:]))
            print(' ------------------------------------')
        else: 
            print(' Digite um valor valido!!! \n')
            continue

    elif base == 3:
        octal = int(input('\n Digite o numero em octa desejado:'))
        octalToDec = str(octal)
        if all (c in '01234567' for c in octalToDec):
            octalNum = int(octalToDec, 8)
            print(' \n------------------------------------')
            print(' {} convertido para binario eh {}' .format(octal, bin(octal)[2:]))
            print(' {} convertido para decimal eh {}' .format(octal, int(octalToDec, 8)))
            print(' {} convertido para hexadecimal eh {}' .format(octal, hex(octalNum)[2:]))
            print(' ------------------------------------')
        else:
            print(' Digite um valor valido!!! \n')
            continue

    elif base == 4:
        hexa = input('\n Digite o numero em hexadecimal desejado:')
        if all (c in '0123456789abcdef' for c in hexa):
            hexaToDec = int(hexa, 16)
            print(' \n------------------------------------')
            print(' {} convertido para binario eh {}' .format(hexa, bin(hexaToDec)[2:]))
            print(' {} convertido para octal eh {}' .format(hexa, oct(hexaToDec)[2:]))
            print(' {} convertido para decimal eh {}' .format(hexa, hexaToDec))
            print(' ------------------------------------')
        else: 
            print(' Digite um valor valido!!! \n')
            continue

    elif base == 5:
        print(' saindo...')
        break

    else:
        print(' Digite um valor valido!!! \n')
    
