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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=364 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-06 19:29:32
