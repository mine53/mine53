# Boş bir liste oluşturulması
todo_list = []

# Yapılacakları listeleme fonksiyonu
def listele():
    print("Yapılacaklar Listesi:")
    if not todo_list:
        print("Liste boş.")
    else:
        for index, item in enumerate(todo_list):
            print(f"{index + 1}. {item}")

# Yapılacak eklemek için fonksiyon
def ekle(item):
    todo_list.append(item)
    print(f"'{item}' eklendi.")

# Yapılacak silmek için fonksiyon
def sil(index):
    if 0 <= index < len(todo_list):
        item = todo_list.pop(index)
        print(f"'{item}' silindi.")
    else:
        print("Geçersiz indeks.")

# Ana döngü
while True:
    print("\nYapılacaklar Listesi Uygulaması")
    print("1. Listele")
    print("2. Ekle")
    print("3. Sil")
    print("4. Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == '1':
        listele()
    elif secim == '2':
        item = input("Yapılacak öğe: ")
        ekle(item)
    elif secim == '3':
        index = int(input("Silmek istediğiniz öğenin indeksi: ")) - 1
        sil(index)
    elif secim == '4':
        print("Uygulamadan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")

