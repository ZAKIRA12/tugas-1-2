kamus = {
"rumah" :"yaitu terbuat dari berbagai macam bahan,tergantung dari lokasi,budaya,dan ketersediaan materi",
"kasur" :"yaitu terbuat dari berbagai macam bahan,baik tradisional maupun moderen",
"tas"   :"yaitu terbuat dari biasa terbuat dariberbagai macam bahan baik yang alami maupun sintetis",
"bantal":"yaitu terbuat dari berbagai macam bahan,yaitu kapuk,bulu angsa,lateks,",
"lampu ":"yaitu terbuat dari berbagai macam yaitu kaca,filamen,gas inert, soket"
    }

    
kata = input("Masukkan benda yang ingin di cari bahan pembuatannya: ").lower()

    
if kata in kamus:
        print(f"Bahan dari {kata} {kamus[kata]}")
else:
        print(f"Maaf, bahan dari {kata} tidak ditemukan dalam kamus.")

