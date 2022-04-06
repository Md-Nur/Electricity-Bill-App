-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: test_elec_bill
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `miter`
--

DROP TABLE IF EXISTS `miter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `miter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `1st_sub1` int NOT NULL,
  `1st_sub2` int NOT NULL,
  `1st_main` int NOT NULL,
  `2nd_sub1` int NOT NULL,
  `2nd_sub2` int NOT NULL,
  `2nd_main` int NOT NULL,
  `4th_sub1` int NOT NULL,
  `4th_sub2` int NOT NULL,
  `4th_sub3` int NOT NULL,
  `4th_sub4` int NOT NULL,
  `month` varchar(45) NOT NULL,
  `year` int NOT NULL,
  `current_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `miter`
--

LOCK TABLES `miter` WRITE;
/*!40000 ALTER TABLE `miter` DISABLE KEYS */;
INSERT INTO `miter` VALUES (136,309,4516,0,2706,3193,2028,734,921,2721,892,'ফেব্রুয়ারি',2022,'2022-03-16 21:28:11'),(200,422,4601,0,2771,3281,2144,762,961,2843,966,'মার্চ',2022,'2022-04-01 20:56:06');
/*!40000 ALTER TABLE `miter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `id` int NOT NULL AUTO_INCREMENT,
  `room_no` int NOT NULL,
  `year` int NOT NULL,
  `month` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `rate` decimal(10,2) NOT NULL,
  `room_fare` int NOT NULL,
  `room_unit` int NOT NULL,
  `room_advance` int DEFAULT NULL,
  `room_dust` int DEFAULT NULL,
  `room_kichen` int DEFAULT NULL,
  `room_toylet` int DEFAULT NULL,
  `room_frize` int DEFAULT NULL,
  `current_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=371 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (1,101,2022,'ফেব্রুয়ারি','শরীফ',5.72,7500,0,0,50,0,0,0,'2022-03-17 11:36:12'),(2,102,2022,'ফেব্রুয়ারি','আরিফ ',5.45,5300,0,0,30,0,0,0,'2022-03-17 12:20:41'),(3,103,2022,'ফেব্রুয়ারি','নাই',5.45,6300,0,0,30,0,0,0,'2022-03-17 12:21:44'),(4,201,2022,'ফেব্রুয়ারি','নূরজাহান',5.45,5000,0,0,35,25,0,0,'2022-03-17 12:23:28'),(5,202,2022,'ফেব্রুয়ারি','কাশেম',5.45,5000,0,0,35,0,0,0,'2022-03-17 12:25:41'),(6,203,2022,'ফেব্রুয়ারি','ইমরান',5.45,6500,0,0,35,0,0,0,'2022-03-17 12:26:27'),(7,401,2022,'ফেব্রুয়ারি','স্যার',5.45,4000,0,0,30,0,0,0,'2022-03-17 12:27:16'),(8,402,2022,'ফেব্রুয়ারি','মরিয়ম',5.45,4300,0,0,30,0,0,0,'2022-03-17 12:28:17'),(9,403,2022,'ফেব্রুয়ারি','শান্তা',5.45,0,0,0,30,0,0,0,'2022-03-17 12:28:48'),(10,404,2022,'ফেব্রুয়ারি','সোহাগ',5.45,5500,0,0,30,25,0,0,'2022-03-17 12:29:45'),(361,101,2022,'মার্চ','শরীফ',5.72,7500,113,0,50,0,0,0,'2022-04-01 20:56:06'),(362,102,2022,'মার্চ','আরিফ ',5.72,5300,85,0,30,0,0,0,'2022-04-01 20:56:06'),(363,103,2022,'মার্চ','নাই',5.72,6300,0,0,30,0,0,0,'2022-04-01 20:56:06'),(364,201,2022,'মার্চ','নূরজাহান',5.72,5000,65,0,35,25,0,0,'2022-04-01 20:56:06'),(365,202,2022,'মার্চ','কাশেম',5.72,5000,88,0,35,0,0,0,'2022-04-01 20:56:06'),(366,203,2022,'মার্চ','ইমরান',5.72,6500,116,0,35,0,0,0,'2022-04-01 20:56:06'),(367,401,2022,'মার্চ','স্যার',5.72,4000,28,0,30,0,0,0,'2022-04-01 20:56:06'),(368,402,2022,'মার্চ','মরিয়ম',5.72,4300,40,0,30,0,0,0,'2022-04-01 20:56:06'),(369,403,2022,'মার্চ','শান্তা',5.72,0,122,0,30,0,0,0,'2022-04-01 20:56:06'),(370,404,2022,'মার্চ','সোহাগ',5.72,5500,74,0,0,25,0,0,'2022-04-01 20:56:06');
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-06 17:06:20
