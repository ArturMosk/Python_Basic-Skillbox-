def move(disks, rod_x, rod_y):
    if disks == 1:
        print('Переложить диск 1 со стержня номер {} на стержень номер {}'.format(rod_x, rod_y))
        return
    move(disks - 1, rod_x, 6 - rod_x - rod_y)
    print('Переложить диск {} со стержня номер {} на стержень номер {}'.format(disks, rod_x, rod_y))
    move(disks - 1, 6 - rod_x - rod_y, rod_y)


disks_amt = int(input('Введите количество дисков: '))
move(disks_amt, 1, 3)
