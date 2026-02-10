import pandas as pd
from collections import Counter

# Baca data
df = pd.read_excel("data_kuesioner.xlsx")
pertanyaan = df.iloc[:, 1:]          # Q1–Q17
semua_jawaban = pertanyaan.values.flatten()
total_respon = semua_jawaban.size
jumlah_responden = len(df)

# Frekuensi global
counter = Counter(semua_jawaban)

# Skor
skor = {
    "SS": 6,
    "S": 5,
    "CS": 4,
    "CTS": 3,
    "TS": 2,
    "STS": 1
}

target_question = input()


if target_question == "q1":
    # Pada kusioner dari keseluruhan data, skala mana yang paling banyak dipilih oleh partisipan? sertakan jumlah dan persen
    # Contoh Jawaban: CS|500|70.1
    if target_question == "q1":
        skala = max(counter, key=counter.get)
        jumlah = counter[skala]
        persen = jumlah / total_respon * 100
        print(f"{skala}|{jumlah}|{persen:.1f}")

elif target_question == "q2":
    # Pada kusioner dari keseluruhan data, skala mana yang paling sedikit dipilih oleh partisipan? sertakan jumlah dan persen
    # Contoh Jawaban: TS|1|1.1
        skala = min(counter, key=counter.get)
        jumlah = counter[skala]
        persen = jumlah / total_respon * 100
        print(f"{skala}|{jumlah}|{persen:.1f}")


elif target_question == "q3":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala SS (Sangat Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
        target = "SS"
        hasil = {c: (pertanyaan[c] == target).sum() for c in pertanyaan.columns}
        q = max(hasil, key=hasil.get)
        print(f"{q}|{hasil[q]}|{hasil[q]/jumlah_responden*100:.1f}")

elif target_question == "q4":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala S (Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
        target = "S"
        hasil = {c: (pertanyaan[c] == target).sum() for c in pertanyaan.columns}
        q = max(hasil, key=hasil.get)
        print(f"{q}|{hasil[q]}|{hasil[q]/jumlah_responden*100:.1f}")

elif target_question == "q5":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala CS (Cukup Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
        target = "CS"
        hasil = {c: (pertanyaan[c] == target).sum() for c in pertanyaan.columns}
        q = max(hasil, key=hasil.get)
        print(f"{q}|{hasil[q]}|{hasil[q]/jumlah_responden*100:.1f}")

elif target_question == "q6":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala CTS (Cukup Tidak Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
        target = "CTS"
        hasil = {c: (pertanyaan[c] == target).sum() for c in pertanyaan.columns}
        q = max(hasil, key=hasil.get)
        print(f"{q}|{hasil[q]}|{hasil[q]/jumlah_responden*100:.1f}")

elif target_question == "q7":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala TS (Tidak Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
        target = "TS"
        hasil = {c: (pertanyaan[c] == target).sum() for c in pertanyaan.columns}
        q = max(hasil, key=hasil.get)
        print(f"{q}|{hasil[q]}|{hasil[q]/jumlah_responden*100:.1f}")

elif target_question == "q8":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang pilihan skala TS (Tidak Setuju) paling banyak? sertakan jumlah dan persen
    # Contoh Jawaban: Q2|30|34.4
        target = "STS"
        hasil = {c: (pertanyaan[c] == target).sum() for c in pertanyaan.columns}
        q = max(hasil, key=hasil.get)
        print(f"{q}|{hasil[q]}|{hasil[q]/jumlah_responden*100:.1f}")

elif target_question == "q9":
    # Pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana saja yang terdapat memilih skala STS (Sangat Tidak Setuju)? sertakan jumlah dan persen
    # Contoh Jawaban: Q1:0.1|Q2:0.2|Q3:0.1
        hasil = []
        for c in pertanyaan.columns:
            j = (pertanyaan[c] == "STS").sum()
            if j > 0:
                hasil.append(f"{c}:{j/jumlah_responden*100:.1f}")
        print("|".join(hasil))

elif target_question == "q10":
    # Jika skala skor untuk masing masing skala adalah 6, 5, 4, 3, 2, 1 untuk SS, S, CS, CTS, TS, STS
    # Berapa skor rata-rata keseluruhan pertanyaan?
    # Contoh Jawaban: 5.60
        total = sum(skor[j] for j in semua_jawaban)
        print(f"{total/total_respon:.2f}")

elif target_question == "q11":
    # Jika skala skor untuk masing masing skala adalah 6, 5, 4, 3, 2, 1 untuk SS, S, CS, CTS, TS, STS
    # Maka pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang memiliki skor rata-rata tertinggi?
    # Contoh Jawaban: Q1:5.60
        rata = pertanyaan.replace(skor).infer_objects(copy=False).mean()
        q = rata.idxmax()
        print(f"{q}:{rata[q]:.2f}")

elif target_question == "q12":
    # Jika skala skor untuk masing masing skala adalah 6, 5, 4, 3, 2, 1 untuk SS, S, CS, CTS, TS, STS
    # Maka pada kusioner dari pertanyaan Q1 sampai Q17, pertanyaan mana yang memiliki skor rata-rata terendah?
    # Contoh Jawaban: Q2:3.60
        rata = pertanyaan.replace(skor).infer_objects(copy=False).mean()
        q = rata.idxmin()
        print(f"{q}:{rata[q]:.2f}")

elif target_question == "q13":
    # Jika skala di kategorikan menjadi positif (SS dan S), netral (CS) dan negatif (CTS, TS dan STS)
    # Maka hitung jumlah responden dan persentase masing-masing kategori
    # Contoh Jawaban: positif=1000:80.1|netral=200:10.1|negatif=200:100.2
        positif = sum(j in ["SS", "S"] for j in semua_jawaban)
        netral = sum(j == "CS" for j in semua_jawaban)
        negatif = sum(j in ["CTS", "TS", "STS"] for j in semua_jawaban)

        print(
            f"positif={positif}:{positif/total_respon*100:.1f}|"
            f"netral={netral}:{netral/total_respon*100:.1f}|"
            f"negatif={negatif}:{negatif/total_respon*100:.1f}"
        )