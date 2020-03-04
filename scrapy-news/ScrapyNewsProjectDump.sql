CREATE DATABASE  IF NOT EXISTS `scrapy` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `scrapy`;
-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: scrapy
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add auth group',7,'add_authgroup'),(26,'Can change auth group',7,'change_authgroup'),(27,'Can delete auth group',7,'delete_authgroup'),(28,'Can view auth group',7,'view_authgroup'),(29,'Can add auth group permissions',8,'add_authgrouppermissions'),(30,'Can change auth group permissions',8,'change_authgrouppermissions'),(31,'Can delete auth group permissions',8,'delete_authgrouppermissions'),(32,'Can view auth group permissions',8,'view_authgrouppermissions'),(33,'Can add auth permission',9,'add_authpermission'),(34,'Can change auth permission',9,'change_authpermission'),(35,'Can delete auth permission',9,'delete_authpermission'),(36,'Can view auth permission',9,'view_authpermission'),(37,'Can add auth user',10,'add_authuser'),(38,'Can change auth user',10,'change_authuser'),(39,'Can delete auth user',10,'delete_authuser'),(40,'Can view auth user',10,'view_authuser'),(41,'Can add auth user groups',11,'add_authusergroups'),(42,'Can change auth user groups',11,'change_authusergroups'),(43,'Can delete auth user groups',11,'delete_authusergroups'),(44,'Can view auth user groups',11,'view_authusergroups'),(45,'Can add auth user user permissions',12,'add_authuseruserpermissions'),(46,'Can change auth user user permissions',12,'change_authuseruserpermissions'),(47,'Can delete auth user user permissions',12,'delete_authuseruserpermissions'),(48,'Can view auth user user permissions',12,'view_authuseruserpermissions'),(49,'Can add django admin log',13,'add_djangoadminlog'),(50,'Can change django admin log',13,'change_djangoadminlog'),(51,'Can delete django admin log',13,'delete_djangoadminlog'),(52,'Can view django admin log',13,'view_djangoadminlog'),(53,'Can add django content type',14,'add_djangocontenttype'),(54,'Can change django content type',14,'change_djangocontenttype'),(55,'Can delete django content type',14,'delete_djangocontenttype'),(56,'Can view django content type',14,'view_djangocontenttype'),(57,'Can add django migrations',15,'add_djangomigrations'),(58,'Can change django migrations',15,'change_djangomigrations'),(59,'Can delete django migrations',15,'delete_djangomigrations'),(60,'Can view django migrations',15,'view_djangomigrations'),(61,'Can add django session',16,'add_djangosession'),(62,'Can change django session',16,'change_djangosession'),(63,'Can delete django session',16,'delete_djangosession'),(64,'Can view django session',16,'view_djangosession'),(65,'Can add news',17,'add_news'),(66,'Can change news',17,'change_news'),(67,'Can delete news',17,'delete_news'),(68,'Can view news',17,'view_news');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'main','authgroup'),(8,'main','authgrouppermissions'),(9,'main','authpermission'),(10,'main','authuser'),(11,'main','authusergroups'),(12,'main','authuseruserpermissions'),(13,'main','djangoadminlog'),(14,'main','djangocontenttype'),(15,'main','djangomigrations'),(16,'main','djangosession'),(17,'main','news'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-03-03 11:43:52.060142'),(2,'auth','0001_initial','2020-03-03 11:43:52.217177'),(3,'admin','0001_initial','2020-03-03 11:43:52.650275'),(4,'admin','0002_logentry_remove_auto_add','2020-03-03 11:43:52.739294'),(5,'admin','0003_logentry_add_action_flag_choices','2020-03-03 11:43:52.748297'),(6,'contenttypes','0002_remove_content_type_name','2020-03-03 11:43:52.854320'),(7,'auth','0002_alter_permission_name_max_length','2020-03-03 11:43:52.905332'),(8,'auth','0003_alter_user_email_max_length','2020-03-03 11:43:52.922336'),(9,'auth','0004_alter_user_username_opts','2020-03-03 11:43:52.928337'),(10,'auth','0005_alter_user_last_login_null','2020-03-03 11:43:52.967346'),(11,'auth','0006_require_contenttypes_0002','2020-03-03 11:43:52.970347'),(12,'auth','0007_alter_validators_add_error_messages','2020-03-03 11:43:52.975348'),(13,'auth','0008_alter_user_username_max_length','2020-03-03 11:43:53.021358'),(14,'auth','0009_alter_user_last_name_max_length','2020-03-03 11:43:53.079372'),(15,'auth','0010_alter_group_name_max_length','2020-03-03 11:43:53.095375'),(16,'auth','0011_update_proxy_permissions','2020-03-03 11:43:53.101376'),(17,'sessions','0001_initial','2020-03-03 11:43:53.123381'),(18,'main','0001_initial','2020-03-03 15:01:06.347155');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news`
--

DROP TABLE IF EXISTS `news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `news` (
  `news_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `subtitle` varchar(255) NOT NULL,
  `context` text NOT NULL,
  `post_url` varchar(255) NOT NULL,
  `img_url` varchar(255) NOT NULL,
  `post_date` datetime NOT NULL,
  `create_date` datetime NOT NULL,
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news`
--

LOCK TABLES `news` WRITE;
/*!40000 ALTER TABLE `news` DISABLE KEYS */;
INSERT INTO `news` VALUES (72,'戴維斯歸隊單節扭轉戰局 湖人力壓殘陣76人','NBA台灣 / udn記者陳元廷／綜合外電報導','一口氣缺了安比德（Joel Embiid）、西蒙斯（Ben Simmons）與理查森（Josh Richardson）三員戰將，76人今天（4號）來到洛城迎戰西區龍頭湖人，打了1節半的好球之後再難帶給紫金軍團威脅，終場以107比120不敵對手。前場迎戰洛城另一支勁旅快艇，小將米爾頓（Shake Milton）挺身轟生涯新高39分，雖沒有替帶來勝利但也證明傷兵滿營76人仍有戰力，球隊本場也有不錯開局，可惜火熱進攻手感只維持1節半，一度領先13分證明是曇花一現。回歸的戴維斯（Anthony Davis）第2節獨攬18分，且命中率是完美的7投7中，一人得分只比對手整節少1分而已，湖人也從13分落後一舉翻盤並倒打拿到11分超前優勢，之後在末節雖被追到9分，但76人始終未能再越雷池一步。戴維斯有37分、13籃板與4抄截貢獻，勇冠全隊，詹姆斯（LeBron James）則繳22分、14助攻與7籃板，此役除掛傷號的卡盧索（Alex Caruso）外全員都得到出賽機會；76人方面，羅賓森（Glenn Robinson III）得25分，寫轉隊代表作。','https://nba.udn.com/nba/story/6780/4388351','https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2020/03/04/99/7549504.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600','2020-03-04 13:44:00','2020-03-04 15:59:55'),(76,'怪物新人新挑戰 威廉森連續出賽拚紀錄','聯合報 / 記者曾思儒／即時報導','鵜鶘隊話題新人威廉森（Zion Williamson）將迎接NBA生涯首度的「背靠背」出賽，他今天（4號）對灰狼隊攻下25分，繼續推進聯盟20歲以下球員連續得分20分以上場次紀錄，球團也計畫讓他明天對獨行俠隊再上場。威廉森季前動了膝蓋微創手術，美國時間今年1月22日才復出，但他也展現外界期待的身手，今天球隊雖以134：139吞敗，但他連續20分場次已累積到12場，繼續將原本聯盟紀錄9場向上改寫。鵜鶘今天碰灰狼、明天戰獨行俠，將是威廉森復出後首度連續出賽，教頭簡崔（Alvin Gentry）表示，計畫讓威廉森連續上陣，球隊的醫療團隊也會持續注意選秀狀元的狀況。先前鵜鶘鵜鶘總管葛里芬（David Griffin）曾提到，球團會多保護威廉森，尤其是碰上連續出賽的場次，不過鵜鶘在威廉森復出後還沒遇「背靠背」出賽；就實際上來說，威廉森其實已經有過連續出賽紀錄，他美國時間2月13日出戰雷霆隊，隔天就飛到芝加哥參加NBA明星周的新秀對抗賽。今天碰灰狼上場33分鐘的威廉森表示，連續出賽他沒有問題，「我們有很好的訓練團隊，隔天都會有很完整的恢復，他們會幫助我明天準備妥當」。他也提到，連續出賽對復健過程是重要一環，自己賽後也必須好好恢復，來延續這幾場的高檔演出。不過鵜鶘今天輸球後，戰績已落到26勝35敗，目前和西區第8的灰熊隊場差已達4場，想前進季後賽難度愈來愈高。','https://nba.udn.com/nba/story/6780/4388482','https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2020/03/04/1/7549982.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600','2020-03-04 15:14:00','2020-03-04 16:01:52'),(77,'「Logo Shot」全場驚艷 詹皇：沒練過的不投','聯合報 / 記者林宋以情／即時報導','拚戰聯盟第17個球季，35歲的湖人球星詹姆斯（LeBron James）仍不斷鞭策精進。4日面對76人隊，詹姆斯第3節秀一手「Logo Shot」驚艷四座，詹皇本人倒是顯得淡定，表示舉凡自己出手必定是滿懷信心。湖人隊今日120：107擊敗傷兵滿營，兩大球星安比德（Joel Embiid）、西蒙斯（Ben Simmons）缺陣的76人隊，戴維斯（Anthony Davis）攻下37分、13籃板、4抄截，詹姆斯挹注22分、14助攻、7籃板，包括他第3節10分46秒，帶球過半場後在距離籃框36呎處飆進超大號三分球，令主場湖人迷驚呼連連。賽後被問到這驚鴻一撇好球，詹姆斯表示並非運氣，而是苦練成果，「我知道我下了多少苦工，我沒練過的從來不投，這是我生涯中不曾做過的。我下過功夫，相信我的技巧，讓球帶著自信劃過空中」。戴維斯談到詹姆斯的「Logo Shot」也直呼意外，但他能感覺到詹姆斯對於自己的出手充滿自信，「沒人知道他會這麼做。我以為他會傳給我，結果他拔起來就投。當他投進後，所有人都心想『他從哪裡投進的？』」','https://nba.udn.com/nba/story/6780/4388639','https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2020/03/04/1/7550157.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=1050&exp=3600','2020-03-04 15:49:00','2020-03-04 16:01:52');
/*!40000 ALTER TABLE `news` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-04 23:55:54
