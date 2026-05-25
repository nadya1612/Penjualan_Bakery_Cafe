# ===================================
# [Bakery/Coffee shop Cashier app]
# ===================================
# Developed by. Nadya Divia
# JCDS - [Class Batch]


# /************************************/

# /===== Data Model =====/
# Create your data model here
 # Example data model
data = {
    "product_id" : [],
    "product_name" : [],
    "product_category" : [],
    "product_stock" : [],
    "product_price" : [],
    "product_total_sold" : []
}
cart = []

list_product = [
    {"product_id" : "1", "product_name": "Roti",        "product_stock":10, "product_price":20_000, "product_category" : "Bread", "product_total_sold" : 20},
    {"product_id" : "2", "product_name": "croissant",   "product_stock":10, "product_price":25_000, "product_category" : "Pastry", "product_total_sold" : 30},
    {"product_id" : "3", "product_name": "Donat",       "product_stock":10, "product_price":15_000, "product_category" : "Bread", "product_total_sold" : 50},
    {"product_id" : "4", "product_name": "Latte",       "product_stock":10, "product_price":30_000, "product_category" : "Coffee", "product_total_sold" :10 },
    {"product_id" : "5", "product_name": "Americano",   "product_stock":10, "product_price":25_000, "product_category" : "Coffee","product_total_sold" : 60}
]
# /===== Feature Program =====/
# Create your feature program here
def read_menu():
    print("\nSelamat datang di aplikasi kasir Bakery/Coffee \n")
    print("1. Lihat Daftar Menu ")
    print("2.Tambah Daftar Menu")
    print("3.Update Daftar Menu")
    print("4.Hapus Daftar Menu")
    print("5.Beli produk")
    print("6.Laporan Penjualan")
    print("7. keluar program\n")
    input_menu = input("[!] Pilih menu :")
    return input_menu

def get_product(data):
    print("\nDaftar Menu")
    print(f"{'ID' : <5}{'Nama' :<15}{'category':<12}{'price':<12} {'sold':<7}")
    print("-"*60)
    for product in data: 
        
        product_id  = product["product_id"]
        product_name = product ["product_name"]
        product_category = product["product_category"]
        product_stock = product["product_stock"]
        product_price = product["product_price"]
        product_total_sold = product["product_total_sold"]

        print(f"{product_id : <5}{product_name:<15} {product_stock:<7} {product_price:<12}{product_category :<12} {product_total_sold:<7}")
    
def search_product(search_product_name):  
    search_result =[] 
    for product in list_product:
        product_name = product ["product_name"]
        
        if search_product_name.lower() in product_name.lower():
            search_result.append(product)
    if len (search_result) > 0:
        get_product(search_result)
    else :
        print("Produk tidak ditemukan") 
    get_product(search_result)


def create_menu(product_id, product_name, product_category, product_stock = 0, product_price = 0, product_total_sold = 0):
    product = {
        "product_id" :product_id,
        "product_name" : product_name,
        "product_category" : product_category,
        "product_stock" : product_stock,
        "product_price" : product_price,
        "product_total_sold" : product_total_sold   
    }
    print(product)
    confirm = input("Apakah ingin lanjut untuk menambahkan produk (y/t)?")
    if confirm.lower() == "y":
        list_product.append(product)
        print("Produk baru berhasil ditambahkan !")
    else:
        print("Produk baru gagal ditambahkan !")
    get_product(list_product)

    

def update_menu (product_id):
    
    for product in list_product:
        if product["product_id"] == product_id:
            selected_product = product
            print("\n Produk ditemukan !")
            print(f"{'ID' : <5}{'Nama' :<15}{'category':<12}{'price':<12} {'sold':<7}")
            print("-"*60)
            print(f"ID       : {selected_product['product_id']}")
            print(f"Nama     : {selected_product['product_name']}")
            print(f"Category    : {selected_product['product_category']}")
            print(f"Stock    : {selected_product['product_stock']}")
            print(f"Harga    : {selected_product['product_price']}")
            print(f"Total sold    : {selected_product['product_total_sold']}")


            product["product_name"] = input("Masukkan nama baru        : ")
            product["product_category"] = input("Masukkan category baru    : ")
            product["product_stock"] = input("Masukkan stock baru  : ")
            product["product_price"] = input("Masukkan harga baru : ")
            product["product_total_sold"] = input("Masukkan total produk baru yang sudah terjual : ")

            print(product)
            confirm = input("Apakah yakin ingin lanjut untuk memperbaharui produk ? (y/t)")
            if confirm.lower() == "y":
                print("Informasi produk berhasil diperbaharui !")
            else:
                print("Informasi produk gagal diperbaharui !")
            return
    print("Produk tidak ditemukan !")
          
    


def delete(data):
    
    get_product(data)
    
    del_index = input("Masukkan ID item yang ingin dihapus dari daftar menu : ")
    
    for i in range (len(data)):
        
        if  data[i]["product_id"] == del_index :
            
            confirm = input("Apakah ingin lanjut untuk menghapus item (y/t)?")

            if confirm.lower() == "y":
                data.pop(i)
            

                print("Item berhasil dihapus !")
                get_product(data)
            else:
                print("Item gagal didihapus !")
            return
            
    print("Produk tidak ditemukan!")

def buy_item(data, cart):
    get_product(data)
    buy_item =input("Masukkan ID item yang ingin di beli : ")
    for product in data :
        if product["product_id"] == buy_item:
            print(f"\nItem : {product['product_name']}")
            print(f" Harga Item : {product['product_price']}")
            print(f"Stock Item : {product['product_stock']}")
            print(f"Item Sold sebanyak : {product['product_total_sold']}")
            jumlah = int(input("Masukkan jumlah item yang ingin dibeli :"))
            if jumlah <= product["product_stock"]:
                total_price = jumlah * product["product_price"]
                confirm = input("Apakah ingin dimasukkan dalam cart? (y/t)")
                if confirm.lower() == "y":
                    cart_item = { 
                        "product_id"        : product["product_id"],
                        "product_name"      : product["product_name"],
                        "product_price"     : product["product_price"],
                        "Qty"               : jumlah,
                        "product_total_sold": product["product_total_sold"],
                        "sub_total"          : total_price
                    }
                    cart.append(cart_item)

                    product["product_stock"] -= jumlah
                    product["product_total_sold"] += jumlah
                    print("Produk berhasil ditambahkan ke keranjang!")
                    print("\n===Keranjang Belanja ===")

                    if len(cart) == 0:
                        print("Keranjang kosong!")
                        return
                    print(f"{'Nama': <15}{'Harga': <10}{'Qty': <10}{'Subtotal'}")
                    print("-" * 60 )

                    total_price = 0
                    for item in cart:
                        print(
                            f"{item['product_name']:<15}"
                            f"{item['product_price']:<10}"
                            f"{item['Qty']:<10}"
                            f"{item['sub_total']}"
                        )
                        total_price += item["sub_total"]
                    print("-" * 60)
                    print(f"Total bayar : Rp {total_price}")
                else:
                    print("Pembeliaan dibatalkan")
                
            else:
                print("Stock tidak cukup")
            return
    print("Produk tidak ditemukan!")
def report(data):
    print("\n===Laporan Penjualan===") 
    print(f"{'ID': <15}{'Nama': <15}{'Terjual': <10}{'Total_Pendapatan'}")
    print("-" * 65 )   

    total_revenue = 0
    for product in data:
        
        revenue = (product["product_total_sold"] * product["product_price"])
        total_revenue += revenue
        print(
            f"{product['product_id']:<15}"
            f"{product['product_name']:<15}"
            f"{product['product_total_sold']:<10}"
            f"{revenue}"
            )
    print("-" * 65)
    print(f"Total Pendapatan : {total_revenue}")

                


        
            

# /===== Main Program =====/
# Create your main program here
running = True
while running:
    input_user = read_menu()

    if input_user == "1":
        while running:
            print ("\n Sub menu Lihat Daftar Menu\n")
            print(" 1. Lihat semua Daftar Menu")
            print(" 2. Cari Daftar Menu")
            print(" 3. Kembali ke pilihan awal")
            input_sub_menu = input("Pilih Menu :")
            if input_sub_menu == "1":
                get_product(list_product)
            elif input_sub_menu == "2" : 
                search = input("Masukkan nama menu: ")
                search_product(search)
            elif input_sub_menu == "3" :
                break
            else:
                print("Menu tidak tersedia!")

    elif input_user == "2":
        print("\n Tambah Daftar Menu :")
        product_id = input("Masukkan ID produk : ")
        product_name = input("Masukkan nama produk : ")
        product_category = input("Masukkan category produk : ")
        product_stock = int(input("Masukkan stock produk : "))
        product_price = int (input ("Masukkan harga produk : "))
        product_total_sold = int (input ("Masukkan total produk yang sudah terjual : "))
        create_menu(product_id, product_name, product_category, product_stock, product_price, product_total_sold)
        
        
    elif input_user == "3":
        
        product_id = input("Masukkan ID produk : ")
        update_menu(product_id)
        get_product(list_product)
    elif input_user == "4":
        delete(list_product)
    elif input_user == "5":
        buy_item(list_product, cart)
    elif input_user == "6":
        report(list_product)
    elif input_user == "7":
        running = False
    else:
            print("Input is not valid !")


