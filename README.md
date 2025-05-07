# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

**Jaya Jaya Institut**, sebuah perguruan tinggi yang didirikan pada tahun 2000, telah lebih dari dua puluh tahun menghasilkan lulusan berprestasi di berbagai bidang. Namun, layaknya banyak lembaga pendidikan lainnya, institusi ini dihadapkan pada tantangan besar berupa tingginya angka putus studi atau dropout siswa.

Permasalahan dropout merupakan isu krusial bagi sebuah institusi pendidikan. Angka putus studi yang tinggi tidak hanya mencederai reputasi lembaga dan menurunkan persentase kelulusan, tetapi juga dapat mengurangi daya tarik bagi calon mahasiswa di masa depan. Selain itu, tingginya dropout sering kali mencerminkan adanya kendala mendasar dalam seleksi penerimaan, proses pembelajaran, maupun dukungan akademik yang disediakan oleh institusi.

### Permasalahan Bisnis

Jaya Jaya Institut menghadapi tantangan dalam mengurangi angka putus studi (dropout) di kalangan mahasiswanya. Pertanyaan kunci yang perlu dijawab meliputi: bagaimana cara mengidentifikasi sejak dini mahasiswa yang berisiko melakukan dropout; faktor‑faktor apa saja yang paling berperan dalam keputusan mereka untuk berhenti studi; serta strategi apa yang efektif untuk meningkatkan retensi dan memastikan lebih banyak mahasiswa menyelesaikan program pendidikan mereka.

### Cakupan Proyek

Proyek ini akan dimulai dengan analisis data, memanfaatkan data historis dan demografis mahasiswa untuk menemukan variabel‑variabel utama yang berhubungan dengan dropout. Selanjutnya, akan dibuat visualisasi dan pelaporan berupa dashboard interaktif untuk memantau dan mengeksplorasi faktor‑faktor tersebut secara real‑time. Akhirnya, berdasarkan temuan analisis, tim akan merumuskan rekomendasi dan intervensi konkret—seperti program pendampingan, penyesuaian kurikulum, atau kebijakan dukungan akademik—untuk menurunkan angka dropout dan meningkatkan kelulusan.

### Persiapan

Sumber data: dataset yang digunakan merupakan dataset [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance).

- Setup environment:
  ```
  conda create --name dicoding python==3.12
  ```
- Install requirements:
  ```
  pip install -r requirements.txt
  ```
- Setup metabase:
  ```
  docker pull metabase/metabase:v0.46.4
  docker run -p 3000:3000 --name metabase metabase/metabase
  ```
  Akses metabase pada http://localhost:3000/setup dan lakukan setup.
- Setup database (supabase):

  - Buat akun dan login https://supabase.com/dashboard/sign-in.
  - Buat new project
  - Copy URI pada database setting
  - Kirim dataset menggunakan sqlalchemy

  ```python
  from sqlalchemy import create_engine

  URL = "DATABASE_URL"

  engine = create_engine(URL)
  df.to_sql('dataset', engine)
  ```

## Business Dashboard

Dashboard ini dirancang untuk memberikan gambaran menyeluruh mengenai “Status” mahasiswa—apakah mereka dropout, sedang menempuh studi (enrolled), atau telah lulus (graduated). Melalui visualisasi proporsi masing‑masing kategori, tim institusi dapat memantau fluktuasi tingkat dropout secara real‑time. Dengan demikian, apabila terjadi lonjakan angka dropout, langkah‑langkah mitigasi dapat segera dirancang dan diterapkan untuk mencegah dampak lebih luas.

Lebih jauh, dashboard ini menyajikan analisis komprehensif atas berbagai faktor—seperti prestasi akademik, ketersediaan beasiswa, beban biaya pendidikan, serta latar belakang kualifikasi orang tua—yang berpengaruh pada keputusan mahasiswa untuk berhenti studi. Dengan memahami kekuatan dan arah pengaruh tiap variabel, institusi dapat merumuskan kebijakan dan intervensi yang lebih tepat sasaran, misalnya program pendampingan bagi mahasiswa berisiko tinggi atau penyesuaian skema beasiswa, sehingga upaya peningkatan retensi menjadi lebih efektif.

## Menjalankan Sistem Machine Learning

Dalam proyek ini, sebuah prototipe telah disiapkan untuk melakukan prediksi menggunakan model yang telah dilatih.

- **Menjalankan secara lokal**
  Buka terminal pada direktori proyek, kemudian ketik:

  ```bash
  streamlit run app.py
  ```

- **Akses melalui web**
  Silakan buka prototipe langsung di [tautan ini](https://dicoding-permasalahan-insitusi-pendidikan-fr5ke8tglqb7weakkcic.streamlit.app/).

## Conclusion

Proyek ini bertujuan mengatasi permasalahan tingginya angka putus studi di Jaya Jaya Institut. Berikut rangkuman temuan dan rekomendasi:

Untuk mengidentifikasi sejak dini siswa yang berisiko dropout, kami mengembangkan model prediktif—misalnya menggunakan algoritma Decision Tree—yang memanfaatkan data historis serta variabel demografis, akademik, dan ekonomi. Model ini mampu mengenali pola­–pola risiko dengan akurasi memadai, sehingga institusi dapat melakukan intervensi lebih awal.

Analisis lebih lanjut terhadap korelasi dan pentingnya fitur dalam model menunjukkan bahwa latar belakang akademik (seperti nilai rata‑rata dan beban unit per semester) serta kondisi ekonomi (misalnya status beasiswa atau displacement) menjadi faktor penentu dalam keputusan siswa untuk berhenti studi. Contohnya, mahasiswa yang mengalami kesulitan akademik pada semester pertama atau kedua memiliki probabilitas lebih tinggi untuk dropout.

Berdasarkan wawasan tersebut, Jaya Jaya Institut dapat meningkatkan retensi mahasiswa melalui beberapa strategi: memperkuat program bimbingan akademik sejak dini, menyederhanakan kurikulum untuk mengurangi beban studi, serta menambah dukungan finansial bagi mereka yang membutuhkan. Dengan intervensi yang tepat sasaran dan berbasis data, diharapkan lebih banyak mahasiswa akan menyelesaikan pendidikan mereka.

### Rekomendasi Action Items

Berikut beberapa rekomendasi langkah konkret yang dapat diambil institusi untuk mengatasi masalah dropout dan mencapai target retensi:

Institusi sebaiknya mengimplementasikan sistem pemantauan siswa berbasis data. Dengan mengintegrasikan model prediktif ke dalam proses pemantauan rutin, tim akademik dapat mengidentifikasi mahasiswa berisiko tinggi mengalami dropout lebih awal. Begitu terdeteksi, intervensi seperti bimbingan akademik intensif atau dukungan lainnya dapat segera diberikan untuk mencegah putus studi.

Selanjutnya, perlu dikembangkan program dukungan akademik dan psikologis yang lebih komprehensif. Berdasarkan faktor‑faktor risiko yang telah diungkap, institusi dapat memperluas akses ke layanan bimbingan belajar, menyediakan sesi konseling reguler, serta menawarkan dukungan kesehatan mental bagi siswa yang rentan. Pendekatan holistik ini membantu mahasiswa mengatasi hambatan non‑akademik yang sering kali memicu keputusan untuk dropout.

Terakhir, evaluasi dan optimalisasi kurikulum serta metode pengajaran layak diprioritaskan, terutama pada program studi dengan angka dropout tinggi. Penyesuaian bisa berupa penambahan fleksibilitas dalam penjadwalan mata kuliah, penyediaan materi pendukung ekstra, atau inovasi dalam metode penyampaian pembelajaran. Langkah‑langkah ini akan mengurangi beban akademik siswa dan meningkatkan keterlibatan mereka dalam proses belajar.
