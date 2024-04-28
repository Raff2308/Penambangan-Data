import streamlit as st  # Mengimpor modul Streamlit dengan alias 'st'
import pandas as pd  # Mengimpor modul pandas dengan alias 'pd'
import joblib  # Mengimpor modul joblib untuk penggunaan model yang disimpan
from sklearn.preprocessing import LabelEncoder  # Mengimpor LabelEncoder dari modul preprocessing di sklearn

model = joblib.load("Rafi.joblib")  # Memuat model yang telah disimpan dengan nama "Rafi.joblib"

mapped_data = pd.read_csv("Transformed Data Set - Sheet1.csv")  # Membaca data dari file CSV yang telah diubah dan menyimpannya dalam DataFrame mapped_data
st.title("Halo")  # Menampilkan judul "Halo" pada aplikasi Streamlit

label_encoders = {}  # Membuat kamus kosong untuk menyimpan objek LabelEncoder
for column in mapped_data.columns:  # Looping melalui setiap kolom dalam mapped_data
    le = LabelEncoder()  # Membuat objek LabelEncoder baru
    mapped_data[column] = le.fit_transform(mapped_data[column])  # Mengubah nilai dalam kolom menjadi nilai terenkripsi menggunakan LabelEncoder
    label_encoders[column] = le  # Menyimpan objek LabelEncoder dalam kamus label_encoders dengan nama kolom sebagai kunci

color_op = ['Cool', 'Neutral', 'Warm']  # Daftar pilihan warna
music_genre_op = ['Rock', 'Hip hop', 'Folk/Traditional', 'Jazz/Blues', 'Pop', 'Electronic', 'R&B and soul']  # Daftar pilihan genre musik
beverage_op = ['Vodka', 'Wine', 'Whiskey', "Doesn't drink", 'Beer', 'Other']  # Daftar pilihan minuman beralkohol
soft_drink_op = ['7UP/Sprite', 'Coca Cola/Pepsi', 'Fanta', 'Other']  # Daftar pilihan minuman ringan

color_map = {'Cool': 1, 'Neutral': 2, 'Warm': 3}  # Pemetaan nilai numerik untuk warna
music_genre_map = {'Rock': 1, 'Hip hop': 2, 'Folk/Traditional': 3, 'Jazz/Blues': 4, 'Pop': 5, 'Electronic': 6, 'R&B and soul': 7}  # Pemetaan nilai numerik untuk genre musik
beverage_map = {'Vodka': 1, 'Wine': 2, 'Whiskey': 3, "Doesn't drink": 4, 'Beer': 5, 'Other': 6}  # Pemetaan nilai numerik untuk minuman beralkohol
soft_drink_map = {'7UP/Sprite': 1, 'Coca Cola/Pepsi': 2, 'Fanta': 3, 'Other': 4}  # Pemetaan nilai numerik untuk minuman ringan

favorite_color = st.selectbox('Favorite Color', ['Select'] + color_op)  # Menampilkan dropdown dengan pilihan warna
favorite_music_genre = st.selectbox('Favorite Music Genre', ['Select'] + music_genre_op)  # Menampilkan dropdown dengan pilihan genre musik
favorite_beverage = st.selectbox('Favorite Beverage', ['Select'] + beverage_op)  # Menampilkan dropdown dengan pilihan minuman beralkohol
favorite_soft_drink = st.selectbox('Favorite Soft Drink', ['Select'] + soft_drink_op)  # Menampilkan dropdown dengan pilihan minuman ringan

if st.button('Predict'):  # Menjalankan blok kode jika tombol 'Predict' ditekan
    if favorite_color != 'Select' and favorite_music_genre != 'Select' and favorite_beverage != 'Select' and favorite_soft_drink != 'Select':  # Memeriksa apakah semua dropdown telah dipilih
        favorite_color_numeric = color_map[favorite_color]  # Mengonversi warna favorit menjadi nilai numerik
        favorite_music_genre_numeric = music_genre_map[favorite_music_genre]  # Mengonversi genre musik favorit menjadi nilai numerik
        favorite_beverage_numeric = beverage_map[favorite_beverage]  # Mengonversi minuman beralkohol favorit menjadi nilai numerik
        favorite_soft_drink_numeric = soft_drink_map[favorite_soft_drink]  # Mengonversi minuman ringan favorit menjadi nilai numerik

        prediction = model.predict([[favorite_color_numeric, favorite_music_genre_numeric, favorite_beverage_numeric, favorite_soft_drink_numeric]])[0]  # Melakukan prediksi menggunakan model yang telah diload

        st.write(f"Predicted Gender: {prediction}")  # Menampilkan hasil prediksi
    else:
        st.write("Please select values for all features.")  # Menampilkan pesan jika tidak semua dropdown dipilih
