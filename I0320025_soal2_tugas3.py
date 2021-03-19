#Membuat dictionary biodata
dict = {"Nama":"Desyana Ratna Pinasthi",
        "Hobi":["Menggambar","Membaca komik","Mendengarkan musik"],
        "Sosial media":["Twitter:desyaa_rtn","Instagram:desyaa_rtn","Facebook:Desyana Chichi"],
        "Lagu favorit":["Rewrite The Stars","Utakata Hanabi","Dynamite"],
        "Makanan favorit":["mie ayam","kwetiau","Kebab"],
        }
print(dict)

#Mengubah dictionary hobi dan sosmed
dict["Hobi"][1]=("Menulis cerita")
dict["Sosial media"][2]=("Line:desyaartn")

#Menghapus 2 makanan favorit
del dict["Makanan favorit"][0:2]

#Menambahkan hobi
dict["Hobi"].append("Menonton film")

#Menampilkan dictionary terbaru
print(dict)
