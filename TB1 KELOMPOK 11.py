print("------Selamat Datang di McGoofy------")
pembeli = input("\nMasukkan Nama Pembeli: ")
print(f"Nama Pembeli: {pembeli}")
tempat = input("\nDine In / Take Away: ")
if tempat.lower() == "dine in": 
    meja = int(input("Nomor Meja Anda: "))

def fungsimakanan():
    makanan = [] # untuk memasukkan makanan yang dipilih ke dalam sebuah list

    while True:
        menu_makanan = [
            {"nama": "Spicy Chicken", "harga": 24000},
            {"nama": "Krispy Chicken", "harga": 24000},
            {"nama": "Big Mac", "harga": 41000},
            {"nama": "Cheeseburger", "harga": 32000},
            {"nama": "Cheeseburger Deluxe", "harga": 33500},
            {"nama": "Double Cheese Burger", "harga": 39500},
            {"nama": "Triple Cheese Burger", "harga": 61500},
            {"nama": "Beef Burger Deluxe", "harga": 25000},
            {"nama": "Chicken Burger Deluxe", "harga": 25000},
            {"nama": "McSpicy", "harga": 41000},
            {"nama": "McChicken", "harga": 32000},
            {"nama": "Fish Fillet Burger", "harga": 32000},
            {"nama": "-", "harga": 0} # jika tidak membeli makanan
        ]

        print("\n-------------MENU MAKANAN-------------\n")
        for i in range(len(menu_makanan)):
            if i < 9: # agar tulisan saat output sejajar dengan angka yang memiliki 2 digit
                print(f"{i + 1}.  {menu_makanan[i]['nama']: <24} Rp {menu_makanan[i]['harga']}")
            else:
                print(f"{i + 1}. {menu_makanan[i]['nama']: <24} Rp {menu_makanan[i]['harga']}")

        nomor = int(input("\nMasukkan Pilihan: ")) # untuk memilih makanan

        if 1 <= nomor < len(menu_makanan):
            porsi = int(input("Berapa Porsi: ")) # untuk mengisi berapa porsi yang dibeli
            makanan.append((menu_makanan[nomor - 1]['nama'], porsi, porsi * menu_makanan[nomor - 1]["harga"])) # memasukkan makanan dan porsi yang di pilih ke dalam list makanan
            # dengan urutan [0] = nama makanannya, [1] = jumlah porsinya, [2] = harga totalnya (harga dikali porsi)
        elif nomor == len(menu_makanan): # untuk membuat jika tidak membeli makanan akan langsung dilanjutkan ke pemilihan selanjutnya
            break
        else: # agar angka pilihan selalu sesuai
            print("Pilihan tidak ada, silahkan masukkan lagi!!")
            continue

        pilihan_lagi = input("Apakah Anda ingin memilih makanan lagi? (ya/tidak): ") # jika ingin memilih makanan lagi maka akan mengulang loop dari awal
        if pilihan_lagi.lower() != "ya": # kalau jawaban tidak maka akan lanjut ke bagian snack
            break

    return makanan

def fungsisnacks():
    snacks = []

    while True:
        menu_snacks = [
            {"nama": "Chicken Fingers", "harga": 14500},
            {"nama": "Spicy Chichken Bites", "harga": 13000},
            {"nama": "Apple Pie", "harga": 12500},
            {"nama": "McNuggets 4 pcs", "harga": 26000},
            {"nama": "McNuggets 6 pcs", "harga": 38500},
            {"nama": "McNuggets 9 pcs", "harga": 53500},
            {"nama": "Fish Snack Wrap", "harga": 17500},
            {"nama": "Rica Rica Fish Rice", "harga": 24500},
            {"nama": "French Fries Large ", "harga": 25500},
            {"nama": "Sweet Corn", "harga": 13000},
            {"nama": "-", "harga": 0} # jika tidak membeli snacks
        ]

        print("\n-------------MENU SNACKS-------------\n")
        for i in range(len(menu_snacks)):
            if i < 9:
                print(f"{i + 1}.  {menu_snacks[i]['nama']: <24} Rp {menu_snacks[i]['harga']}")
            else:
                print(f"{i + 1}. {menu_snacks[i]['nama']: <24} Rp {menu_snacks[i]['harga']}")

        nomor = int(input("\nMasukkan Pilihan: "))

        if 1 <= nomor < len(menu_snacks):
            porsi = int(input("Berapa Porsi: "))
            snacks.append((menu_snacks[nomor - 1]['nama'], porsi, porsi * menu_snacks[nomor - 1]["harga"]))
        elif nomor == len(menu_snacks):
            break
        else:
            print("Pilihan tidak ada, silahkan masukkan lagi!!")
            continue

        pilihan_lagi = input("Apakah Anda ingin memilih snacks lagi? (ya/tidak): ")
        if pilihan_lagi.lower() != "ya":
            break

    return snacks


def fungsiminuman():
    minuman = []

    while True:
        menu_minuman = [
            {"nama": "Hot Tea", "harga": 12000},
            {"nama": "Hot Coffee", "harga": 12000},
            {"nama": "Bottled Mineral Water", "harga": 11500},
            {"nama": "Milo, Medium", "harga": 21500},
            {"nama": "Tehbotol Tawar", "harga": 9500},
            {"nama": "Iced Lychee Tea", "harga": 20000},
            {"nama": "Fruit Tea Blackcurrant", "harga": 9500},
            {"nama": "Fruit Tea Lemon, Large", "harga": 14000},
            {"nama": "Coke Float", "harga": 15000},
            {"nama": "Fanta Float", "harga": 15000},
            {"nama": "Coca-Cola, Large", "harga": 14000},
            {"nama": "Fanta, Large", "harga": 14000},
            {"nama": "Sprite, Large", "harga": 14000},
            {"nama": "-", "harga": 0}  # Jika tidak membeli minuman
        ]

        print("\n-------------MENU MINUMAN-------------\n")
        for i in range(len(menu_minuman)):
            if i < 9:
                print(f"{i + 1}.  {menu_minuman[i]['nama']: <24} Rp {menu_minuman[i]['harga']}")
            else:
                print(f"{i + 1}. {menu_minuman[i]['nama']: <24} Rp {menu_minuman[i]['harga']}")

        nomor = int(input("\nMasukkan Pilihan: "))

        if 1 <= nomor < len(menu_minuman):
            gelas = int(input("Berapa Gelas: "))
            minuman.append((menu_minuman[nomor - 1]['nama'], gelas, gelas * menu_minuman[nomor - 1]["harga"]))
        elif nomor == len(menu_minuman):
            break
        else:
            print("Pilihan tidak ada, silahkan masukkan lagi!!")
            continue

        pilihan_lagi = input("Apakah Anda ingin memilih minuman lagi? (ya/tidak): ")
        if pilihan_lagi.lower() != "ya":
            break

    return minuman

def fungsidessert():
    dessert = []

    while True:
        menu_dessert = [
            {"nama": "McFlurry Choco", "harga": 14000},
            {"nama": "McFlurry Feat. Oreo", "harga": 14000},
            {"nama": "Strawberry Sundae", "harga": 12000},
            {"nama": "Choco Sundae", "harga": 12000},
            {"nama": "Choco Strawberry Sundae", "harga": 13000},
            {"nama": "Matcha McFlurry w/ Oreo", "harga": 12000},
            {"nama": "Tiramisu McFlurry", "harga": 18000},
            {"nama": "-", "harga": 0}  # Jika tidak membeli dessert
        ]

        print("\n-------------MENU DESSERT-------------\n")
        for i in range(len(menu_dessert)):
            if i < 9:
                print(f"{i + 1}.  {menu_dessert[i]['nama']: <24} Rp {menu_dessert[i]['harga']}")
            else:
                print(f"{i + 1}. {menu_dessert[i]['nama']: <24} Rp {menu_dessert[i]['harga']}")

        nomor = int(input("\nMasukkan Pilihan: "))

        if 1 <= nomor < len(menu_dessert):
            cup = int(input("Berapa Cup: "))
            dessert.append((menu_dessert[nomor - 1]['nama'], cup, cup * menu_dessert[nomor - 1]["harga"]))
        elif nomor == len(menu_dessert):
            break
        else:
            print("Pilihan tidak ada, silahkan masukkan lagi!!")
            continue

        pilihan_lagi = input("Apakah Anda ingin memilih dessert lagi? (ya/tidak): ")
        if pilihan_lagi.lower() != "ya":
            break

    return dessert

makanan = fungsimakanan()
snacks = fungsisnacks()
minuman = fungsiminuman()
dessert = fungsidessert()

totalmkn = sum(item[2] for item in makanan) # untuk menjumlahkan total harga pada item makanan
totalsnk = sum(item[2] for item in snacks) # untuk menjumlahkan total harga pada item snacks
totalmnm = sum(item[2] for item in minuman) # untuk menjumlahkan total harga pada item minuman
totaldst = sum(item[2] for item in dessert) # untuk menjumlahkan total harga pada item dessert
service = 0
if tempat.lower() == "take away": # jika mengambil take away akan ada tambahan biaya sebanyak Rp 3000
    service = 3000 
total = totalmkn + totalmnm + totalsnk + totaldst + service # harga total (termasuk service) sebelum ditambah pajak
tax = int(total / 10) # harga pajak 10%
totalsemua = tax + total # harga total yang harus dibayar tambah pajak

metode_pembayaran = input("\nPilih metode pembayaran: ")
print("Total harus dibayar: Rp", totalsemua)
while True: # diberikan loop agar jika uang kurang bisa mengulang lagi
    if metode_pembayaran.lower() == "cash":
        uang = int(input("Uang Tunai Pembeli: Rp "))
        kembalian = int(uang - totalsemua) # untuk menentukan berapa banyak kembalian yang diperoleh
        if kembalian >= 0:
            print("Kembalian: Rp", kembalian)
        else:
            print("Maaf uang anda kurang, silahkan coba lagi\n") # jika kurang akan disuruh memasukan nominal lagi
            continue
    else: # jika cashless maka tidak harus mengisi uang yang akan dibayar dan tidak akan ada kembalian
        uang = totalsemua # uang yang dibayar otomatis sama dengan harga totalnya
        kembalian = -1

    print("\n======================================")
    print("============= STRUK BELI =============")
    print("======================================")
    print("Name\t\t:", pembeli)
    if tempat.lower() == "dine in": 
        print("Table Number \t:", meja)

    for item in makanan:
        print(f"Item\t\t: {item[1]} {item[0]} (Rp {item[2]})") # untuk menuliskan semua list yang ada dalam list makanan, dimulai dari porsi, nama makanan, lalu harganya
    for item in snacks:
        print(f"\t\t  {item[1]} {item[0]} (Rp {item[2]})")
    for item in minuman:
        print(f"\t\t  {item[1]} {item[0]} (Rp {item[2]})")
    for item in dessert:
        print(f"\t\t  {item[1]} {item[0]} (Rp {item[2]})")

    if tempat.lower() == "take away": # jika take away maka akan jadi Take-Out dan ditambah biaya service sebanyak Rp 3000
        print("\nTake-Out Total\t: Rp", totalsemua)
    else: # jika Dine In maka akan jadi Eat-In dan tidak ada tambahan biaya
        print("\nEat-In Total\t: Rp", totalsemua)

    if metode_pembayaran.lower() == "cash":  # jika pakai uang cash maka akan Cash Tendered
        print("Cash Tendered\t: Rp", uang)
    else: # jika tidak menggunakan cash makan akan cashless
        print(f"Cashless {metode_pembayaran}\t: Rp {uang}")

    if kembalian >= 0:
        print("Change\t\t: Rp", kembalian)

    print("\nNet Sales\t: Rp", total) # Harga sebelum ditmambah pajak
    print("\nTax\t10%\t: Rp", tax)
    print("======================================")
    break