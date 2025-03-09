import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime

# Data film berdasarkan genre
movies = {
    "Horror": [
("The Conjuring", 
 "Pasangan paranormal Ed dan Lorraine Warren dipanggil untuk membantu keluarga Perron yang dihantui roh jahat di rumah mereka. "
 "Saat menyelidiki, mereka menemukan sejarah gelap rumah tersebut yang penuh dengan kejadian-kejadian supranatural yang mengerikan. "
 "Semakin dalam mereka menggali, semakin besar bahaya yang mengancam keselamatan mereka dan keluarga tersebut. "
 "Dikelilingi oleh teror dan entitas jahat yang tak terlihat, mereka harus berjuang melawan kekuatan gelap yang mengancam nyawa mereka.")
,

        ("Get Out", 
 "Seorang pria muda bernama Chris mengunjungi keluarga pacarnya yang tampaknya sempurna, namun segera ia merasa ada yang aneh. "
 "Saat ia mulai menggali lebih dalam, ia menyadari bahwa ada sesuatu yang sangat salah dengan keluarga pacarnya, "
 "dan mereka menyembunyikan rahasia kelam yang berbahaya. "
 "Dengan ketegangan yang terus meningkat, Chris harus berjuang untuk melarikan diri dari situasi yang semakin mengerikan, "
 "sementara ia berhadapan dengan kenyataan mengerikan yang mengungkapkan sisi gelap dari rasisme yang tersembunyi. "
 "Apakah Chris akan berhasil keluar sebelum terlambat, ataukah ia terjebak dalam perangkap yang lebih besar dari yang ia duga?")
,
        ("A Quiet Place", 
 "Di dunia yang hancur setelah serangan makhluk menyeramkan yang berburu dengan pendengaran super tajam, satu-satunya cara untuk bertahan hidup adalah tetap diam. "
 "Keluarga Abbott hidup dalam keheningan mutlak, berkomunikasi hanya dengan isyarat dan bergerak perlahan untuk menghindari perhatian makhluk yang siap menyerang jika ada suara. "
 "Namun, saat mereka mendekati kelahiran anak kedua, mereka menyadari bahwa keheningan tidak hanya menjadi cara untuk bertahan hidup, "
 "tetapi juga bisa menjadi akhir dari segalanya. "
 "Akankah mereka dapat melindungi diri dan anak-anak mereka dalam dunia yang penuh ancaman ini, ataukah suara terakhir mereka akan menjadi pembawa malapetaka?")
,
        ("Hereditary", 
 "Sebuah film horor psikologis yang mencekam, di mana keluarga Graham harus menghadapi warisan gelap yang mereka warisi, "
 "setelah kehilangan nenek mereka yang misterius. Ketika misteri keluarga terungkap, teror yang tidak terduga mulai menghantui mereka. "
 "Keberadaan kekuatan jahat yang melibatkan ibu dan anak mereka membentuk konspirasi yang menakutkan. "
 "Apakah mereka dapat melarikan diri dari nasib yang sudah digariskan, ataukah mereka akan dihancurkan oleh kegelapan masa lalu?"),

("The Shining", 
 "Seorang penulis yang kehilangan akal sehatnya setelah terisolasi bersama keluarganya di sebuah hotel yang sudah lama kosong. "
 "Kehidupan mereka menjadi semakin berbahaya saat hotel itu mengungkapkan sisi gelapnya, dan sebuah kekuatan supernatural mulai mengendalikan si penulis. "
 "Misteri dan ketakutan menggulung dalam alur cerita yang mengarah pada kekacauan yang tidak bisa dihindari. "
 "Apakah keluarganya bisa bertahan hidup, ataukah mereka akan jatuh dalam perangkap kegilaan yang merenggut nyawa?"),

("It", 
 "Badut pembunuh yang menakutkan muncul setiap 27 tahun di kota kecil Derry, mengincar anak-anak dengan cara yang paling mengerikan. "
 "Sekelompok anak muda harus menghadapi ketakutan terburuk mereka, serta keberanian yang belum pernah mereka rasakan, "
 "untuk menghentikan teror badut itu. Namun, seiring mereka semakin dekat dengan kebenaran, mereka menyadari bahwa musuh yang mereka hadapi jauh lebih besar dari yang mereka bayangkan. "
 "Apakah mereka mampu mengalahkan 'It', ataukah mereka akan menjadi korban berikutnya?"),

("The Exorcist", 
 "Seorang gadis muda yang dirasuki oleh setan menyebabkan teror luar biasa di sekitarnya. Keluarga dan orang-orang terdekatnya terperangkap dalam situasi yang tidak bisa mereka jelaskan. "
 "Dengan bantuan seorang pendeta yang berani, mereka berusaha melakukan ritual pengusiran setan yang sangat berbahaya. "
 "Namun, saat kekuatan jahat semakin kuat, mereka harus menghadapi pertaruhan terbesar dalam hidup mereka. "
 "Akankah pengusiran itu berhasil, ataukah kegelapan yang ada di dalam gadis itu akan menghancurkan segalanya?"),

("The Witch", 
 "Di New England abad ke-17, sebuah keluarga Puritan yang tinggal di pinggiran hutan terisolasi mulai mengalami kejadian-kejadian aneh dan mengerikan. "
 "Setelah anak bungsu mereka hilang, mereka mulai merasakan adanya kekuatan jahat yang mengintai mereka di balik keheningan hutan. "
 "Dalam ketegangan dan ketakutan, mereka harus bertahan hidup dan mencoba untuk memahami apa yang sedang terjadi. "
 "Namun, semakin mereka menggali, semakin mereka terperangkap dalam ritual-ritual yang lebih mengerikan dari yang mereka bayangkan."),

("Midsommar", 
 "Sebuah keluarga muda pergi ke Swedia untuk merayakan festival musim panas yang tampaknya indah, hanya untuk menemukan bahwa ada sesuatu yang lebih gelap di balik tradisi yang mereka ikuti. "
 "Saat mereka semakin mendalami ritual-ritual yang dilakukan oleh masyarakat setempat, mereka menyadari bahwa mereka sedang berhadapan dengan kekuatan yang tidak dapat mereka hentikan. "
 "Semakin malam semakin mencekam, dan mereka terjebak dalam ketakutan yang tidak bisa mereka hindari. "
 "Apakah mereka bisa melarikan diri, atau apakah mereka akan menjadi bagian dari sesuatu yang lebih besar dan lebih mengerikan?"),

("Us: Horor", 
 "Keluarga Wilson pergi berlibur ke pantai, hanya untuk bertemu dengan doppelganger mereka sendiri, yang ternyata bukan hanya memiliki penampilan yang mirip, "
 "tetapi juga membawa teror besar ke dalam hidup mereka. Ketakutan dan ketegangan meningkat saat mereka berjuang untuk bertahan hidup, "
 "dan sebuah rahasia mengerikan terungkap mengenai apa yang sebenarnya terjadi pada keluarga mereka. "
 "Akankah mereka bisa mengalahkan musuh mereka sendiri, ataukah mereka akan terperangkap dalam kegelapan yang tidak mereka pahami?"),

("Pengabdi Setan", 
     "Kisah keluarga yang hidupnya berubah drastis setelah sang ibu meninggal dunia akibat penyakit misterius. "
     "Setelah kematiannya, mereka mulai mengalami kejadian-kejadian aneh dan menyeramkan di rumah mereka. "
     "Ternyata, sang ibu memiliki hubungan dengan sekte misterius yang membuat seluruh keluarga menjadi target kutukan. "
     "Dalam perjuangan melawan kekuatan gelap yang terus mengintai, apakah mereka akan mampu bertahan hidup ataukah mereka akan menjadi korban ritual mengerikan?"),

("Sebelum Iblis Menjemput", 
     "Setelah ayah mereka jatuh sakit karena terlibat dalam perjanjian gelap, Alfie dan saudara tirinya, Maya, kembali ke villa tua keluarga untuk mencari jawaban. "
     "Namun, mereka malah memicu kekuatan iblis yang menghantui tempat itu. "
     "Mereka harus menghadapi kengerian yang tak terduga dan membongkar rahasia kelam yang melibatkan keluarga mereka. "
     "Dengan ancaman iblis yang semakin kuat, apakah mereka mampu keluar hidup-hidup ataukah terperangkap dalam neraka dunia?"),

        ],
    #DAFTAR FILM KOMEDY 
    "Comedy": [
        ("The Hangover", 
 "Setelah pesta bujangan yang liar di Las Vegas, sekelompok teman terbangun tanpa ingatan tentang apa yang terjadi semalam. "
 "Mereka harus mencari petunjuk untuk menemukan pengantin pria yang hilang dan menghadapi serangkaian kejadian kocak yang membuat mereka semakin bingung. "
 "Apa yang sebenarnya terjadi di malam itu? Akankah mereka berhasil mengingat segalanya sebelum semuanya terlambat?"),

("Bridesmaids", 
 "Saat sahabat terbaiknya mempersiapkan pernikahan, Annie terjebak dalam persaingan tak terduga dengan pengiring pengantin lainnya. "
 "Dari momen kocak hingga konflik tak terhindarkan, Annie berjuang untuk menjadi pengiring pengantin yang sempurna sambil menghadapi kehidupan pribadi yang berantakan. "
 "Akankah dia bisa menghadapi tekanan pernikahan atau malah membuat segalanya menjadi kacau?"),

("Jumanji", 
 "Empat remaja menemukan sebuah permainan papan misterius yang membawa mereka ke dalam dunia petualangan penuh bahaya dan kejutan. "
 "Setiap langkah dalam permainan membawa mereka semakin dalam ke dunia yang lebih gila, dan mereka harus menyelesaikan misi untuk kembali ke dunia nyata. "
 "Akankah mereka berhasil bertahan hidup dan keluar dari permainan, ataukah mereka terjebak selamanya?"),

("The Big Lebowski", 
 "Seorang pria malas bernama Jeffrey Lebowski, yang dikenal sebagai 'The Dude', terjebak dalam sebuah intrik yang rumit setelah kesalahan identitas. "
 "Dengan bantuan teman-temannya yang eksentrik, ia mencoba memecahkan masalah yang semakin membingungkan. "
 "Keanehan demi keanehan terus muncul dalam perjalanan 'The Dude' yang tidak pernah terduga, mengarah pada petualangan yang absurd dan kocak."),

("Superbad", 
 "Dua sahabat remaja, Seth dan Evan, berusaha keras untuk kehilangan keperawanan mereka sebelum lulus SMA. "
 "Namun, berbagai masalah dan kejadian lucu muncul di sepanjang perjalanan mereka untuk mencapai tujuan tersebut. "
 "Bisakah mereka berhasil atau malah terjebak dalam situasi yang semakin absurd?"),

("Mean Girls", 
 "Film komedi yang mengungkap kehidupan sosial di sekolah menengah, di mana Cady Heron, seorang gadis baru, harus menghadapi geng populer yang dikenal sebagai 'The Plastics'. "
 "Melalui drama, persahabatan, dan persaingan, Cady belajar tentang dinamika sosial yang rumit, dan bagaimana keputusannya bisa mengubah hidupnya selamanya. "
 "Apakah dia akan menjadi bagian dari 'Plastics', ataukah dia akan menentang sistem tersebut?"),

("Cek Toko Sebelah", 
     "Erwin, seorang pekerja kantoran sukses, mendapati dirinya terjebak dalam konflik keluarga saat ayahnya, Koh Afuk, "
     "memintanya untuk mengambil alih toko kelontong keluarga. Sementara itu, kakaknya, Yohan, merasa tidak dihargai "
     "karena tidak dipercaya untuk mengelola toko. Film ini mengisahkan dilema keluarga dengan bumbu komedi dan sentuhan emosional."),

    ("Cek Toko Sebelah 2", 
     "Dalam sekuelnya, Erwin sedang mempersiapkan pernikahan dengan Natalie, tetapi menemui banyak tantangan dari keluarga Natalie, "
     "khususnya ayahnya yang perfeksionis. Di sisi lain, Yohan dan istrinya, Ayu, menghadapi tekanan untuk memiliki anak. "
     "Film ini mengangkat isu hubungan keluarga dan pernikahan dengan gaya humor khas Ernest Prakasa."),

    ("Warkop DKI Reborn", 
     "Mengisahkan Dono, Kasino, dan Indro yang bekerja sebagai agen rahasia untuk misi memecahkan sebuah kasus besar. "
     "Namun, mereka malah terjebak dalam berbagai kekacauan dan situasi lucu. Film ini merupakan adaptasi modern dari kisah klasik Warkop DKI, "
     "dengan nuansa nostalgia yang kental."),

    ("Shaun of the Dead", 
     "Film komedi zombie yang unik, di mana Shaun dan teman-temannya berusaha bertahan hidup di tengah wabah zombie yang tiba-tiba muncul. "
     "Namun, mereka tidak hanya berjuang untuk bertahan hidup, tetapi juga menghadapi masalah kehidupan pribadi yang harus mereka selesaikan. "
     "Akankah mereka dapat menyelamatkan dunia, ataukah mereka akan menjadi bagian dari 'zombie' itu sendiri?"),
    
    ("Susah Sinyal", 
     "Ellen, seorang pengacara sukses, berusaha memperbaiki hubungannya dengan anak perempuannya, Kiara, "
     "yang merasa diabaikan. Dalam perjalanan liburan mereka ke Sumba, mereka menghadapi berbagai situasi lucu "
     "dan menyentuh yang menguji hubungan keluarga mereka. Akankah mereka bisa menemukan kembali kedekatan mereka?"),

    ("Yowis Ben", 
     "Bayu, seorang siswa SMA yang naksir dengan teman sekolahnya, Susan, memutuskan untuk membentuk sebuah band bersama teman-temannya "
     "untuk mendapatkan perhatian Susan. Namun, perjuangan mereka di dunia musik menghadirkan berbagai tantangan lucu dan penuh warna. "
     "Bisakah Bayu mencapai mimpinya, baik dalam cinta maupun musik?")

    ],
    #daftar film action
    "Action": [
        ("G.I. Joe: Retaliation", 
 "Ketika tim G.I. Joe dijebak atas kejahatan yang tidak mereka lakukan, mereka diserang oleh pasukan militer AS yang dikendalikan oleh organisasi Cobra. "
 "Hanya segelintir anggota yang selamat, termasuk Roadblock, yang harus memimpin misi balas dendam untuk membersihkan nama mereka dan menghentikan Cobra dari menguasai dunia. "
 "Dengan bantuan General Joe Colton, mereka menghadapi musuh yang lebih kuat dan lebih licik dari sebelumnya. "
 "Di tengah ledakan aksi dan pertempuran mematikan, film ini menyuguhkan drama tentang kepercayaan, pengorbanan, dan pentingnya kekompakan tim. "
 "Apakah G.I. Joe mampu menggagalkan rencana Cobra yang berbahaya dan memulihkan kehormatan mereka, atau akankah dunia tunduk pada kekuatan jahat?"),

("Mad Max: Fury Road", 
 "Aksi pasca-apokaliptik yang spektakuler. Di dunia pasca-apokaliptik yang tandus, Max, seorang pria yang kehilangan segalanya, bergabung dengan Imperator Furiosa dalam pelarian dari penguasa tirani Immortan Joe. "
 "Mereka melakukan perjalanan melewati gurun, melawan pasukan Immortan Joe yang ganas. "
 "Akan kah mereka berhasil melarikan diri, atau akankah mereka terjebak dalam dunia yang dipenuhi kekacauan dan keputusasaan?"),

("Spider-Man: No Way Home (2021)", 
 "Ketika identitas Peter Parker sebagai Spider-Man terungkap kepada dunia, hidupnya berubah menjadi kacau. "
 "Dituduh sebagai pembunuh Mysterio, Peter menghadapi tekanan besar yang memengaruhi kehidupan pribadinya, teman-temannya, dan keluarganya. "
 "Untuk memperbaiki segalanya, ia meminta bantuan Doctor Strange, tetapi mantra yang salah malah membuka multiverse, membawa musuh dari dunia lain masuk ke dunianya. "
 "Dihadapkan pada tantangan terbesar dalam hidupnya, Peter bertemu dengan Spider-Man dari dimensi lain, bekerja sama untuk menghentikan musuh seperti Green Goblin, Doc Ock, dan Electro. "
 "Apakah Peter mampu mengembalikan segalanya ke tempat semula tanpa kehilangan lebih banyak hal yang ia cintai?"),

("The Matrix", 
 "Film aksi sci-fi klasik yang revolusioner. Kehidupan sehari-hari Neo tampak normal, hingga sebuah pesan misterius membuka matanya terhadap realitas yang lebih besar dari sekadar dunia digital. "
 "Dunia yang dia kenal ternyata hanyalah ilusi, dan satu-satunya cara untuk membebaskan dirinya adalah dengan bergabung dalam pemberontakan melawan mesin-mesin penguasa dunia. "
 "Dengan bantuan seorang guru legendaris, Neo harus memutuskan apakah dia benar-benar siap untuk menjalani takdir yang telah ditentukan. "
 "Dalam pertarungan antara manusia dan mesin, siapa yang akan mengendalikan masa depan? Kebenaran yang tersembunyi dalam dunia maya ini akan mengubah pandanganmu selamanya."),

("Die Hard", 
 "Aksi laga yang menegangkan dengan Bruce Willis sebagai pahlawan. John McClane, seorang polisi New York, harus menyelamatkan para sandera di sebuah gedung pencakar langit setelah sekelompok teroris mengambil alih. "
 "Dengan hanya mengandalkan keterampilan dan kecerdikan, McClane berjuang melawan mereka untuk menyelamatkan hari. "
 "Akankah dia berhasil menyelamatkan para sandera dan menghentikan teroris, ataukah dia terjebak dalam jebakan berbahaya yang mereka atur?"),

("The Raid", 
 "Aksi laga dari Indonesia yang brutal dan memukau. Dalam gedung yang penuh dengan penjahat, satu tim SWAT Indonesia terperangkap dalam misi penyelamatan yang paling brutal. "
 "Saat mereka memasuki gedung tersebut, mereka mengetahui bahwa mereka bukan hanya melawan kriminal biasa, tetapi juga menghadapi jaringan yang tak terduga dan penuh kekejaman. "
 "Dengan keterbatasan waktu dan ruang, anggota tim harus bertarung dengan nyawa mereka sendiri untuk bertahan hidup. "
 "Setiap langkah dan pertarungan semakin mencekam, membuat The Raid menjadi salah satu film laga paling brutal dan menegangkan yang pernah ada. "
 "Apakah mereka akan berhasil keluar hidup-hidup atau malah terkubur dalam darah?"),

("Mission: Impossible – Fallout", 
 "Ethan Hunt dan timnya harus menghadapi konsekuensi dari misi yang gagal dan menghadapi musuh baru yang berbahaya. "
 "Dalam mengejar ancaman yang bisa menghancurkan dunia, Hunt harus memilih antara keselamatan tim dan dunia. "
 "Apakah dia akan dapat menyelamatkan dunia atau akan terpaksa membuat pengorbanan yang lebih besar?"),

("The Dark Knight", 
 "Film superhero yang gelap dan realistis. Batman berusaha untuk mengungkap identitas Joker, seorang kriminal jenius yang ingin menciptakan kekacauan di Gotham City. "
 "Konflik ini menguji batas-batas moralitas, keadilan, dan pengorbanan. "
 "Siapa yang akan menang dalam permainan antara kebaikan dan kejahatan, Batman atau Joker, dan apa yang harus dipertaruhkan demi mencapainya?"),

        ("Black Panther", 
 "Film superhero yang merayakan budaya Afrika. T'Challa, pewaris takhta Wakanda, harus mengatasi ujian besar saat ayahnya meninggal. "
 "Sebagai Raja baru, ia harus mempertahankan kehormatan dan keamanan kerajaan yang kaya dengan "
 "teknologi canggih dan rahasia besar. Namun, muncul musuh yang mengancam masa depan Wakanda, yang "
 "membuat T'Challa harus membuat keputusan besar tentang siapa yang pantas memimpin. "
 "Dengan latar belakang budaya Afrika yang kaya, film ini menggabungkan aksi spektakuler dengan pesan "
 "yang dalam tentang identitas dan tanggung jawab. Dalam perjuangan ini, siapa yang akan menguasai "
 "Wakanda, dan apa yang harus dikorbankan untuk memastikan masa depan yang lebih baik?"),
        
        ("The Bourne Identity", 
 "Aksi mata-mata yang menegangkan. Jason Bourne terbangun dengan kehilangan ingatan "
 "tanpa mengetahui siapa dirinya atau mengapa dia menjadi sasaran pembunuh bayaran. "
 "Ketika ia mulai mencari tahu siapa yang telah mencoba membunuhnya, ia menemukan dirinya terjebak "
 "dalam konspirasi besar yang melibatkan agen pemerintah dan jaringan rahasia. "
 "Setiap langkah yang ia ambil mengarah pada penemuan yang lebih mengejutkan, dan semakin ia mencoba "
 "mengungkap kebenaran, semakin dalam ia terjebak dalam permainan berbahaya. "
 "Apakah Bourne akan berhasil menemukan identitasnya yang sebenarnya, ataukah ia justru menjadi pion "
 "dalam permainan yang lebih besar dari yang ia bayangkan?"),
        
        ("Headshot", 
     "Seorang pria misterius bernama Ishmael ditemukan dalam keadaan terluka parah dan hilang ingatan. "
     "Namun, ketika masa lalunya yang kelam mulai terungkap, ia terlibat dalam aksi penuh kekerasan untuk melindungi orang-orang yang ia sayangi. "
     "Film ini menawarkan aksi mendebarkan dengan pertarungan intens yang menguji batas kekuatan Ishmael."), 
        
        ("Serigala Terakhir", 
     "Nardo, seorang mantan gangster yang mencoba menjalani hidup damai, kembali terjebak dalam dunia kriminal saat sahabatnya dibunuh. "
     "Dalam upayanya untuk mencari keadilan, ia harus menghadapi musuh lama dan konflik internal yang semakin rumit. "
     "Film ini menggabungkan aksi brutal dengan cerita emosional yang mendalam.")
],
    
    #DAFTAR FILM DRAMA
    "Drama": [
        ("Schindler's List", "Drama sejarah tentang seorang pengusaha Jerman yang menyelamatkan nyawa ribuan orang Yahudi selama Holocaust. Di tengah kegelapan Holocaust, seorang pengusaha Jerman yang awalnya hanya mencari keuntungan, justru menemukan keberanian untuk melakukan tindakan heroik. Oskar Schindler, begitulah namanya, menyaksikan kekejaman yang tak terbayangkan terhadap orang-orang Yahudi. Tergerak oleh rasa kemanusiaan, ia membuat keputusan yang akan mengubah hidupnya selamanya: melindungi ribuan nyawa dengan cara yang tak terduga. Bisakah seorang individu benar-benar membuat perbedaan di tengah kehancuran sebuah bangsa?"),
        ("The Shawshank Redemption", "Kisah tentang seorang pria yang tidak bersalah yang dipenjara seumur hidup. Andy Dufresne, seorang bankir yang dijatuhi hukuman seumur hidup atas pembunuhan yang tidak dilakukannya, masuk ke penjara Shawshank. Di balik tembok penjara yang dingin dan keras, Andy menemukan cara untuk bertahan hidup, bahkan berkembang. Dengan kecerdasannya, ia membangun jaringan dan merencanakan pelarian yang hampir mustahil. Namun, di balik rencananya yang cerdik, tersimpan juga sebuah kisah persahabatan yang mengharukan. Bisakah Andy berhasil keluar dari neraka yang ia tempati?"),
        ("12 Angry Men", "Drama pengadilan yang menegangkan tentang 12 juri yang harus memutuskan nasib seorang remaja. Suhu di ruang sidang memanas saat 12 juri harus memutuskan nasib seorang remaja yang dituduh membunuh ayahnya. Awalnya, semua juri kecuali satu yakin akan bersalahnya terdakwa. Namun, satu per satu, keraguan mulai muncul saat mereka mendiskusikan bukti-bukti yang ada. Ketegangan dan perdebatan sengit pun tak terhindarkan. Bisakah mereka menemukan kebenaran di balik kasus ini?"),
        ("Forrest Gump", "Kisah hidup seorang pria sederhana yang mengalami peristiwa-peristiwa bersejarah. Seorang pria sederhana dengan IQ rendah, Forrest Gump, menyaksikan sejarah Amerika Serikat dari dekat. Dari masa kecilnya yang penuh tantangan hingga menjadi seorang pahlawan perang, Forrest selalu berada di tempat yang tepat pada waktu yang tepat. Melalui kisahnya yang unik, kita diajak untuk merenungkan tentang kehidupan, cinta, dan keberuntungan. Bisakah seorang pria biasa membuat dampak yang luar biasa pada dunia?"),
        ("The Green Mile", "Drama fantasi tentang seorang penjaga penjara yang bertemu dengan seorang narapidana yang memiliki kekuatan supernatural. Paul Edgecombe, seorang penjaga penjara yang baik hati, bertemu dengan seorang narapidana yang memiliki kekuatan supernatural. John Coffey, begitulah namanya, dituduh membunuh dua gadis kecil, namun Paul merasakan ada sesuatu yang berbeda pada John. Seiring berjalannya waktu, Paul menyadari bahwa John adalah orang yang tidak bersalah dan memiliki kemampuan untuk menyembuhkan orang lain. Bisakah Paul menyelamatkan John dari hukuman mati?"),
        ("The Godfather (seri)", "Drama kriminal klasik tentang keluarga mafia Italia-Amerika. Don Vito Corleone, seorang bos mafia yang karismatik, memimpin keluarganya dengan tangan besi. Kisah ini mengikuti naik turunnya keluarga Corleone dalam dunia kejahatan yang penuh intrik dan pengkhianatan. Kekuasaan, uang, dan balas dendam menjadi motif utama dalam setiap konflik yang mereka hadapi. Bisakah keluarga Corleone mempertahankan kekuasaannya di tengah persaingan yang sengit?"),
        ("The Lord of the Rings (trilogi)", "Epik fantasi tentang perjuangan melawan kekuatan jahat. Di tengah kekejaman Holocaust, seorang ayah Yahudi berusaha melindungi anaknya dari kenyataan pahit yang sedang terjadi. Dengan humor dan imajinasi, ia menciptakan sebuah dunia fantasi bagi anaknya, seolah-olah mereka sedang bermain permainan. Namun, bisakah ia terus melindungi anaknya dari kekejaman perang?"),
        ("Life is Beautiful", "Drama komedi tentang seorang ayah Yahudi yang berusaha melindungi anaknya dari kekejaman Holocaust dengan cara yang unik. Di tengah kekejaman Holocaust, seorang ayah Yahudi berusaha melindungi anaknya dari kenyataan pahit yang sedang terjadi. Dengan humor dan imajinasi, ia menciptakan sebuah dunia fantasi bagi anaknya, seolah-olah mereka sedang bermain permainan. Namun, bisakah ia terus melindungi anaknya dari kekejaman perang?"),
        ("The Notebook", 
     "Kisah cinta abadi antara Noah dan Allie, yang dimulai di musim panas saat mereka muda. "
     "Meskipun mereka berasal dari latar belakang sosial yang berbeda, cinta mereka tumbuh kuat. "
     "Namun, kehidupan dan waktu memisahkan mereka, hingga mereka harus menghadapi keputusan yang sulit untuk bersama. "
     "Dalam perjalanan hidup yang penuh emosi, apakah cinta sejati dapat bertahan melawan segalanya?"),
    
    ("Ada Apa Dengan Cinta?", 
     "Cinta, seorang remaja populer di sekolah, bertemu dengan Rangga, seorang pemuda pendiam dan penuh misteri. "
     "Pertemuan mereka memicu hubungan yang penuh konflik, persahabatan, dan romansa. "
     "Namun, perbedaan kepribadian dan situasi hidup mereka menjadi tantangan yang sulit untuk diatasi. "
     "Apakah mereka akan menemukan cara untuk bersama, ataukah perbedaan itu akan memisahkan mereka?"),
    
        ("The Pianist", "Drama perang tentang seorang pianis Yahudi yang berjuang untuk bertahan hidup di Warsawa yang diduduki Nazi. Wladyslaw Szpilman, seorang pianis Yahudi, harus berjuang untuk bertahan hidup di Warsawa yang diduduki Nazi. Ia menyaksikan kehancuran kota dan kehilangan orang-orang yang dicintainya. Dalam perjuangannya untuk tetap hidup, musik menjadi satu-satunya pelariannya. Bisakah ia bertahan hidup di tengah keputusasaan dan menemukan kembali semangat hidupnya?"),
        ("Parasite", "Drama Korea Selatan yang memenangkan Oscar tentang perjuangan kelas sosial. Dua keluarga dengan latar belakang sosial yang berbeda terlibat dalam sebuah permainan kucing-mengucang yang penuh intrik. Keluarga Kim, yang miskin, berhasil menyusup ke dalam kehidupan keluarga Park yang kaya raya. Namun, rahasia dan kebohongan yang terungkap mengancam untuk menghancurkan semuanya. Bisakah mereka mempertahankan kehidupan baru mereka atau harus kembali ke kenyataan yang pahit?")
    ],
    #DAFTAR FILM
    "Sci-Fi": [
    ("Interstellar", "Petualangan luar angkasa yang epik tentang pencarian rumah baru bagi umat manusia. Bayangkan sebuah dunia di ambang kehancuran. Manusia mencari harapan di bintang-bintang, dalam sebuah misi berani untuk menemukan planet yang layak huni. Namun, perjalanan melintasi galaksi ini bukan tanpa konsekuensi. Relativitas waktu yang membengkokkan, lubang hitam yang misterius, dan keputusan-keputusan sulit yang harus diambil demi kelangsungan hidup umat manusia. Apakah mereka akan menemukan rumah baru? Atau justru terjebak dalam pusaran waktu yang tak berujung?"),
    ("Blade Runner 2049", "Film noir futuristik tentang replika manusia yang mencari jati diri. Di masa depan yang dystopian, replika manusia yang hampir tak terbedakan dari manusia asli hidup dalam bayang-bayang. Seorang Blade Runner muda, dengan tugas memburu replika yang membangkang, menemukan rahasia gelap yang mengguncang fondasi eksistensinya. Saat dia menggali lebih dalam, dia menemukan bahwa garis antara manusia dan mesin semakin kabur. Siapakah dia sebenarnya? Dan apa arti menjadi manusia di dunia yang penuh dengan tiruan?"),
    ("Your Name", "Anime romantis tentang pertukaran tubuh antara seorang siswa laki-laki dan perempuan. Di sebuah desa terpencil di Jepang, seorang gadis SMA bertukar tubuh dengan seorang siswa SMA dari Tokyo. Mereka harus beradaptasi dengan kehidupan satu sama lain, menghadapi tantangan yang tak terduga, dan mencari cara untuk kembali ke tubuh masing-masing. Di tengah kebingungan dan kekacauan, mereka menemukan koneksi yang mendalam dan menyadari bahwa takdir telah mempertemukan mereka."),
    ("Eternal Sunshine of the Spotless Mind", "Romantis sci-fi tentang sepasang kekasih yang berusaha menghapus ingatan tentang satu sama lain. Sebuah prosedur medis yang memungkinkan seseorang untuk menghapus ingatan tentang orang yang dicintai. Seorang pria yang baru saja menjalani prosedur ini mulai meragukan keputusannya. Saat dia berusaha untuk melupakan mantan kekasihnya, dia justru semakin teringat akan cinta mereka. Dalam perjalanan melintasi labirin ingatannya, dia menemukan bahwa cinta sejati sulit untuk dihapus."),
    ("Inception", "Seorang pencuri yang mengkhususkan diri dalam mencuri informasi dengan memasuki mimpi orang lain ditawarkan kesempatan untuk menghapus masa lalunya dengan cara melakukan pencurian yang berbeda: menanamkan ide dalam pikiran seseorang. Namun, semakin dalam mereka menyelami mimpi, semakin sulit untuk membedakan antara mimpi dan kenyataan."),
    ("The Matrix", "Dalam dunia yang tampaknya normal, seorang programmer komputer bernama Neo menemukan bahwa realitas yang dia ketahui hanyalah simulasi buatan yang diciptakan oleh mesin untuk mengendalikan umat manusia. Bergabung dengan sekelompok pemberontak, Neo berusaha untuk membebaskan umat manusia dari cengkraman mesin dan mengguncang fondasi dunia virtual tersebut."),
    ("The Martian", "Setelah kecelakaan yang membuatnya terdampar sendirian di Mars, seorang astronot berusaha bertahan hidup dengan sumber daya terbatas. Dengan kecerdikan dan semangat juang yang tinggi, dia mencoba untuk bertahan hidup sembari mencari cara untuk berkomunikasi dengan bumi dan berharap ada yang datang menolongnya."),
    ("Arrival", "Seorang ahli bahasa dipanggil untuk membantu komunikasi dengan makhluk luar angkasa yang tiba di Bumi. Dengan tantangan bahasa yang kompleks dan waktu yang terbatas, dia mulai mengungkap kebenaran yang lebih besar yang mengubah cara pandangnya terhadap waktu, kehidupan, dan masa depan."),
    ("Minority Report", "Di masa depan, kejahatan dapat dicegah sebelum terjadi dengan menggunakan teknologi yang dapat memprediksi masa depan. Seorang petugas polisi yang bekerja di sistem ini justru dijadikan target ketika dia diprediksi akan melakukan kejahatan. Dia berusaha untuk membuktikan bahwa dia tidak bersalah dalam sebuah dunia yang sangat bergantung pada teknologi untuk menentukan nasib."),
    ("Looper", "Dalam masa depan, pembunuhan disponsori oleh mafia dan menggunakan perjalanan waktu. Seorang pembunuh bayaran yang tugasnya adalah mengeksekusi target yang dikirimkan ke masa lalu, akhirnya dihadapkan dengan masa depannya sendiri sebagai target. Sebuah cerita penuh ketegangan dan dilema moral yang membuatnya mempertanyakan siapa yang benar dan siapa yang salah."),
   ("Gravity", "Dalam petualangan luar angkasa yang menegangkan, dua astronot terdampar di luar angkasa setelah kecelakaan yang menghancurkan pesawat mereka. Dr. Ryan Stone, seorang ilmuwan medis yang pertama kali berangkat ke luar angkasa, dan Matt Kowalski, seorang astronot berpengalaman yang melakukan misi terakhirnya, terpaksa bekerja sama untuk bertahan hidup. Dengan pasokan oksigen yang semakin menipis, mereka harus mengatasi kesulitan ekstrem dan berjuang melawan kekosongan luar angkasa yang mematikan. Setiap langkah penuh dengan ketegangan, menghadapi rintangan yang tak terduga dan ancaman dari orbit yang tidak stabil. Bisakah mereka bertahan hidup dan kembali ke Bumi, atau akankah mereka terjebak selamanya di ruang angkasa?"),
    ("Snowpiercer", "Setelah dunia membeku akibat eksperimen iklim yang gagal, sisa umat manusia bertahan hidup di atas kereta api raksasa yang tak pernah berhenti. Kelas sosial yang terbentuk di dalam kereta menciptakan ketegangan yang mendorong sekelompok pemberontak untuk melawan sistem yang menindas mereka.")
]

}

# Fungsi untuk mengganti frame
def show_frame(frame):
    frame.tkraise()


# Fungsi untuk membuka FAQ
def show_faq():
    # Buat jendela baru untuk FAQ
    faq_window = tk.Toplevel()
    faq_window.title("FAQ")
    faq_window.geometry("500x600")
    faq_window.configure(bg="#f5f5f5")

    # Label judul
    tk.Label(faq_window, text="FAQ - Frequently Asked Questions", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

    # Daftar pertanyaan dan jawaban
    faqs = [
        ("Apa fungsi tombol Movie pada aplikasi ini? ",
        "Tombol Movie digunakan untuk memulai eksplorasi berbagai genre film yang tersedia di aplikasi."),
        ("Genre film apa saja yang tersedia di aplikasi ini?",
        "Aplikasi menyediakan 5 genre film, seperti, horor, komedi, aksi, drama, dan sci-fi."),
        ("Bagaimana cara memilih genre film yang ingin saya tonton?",
        "Setelah mengklik tombol Movie pilih salah satu dari 5 genre film yang tersedia di tampilan berikutnya."),
        ("Apa yang terjadi setelah saya memilih genre film?",
        "Setelah memilih genre, Anda akan diarahkan ke daftar 10 film populer dari genre tersebut."),
        ("Bagaimana cara melihat detail atau sinopsis dari sebuah film?",
        "Klik judul film yang Anda inginkan untuk melihat detail dan sinopsis singkatnya."),
        ("Apakah saya bisa melihat film dari beberapa genre sekaligus?",
        "Saat ini, Anda hanya bisa memilih satu genre film dalam satu waktu. Untuk memilih genre lain, kembali ke halaman awal."),
        ("Apa yang dimaksud dengan sinopsis di aplikasi ini?",
        "Sinopsis adalah ringkasan singkat tentang cerita dari film yang Anda pilih, yang membantu Anda memahami isi cerita sebelum menonton."),
        ("Apakah aplikasi ini menyediakan rekomendasi film terbaru?",
        "Ya, aplikasi ini memberikan daftar film populer dalam genre tertentu yang mungkin relevan dengan preferensi Anda."),
        ("Bagaimana cara kembali ke halaman awal dari detail film?",
        "Anda dapat menggunakan tombol Kembali yang tersedia di bagian atas atau bawah layar untuk kembali ke halaman awal."),
        ("Apakah aplikasi ini memungkinkan streaming langsung film?",
        "Tidak, aplikasi ini hanya memberikan informasi tentang film, seperti genre, daftar film, dan sinopsis. Streaming belum tersedia.")
    ]
    # Tampilkan FAQ
    faq_frame = tk.Frame(faq_window, bg="#f5f5f5")
    faq_frame.pack(fill="both", expand=True, padx=20, pady=10)

   # Fungsi untuk menampilkan/menghilangkan jawaban
    def toggle_answer(button, answer_label):
        if answer_label.winfo_ismapped():  # Jika label jawaban terlihat
            answer_label.pack_forget()  # Sembunyikan jawaban
            button.configure(text="➕ " + button.cget("text")[2:])  # Ubah ikon ke tambah
        else:
            answer_label.pack(fill="x", pady=5)  # Tampilkan jawaban
            button.configure(text="➖ " + button.cget("text")[2:])  # Ubah ikon ke kurang

    # Loop untuk menampilkan daftar pertanyaan
    for question, answer in faqs:
        # Tombol untuk pertanyaan
        question_button = tk.Button(
            faq_frame,
            text="➕ " + question,
            font=("Arial", 12, "bold"),
            bg="#f5f5f5",
            fg="#17a2b8",
            anchor="w",
            relief="flat",
            activebackground="#e8f0fe",
            command=lambda b=None, q=None: None  # Placeholder, akan diubah di bawah
        )
        question_button.pack(fill="x", pady=5)

        # Label untuk jawaban (awal disembunyikan)
        answer_label = tk.Label(
            faq_frame,
            text=f"ANSWER: {answer}",
            font=("Arial", 12),
            bg="#f5f5f5",
            fg="#333",
            anchor="w",
            wraplength=450
        )

        # Sambungkan tombol ke fungsi toggle_answer
        question_button.configure(command=lambda b=question_button, l=answer_label: toggle_answer(b, l))

    # Tombol untuk menutup jendela FAQ
    close_button = tk.Button(
        faq_window,
        text="Close FAQ",
        font=("Arial", 12),
        bg="#17a2b8",
        fg="white",
        activebackground="#138496",
        activeforeground="white",
        command=faq_window.destroy
    )
    close_button.pack(pady=10)


def show_movie_list(genre):
    movie_label.config(text=f"Movies in {genre}")
    
    # Hapus widget tombol film sebelumnya
    for widget in movies_list.winfo_children():
        widget.destroy()

    # Atur layout grid, ini akan mengatur tombol dalam format grid (3 kolom, 2 baris)
    row = 0
    column = 0

    # Menampilkan daftar film berdasarkan genre
    for movie, _ in movies[genre]:
        # Membuat tombol untuk setiap film
        btn = tk.Button(movies_list, text=movie, font=("Arial", 12), fg="white", bg="#FF8000",
                        activebackground="#FF8000", activeforeground="white",
                        command=lambda m=movie, g=genre: show_movie_detail(m, g))
        
        # Menempatkan tombol dalam grid dengan 3 kolom dan 2 baris
        btn.grid(row=row, column=column, pady=5, padx=5, sticky="ew")  # sticky="ew" agar tombol mengisi lebar kolom

        # Update kolom dan baris untuk layout grid
        column += 1
        if column > 2:  # Jika sudah 3 kolom, pindah ke baris berikutnya
            column = 0
            row += 1

    # Tampilkan frame yang berisi daftar film
    show_frame(frame_movies)


# Fungsi untuk menampilkan detail film
def show_movie_detail(movie, genre):
    description = next(desc for m, desc in movies[genre] if m == movie)
    movie_title_label.config(text=movie)
    movie_description_label.config(text=description)
    show_frame(frame_movie_detail)

# Inisialisasi root
root = tk.Tk()
root.title("Nonton Film")
root.geometry("800x600")
root.config(bg="#f5f5f5")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Membuat kontainer
container = tk.Frame(root, bg="#f5f5f5")
container.grid(row=0, column=0, sticky="nsew")
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Menyiapkan frame-frame
frames = {}
for F in ["main", "genre", "movies", "movie_detail"]:
    frame = tk.Frame(container, bg="#f5f5f5")
    frame.grid(row=0, column=0, sticky="nsew")
    frames[F] = frame

# Frame utama
frame_main = frames["main"]
# Mengubah warna latar belakang frame utama menjadi warna
frame_main.config(bg="#588157")

# Label pertama dengan teks putih untuk kontras
tk.Label(frame_main, text="Selamat Datang Di Nonton Film", font=("Arial", 24, "bold"), bg="#588157", fg="white").pack(pady=(20, 10))

# Label kedua untuk bagian bawah dengan teks putih untuk kontras
tk.Label(frame_main, text="Kamu bisa mendapatkan film dengan rekomendasi terbaik disini", font=("Arial", 14), bg="#588157", fg="white").pack(pady=10)

# Tombol dengan warna biru yang lebih terang saat aktif
tk.Button(frame_main, text="Movies", font=("Arial", 14), fg="white", bg="#28a745", width=20,
          activebackground="#218838", activeforeground="white", command=lambda: show_frame(frame_genre)).pack(pady=10)
# Tambahkan tombol Chatbot di frame utama
tk.Button(frame_main, text="Chatbot", font=("Arial", 14), fg="white", bg="#bb9457", width=20,
          activebackground="#138496", activeforeground="white", command=lambda: show_frame(frame_chatbot)).pack(pady=10)

tk.Button(frame_main, text="FAQ", font=("Arial", 14), fg="white", bg="#17a2b8", width=20,
          activebackground="#138496", activeforeground="white", command=show_faq).pack(pady=10)  # Menggunakan fungsi baru

tk.Button(frame_main, text="Tentang Aplikasi", font=("Arial", 14), fg="white", bg="#ffc107", width=20,
          activebackground="#e0a800", activeforeground="white", command=lambda: messagebox.showinfo("About", "Nonton Film adalah aplikasi yang dirancang untuk membantu Anda menemukan film-film menarik berdasarkan genre pilihan. Dengan antarmuka yang sederhana dan mudah digunakan, Anda dapat menjelajahi berbagai genre film, membaca sinopsis, serta mendapatkan rekomendasi film terbaik. Aplikasi ini hadir untuk memberikan pengalaman menonton yang lebih menyenangkan dan memudahkan Anda dalam memilih film sesuai dengan selera.")).pack(pady=10)
# Frame pilihan genre
frame_genre = frames["genre"]
#mewarnai bakcgrpund pada halaman genre
frame_genre.config(bg="#006A67")
#pewarnaan pada tulisan teks. bg=border nya, fg=warna tulisannya
tk.Label(frame_genre, text="Pilih Genre Film Yang Kamu Inginkan", font=("Arial", 18, "bold"), bg="#006A67", fg="white").pack(pady=20)



# Menentukan ukuran tombol agar konsisten
button_width = 25  # Lebar tombol (jumlah karakter yang sesuai)
button_height = 2  # Tinggi tombol (jumlah baris teks yang sesuai)

for genre in movies.keys():
    tk.Button(frame_genre, text=genre, font=("Arial", 14), fg="white", bg="#85A98F", width=button_width,
              height=button_height, activebackground="#85A98F", activeforeground="white", anchor="center", 
              command=lambda g=genre: show_movie_list(g)).pack(pady=5, padx=20)

# Tombol Back dengan ukuran yang seragam
tk.Button(frame_genre, text="Back", font=("Arial", 12), fg="white", bg="#6c757d", width=button_width, 
          height=button_height, activebackground="#5a6268", activeforeground="white", anchor="center", 
          command=lambda: show_frame(frame_main)).pack(pady=10, padx=20)


# Frame daftar film
frame_movies = frames["movies"]
frame_movies.config(bg="#3D3BF3")
movie_label = tk.Label(frame_movies, text="", font=("Arial", 18, "bold"), bg="#3D3BF3", fg="#f5f5f5")
movie_label.pack(pady=20)
movies_list = tk.Frame(frame_movies, bg="#3D3BF3")
movies_list.pack(pady=10)
tk.Button(frame_movies, text="Back", font=("Arial", 12), fg="white", bg="#6c757d",
          activebackground="#5a6268", activeforeground="white", command=lambda: show_frame(frame_genre)).pack(pady=10)

# Frame detail film dengan desain baru
frame_movie_detail = frames["movie_detail"]
frame_movie_detail.config(bg="#3D3BF3")



# Membuat Canvas di dalam frame_movie_detail
canvas_detail = tk.Canvas(frame_movie_detail, width=800, height=600, highlightthickness=0)
canvas_detail.pack(fill="both", expand=True)

# Warna untuk background berdasarkan loop
for i in range(255):
    color = f"#{255-i:02x}{180+i//2:02x}{200-i:02x}"

# Membuat Label untuk judul film
movie_title_label = tk.Label(canvas_detail, text="Movie Title", font=("Arial", 20, "bold"), bg="#ffffff", fg="#333")
movie_title_label.place(relx=0.5, rely=0.25, anchor="center")



# Membuat Label untuk deskripsi film
movie_description_label = tk.Label(canvas_detail, text="Movie Description", font=("Arial", 14), bg="#B59F78", fg="#444", 
                                   wraplength=600, justify="left", relief="solid", borderwidth=1, padx=15, pady=10)
movie_description_label.place(relx=0.5, rely=0.5, anchor="center")  # Menempatkan Label di tengah Canvas

# Membuat tombol 'Back'
# Tombol Back
tk.Button(canvas_detail, text="Back", font=("Arial", 12), fg="white", bg="#ff6f61",
          activebackground="#d9534f", activeforeground="white", command=lambda: show_frame(frame_movies)).place(relx=0.5, rely=0.75, anchor="center")

# Fungsi chatbot
chatbot_responses = {
    "hai": "Hai! Ada yang bisa saya bantu?",
    "hallo": "Halo! Ada yang bisa saya bantu?",
    "halo": "Halo! Ada yang bisa saya bantu?",
    "apa kabar": "Saya baik, terima kasih! Bagaimana dengan Anda?",
    "baik": "Syukurlah. Semoga hari mu menyenangkan!",
    "tidak baik": "Cobalah menonton film. Supaya mood hari ini membaik!",
    "ente kiper terbaik di dunia": "terima kasih bang messi",
    "dimanakah saya bisa menontonnya?":"Kamu bisa menontonnya di aplikasi NETFLIX, AMAZON PRIME VIDEO, DISNEY+, YOUTUBE, dan masih banyak lagi",
    "dimanakah saya bisa menonton film tersebut?":"Kamu bisa menontonnya di aplikasi NETFLIX, AMAZON PRIME VIDEO, DISNEY+, YOUTUBE, dan masih banyak lagi",
    "dimana saya bisa menontonnya?":"Kamu bisa menontonnya di aplikasi NETFLIX, AMAZON PRIME VIDEO, DISNEY+, YOUTUBE, dan masih banyak lagi",
    "kono yaro baka yaro": "artinya apa bang messi?",
    "saran film": "Jika lagi ingin menonton film horror, cobalah film pengabdi setan. bikin merinding",
    
    # Respons untuk genre
    "genre": "Genre yang tersedia adalah Horror, Comedy, Action, Drama, dan juga Sci-Fi. Silakan pilih salah satu!",
    "sci-fi": "Sci-fi, atau science fiction, adalah genre dalam film, buku, atau media lain yang menggunakan elemen-elemen fiksi berbasis sains, teknologi, dan spekulasi tentang masa depan. Cerita dalam genre ini sering kali melibatkan hal-hal seperti perjalanan waktu, kehidupan di luar bumi, teknologi canggih, dan eksplorasi luar angkasa.",
    "comedy": "comedy juga seru. Coba film komedi dari indo. CEK TOKO SEBELAH. jika sudah pernah yang series pertama, coba CEK TOKO SEBELAH 2. Dijamin ketawa",
    "saran salah satu film sci-fi":"interstellar dan gravity coba deh. Keren tuh. Seru",
    
    # Tentang aplikasi
    "tentang aplikasi": "Nonton Film adalah aplikasi rekomendasi film terbaik. Gunakan fitur 'About App' untuk info lebih lengkap.",
    
    # Umum
    "film": "Kami memiliki banyak rekomendasi film. Coba gunakan fitur 'Movies' di aplikasi ini!",
    "selain": "Jika rekomendasi ku kurang, coba lihat di menu Movies. Di sana ada banyak genre dan nama film yang seru.",
    "menarik": "Cobalah film dari genre action dan sci-fi. Di sana banyak adegan menegangkan dan seru.",
    "salah satu": "Jika senang genre action, coba nonton film *G.I. Joe: Retaliation*. Saya suka film itu. Jika ingin yang dari Indonesia, coba film *The Raid*, sangat menegangkan.",
    
    # Respons untuk pertanyaan terkait film
    "film itu seru?": "Oh tentu saja. Cobalah menontonnya.",
    "film nya seru?": "Oh tentu saja. Cobalah menontonnya.",
    
    # Respons terkait pertanyaan personal
    "untuk ku?": "Cobalah menonton film *The RAID*. Film itu seru dan bergenre Action.",
    "untuk saya?": "Oh tentu saja. Cobalah menontonnya.",
    "untuk ku": "Oh tentu saja. Cobalah menontonnya.",
    "untuk saya": "Oh tentu saja. Cobalah menontonnya.",
    
    # Respons untuk pertanyaan lebih kompleks
    "genre apa yang seru": "Tergantung kamu menyukai jenis genre apa. Jika kamu sedang jatuh cinta, cobalah genre romance.",
    "film apa yang bagus": "Kami memiliki banyak rekomendasi film. Coba gunakan fitur 'Movies' di aplikasi ini!",
    "action": "Ooh, kamu lagi pengen yang penuh aksi! 💥 Berikut beberapa film action yang wajib banget ditonton:\n1. *John Wick* - Kejar-kejaran yang luar biasa, penuh dengan pertarungan keren dan cerita yang seru! 🕶️\n2. *Mad Max: Fury Road* - Dunia pasca-apokaliptik dengan aksi ekstrem dan visual yang spektakuler! 🌪️\n3. *Die Hard* - Film klasik yang selalu jadi favorit para penggemar action, dengan Bruce Willis yang legendaris! 🔫",
    
    # Respons terkait rekomendasi film berdasarkan genre
    "film apa yang seru": "Tergantung mood kamu! 😄 Kalau kamu lagi pengen action, coba nonton *John Wick* atau *Mad Max: Fury Road* — banyak aksi dan kejar-kejaran! 💥 Kalau mau yang penuh ketegangan, *The Conjuring* atau *Hereditary* cocok banget buat kamu yang suka film horror. 👻",
    "hari ini film apa yang seru?": "Tergantung mood kamu! 😄 Kalau kamu lagi pengen action, coba nonton *John Wick* atau *Mad Max: Fury Road* — banyak aksi dan kejar-kejaran! 💥 Kalau mau yang penuh ketegangan, *The Conjuring* atau *Hereditary* cocok banget buat kamu yang suka film horror. 👻",
    
    # Respons untuk ucapan terima kasih
    "terima kasih": "Sama-sama. Ada lagi yang bisa saya bantu?",
    
    # Tempat menonton film
    "nonton film nya dimana?": "Cobalah untuk menonton film yang kamu pilih di aplikasi NETFLIX dan sejenisnya. Untuk saat ini, aplikasi hanya bisa merekomendasikan genre atau film untuk kamu.",
    
    # Menanyakan apakah sudah menonton film tersebut
    "saya pernah menonton film itu?": "Mungkin kamu sudah pernah menonton film itu! Coba ingat-ingat lagi, siapa tahu kamu merasa familiar dengan ceritanya. Jika tidak, mungkin ini saat yang tepat untuk menontonnya!",
    
    # Menanyakan tempat menonton film
    "dimanakah saya bisa menonton film itu?": "Kamu bisa menonton film itu di berbagai platform streaming seperti Netflix, Disney+, Amazon Prime, atau platform lain yang menyediakan film tersebut. Pastikan cek ketersediaannya di platform pilihan kamu!",
    
    # Saran film lainnya
    "apakah ada saran film lain?": "Tentu! Jika kamu suka genre action, coba nonton *The Dark Knight* atau *The Avengers*. Untuk yang suka horor, *A Quiet Place* atau *It* bisa jadi pilihan seru. Ada banyak pilihan di aplikasi ini yang bisa kamu coba!",
    
    # Film horor yang menarik
    "film horor apa yang menarik?": "Film horor yang menarik adalah *The Conjuring* — sebuah cerita yang penuh ketegangan dan hantu-hantu menakutkan! 👻 Atau coba *Hereditary* untuk sensasi horor yang lebih psikologis dan mencekam!",
    
    # Film komedi yang menarik
    "film komedi apa yang menarik?": "Untuk film komedi, kamu bisa coba *The Hangover* — sebuah petualangan lucu yang penuh kejutan! Atau kalau suka yang ringan, *22 Jump Street* pasti bikin ketawa terbahak-bahak! 😂",
    
    # Film drama yang menarik
    "film drama apa yang menarik?": "Jika kamu suka drama, coba tonton *The Pursuit of Happyness*, kisah inspiratif tentang perjuangan hidup. Atau *La La Land* jika kamu ingin menikmati kisah cinta yang indah dengan musik yang memukau! 🎶",
    
    # Film sci-fi yang menarik
    "film sci-fi apa yang menarik?": "Untuk film sci-fi, *Inception* adalah pilihan yang sangat menarik — penuh dengan konsep waktu dan mimpi yang bikin penasaran! Jika ingin yang lebih klasik, coba *The Matrix* atau *Interstellar*, keduanya sangat menegangkan dan penuh dengan teknologi futuristik! 🚀",
    
    # Ucapan perpisahan
    "tidak": "Terima kasih sudah menggunakan aplikasi ini! Sampai jumpa lagi! 🎥👋",
    "bye": "Terima kasih sudah menggunakan aplikasi ini! Sampai jumpa lagi! 🎥👋",
    # Ucapan Salam dan Pengenalan Aplikasi
    "selamat pagi": "Selamat pagi! Apa yang bisa saya bantu hari ini? 😊",
    "selamat siang": "Selamat siang! Ada yang bisa saya bantu? 🌞",
    "selamat malam": "Selamat malam! Semoga harimu menyenangkan. Apa yang bisa saya bantu? 🌙",
    
    # Tentang Film
    "film terbaru": "Film terbaru yang sedang populer adalah *Dune: Part Two*, *Guardians of the Galaxy Vol. 3*, dan *The Flash*. Kalau ingin yang lebih seru, cek juga film *Oppenheimer* yang penuh drama sejarah!",
    "film apa yang lagi hits?": "Beberapa film yang lagi hits sekarang adalah *The Marvels*, *Barbie*, dan *Mission Impossible: Dead Reckoning Part One*. Jangan sampai ketinggalan!",
    
    # Rekomendasi Film Berdasarkan Genre
    "film action seru": "Kalau kamu suka film action, coba tonton *Fast & Furious 10*, *Mad Max: Fury Road*, atau *John Wick* untuk aksi yang tak terlupakan!",
    "film drama seru": "Untuk drama, *The Pursuit of Happyness* dan *The Green Mile* adalah pilihan yang pasti menyentuh hati. Jangan lupa tonton *La La Land* kalau suka kisah cinta!",
    "film komedi seru": "Kalau kamu ingin tertawa terbahak-bahak, coba tonton *Superbad*, *21 Jump Street*, atau *The Hangover*! Dijamin ngakak!",
    "film horor seru": "Coba tonton *The Conjuring*, *Hereditary*, atau *A Quiet Place* untuk pengalaman horor yang menegangkan! 🕯️👻",
    "film sci-fi seru": "Untuk sci-fi, *Interstellar*, *Inception*, atau *The Matrix* bisa membuat kamu berpikir keras! Kalau ingin yang lebih ringan, *Ready Player One* juga seru banget!",
    
    # Rekomendasi Berdasarkan Mood
    "film romantis": "Untuk film romantis, *The Notebook* dan *Titanic* adalah pilihan yang pasti membuatmu terharu. Kalau ingin yang lebih modern, coba *500 Days of Summer*!",
    "film petualangan": "Untuk film petualangan seru, coba *Indiana Jones*, *Pirates of the Caribbean*, atau *Jumanji: Welcome to the Jungle*. Kamu akan dibawa ke dunia yang penuh petualangan!",
    "film keluarga": "Untuk film keluarga yang cocok ditonton bersama, coba *The Lion King*, *Toy Story*, atau *Finding Nemo*. Pasti seru dan penuh pesan moral!",
    
    # Menanyakan Tentang Film
    "film ini bagus gak?": "Oh tentu saja! Coba tonton film tersebut, pasti seru! 😊",
    "film ini seru gak?": "Film ini memang seru! Pasti kamu akan menikmati ceritanya.",
    "film ini cocok buat saya gak?": "Tergantung selera kamu! Kalau suka genre yang seru, pasti kamu akan suka! Cobalah dan lihat sendiri.",
    
    # Film Favorit
    "film favorit saya": "Film favoritmu pasti yang terbaik! Kalau kamu suka action, *The Dark Knight* pasti jadi pilihan terbaik. Kalau horor, *The Conjuring* nggak boleh dilewatkan!",
    
    # Ucapan Perpisahan
    "terima kasih sudah membantu": "Sama-sama! Senang bisa membantu kamu. Semoga kamu menemukan film yang seru! 🎬",
    "bye bye": "Sampai jumpa! Terima kasih sudah menggunakan aplikasi kami. 🎥👋",
    "terima kasih atas rekomendasinya": "Sama-sama! Semoga filmnya seru! 😊",
    
    # Tempat Streaming Film
    "film ini ada di platform apa?": "Cek film ini di platform seperti Netflix, Amazon Prime Video, Disney+, atau HBO Max. Pastikan tersedia di wilayah kamu!",
    "dimana saya bisa nonton film ini?": "Film ini bisa kamu temukan di Netflix, Amazon Prime, atau platform streaming lainnya yang tersedia. Jangan lupa cek harga langganan mereka!",
    
    # Genre Horror
    "film horor apa yang wajib ditonton?": "Cobalah *The Ring*, *The Conjuring*, atau *The Grudge*. Kalau kamu ingin horor psikologis, *Hereditary* dan *Midsommar* adalah pilihan yang tepat!",
    
    # Film Superhero
    "film superhero apa yang seru?": "Untuk film superhero, kamu bisa coba *Avengers: Endgame*, *Spider-Man: No Way Home*, atau *The Dark Knight*. Seru banget, pasti nggak bakal nyesel!",
    
    # Film Animasi
    "film animasi apa yang bagus?": "Film animasi yang bagus seperti *Toy Story*, *Frozen*, atau *Zootopia* sangat cocok untuk kamu yang ingin hiburan ringan namun mengena. Jangan lupa tonton juga *Spider-Man: Into the Spider-Verse*!",
    
    # Film Petualangan
    "film petualangan apa yang seru?": "Jika kamu suka petualangan, *The Lord of the Rings*, *Harry Potter*, atau *Pirates of the Caribbean* pasti akan membawa kamu ke dunia fantasi yang menakjubkan!",
    
    # Film Misteri
    "film misteri apa yang menarik?": "Untuk film misteri, *Shutter Island*, *The Girl with the Dragon Tattoo*, dan *Gone Girl* bisa menjadi pilihan seru! Penuh teka-teki yang membuat penasaran!",
    
    # Film Biografi
    "film biografi apa yang bagus?": "Film biografi seperti *The Theory of Everything* tentang Stephen Hawking atau *Bohemian Rhapsody* tentang Queen pasti menginspirasi dan menyentuh hati!",
    
    # Film Laga
    "film laga apa yang seru?": "Kalau kamu suka film laga, *John Wick*, *The Raid*, dan *Mad Max: Fury Road* adalah pilihan terbaik yang wajib kamu tonton!",

}

conversation_state = {}

# Fungsi untuk menampilkan sambutan ketika chatbot diakses
def display_welcome_message():
    add_message("bot", "Selamat datang di chatbot kami, ada yang bisa saya bantu?")
    
def match_keyword_response(user_input):
    user_input = user_input.lower()
    
    # Urutkan kata kunci berdasarkan panjangnya (prioritas ke kata kunci lebih spesifik)
    sorted_keywords = sorted(chatbot_responses.keys(), key=len, reverse=True)
    
    for keyword in sorted_keywords:
        if keyword in user_input:
            return chatbot_responses[keyword]

    
    if "halo" in user_input or "hai" in user_input:
        return random.choice(chatbot_responses["halo"])
    
    return "Maaf, saya tidak mengerti. Coba kata kunci lain."
def add_message(sender, message):
    chatbot_output.config(state=tk.NORMAL)  # Aktifkan editing untuk menambahkan pesan
    
    if sender == "user":
        # Tambahkan label pengirim "You"
        chatbot_output.insert(tk.END, "You:\n", "user_label")
        # Tambahkan pesan pengguna
        chatbot_output.insert(tk.END, f"{message}\n\n", "user_message")
    else:
        # Tambahkan label pengirim "Chatbot"
        chatbot_output.insert(tk.END, "Chatbot:\n", "bot_label")
        # Tambahkan pesan chatbot
        chatbot_output.insert(tk.END, f"{message}\n\n", "bot_message")
    
    chatbot_output.config(state=tk.DISABLED)  # Nonaktifkan kembali editing
    chatbot_output.see(tk.END)  # Scroll otomatis ke bagian bawah
    
frame_chatbot = tk.Frame(container, bg="#f5f5f5")
frame_chatbot.grid(row=0, column=0, sticky="nsew")

# Komponen untuk chatbot
tk.Label(frame_chatbot, text="Chatbot", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

# Area output chatbot dengan scrollbar
output_frame = tk.Frame(frame_chatbot, bg="#f5f5f5")
output_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Chatbot output (text area)
chatbot_output = tk.Text(output_frame, font=("Arial", 12), bg="white", fg="#333", wrap="word", state=tk.DISABLED)
chatbot_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# Tambahkan gaya khusus untuk label dan pesan
chatbot_output.tag_config("user_label",justify="right" , foreground="#007BFF", font=("Arial", 10, "bold"))
chatbot_output.tag_config("bot_label", justify="left", foreground="#333", font=("Arial", 10, "bold"))
chatbot_output.tag_config("user_message", justify="right",foreground="#333", font=("Arial", 12), lmargin1=10, lmargin2=10)
chatbot_output.tag_config("bot_message",justify="left", foreground="#333", font=("Arial", 12), lmargin1=10, lmargin2=10)


# Scrollbar untuk chatbot_output
scrollbar = tk.Scrollbar(output_frame, command=chatbot_output.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Hubungkan scrollbar dengan area teks
chatbot_output.config(yscrollcommand=scrollbar.set)

# Fungsi untuk menangani input pengguna
def handle_chatbot_input():
    user_input = chatbot_entry.get()
    chatbot_entry.delete(0, tk.END)

    if user_input.strip():
        # Tambahkan pesan pengguna
        add_message("user", user_input)
        
        # Dapatkan respons chatbot
        response = match_keyword_response(user_input)
        
        # Tambahkan pesan chatbot
        add_message("bot", response)

# Entry untuk input pengguna
chatbot_entry = tk.Entry(frame_chatbot, font=("Arial", 14), bg="white", fg="#333")
chatbot_entry.pack(pady=5, padx=20, fill=tk.X)

tk.Button(frame_chatbot, text="Kirim", font=("Arial", 12), bg="#007BFF", fg="white",
          activebackground="#0056b3", activeforeground="white", command=handle_chatbot_input).pack(pady=5)

tk.Button(frame_chatbot, text="Back", font=("Arial", 12), bg="#6c757d", fg="white",
          activebackground="#5a6268", activeforeground="white", command=lambda: show_frame(frame_main)).pack(pady=10)

# Panggil fungsi sambutan ketika frame chatbot ditampilkan
display_welcome_message()

# Tampilkan frame utama
show_frame(frame_main)

# Jalankan aplikasi
root.mainloop()
