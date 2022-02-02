-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 04 Oca 2022, 14:44:52
-- Sunucu sürümü: 10.4.22-MariaDB
-- PHP Sürümü: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `veritabani2`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `asi_tablosu`
--

CREATE TABLE `asi_tablosu` (
  `asi_id` int(11) NOT NULL,
  `asi_ismi` varchar(30) COLLATE utf8_turkish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci COMMENT='Aşı türleri burada tutuluyor';

--
-- Tablo döküm verisi `asi_tablosu`
--

INSERT INTO `asi_tablosu` (`asi_id`, `asi_ismi`) VALUES
(1, 'Yok'),
(2, 'Sinovac'),
(3, 'Biontech');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `belirtiler_tablo`
--

CREATE TABLE `belirtiler_tablo` (
  `belirti_id` int(11) NOT NULL,
  `tc` varchar(12) COLLATE utf8_turkish_ci NOT NULL,
  `belirti_ismi` varchar(50) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `belirtiler_tablo`
--

INSERT INTO `belirtiler_tablo` (`belirti_id`, `tc`, `belirti_ismi`) VALUES
(23, '15426594874', 'Halsizlik'),
(24, '15426594874', 'İshal'),
(30, '36523233659', 'Nefes Darlığı'),
(31, '36523233659', 'Tat ve Koku Kaybı'),
(32, '36525152456', 'Kemik Ağrısı'),
(33, '41511254965', 'Göğüs Ağrısı'),
(34, '41511254965', 'Yüksek Ateş');

-- --------------------------------------------------------

--
-- Görünüm yapısı durumu `bulastiran_covidliler`
-- (Asıl görünüm için aşağıya bakın)
--
CREATE TABLE `bulastiran_covidliler` (
`tc` varchar(12)
,`isim` varchar(50)
,`soyad` varchar(50)
,`temasli_tc` varchar(12)
);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `calisanlar`
--

CREATE TABLE `calisanlar` (
  `calisanlar_id` int(11) NOT NULL,
  `tc` varchar(12) COLLATE utf8_turkish_ci NOT NULL,
  `isim` varchar(50) COLLATE utf8_turkish_ci NOT NULL,
  `soyad` varchar(50) COLLATE utf8_turkish_ci NOT NULL,
  `kan_grubu` varchar(20) COLLATE utf8_turkish_ci DEFAULT NULL,
  `dogdugu_sehir` varchar(50) COLLATE utf8_turkish_ci DEFAULT NULL,
  `pozisyon` varchar(200) COLLATE utf8_turkish_ci DEFAULT NULL,
  `maas` int(6) DEFAULT NULL,
  `lisans` int(11) DEFAULT NULL,
  `yuksek_lisans` int(11) DEFAULT NULL,
  `doktora` int(11) DEFAULT NULL,
  `asi_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `calisanlar`
--

INSERT INTO `calisanlar` (`calisanlar_id`, `tc`, `isim`, `soyad`, `kan_grubu`, `dogdugu_sehir`, `pozisyon`, `maas`, `lisans`, `yuksek_lisans`, `doktora`, `asi_id`) VALUES
(51, '11111111111', 'Ahmet', 'Sert', 'A+', 'Adana', 'Java Developer', 9000, 60, 0, 0, 3),
(36, '14526587496', 'Mehmet Ali', 'Ardıç', '0+', 'Manisa', 'Java Developer', 5500, 21, 106, 100, 3),
(32, '15426594874', 'Elif Dilay', 'Altınkaya', 'B-', 'Trabzon', 'Pazarlamacı', 5600, 74, 0, 0, 1),
(28, '26535145698', 'Servet', 'Akış', 'AB-', 'Konya', 'Sistem Analisti', 6400, 45, 45, 45, 3),
(29, '35412657845', 'İclal', 'Akkoyun', 'AB+', 'Gaziantep', 'Sistem Analisti', 5700, 165, 145, 0, 3),
(22, '36512589544', 'Cemile', 'Doğan', 'B-', 'İstanbul', 'Veritabanı Yönetimi', 5900, 46, 60, 0, 2),
(43, '36522365215', 'İsmail', 'Çelik', 'AB+', 'Giresun', 'Web Developer', 6200, 2, 32, 0, 2),
(37, '36523233659', 'Sevinç', 'Ak', 'B+', 'Zonguldak', 'Pazarlamacı', 4500, 106, 0, 0, 1),
(21, '36525152456', 'Melike', 'Ay', 'A-', 'İstanbul', 'Bulut Yöneticisi', 5500, 106, 106, 106, 1),
(45, '41511254965', 'Ömer', 'Ataş', 'A+', 'İstanbul', 'Siber Güvenlik', 5700, 66, 36, 0, 1),
(24, '42653164696', 'Murat', 'Alabakan', 'AB-', 'Elazığ', 'Pazarlamacı', 5600, 126, 127, 134, 2),
(44, '45625361524', 'Senanur', 'Sevgi', 'AB-', 'Giresun', 'Pazarlamacı', 4500, 25, 0, 0, 2),
(38, '45654454125', 'Cihan', 'Akarpınar', 'B+', 'Isparta', 'Siber Güvenlik', 5800, 140, 61, 12, 1),
(26, '45784598457', 'Ceren', 'Ağca', 'A-', 'Bayburt', 'Web Developer', 5600, 86, 85, 0, 2),
(40, '46532659745', 'Senem', 'Aksevim', 'AB+', 'Trabzon', 'Siber Güvenlik', 7000, 120, 120, 120, 2),
(39, '47658325647', 'Ayşe', 'Aksoy', 'B+', 'Sivas', 'Java Developer', 5800, 15, 165, 42, 1),
(20, '47854123654', 'Hüseyin', 'Türkmen', 'A+', 'Giresun', 'Java Developer', 5850, 120, 120, 0, 2),
(47, '54784598452', 'Furkan', 'Kızılpınar', 'A+', 'Zonguldak', 'Bilgi İşlem', 5800, 106, 85, 106, 2),
(31, '54854152415', 'Elif Tuğçe', 'Altaş', 'B-', 'İstanbul', 'Sistem Analisti', 145, 85, 16, 16, 3),
(46, '56245285474', 'Ahmet', 'Akyol', '0+', 'İzmir', 'Bilgi İşlem', 5900, 165, 25, 25, 2),
(33, '56948251478', 'Rana', 'Altınoklu', '0-', 'Artvin', 'Sistem Operatörü', 5600, 106, 120, 0, 2),
(35, '65415263548', 'Halim', 'Aral', '0+', 'Ankara', 'Bilgi İşlem', 5700, 21, 0, 0, 2),
(30, '74654321402', 'Semina', 'Aktuna', 'B+', 'Şanlıurfa', 'Sistem Analisti', 5700, 140, 140, 145, 1);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `calisma_sureleri`
--

CREATE TABLE `calisma_sureleri` (
  `id` int(11) NOT NULL,
  `tc` varchar(12) COLLATE utf8_turkish_ci NOT NULL,
  `haftaicigiris` time DEFAULT NULL,
  `haftaicicikis` time DEFAULT NULL,
  `cumartesigiris` time DEFAULT NULL,
  `cumartesicikis` time DEFAULT NULL,
  `pazargiris` time DEFAULT NULL,
  `pazarcikis` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `calisma_sureleri`
--

INSERT INTO `calisma_sureleri` (`id`, `tc`, `haftaicigiris`, `haftaicicikis`, `cumartesigiris`, `cumartesicikis`, `pazargiris`, `pazarcikis`) VALUES
(2, '14526587496', '10:00:00', '17:00:00', '12:00:00', '16:00:00', '00:00:00', '00:00:00'),
(3, '15426594874', '10:00:00', '18:00:00', '12:00:00', '16:00:00', '00:00:00', '00:00:00'),
(6, '26535145698', '10:00:00', '17:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00'),
(7, '35412657845', '08:00:00', '18:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00'),
(8, '36512589544', '10:00:00', '15:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00'),
(9, '36522365215', '08:00:00', '17:00:00', '11:00:00', '17:00:00', '12:00:00', '17:00:00'),
(10, '36523233659', '11:00:00', '18:00:00', '16:00:00', '23:30:00', '00:00:00', '00:00:00'),
(11, '36525152456', '10:00:00', '18:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00'),
(12, '41511254965', '12:00:00', '22:00:00', '12:00:00', '22:00:00', '00:00:00', '00:00:00'),
(13, '42653164696', '09:00:00', '17:00:00', '09:00:00', '17:00:00', '12:00:00', '22:00:00'),
(14, '45625361524', '10:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '18:20:00'),
(15, '45654454125', '10:30:00', '17:20:00', '15:00:00', '18:00:00', '00:00:00', '00:00:00'),
(16, '45784598457', '10:00:00', '20:00:00', '15:00:00', '20:00:00', '15:20:00', '22:00:00'),
(17, '46532659745', '11:30:00', '19:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00'),
(18, '47658325647', '08:10:00', '16:30:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00'),
(19, '47854123654', '10:00:00', '18:00:00', '10:00:00', '16:00:00', '00:00:00', '00:00:00'),
(20, '54784598452', '10:20:00', '18:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00'),
(21, '54854152415', '10:00:00', '18:00:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00'),
(22, '56245285474', '11:00:00', '20:00:00', '10:00:00', '22:00:00', '00:00:00', '00:00:00'),
(23, '56948251478', '10:00:00', '19:00:00', '10:00:00', '18:15:00', '12:30:00', '18:00:00'),
(24, '65415263548', '10:00:00', '21:08:00', '00:00:00', '00:00:00', '00:00:00', '00:00:00'),
(25, '74654321402', '11:00:00', '19:20:00', '15:00:00', '21:00:00', '16:00:00', '22:00:00'),
(26, '11111111111', '11:00:00', '18:00:00', '10:00:00', '18:00:00', '10:00:00', '20:00:00');

-- --------------------------------------------------------

--
-- Görünüm yapısı durumu `covidliye_dokunanlar`
-- (Asıl görünüm için aşağıya bakın)
--
CREATE TABLE `covidliye_dokunanlar` (
`temas_eden_tc` varchar(12)
,`isim` varchar(50)
,`soyad` varchar(50)
,`koronali` varchar(12)
);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `covid_tablosu`
--

CREATE TABLE `covid_tablosu` (
  `covid_id` int(11) NOT NULL,
  `tc` varchar(12) COLLATE utf8_turkish_ci NOT NULL,
  `pozitif_tarihi` date DEFAULT NULL,
  `negatif_tarihi` date DEFAULT NULL,
  `asi_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `covid_tablosu`
--

INSERT INTO `covid_tablosu` (`covid_id`, `tc`, `pozitif_tarihi`, `negatif_tarihi`, `asi_id`) VALUES
(27, '15426594874', '2021-05-02', '2021-05-16', 3),
(32, '36523233659', '2021-07-12', '2021-07-22', 3),
(33, '36525152456', '2021-05-06', '2021-05-22', 3),
(34, '41511254965', '2021-11-04', '2021-11-20', 3),
(40, '11111111111', '2021-12-01', '2022-01-14', 3);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hastalik_tablo`
--

CREATE TABLE `hastalik_tablo` (
  `hastalik_id` int(5) NOT NULL,
  `tc` varchar(12) COLLATE utf8_turkish_ci NOT NULL,
  `hastalik_adi` text COLLATE utf8_turkish_ci DEFAULT NULL,
  `hastalik_tarihi` date DEFAULT NULL,
  `ilac` text COLLATE utf8_turkish_ci DEFAULT NULL,
  `doz` text COLLATE utf8_turkish_ci DEFAULT NULL,
  `semptomlar` text COLLATE utf8_turkish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `hastalik_tablo`
--

INSERT INTO `hastalik_tablo` (`hastalik_id`, `tc`, `hastalik_adi`, `hastalik_tarihi`, `ilac`, `doz`, `semptomlar`) VALUES
(17, '14526587496', 'Grip', '2021-12-12', 'Theraflu', '3', 'Burun Akıntısı'),
(18, '26535145698', 'İnsomnia', '2021-05-14', 'Atarax', '1', 'Uykusuzluk'),
(19, '35412657845', 'Diş Ağrısı', '2021-04-14', 'Parol', '3', 'Diş Ağrısı'),
(20, '56245285474', 'Grip', '2021-03-24', 'Gripin', '2', 'Yüksek Ateş'),
(24, '11111111111', 'Grip', '2022-01-01', 'Parol', '2', 'Burun Akıntısı');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hobiler_tablosu`
--

CREATE TABLE `hobiler_tablosu` (
  `hobi_id` int(11) NOT NULL,
  `tc` varchar(12) COLLATE utf8_turkish_ci NOT NULL,
  `hobi_ismi` varchar(50) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `hobiler_tablosu`
--

INSERT INTO `hobiler_tablosu` (`hobi_id`, `tc`, `hobi_ismi`) VALUES
(5, '14526587496', 'Yüzmek');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kronik_hastalik_tablo`
--

CREATE TABLE `kronik_hastalik_tablo` (
  `kronik_hastalik_id` int(11) NOT NULL,
  `tc` varchar(12) COLLATE utf8_turkish_ci NOT NULL,
  `kronik_hastalik_ismi` varchar(50) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `kronik_hastalik_tablo`
--

INSERT INTO `kronik_hastalik_tablo` (`kronik_hastalik_id`, `tc`, `kronik_hastalik_ismi`) VALUES
(13, '36523233659', 'Diyabet'),
(17, '41511254965', 'Akciğer Yetmezliği'),
(18, '41511254965', 'Bronşit');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `temasli_calisanlar_tablo`
--

CREATE TABLE `temasli_calisanlar_tablo` (
  `temasli_id` int(11) NOT NULL,
  `tc` varchar(12) COLLATE utf8_turkish_ci NOT NULL,
  `temasli_tc` varchar(12) COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `temasli_calisanlar_tablo`
--

INSERT INTO `temasli_calisanlar_tablo` (`temasli_id`, `tc`, `temasli_tc`) VALUES
(11, '36523233659', '54784598452'),
(12, '36523233659', '56245285474'),
(13, '36523233659', '74654321402');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `universite_tablosu`
--

CREATE TABLE `universite_tablosu` (
  `universite_id` int(11) NOT NULL,
  `lisans` int(11) DEFAULT NULL,
  `yuksek_lisans` int(11) DEFAULT NULL,
  `doktora` int(11) DEFAULT NULL,
  `universite_ismi` text COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `universite_tablosu`
--

INSERT INTO `universite_tablosu` (`universite_id`, `lisans`, `yuksek_lisans`, `doktora`, `universite_ismi`) VALUES
(1, 1, 1, 1, 'ABANT İZZET BAYSAL ÜNİVERSİTESİ'),
(2, 2, 2, 2, 'ABDULLAH GÜL ÜNİVERSİTESİ'),
(3, 3, 3, 3, 'ACIBADEM MEHMET ALİ AYDINLAR ÜNİVERSİTESİ'),
(4, 4, 4, 4, 'ADANA BİLİM VE TEKNOLOJİ ÜNİVERSİTESİ'),
(5, 5, 5, 5, 'ADIYAMAN ÜNİVERSİTESİ'),
(6, 6, 6, 6, 'ADNAN MENDERES ÜNİVERSİTESİ'),
(7, 7, 7, 7, 'AFYON KOCATEPE ÜNİVERSİTESİ'),
(8, 8, 8, 8, 'AĞRI İBRAHİM ÇEÇEN ÜNİVERSİTESİ'),
(9, 9, 9, 9, 'AHİ EVRAN ÜNİVERSİTESİ'),
(10, 10, 10, 10, 'AKDENİZ KARPAZ ÜNİVERSİTESİ'),
(11, 11, 11, 11, 'AKDENİZ ÜNİVERSİTESİ'),
(12, 12, 12, 12, 'AKSARAY ÜNİVERSİTESİ'),
(13, 13, 13, 13, 'ALANYA ALAADDİN KEYKUBAT ÜNİVERSİTESİ'),
(14, 14, 14, 14, 'ALANYA HAMDULLAH EMİN PAŞA ÜNİVERSİTESİ'),
(15, 15, 15, 15, 'ALTINBAŞ ÜNİVERSİTESİ'),
(16, 16, 16, 16, 'AMASYA ÜNİVERSİTESİ'),
(17, 17, 17, 17, 'ANADOLU ÜNİVERSİTESİ'),
(18, 18, 18, 18, 'ANKARA SOSYAL BİLİMLER ÜNİVERSİTESİ'),
(19, 19, 19, 19, 'ANKARA ÜNİVERSİTESİ'),
(20, 20, 20, 20, 'ANKARA YILDIRIM BEYAZIT ÜNİVERSİTESİ'),
(21, 21, 21, 21, 'ANTALYA AKEV ÜNİVERSİTESİ'),
(22, 22, 22, 22, 'ANTALYA BİLİM ÜNİVERSİTESİ'),
(23, 23, 23, 23, 'ARDAHAN ÜNİVERSİTESİ'),
(24, 24, 24, 24, 'ARTVİN ÇORUH ÜNİVERSİTESİ'),
(25, 25, 25, 25, 'ATAŞEHİR ADIGÜZEL MESLEK YÜKSEKOKULU'),
(26, 26, 26, 26, 'ATATÜRK ÜNİVERSİTESİ'),
(27, 27, 27, 27, 'ATILIM ÜNİVERSİTESİ'),
(28, 28, 28, 28, 'AVRASYA ÜNİVERSİTESİ'),
(29, 29, 29, 29, 'AVRUPA MESLEK YÜKSEKOKULU'),
(30, 30, 30, 30, 'BAHÇEŞEHİR ÜNİVERSİTESİ'),
(31, 31, 31, 31, 'BALIKESİR ÜNİVERSİTESİ'),
(32, 32, 32, 32, 'BANDIRMA ONYEDİ EYLÜL ÜNİVERSİTESİ'),
(33, 33, 33, 33, 'BARTIN ÜNİVERSİTESİ'),
(34, 34, 34, 34, 'BAŞKENT ÜNİVERSİTESİ'),
(35, 35, 35, 35, 'BATMAN ÜNİVERSİTESİ'),
(36, 36, 36, 36, 'BAYBURT ÜNİVERSİTESİ'),
(37, 37, 37, 37, 'BEYKENT ÜNİVERSİTESİ'),
(38, 38, 38, 38, 'BEYKOZ ÜNİVERSİTESİ'),
(39, 39, 39, 39, 'BEZM-İ ÂLEM VAKIF ÜNİVERSİTESİ'),
(40, 40, 40, 40, 'BİLECİK ŞEYH EDEBALİ ÜNİVERSİTESİ'),
(41, 41, 41, 41, 'BİNGÖL ÜNİVERSİTESİ'),
(42, 42, 42, 42, 'BİRUNİ ÜNİVERSİTESİ'),
(43, 43, 43, 43, 'BİTLİS EREN ÜNİVERSİTESİ'),
(44, 44, 44, 44, 'BOĞAZİÇİ ÜNİVERSİTESİ'),
(45, 45, 45, 45, 'BOZOK ÜNİVERSİTESİ'),
(46, 46, 46, 46, 'BURSA TEKNİK ÜNİVERSİTESİ'),
(47, 47, 47, 47, 'BÜLENT ECEVİT ÜNİVERSİTESİ'),
(48, 48, 48, 48, 'CUMHURİYET ÜNİVERSİTESİ'),
(49, 49, 49, 49, 'ÇAĞ ÜNİVERSİTESİ'),
(50, 50, 50, 50, 'ÇANAKKALE ONSEKİZ MART ÜNİVERSİTESİ'),
(51, 51, 51, 51, 'ÇANKAYA ÜNİVERSİTESİ'),
(52, 52, 52, 52, 'ÇANKIRI KARATEKİN ÜNİVERSİTESİ'),
(53, 53, 53, 53, 'ÇUKUROVA ÜNİVERSİTESİ'),
(54, 54, 54, 54, 'DİCLE ÜNİVERSİTESİ'),
(55, 55, 55, 55, 'DOĞU AKDENİZ ÜNİVERSİTESİ'),
(56, 56, 56, 56, 'DOĞUŞ ÜNİVERSİTESİ'),
(57, 57, 57, 57, 'DOKUZ EYLÜL ÜNİVERSİTESİ'),
(58, 58, 58, 58, 'DUMLUPINAR ÜNİVERSİTESİ'),
(59, 59, 59, 59, 'DÜZCE ÜNİVERSİTESİ'),
(60, 60, 60, 60, 'EGE ÜNİVERSİTESİ'),
(61, 61, 61, 61, 'ERCİYES ÜNİVERSİTESİ'),
(62, 62, 62, 62, 'ERZİNCAN ÜNİVERSİTESİ'),
(63, 63, 63, 63, 'ERZURUM TEKNİK ÜNİVERSİTESİ'),
(64, 64, 64, 64, 'ESKİŞEHİR OSMANGAZİ ÜNİVERSİTESİ'),
(65, 65, 65, 65, 'FARUK SARAÇ TASARIM MESLEK YÜKSEKOKULU'),
(66, 66, 66, 66, 'FATİH SULTAN MEHMET VAKIF ÜNİVERSİTESİ'),
(67, 67, 67, 67, 'FIRAT ÜNİVERSİTESİ'),
(68, 68, 68, 68, 'GALATASARAY ÜNİVERSİTESİ'),
(69, 69, 69, 69, 'GAZİ ÜNİVERSİTESİ'),
(70, 70, 70, 70, 'GAZİANTEP ÜNİVERSİTESİ'),
(71, 71, 71, 71, 'GAZİOSMANPAŞA ÜNİVERSİTESİ'),
(72, 72, 72, 72, 'GEBZE TEKNİK ÜNİVERSİTESİ'),
(73, 73, 73, 73, 'GİRESUN ÜNİVERSİTESİ'),
(74, 74, 74, 74, 'GİRNE AMERİKAN ÜNİVERSİTESİ'),
(75, 75, 75, 75, 'GİRNE ÜNİVERSİTESİ'),
(76, 76, 76, 76, 'GÜMÜŞHANE ÜNİVERSİTESİ'),
(77, 77, 77, 77, 'HACETTEPE ÜNİVERSİTESİ'),
(78, 78, 78, 78, 'HAKKARİ ÜNİVERSİTESİ'),
(79, 79, 79, 79, 'HALİÇ ÜNİVERSİTESİ'),
(80, 80, 80, 80, 'HARRAN ÜNİVERSİTESİ'),
(81, 81, 81, 81, 'HASAN KALYONCU ÜNİVERSİTESİ'),
(82, 82, 82, 82, 'HİTİT ÜNİVERSİTESİ'),
(83, 83, 83, 83, 'IĞDIR ÜNİVERSİTESİ'),
(84, 84, 84, 84, 'IŞIK ÜNİVERSİTESİ'),
(85, 85, 85, 85, 'İBN HALDUN ÜNİVERSİTESİ'),
(86, 86, 86, 86, 'İHSAN DOĞRAMACI BİLKENT ÜNİVERSİTESİ'),
(87, 87, 87, 87, 'İNÖNÜ ÜNİVERSİTESİ'),
(88, 88, 88, 88, 'İSKENDERUN TEKNİK ÜNİVERSİTESİ'),
(89, 89, 89, 89, 'İSTANBUL 29 MAYIS ÜNİVERSİTESİ'),
(90, 90, 90, 90, 'İSTANBUL AREL ÜNİVERSİTESİ'),
(91, 91, 91, 91, 'İSTANBUL AYDIN ÜNİVERSİTESİ'),
(92, 92, 92, 92, 'İSTANBUL AYVANSARAY ÜNİVERSİTESİ'),
(93, 93, 93, 93, 'İSTANBUL BİLGİ ÜNİVERSİTESİ'),
(94, 94, 94, 94, 'İSTANBUL ESENYURT ÜNİVERSİTESİ'),
(95, 95, 95, 95, 'İSTANBUL GEDİK ÜNİVERSİTESİ'),
(96, 96, 96, 96, 'İSTANBUL GELİŞİM ÜNİVERSİTESİ'),
(97, 97, 97, 97, 'İSTANBUL KAVRAM MESLEK YÜKSEKOKULU'),
(98, 98, 98, 98, 'İSTANBUL KENT ÜNİVERSİTESİ'),
(99, 99, 99, 99, 'İSTANBUL KÜLTÜR ÜNİVERSİTESİ'),
(100, 100, 100, 100, 'İSTANBUL MEDENİYET ÜNİVERSİTESİ'),
(101, 101, 101, 101, 'İSTANBUL MEDİPOL ÜNİVERSİTESİ'),
(102, 102, 102, 102, 'İSTANBUL RUMELİ ÜNİVERSİTESİ'),
(103, 103, 103, 103, 'İSTANBUL SABAHATTİN ZAİM ÜNİVERSİTESİ'),
(104, 104, 104, 104, 'İSTANBUL ŞEHİR ÜNİVERSİTESİ'),
(105, 105, 105, 105, 'İSTANBUL ŞİŞLİ MESLEK YÜKSEKOKULU'),
(106, 106, 106, 106, 'İSTANBUL TEKNİK ÜNİVERSİTESİ'),
(107, 107, 107, 107, 'İSTANBUL TİCARET ÜNİVERSİTESİ'),
(108, 108, 108, 108, 'İSTANBUL ÜNİVERSİTESİ'),
(109, 109, 109, 109, 'İSTANBUL YENİ YÜZYIL ÜNİVERSİTESİ'),
(110, 110, 110, 110, 'İSTİNYE ÜNİVERSİTESİ'),
(111, 111, 111, 111, 'İZMİR DEMOKRASİ ÜNİVERSİTESİ'),
(112, 112, 112, 112, 'İZMİR EKONOMİ ÜNİVERSİTESİ'),
(113, 113, 113, 113, 'İZMİR KATİP ÇELEBİ ÜNİVERSİTESİ'),
(114, 114, 114, 114, 'İZMİR YÜKSEK TEKNOLOJİ ENSTİTÜSÜ'),
(115, 115, 115, 115, 'KADİR HAS ÜNİVERSİTESİ'),
(116, 116, 116, 116, 'KAFKAS ÜNİVERSİTESİ'),
(117, 117, 117, 117, 'KAHRAMANMARAŞ SÜTÇÜ İMAM ÜNİVERSİTESİ'),
(118, 118, 118, 118, 'KAPADOKYA ÜNİVERSİTESİ'),
(119, 119, 119, 119, 'KARABÜK ÜNİVERSİTESİ'),
(120, 120, 120, 120, 'KARADENİZ TEKNİK ÜNİVERSİTESİ'),
(121, 121, 121, 121, 'KARAMANOĞLU MEHMETBEY ÜNİVERSİTESİ'),
(122, 122, 122, 122, 'KASTAMONU ÜNİVERSİTESİ'),
(123, 123, 123, 123, 'KIBRIS AMERİKAN ÜNİVERSİTESİ'),
(124, 124, 124, 124, 'KIBRIS İLİM ÜNİVERSİTESİ'),
(125, 125, 125, 125, 'KIBRIS SOSYAL BİLİMLER ÜNİVERSİTESİ'),
(126, 126, 126, 126, 'KIRIKKALE ÜNİVERSİTESİ'),
(127, 127, 127, 127, 'KIRKLARELİ ÜNİVERSİTESİ'),
(128, 128, 128, 128, 'KİLİS 7 ARALIK ÜNİVERSİTESİ'),
(129, 129, 129, 129, 'KOCAELİ ÜNİVERSİTESİ'),
(130, 130, 130, 130, 'KOÇ ÜNİVERSİTESİ'),
(131, 131, 131, 131, 'KONYA GIDA VE TARIM ÜNİVERSİTESİ'),
(132, 132, 132, 132, 'KTO KARATAY ÜNİVERSİTESİ'),
(133, 133, 133, 133, 'LEFKE AVRUPA ÜNİVERSİTESİ'),
(134, 134, 134, 134, 'MALTEPE ÜNİVERSİTESİ'),
(135, 135, 135, 135, 'MANİSA CELAL BAYAR ÜNİVERSİTESİ'),
(136, 136, 136, 136, 'MARDİN ARTUKLU ÜNİVERSİTESİ'),
(137, 137, 137, 137, 'MARMARA ÜNİVERSİTESİ'),
(138, 138, 138, 138, 'MEF ÜNİVERSİTESİ'),
(139, 139, 139, 139, 'MEHMET AKİF ERSOY ÜNİVERSİTESİ'),
(140, 140, 140, 140, 'MERSİN ÜNİVERSİTESİ'),
(141, 141, 141, 141, 'MİLLİ SAVUNMA ÜNİVERSİTESİ'),
(142, 142, 142, 142, 'MİMAR SİNAN GÜZEL SANATLAR ÜNİVERSİTESİ'),
(143, 143, 143, 143, 'MUĞLA SITKI KOÇMAN ÜNİVERSİTESİ'),
(144, 144, 144, 144, 'MUNZUR ÜNİVERSİTESİ'),
(145, 145, 145, 145, 'MUSTAFA KEMAL ÜNİVERSİTESİ'),
(146, 146, 146, 146, 'MUŞ ALPARSLAN ÜNİVERSİTESİ'),
(147, 147, 147, 147, 'NAMIK KEMAL ÜNİVERSİTESİ'),
(148, 148, 148, 148, 'NECMETTİN ERBAKAN ÜNİVERSİTESİ'),
(149, 149, 149, 149, 'NEVŞEHİR HACI BEKTAŞ VELİ ÜNİVERSİTESİ'),
(150, 150, 150, 150, 'NİĞDE ÖMER HALİSDEMİR ÜNİVERSİTESİ'),
(151, 151, 151, 151, 'NİŞANTAŞI ÜNİVERSİTESİ'),
(152, 152, 152, 152, 'NUH NACİ YAZGAN ÜNİVERSİTESİ'),
(153, 153, 153, 153, 'OKAN ÜNİVERSİTESİ'),
(154, 154, 154, 154, 'ONDOKUZ MAYIS ÜNİVERSİTESİ'),
(155, 155, 155, 155, 'ORDU ÜNİVERSİTESİ'),
(156, 156, 156, 156, 'ORTA DOĞU TEKNİK ÜNİVERSİTESİ'),
(157, 157, 157, 157, 'OSMANİYE KORKUT ATA ÜNİVERSİTESİ'),
(158, 158, 158, 158, 'ÖZYEĞİN ÜNİVERSİTESİ'),
(159, 159, 159, 159, 'PAMUKKALE ÜNİVERSİTESİ'),
(160, 160, 160, 160, 'PİRİ REİS ÜNİVERSİTESİ'),
(161, 161, 161, 161, 'RECEP TAYYİP ERDOĞAN ÜNİVERSİTESİ'),
(162, 162, 162, 162, 'SABANCI ÜNİVERSİTESİ'),
(163, 163, 163, 163, 'SAĞLIK BİLİMLERİ ÜNİVERSİTESİ'),
(164, 164, 164, 164, 'SAKARYA ÜNİVERSİTESİ'),
(165, 165, 165, 165, 'SANKO ÜNİVERSİTESİ'),
(166, 166, 166, 166, 'SELÇUK ÜNİVERSİTESİ'),
(167, 167, 167, 167, 'SİİRT ÜNİVERSİTESİ'),
(168, 168, 168, 168, 'SİNOP ÜNİVERSİTESİ'),
(169, 169, 169, 169, 'SÜLEYMAN DEMİREL ÜNİVERSİTESİ'),
(170, 170, 170, 170, 'ŞIRNAK ÜNİVERSİTESİ'),
(171, 171, 171, 171, 'TED ÜNİVERSİTESİ'),
(172, 172, 172, 172, 'TOBB EKONOMİ VE TEKNOLOJİ ÜNİVERSİTESİ'),
(173, 173, 173, 173, 'TOROS ÜNİVERSİTESİ'),
(174, 174, 174, 174, 'TRAKYA ÜNİVERSİTESİ'),
(175, 175, 175, 175, 'TÜRK HAVA KURUMU ÜNİVERSİTESİ'),
(176, 176, 176, 176, 'TÜRK-ALMAN ÜNİVERSİTESİ'),
(177, 177, 177, 177, 'UFUK ÜNİVERSİTESİ'),
(178, 178, 178, 178, 'ULUDAĞ ÜNİVERSİTESİ'),
(179, 179, 179, 179, 'ULUSLAR ARASI KIBRIS ÜNİVERSİTESİ'),
(180, 180, 180, 180, 'UŞAK ÜNİVERSİTESİ'),
(181, 181, 181, 181, 'ÜSKÜDAR ÜNİVERSİTESİ'),
(182, 182, 182, 182, 'YAKINDOĞU ÜNİVERSİTESİ'),
(183, 183, 183, 183, 'YALOVA ÜNİVERSİTESİ'),
(184, 184, 184, 184, 'YAŞAR ÜNİVERSİTESİ'),
(185, 185, 185, 185, 'YEDİTEPE ÜNİVERSİTESİ'),
(186, 186, 186, 186, 'YILDIZ TEKNİK ÜNİVERSİTESİ'),
(187, 187, 187, 187, 'YÜKSEK İHTİSAS ÜNİVERSİTESİ'),
(188, 188, 188, 188, 'YÜZÜNCÜ YIL ÜNİVERSİTESİ'),
(189, 189, 189, 189, 'İSTANBUL BİLİM ÜNİVERSİTESİ');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8_turkish_ci NOT NULL,
  `email` text COLLATE utf8_turkish_ci NOT NULL,
  `username` text COLLATE utf8_turkish_ci NOT NULL,
  `password` text COLLATE utf8_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `username`, `password`) VALUES
(7, 'Hüseyin Türkmen', 'hsman@gmail.com', 'hsman', '$5$rounds=535000$o0SgjHv0BS6yby4M$hDCCrN.28VpFRs3tMLGv/BbzjJQARVZx9yKUsasnpr6'),
(8, 'huseyin', 'ahmet@gmail.com', 'hsman28', '$5$rounds=535000$0Sq5mDlfpHXhcIUg$3CQnufwgKTUTaoN.VjFoc4gXuwY6SqaoIKVM0mbxlQ4'),
(9, 'İsmail Çelik', 'deneme@gmail.com', 'valoiso', '$5$rounds=535000$pilMZwdnzeOec3K9$muaCzCPxO6sZr7MOQHHCRi2z8RL26KGVVNVfrqq9Qo/'),
(10, 'Hüseyin Türkmen', 'adursun@hotmail.com', 'fernando', '$5$rounds=535000$LZ732dMhq3PpzK/9$20n7L09lECYvui1oXVwFyMPBOqmMblc3wblR48mlZZ/');

-- --------------------------------------------------------

--
-- Görünüm yapısı `bulastiran_covidliler`
--
DROP TABLE IF EXISTS `bulastiran_covidliler`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `bulastiran_covidliler`  AS SELECT `c`.`tc` AS `tc`, `c`.`isim` AS `isim`, `c`.`soyad` AS `soyad`, `t`.`temasli_tc` AS `temasli_tc` FROM (`calisanlar` `c` join `temasli_calisanlar_tablo` `t`) WHERE `c`.`tc` in (select `t`.`tc` from `temasli_calisanlar_tablo`) ;

-- --------------------------------------------------------

--
-- Görünüm yapısı `covidliye_dokunanlar`
--
DROP TABLE IF EXISTS `covidliye_dokunanlar`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `covidliye_dokunanlar`  AS SELECT `c`.`tc` AS `temas_eden_tc`, `c`.`isim` AS `isim`, `c`.`soyad` AS `soyad`, `t`.`tc` AS `koronali` FROM (`calisanlar` `c` join `temasli_calisanlar_tablo` `t`) WHERE `c`.`tc` in (select `t`.`temasli_tc` from `temasli_calisanlar_tablo`) ;

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `asi_tablosu`
--
ALTER TABLE `asi_tablosu`
  ADD PRIMARY KEY (`asi_id`),
  ADD KEY `asi_id` (`asi_id`);

--
-- Tablo için indeksler `belirtiler_tablo`
--
ALTER TABLE `belirtiler_tablo`
  ADD PRIMARY KEY (`belirti_id`),
  ADD KEY `tc_no` (`tc`);

--
-- Tablo için indeksler `calisanlar`
--
ALTER TABLE `calisanlar`
  ADD PRIMARY KEY (`tc`),
  ADD KEY `tc_no` (`tc`),
  ADD KEY `asi_id` (`asi_id`),
  ADD KEY `lisans` (`lisans`) USING BTREE,
  ADD KEY `yuksek_lisans` (`yuksek_lisans`),
  ADD KEY `doktora` (`doktora`),
  ADD KEY `calisanlar_id` (`calisanlar_id`);

--
-- Tablo için indeksler `calisma_sureleri`
--
ALTER TABLE `calisma_sureleri`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`) USING BTREE,
  ADD KEY `tc_no` (`tc`);

--
-- Tablo için indeksler `covid_tablosu`
--
ALTER TABLE `covid_tablosu`
  ADD PRIMARY KEY (`covid_id`),
  ADD KEY `tc_no` (`tc`),
  ADD KEY `id` (`covid_id`) USING BTREE,
  ADD KEY `asi_id` (`asi_id`);

--
-- Tablo için indeksler `hastalik_tablo`
--
ALTER TABLE `hastalik_tablo`
  ADD PRIMARY KEY (`hastalik_id`),
  ADD KEY `id` (`hastalik_id`),
  ADD KEY `tc_no` (`tc`);

--
-- Tablo için indeksler `hobiler_tablosu`
--
ALTER TABLE `hobiler_tablosu`
  ADD PRIMARY KEY (`hobi_id`),
  ADD KEY `id` (`hobi_id`),
  ADD KEY `tc_no` (`tc`);

--
-- Tablo için indeksler `kronik_hastalik_tablo`
--
ALTER TABLE `kronik_hastalik_tablo`
  ADD PRIMARY KEY (`kronik_hastalik_id`),
  ADD KEY `tc_no` (`tc`);

--
-- Tablo için indeksler `temasli_calisanlar_tablo`
--
ALTER TABLE `temasli_calisanlar_tablo`
  ADD PRIMARY KEY (`temasli_id`),
  ADD KEY `tc_no` (`tc`),
  ADD KEY `temasli_tcno` (`temasli_tc`);

--
-- Tablo için indeksler `universite_tablosu`
--
ALTER TABLE `universite_tablosu`
  ADD PRIMARY KEY (`universite_id`),
  ADD UNIQUE KEY `lisans` (`lisans`),
  ADD UNIQUE KEY `yuksek_lisans` (`yuksek_lisans`),
  ADD UNIQUE KEY `doktora` (`doktora`),
  ADD KEY `id` (`universite_id`);

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `asi_tablosu`
--
ALTER TABLE `asi_tablosu`
  MODIFY `asi_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Tablo için AUTO_INCREMENT değeri `belirtiler_tablo`
--
ALTER TABLE `belirtiler_tablo`
  MODIFY `belirti_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- Tablo için AUTO_INCREMENT değeri `calisanlar`
--
ALTER TABLE `calisanlar`
  MODIFY `calisanlar_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- Tablo için AUTO_INCREMENT değeri `calisma_sureleri`
--
ALTER TABLE `calisma_sureleri`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Tablo için AUTO_INCREMENT değeri `covid_tablosu`
--
ALTER TABLE `covid_tablosu`
  MODIFY `covid_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- Tablo için AUTO_INCREMENT değeri `hastalik_tablo`
--
ALTER TABLE `hastalik_tablo`
  MODIFY `hastalik_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Tablo için AUTO_INCREMENT değeri `hobiler_tablosu`
--
ALTER TABLE `hobiler_tablosu`
  MODIFY `hobi_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Tablo için AUTO_INCREMENT değeri `kronik_hastalik_tablo`
--
ALTER TABLE `kronik_hastalik_tablo`
  MODIFY `kronik_hastalik_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- Tablo için AUTO_INCREMENT değeri `temasli_calisanlar_tablo`
--
ALTER TABLE `temasli_calisanlar_tablo`
  MODIFY `temasli_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Tablo için AUTO_INCREMENT değeri `universite_tablosu`
--
ALTER TABLE `universite_tablosu`
  MODIFY `universite_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=190;

--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `belirtiler_tablo`
--
ALTER TABLE `belirtiler_tablo`
  ADD CONSTRAINT `belirtiler_tablo_ibfk_1` FOREIGN KEY (`tc`) REFERENCES `covid_tablosu` (`tc`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `calisma_sureleri`
--
ALTER TABLE `calisma_sureleri`
  ADD CONSTRAINT `calisma_sureleri_ibfk_1` FOREIGN KEY (`tc`) REFERENCES `calisanlar` (`tc`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `covid_tablosu`
--
ALTER TABLE `covid_tablosu`
  ADD CONSTRAINT `asi_idibfk1` FOREIGN KEY (`asi_id`) REFERENCES `calisanlar` (`asi_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `covid_tablosu_ibfk_1` FOREIGN KEY (`tc`) REFERENCES `calisanlar` (`tc`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `hastalik_tablo`
--
ALTER TABLE `hastalik_tablo`
  ADD CONSTRAINT `hastalik_tablo_ibfk_1` FOREIGN KEY (`tc`) REFERENCES `calisanlar` (`tc`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `hobiler_tablosu`
--
ALTER TABLE `hobiler_tablosu`
  ADD CONSTRAINT `hobiler_tablosu_ibfk_2` FOREIGN KEY (`tc`) REFERENCES `calisanlar` (`tc`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `kronik_hastalik_tablo`
--
ALTER TABLE `kronik_hastalik_tablo`
  ADD CONSTRAINT `kronik_hastalik_tablo_ibfk_1` FOREIGN KEY (`tc`) REFERENCES `covid_tablosu` (`tc`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Tablo kısıtlamaları `temasli_calisanlar_tablo`
--
ALTER TABLE `temasli_calisanlar_tablo`
  ADD CONSTRAINT `temasli_calisanlar_tablo_ibfk_1` FOREIGN KEY (`tc`) REFERENCES `covid_tablosu` (`tc`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `temasli_calisanlar_tablo_ibfk_2` FOREIGN KEY (`temasli_tc`) REFERENCES `calisanlar` (`tc`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
