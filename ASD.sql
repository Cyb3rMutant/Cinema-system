CREATE DATABASE  IF NOT EXISTS `HC` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
USE `HC`;
-- MariaDB dump 10.19  Distrib 10.9.4-MariaDB, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: HC
-- ------------------------------------------------------
-- Server version	10.9.4-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bookings` (
  `BOOKING_REFERENCE` varchar(6) NOT NULL,
  `BOOKING_SEAT_COUNT` int(11) NOT NULL,
  `BOOKING_DATE` date NOT NULL,
  `BOOKING_PRICE` float NOT NULL,
  `SHOW_ID` int(11) NOT NULL,
  `SEAT_TYPE` varchar(16) NOT NULL,
  `CUSTOMER_EMAIL` varchar(128) NOT NULL,
  `REFUND` float DEFAULT NULL,
  `USER_ID` int(11) NOT NULL,
  UNIQUE KEY `BOOKING_REFERENCE` (`BOOKING_REFERENCE`),
  KEY `SHOW_ID` (`SHOW_ID`),
  KEY `CUSTOMER_EMAIL` (`CUSTOMER_EMAIL`),
  KEY `USER_ID` (`USER_ID`),
  CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`CUSTOMER_EMAIL`) REFERENCES `customers` (`CUSTOMER_EMAIL`),
  CONSTRAINT `bookings_ibfk_3` FOREIGN KEY (`USER_ID`) REFERENCES `users` (`USER_ID`),
  CONSTRAINT `bookings_ibfk_4` FOREIGN KEY (`SHOW_ID`) REFERENCES `shows` (`SHOW_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cinemas`
--

DROP TABLE IF EXISTS `cinemas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cinemas` (
  `CINEMA_ID` int(11) NOT NULL AUTO_INCREMENT,
  `CINEMA_ADDRESS` varchar(128) NOT NULL,
  `CITY_NAME` varchar(16) NOT NULL,
  PRIMARY KEY (`CINEMA_ID`),
  KEY `CITY_NAME` (`CITY_NAME`),
  CONSTRAINT `cinemas_ibfk_1` FOREIGN KEY (`CITY_NAME`) REFERENCES `cities` (`CITY_NAME`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cinemas`
--

LOCK TABLES `cinemas` WRITE;
/*!40000 ALTER TABLE `cinemas` DISABLE KEYS */;
INSERT INTO `cinemas` VALUES
(1,'29 Longmead Ave, BS7 8QF','Bristol'),
(2,'38 Cornwall St, B1D 4QS','Birmingham'),
(3,'11 St Mary St, CF5S 4DZ','Cardiff'),
(4,'21 Spencer Rd, CH3Z 1CV','London'),
(10,'brum2','Birmingham'),
(11,'UWE BS16 1QY','Bristol'),
(12,'cardiff2','Cardiff'),
(13,'london2','London');
/*!40000 ALTER TABLE `cinemas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities` (
  `CITY_NAME` varchar(16) NOT NULL,
  `CITY_MORNING_PRICE` float NOT NULL,
  `CITY_AFTERNOON_PRICE` float NOT NULL,
  `CITY_EVENING_PRICE` float NOT NULL,
  PRIMARY KEY (`CITY_NAME`),
  UNIQUE KEY `CITY_NAME` (`CITY_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES
('Birmingham',5,6,7),
('Bristol',6,7,8),
('Cardiff',5,6,7),
('London',10,11,12);
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `CUSTOMER_EMAIL` varchar(128) NOT NULL,
  `CUSTOMER_NAME` varchar(64) NOT NULL,
  `CUSTOMER_PHONE` varchar(11) NOT NULL,
  `CARD_ENDING_DIGITS` varchar(4) NOT NULL,
  PRIMARY KEY (`CUSTOMER_EMAIL`),
  UNIQUE KEY `CUSTOMER_EMAIL` (`CUSTOMER_EMAIL`),
  UNIQUE KEY `CUSTOMER_PHONE` (`CUSTOMER_PHONE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `films`
--

DROP TABLE IF EXISTS `films`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `films` (
  `FILM_TITLE` varchar(64) NOT NULL,
  `FILM_RATING` float NOT NULL,
  `FILM_GENRE` varchar(512) NOT NULL,
  `FILM_YEAR` varchar(4) NOT NULL,
  `FILM_AGE_RATING` varchar(8) NOT NULL,
  `FILM_DURATION` int(11) NOT NULL,
  `FILM_DESCRIPTION` varchar(512) NOT NULL,
  `FILM_CAST` varchar(512) NOT NULL,
  PRIMARY KEY (`FILM_TITLE`),
  UNIQUE KEY `FILM_TITLE` (`FILM_TITLE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `films`
--

LOCK TABLES `films` WRITE;
/*!40000 ALTER TABLE `films` DISABLE KEYS */;
INSERT INTO `films` VALUES
('1917',8.2,'Action  Drama  War','2019','16',119,'April 6th  1917. As an infantry battalion assembles to wage war deep in enemy territory  two soldiers are assigned to race against time and deliver a message that will stop 1 600 men from walking straight into a deadly trap.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Avengers: Infinity War',8.4,'Action  Adventure  Sci-Fi','2018','18',149,'The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Django Unchained',8.4,'Drama  Western','2012','18',165,'With the help of a German bounty-hunter  a freed slave sets out to rescue his wife from a brutal plantation-owner in Mississippi.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('DOOM',10,'JUST DOOM','2020','R',66,'you are the absolute chadest person out there','DOOM SLAYER, doctor hayden, vega'),
('Fight Club',8.8,'Drama','1999','12',139,'An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('fight club 2',9.9,'literally me','2069','R',200,'A film based all around literally me','me, me, me'),
('Gran Torino',8.1,'Drama','2008','PG',116,'Disgruntled Korean War veteran Walt Kowalski sets out to reform his neighbor  Thao Lor  a Hmong teenager who tried to steal Kowalski\'s prized possession: a 1972 Gran Torino.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Hamilton',8.4,'Biography  Drama  History  Musical','2020','18',160,'The real life of one of America\'s foremost founding fathers and first Secretary of the Treasury  Alexander Hamilton. Captured live on Broadway from the Richard Rodgers Theater with the original Broadway cast.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Inception',8.8,'Action  Adventure  Sci-Fi  Thriller','2010','18',148,'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.  but his tragic past may doom the project and his team to disaster.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Interstellar',8.6,'Adventure  Drama  Sci-Fi','2014','18',169,'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Jodaeiye Nader az Simin',8.3,'Drama','2011','PG',123,'A married couple are faced with a difficult decision - to improve the life of their child by moving to another country or to stay in Iran and look after a deteriorating parent who has Alzheimer\'s disease.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Joker',8.4,'Crime  Drama  Thriller','2019','12A',122,'A mentally troubled stand-up comedian embarks on a downward spiral that leads to the creation of an iconic villain.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Jurassic Park',8.2,'Action  Adventure  Sci-Fi  Thriller','1993','12A',127,'A pragmatic paleontologist touring an almost complete theme park on an island in Central America is tasked with protecting a couple of kids after a power failure causes the park\'s cloned dinosaurs to run loose.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Scarface',8.3,'Crime  Drama','1983','12A',170,'In 1980 Miami  a determined Cuban immigrant takes over a drug cartel and succumbs to greed.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Sen to Chihiro no kamikakushi',8.6,'Animation  Adventure  Family  Fantasy  Mystery','2001','12A',125,'During her family\'s move to the suburbs  a sullen 10-year-old girl wanders into a world ruled by gods  witches  and spirits  and where humans are changed into beasts.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Shutter Island',8.2,'Mystery  Thriller','2010','12A',138,'In 1954  a U.S. Marshal investigates the disappearance of a murderer who escaped from a hospital for the criminally insane.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Star Wars: Episode VI - Return of the Jedi',8.3,'Action  Adventure  Fantasy  Sci-Fi','1983','16',131,'After a daring mission to rescue Han Solo from Jabba the Hutt  the Rebels dispatch to Endor to destroy the second Death Star. Meanwhile  Luke struggles to help Darth Vader back from the dark side without falling into the Emperor\'s trap.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Taxi Driver',8.2,'Crime  Drama','1976','18',114,'A mentally unstable veteran works as a nighttime taxi driver in New York City  where the perceived decadence and sleaze fuels his urge for violent action.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('The Batman',7.8,'Action  Crime  Drama  Thriller','2022','12A',176,'When a sadistic serial killer begins murdering key political figures in Gotham  Batman is forced to investigate the city\'s hidden corruption and question his family\'s involvement.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('The Shining',8.4,'Drama  Horror','1980','12A',146,'A family heads to an isolated hotel for the winter where a sinister presence influences the father into violence  while his psychic son sees horrific forebodings from both past and future.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Toy Story',8.3,'Animation  Adventure  Comedy  Family  Fantasy','1995','PG',81,'A cowboy doll is profoundly threatened and jealous when a new spaceman action figure supplants him as top toy in a boy\'s bedroom.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Trainspotting',8.1,'Drama','1996','18',93,'Renton  deeply immersed in the Edinburgh drug scene  tries to clean up and get out  despite the allure of the drugs and influence of friends.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('Up',8.3,'Animation  Adventure  Comedy  Drama  Family','2009','PG',96,'78-year-old Carl Fredricksen travels to Paradise Falls in his house equipped with balloons  inadvertently taking a young stowaway.','Ryan Gosling  Christian Bale  Robert De Niro\r'),
('V for Vendetta',8.2,'Action  Drama  Sci-Fi  Thriller','2005','12A',132,'In a future British dystopian society  a shadowy freedom fighter  known only by the alias of \"V\"  plots to overthrow the tyrannical government - with the help of a young woman.','Ryan Gosling  Christian Bale  Robert De Niro\r');
/*!40000 ALTER TABLE `films` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `listings`
--

DROP TABLE IF EXISTS `listings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `listings` (
  `LISTING_ID` int(11) NOT NULL AUTO_INCREMENT,
  `LISTING_DATE` date DEFAULT NULL,
  `FILM_TITLE` varchar(64) DEFAULT NULL,
  `CINEMA_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`LISTING_ID`),
  KEY `FILM_TITLE` (`FILM_TITLE`),
  KEY `CINEMA_ID` (`CINEMA_ID`),
  CONSTRAINT `listings_ibfk_1` FOREIGN KEY (`FILM_TITLE`) REFERENCES `films` (`FILM_TITLE`),
  CONSTRAINT `listings_ibfk_2` FOREIGN KEY (`CINEMA_ID`) REFERENCES `cinemas` (`CINEMA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `listings`
--

LOCK TABLES `listings` WRITE;
/*!40000 ALTER TABLE `listings` DISABLE KEYS */;
INSERT INTO `listings` VALUES
(30,'2023-01-12','1917',2),
(31,'2023-01-12','Avengers: Infinity War',2),
(32,'2023-01-12','DOOM',2),
(33,'2023-02-12','Fight Club',2),
(34,'2023-02-12','Jodaeiye Nader az Simin',10),
(35,'2023-02-12','Jodaeiye Nader az Simin',2),
(36,'2023-01-12','Star Wars: Episode VI - Return of the Jedi',1),
(37,'2023-01-12','Joker',1),
(38,'2023-01-11','Joker',11),
(39,'2023-01-11','Sen to Chihiro no kamikakushi',11),
(40,'2023-01-11','The Batman',11),
(41,'2023-01-13','The Batman',11),
(42,'2023-01-15','The Batman',11),
(43,'2023-01-15','The Batman',3),
(44,'2023-01-15','The Batman',3),
(45,'2023-01-15','Shutter Island',3),
(46,'2023-01-12','Shutter Island',3),
(47,'2023-01-12','1917',3),
(48,'2023-01-12','1917',12),
(49,'2023-01-12','1917',12),
(50,'2023-01-12','1917',4),
(51,'2023-01-12','1917',4),
(52,'2023-01-12','Hamilton',13),
(53,'2023-01-12','Jurassic Park',13),
(54,'2023-01-12','The Shining',13);
/*!40000 ALTER TABLE `listings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `screens`
--

DROP TABLE IF EXISTS `screens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `screens` (
  `SCREEN_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SCREEN_NUM_VIP_SEATS` int(11) NOT NULL,
  `SCREEN_NUM_UPPER_SEATS` int(11) NOT NULL,
  `SCREEN_NUM_LOWER_SEATS` int(11) NOT NULL,
  `CINEMA_ID` int(11) NOT NULL,
  `SCREEN_NUMBER` int(11) NOT NULL,
  PRIMARY KEY (`SCREEN_ID`),
  KEY `CINEMA_ID` (`CINEMA_ID`),
  CONSTRAINT `screens_ibfk_1` FOREIGN KEY (`CINEMA_ID`) REFERENCES `cinemas` (`CINEMA_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `screens`
--

LOCK TABLES `screens` WRITE;
/*!40000 ALTER TABLE `screens` DISABLE KEYS */;
INSERT INTO `screens` VALUES
(1,5,30,15,1,1),
(2,6,43,21,1,2),
(3,7,49,24,1,3),
(4,8,62,30,1,4),
(5,9,68,33,1,5),
(6,10,74,36,1,6),
(7,5,30,15,2,1),
(8,6,43,21,2,2),
(9,7,49,24,2,3),
(10,8,62,30,2,4),
(11,9,68,33,2,5),
(12,10,74,36,2,6),
(13,5,30,15,3,1),
(14,6,43,21,3,2),
(15,7,49,24,3,3),
(16,8,62,30,3,4),
(17,9,68,33,3,5),
(18,10,74,36,3,6),
(19,5,30,15,4,1),
(20,6,43,21,4,2),
(21,7,49,24,4,3),
(22,8,62,30,4,4),
(23,9,68,33,4,5),
(24,10,74,36,4,6),
(45,10,74,36,10,0),
(46,10,74,36,10,1),
(47,10,74,36,10,2),
(48,10,74,36,10,3),
(49,10,74,36,10,4),
(50,10,74,36,11,0),
(51,10,74,36,11,1),
(52,10,74,36,11,2),
(53,10,74,36,11,3),
(54,10,74,36,11,4),
(55,10,74,36,11,5),
(56,10,74,36,12,0),
(57,10,74,36,12,1),
(58,10,74,36,12,2),
(59,10,74,36,13,0),
(60,10,74,36,13,1),
(61,10,74,36,13,2),
(62,10,74,36,13,3);
/*!40000 ALTER TABLE `screens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shows`
--

DROP TABLE IF EXISTS `shows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shows` (
  `SHOW_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SHOW_TIME` time DEFAULT NULL,
  `SCREEN_ID` int(11) DEFAULT NULL,
  `LISTING_ID` int(11) DEFAULT NULL,
  PRIMARY KEY (`SHOW_ID`),
  KEY `SCREEN_ID` (`SCREEN_ID`),
  KEY `LISTING_ID` (`LISTING_ID`),
  CONSTRAINT `shows_ibfk_2` FOREIGN KEY (`SCREEN_ID`) REFERENCES `screens` (`SCREEN_ID`),
  CONSTRAINT `shows_ibfk_3` FOREIGN KEY (`LISTING_ID`) REFERENCES `listings` (`LISTING_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=438 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shows`
--

LOCK TABLES `shows` WRITE;
/*!40000 ALTER TABLE `shows` DISABLE KEYS */;
INSERT INTO `shows` VALUES
(365,'08:00:00',7,30),
(366,'13:00:00',7,30),
(367,'18:00:00',7,31),
(368,'09:00:00',8,31),
(369,'12:00:00',8,31),
(370,'19:00:00',8,30),
(371,'19:00:00',9,32),
(372,'09:00:00',9,32),
(373,'09:00:00',10,32),
(374,'09:00:00',45,34),
(375,'09:00:00',46,34),
(376,'09:00:00',47,34),
(377,'09:00:00',48,34),
(378,'09:00:00',49,34),
(379,'12:00:00',45,34),
(380,'12:00:00',46,34),
(381,'12:00:00',47,34),
(382,'12:00:00',48,34),
(383,'12:00:00',49,34),
(384,'15:00:00',45,34),
(385,'15:00:00',46,34),
(386,'15:00:00',47,34),
(387,'15:00:00',48,34),
(388,'15:00:00',49,34),
(389,'08:00:00',50,38),
(390,'08:00:00',51,38),
(391,'08:00:00',52,38),
(392,'08:00:00',53,38),
(393,'18:00:00',50,38),
(394,'18:00:00',51,38),
(395,'18:00:00',52,38),
(396,'18:00:00',53,38),
(397,'18:00:00',50,41),
(398,'18:00:00',51,41),
(399,'18:00:00',52,41),
(400,'11:00:00',50,41),
(401,'11:00:00',51,41),
(402,'11:00:00',52,41),
(403,'11:00:00',53,41),
(404,'21:00:00',53,41),
(405,'21:00:00',54,41),
(406,'21:00:00',55,41),
(407,'21:00:00',50,42),
(408,'21:00:00',51,42),
(409,'21:00:00',52,42),
(410,'21:00:00',53,42),
(411,'21:00:00',54,42),
(412,'21:00:00',55,42),
(413,'11:00:00',50,42),
(414,'11:00:00',51,42),
(415,'11:00:00',52,42),
(416,'11:00:00',53,42),
(417,'11:00:00',54,42),
(418,'16:00:00',50,42),
(419,'16:00:00',51,42),
(420,'16:00:00',52,42),
(421,'16:00:00',53,42),
(422,'08:00:00',55,42),
(423,'08:00:00',13,45),
(424,'08:00:00',14,45),
(425,'08:00:00',15,45),
(426,'08:00:00',16,45),
(427,'08:00:00',17,45),
(428,'08:00:00',18,45),
(429,'08:00:00',56,48),
(430,'08:00:00',57,48),
(431,'08:00:00',58,48),
(432,'17:00:00',56,48),
(433,'17:00:00',57,48),
(434,'17:00:00',58,48),
(435,'23:00:00',56,49),
(436,'23:00:00',57,49),
(437,'23:00:00',58,48);
/*!40000 ALTER TABLE `shows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `times_of_day`
--

DROP TABLE IF EXISTS `times_of_day`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `times_of_day` (
  `NAME` varchar(32) NOT NULL,
  `START_TIME` time NOT NULL,
  `END_TIME` time NOT NULL,
  PRIMARY KEY (`NAME`),
  UNIQUE KEY `START_TIME` (`START_TIME`),
  UNIQUE KEY `END_TIME` (`END_TIME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `times_of_day`
--

LOCK TABLES `times_of_day` WRITE;
/*!40000 ALTER TABLE `times_of_day` DISABLE KEYS */;
INSERT INTO `times_of_day` VALUES
('afternoon','12:00:00','17:00:00'),
('evening','17:00:00','23:59:59'),
('morning','08:00:00','12:00:00');
/*!40000 ALTER TABLE `times_of_day` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_types`
--

DROP TABLE IF EXISTS `user_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_types` (
  `USER_TYPE` varchar(16) NOT NULL,
  PRIMARY KEY (`USER_TYPE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_types`
--

LOCK TABLES `user_types` WRITE;
/*!40000 ALTER TABLE `user_types` DISABLE KEYS */;
INSERT INTO `user_types` VALUES
('admin'),
('booking_staff'),
('manager');
/*!40000 ALTER TABLE `user_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `USER_ID` int(11) NOT NULL AUTO_INCREMENT,
  `USER_NAME` varchar(64) NOT NULL,
  `USER_PASSWORD_HASH` varchar(128) NOT NULL,
  `USER_TYPE` varchar(16) NOT NULL,
  `CINEMA_ID` int(11) NOT NULL,
  PRIMARY KEY (`USER_ID`),
  KEY `CINEMA_ID` (`CINEMA_ID`),
  KEY `USER_TYPE` (`USER_TYPE`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`CINEMA_ID`) REFERENCES `cinemas` (`CINEMA_ID`),
  CONSTRAINT `users_ibfk_2` FOREIGN KEY (`USER_TYPE`) REFERENCES `user_types` (`USER_TYPE`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
(1,'b','$5$rounds=535000$1UmwtBHYsAl3ObrD$7W2IAdI8DTmTZHAhZvuQDYZ8i09zcbYdHoVSFBfujF2','booking_staff',1),
(2,'a','$5$rounds=535000$1UmwtBHYsAl3ObrD$7W2IAdI8DTmTZHAhZvuQDYZ8i09zcbYdHoVSFBfujF2','admin',1),
(3,'y','$5$rounds=535000$1UmwtBHYsAl3ObrD$7W2IAdI8DTmTZHAhZvuQDYZ8i09zcbYdHoVSFBfujF2','manager',1),
(5,'bristol booking_staff','$5$rounds=535000$ORhVGzY5NRb8rGFR$Mo0/ygyZjURpqtb/p1/MkFpqpDQfb6Nt5xQPfjDGTx9','booking_staff',1),
(6,'bristol admin','$5$rounds=535000$4I6TzosBXz3FfKw.$Od2kjMyVco4gukliYyrhYL9DZwI699k70CNEsvLtuU8','admin',1),
(7,'bristol manager','$5$rounds=535000$QCJQUWP08uqDJGVH$ykfp4SoAzpivZSMk9IUortS2yzwCA5aNheOvVqpjAT0','manager',1),
(8,'birmigham booking_staff','$5$rounds=535000$LG1LFqg9RNYoAUXn$BBuYEsE6zZwDgYR3GnEcxXGmQHR3TprcikxDVsnlTlD','booking_staff',2),
(9,'birmingham admin','$5$rounds=535000$3CkRSIvDcmpe2fm1$1njZEqPXTsbfRiyEVSXJDxs4.jcEjm/tDwTO0W2ZmN4','admin',2),
(10,'cardiff admin','$5$rounds=535000$mZCZTnCdVNfrrL6p$BPWJe3tHN4q9wqqorfEwrY7KDR5Oddy8xUReFSIsvv8','admin',3),
(11,'birmingham manager','$5$rounds=535000$SaSvS6qWzgxZfBkO$q.x..m6H.wYhkCnCxJYD.lDCB.4JGMtvmxNlJ9fDjYC','manager',2),
(12,'cardiff booking staff','$5$rounds=535000$BL6wxAhmFIxJCSdA$3zco3ZBkZtAJOnevggl0HSOcGRc1P5MA729yvwmRYf8','admin',3),
(13,'cardiff manager','$5$rounds=535000$LBZhlO.IpI54tHOW$rqmho0j0sUveP5JA67FpFzR1wrTx/e/4WGLUFeiM6g/','manager',3),
(14,'london admin','$5$rounds=535000$TxPIV7J9b.sGTeqP$FCXCuacBTvTjqt5PKDxh.VBxKklTNQNu.tsBs.k2hDC','admin',4),
(15,'london booking_staff','$5$rounds=535000$aj5XDfoFn8kCTC1g$BqSdHvnIVkIOd9/mVQ/GCOjoZqxY59J04NXfDi3yBo/','booking_staff',4),
(16,'london manager','$5$rounds=535000$lvuO0fPXQgMFSwVv$mHGQnA4b0NiuT9S5/SANfQ3uPMbarmOHj2V7SI.ztW8','manager',4);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-08 14:48:56
