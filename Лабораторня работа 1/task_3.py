disk_mb = 1.44
pages_in_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

total_char_in_book = pages_in_book * lines_per_page * chars_per_line
total_bytes_per_book = total_char_in_book * bytes_per_char

disk_bytes = disk_mb * 1024 * 1024

num_books_on_disk = int(disk_bytes // total_bytes_per_book)

print("Количество книг, помещающихся на дискету:", num_books_on_disk)