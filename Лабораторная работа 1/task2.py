# TODO Найдите количество книг, которое можно разместить на дискете

volume_of_book = (100 * 50 * 25 * 4) / 1024 / 1024
quantity_of_books = 1.44 // volume_of_book
qua_int = int(quantity_of_books)
print("Количество книг, помещающихся на дискету:", qua_int)

