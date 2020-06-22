-- MySQL dump 10.17  Distrib 10.3.22-MariaDB, for debian-linux-gnueabihf (armv8l)
--
-- Host: localhost    Database: ipsen5groep11
-- ------------------------------------------------------
-- Server version	10.3.22-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Batch`
--

DROP TABLE IF EXISTS `Batch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Batch` (
  `BatchID` varchar(255) NOT NULL,
  `BatchName` varchar(255) NOT NULL,
  `StandardMessage` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`BatchID`),
  UNIQUE KEY `BatchID` (`BatchID`),
  KEY `Batch_fk0` (`StandardMessage`),
  CONSTRAINT `Batch_fk0` FOREIGN KEY (`StandardMessage`) REFERENCES `MessageTemplate` (`MessageID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Batch`
--

LOCK TABLES `Batch` WRITE;
/*!40000 ALTER TABLE `Batch` DISABLE KEYS */;
INSERT INTO `Batch` VALUES ('Datadump voorbeeld bestand.xlsx','Datadump voorbeeld bestand.xlsx',NULL),('Datadump voorbeeld bestand4.xlsx','Datadump voorbeeld bestand4.xlsx',NULL),('Datadump voorbeeld bestand7.xlsx','Datadump voorbeeld bestand7.xlsx',NULL),('Datadump_voorbeeld_bestand.xlsx','Datadump_voorbeeld_bestand.xlsx',NULL);
/*!40000 ALTER TABLE `Batch` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BatchContactPersoon`
--

DROP TABLE IF EXISTS `BatchContactPersoon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BatchContactPersoon` (
  `Contactpersoon` varchar(255) NOT NULL,
  `Batch` varchar(255) NOT NULL,
  PRIMARY KEY (`Contactpersoon`,`Batch`),
  KEY `BatchContactPersoon_fk1` (`Batch`),
  CONSTRAINT `BatchContactPersoon_fk0` FOREIGN KEY (`Contactpersoon`) REFERENCES `ContactPersoon` (`UserID`),
  CONSTRAINT `BatchContactPersoon_fk1` FOREIGN KEY (`Batch`) REFERENCES `Batch` (`BatchID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BatchContactPersoon`
--

LOCK TABLES `BatchContactPersoon` WRITE;
/*!40000 ALTER TABLE `BatchContactPersoon` DISABLE KEYS */;
INSERT INTO `BatchContactPersoon` VALUES ('432e52b2e278dcc7586ed4213256f210b7bd6536bf9b3071c642718c7a514eac','Datadump voorbeeld bestand4.xlsx'),('a3002e260050a9943af0fe3d30073fe6e8c5e741752e97483a3cc987f95f910e','Datadump_voorbeeld_bestand.xlsx'),('c34d8eaf3fe15d540a17821b29d2b5d5844b5a9133d7c59453fc118fdbadc58e','Datadump voorbeeld bestand7.xlsx'),('d6c71c4471bd9c36b56aa9b63e54f0e452f2e10eb29e7d01bad80b89956b766a','Datadump voorbeeld bestand.xlsx'),('d6c71c4471bd9c36b56aa9b63e54f0e452f2e10eb29e7d01bad80b89956b766a','Datadump_voorbeeld_bestand.xlsx'),('e2d4257514dc7671d3321209d0c83f7f52f2e10eb29e7d01bad80b89956b766a','Datadump voorbeeld bestand.xlsx'),('e2d4257514dc7671d3321209d0c83f7f52f2e10eb29e7d01bad80b89956b766a','Datadump_voorbeeld_bestand.xlsx'),('e6958e9fe19be5239698530a5a45b4cb4fc462e4a38b1ef860b237ff0659773d','Datadump voorbeeld bestand4.xlsx');
/*!40000 ALTER TABLE `BatchContactPersoon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Chatbot`
--

DROP TABLE IF EXISTS `Chatbot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Chatbot` (
  `Username` varchar(50) NOT NULL,
  `UserPassword` varchar(255) NOT NULL,
  `Platform` varchar(255) NOT NULL,
  PRIMARY KEY (`Username`),
  KEY `Chatbot_fk0` (`Platform`),
  CONSTRAINT `Chatbot_fk0` FOREIGN KEY (`Platform`) REFERENCES `Platform` (`PlatformName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Chatbot`
--

LOCK TABLES `Chatbot` WRITE;
/*!40000 ALTER TABLE `Chatbot` DISABLE KEYS */;
/*!40000 ALTER TABLE `Chatbot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Contact`
--

DROP TABLE IF EXISTS `Contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Contact` (
  `Username` varchar(255) NOT NULL,
  `Platform` varchar(255) NOT NULL,
  `UserID` varchar(255) NOT NULL,
  PRIMARY KEY (`Username`,`Platform`),
  KEY `Contact_fk0` (`Platform`),
  KEY `Contact_fk1` (`UserID`),
  CONSTRAINT `Contact_fk0` FOREIGN KEY (`Platform`) REFERENCES `Platform` (`PlatformName`),
  CONSTRAINT `Contact_fk1` FOREIGN KEY (`UserID`) REFERENCES `ContactPersoon` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Contact`
--

LOCK TABLES `Contact` WRITE;
/*!40000 ALTER TABLE `Contact` DISABLE KEYS */;
INSERT INTO `Contact` VALUES ('Thomas','whatssssapp,snapchat','2042101ac1f6e7741bfe43f3672e6d7c7fcd4d2535fac49da67b2115c85334a4'),('woeejwej','whatsapp','260550ea68207372d657367b6de47a00c4f79e15f8c6ed0715a8ea44aebc38d8'),('joumoma','snapchat','425b30a5c94efff0a991bcd562303497e6a7130b80d82c439b42321b8d31094f'),('sjoerd','insta','432e52b2e278dcc7586ed4213256f210b7bd6536bf9b3071c642718c7a514eac'),('Justsssassssaaswddsswwwdwdwdwdomebody','whatssssapp,snapchat','464b4694009bc16611242b9f7f3defdf7fcd4d2535fac49da67b2115c85334a4'),('Justsssasssaaswddsswwwdwdwdwdomebody','whatssssapp,snapchat','4b639f1da47802e67255b54f02d40d217fcd4d2535fac49da67b2115c85334a4'),('joumddeasasaaswwdwoma','snaspchat','5f3cb742e43b10a501270cd409f129b5640ba2370c69f1242beace90276cc804'),('assas','assas','600d475fa96e30530b548c9cfbb85187600d475fa96e30530b548c9cfbb85187'),('wejo','bookface','8729cf270309a06fb95118fee420bd8ed07aa810539ae54c093a998349dd1539'),('sss','sss','9f6e6800cfae7749eb6c486619254b9c9f6e6800cfae7749eb6c486619254b9c'),('CKMofficial1','kik','a3002e260050a9943af0fe3d30073fe6e8c5e741752e97483a3cc987f95f910e'),('Anthsony2','snaspchat','b3297c0a30c169527edc56403656b76e640ba2370c69f1242beace90276cc804'),('mekatsten','facesmoel','c34d8eaf3fe15d540a17821b29d2b5d5844b5a9133d7c59453fc118fdbadc58e'),('jemoermoer','bookie','c41da11875328dea57f88ee198f9f7819f535b6ae672f627e4e5f79f2b7c63fe'),('Justsomebody','whatsapp,snapchat, kik','d6c71c4471bd9c36b56aa9b63e54f0e452f2e10eb29e7d01bad80b89956b766a'),('Justsomebody','whatsapp,snapchat','d6c71c4471bd9c36b56aa9b63e54f0e479188f5d22d9f5e7a20bc1e053245f54'),('Thsomas','whatssssapp,snapchat','e15bd765efcf652d4dac45741792280a7fcd4d2535fac49da67b2115c85334a4'),('Justsomebody2','whatsapp,snapchat, kik','e2d4257514dc7671d3321209d0c83f7f52f2e10eb29e7d01bad80b89956b766a'),('jemoer','facebook, meida','e6958e9fe19be5239698530a5a45b4cb4fc462e4a38b1ef860b237ff0659773d'),('thomas','facebook','ef6e65efc188e7dffd7335b646a85a2126cae7718c32180a7a0f8e19d6d40a59'),('thesedlife','kik ','efffc53cd9c0640226f0f66d9c5535f46141ba778e106295983fccd9384a7d3a'),('Anthony2','snaspchat','f2b8139131e85264c1d1aca08685f110640ba2370c69f1242beace90276cc804');
/*!40000 ALTER TABLE `Contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ContactPersoon`
--

DROP TABLE IF EXISTS `ContactPersoon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ContactPersoon` (
  `UserID` varchar(255) NOT NULL,
  `ContactName` varchar(255) DEFAULT NULL,
  `OriginalPost` varchar(255) DEFAULT NULL,
  `CustomMessage` varchar(255) NOT NULL,
  `SocialMedia` varchar(255) DEFAULT NULL,
  `Info` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `UserID` (`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ContactPersoon`
--

LOCK TABLES `ContactPersoon` WRITE;
/*!40000 ALTER TABLE `ContactPersoon` DISABLE KEYS */;
INSERT INTO `ContactPersoon` VALUES ('2042101ac1f6e7741bfe43f3672e6d7c7fcd4d2535fac49da67b2115c85334a4','Thomas','65.432.1.xxx','Leeg',NULL,'Teksfcesdcvscacast van het bericht'),('260550ea68207372d657367b6de47a00c4f79e15f8c6ed0715a8ea44aebc38d8',NULL,'2332.2323.23','Leeg',NULL,'vervelend'),('2d02e669731cbade6a64b58d602cf2a49f6e6800cfae7749eb6c486619254b9c','kummGAMER','hoi help mij','Focus op je school man..','insta','dit is mijn test info'),('425b30a5c94efff0a991bcd562303497e6a7130b80d82c439b42321b8d31094f',NULL,'34.34.34','Helpme',NULL,'Helpme'),('432e52b2e278dcc7586ed4213256f210b7bd6536bf9b3071c642718c7a514eac',NULL,'33.33.33.x','Leeg',NULL,'Het is je boi Wino'),('464b4694009bc16611242b9f7f3defdf7fcd4d2535fac49da67b2115c85334a4','Justsssassssaaswddsswwwdwdwdwdomebody','65.432.1.xxx','Leeg',NULL,'Teksfcesdcvscacast van het bericht'),('4b639f1da47802e67255b54f02d40d217fcd4d2535fac49da67b2115c85334a4','Justsssasssaaswddsswwwdwdwdwdomebody','65.432.1.xxx','Leeg',NULL,'Teksfcesdcvscacast van het bericht'),('5f3cb742e43b10a501270cd409f129b5640ba2370c69f1242beace90276cc804','joumddeasasaaswwdwoma','34.34.34','Leeg',NULL,'Haccdwqssseqcewqqcelpme'),('600d475fa96e30530b548c9cfbb85187600d475fa96e30530b548c9cfbb85187','tessKiller64','what up gamers!?','dit is een test custom bericht','kik','Dit is een tessa :0'),('8729cf270309a06fb95118fee420bd8ed07aa810539ae54c093a998349dd1539','wejo','123.xxx.xxx.xxxx','Leeg',NULL,'last minut '),('8f60c8102d29fcd525162d02eed4566b9f6e6800cfae7749eb6c486619254b9c','antononiyo','doe je best man..','ik doe me best :)','kik','ik doe nogsteets me best'),('9f6e6800cfae7749eb6c486619254b9c9f6e6800cfae7749eb6c486619254b9c',NULL,NULL,'ssss',NULL,NULL),('a3002e260050a9943af0fe3d30073fe6e8c5e741752e97483a3cc987f95f910e','CKMofficial1','42.454.6.xxx','Leeg',NULL,'Ik ben heel alleen'),('b3297c0a30c169527edc56403656b76e640ba2370c69f1242beace90276cc804','Anthsony2','34.34.34','Leeg',NULL,'Haccdwqssseqcewqqcelpme'),('c34d8eaf3fe15d540a17821b29d2b5d5844b5a9133d7c59453fc118fdbadc58e','mekatsten','232.323.232.xxx','Leeg',NULL,'pas op op het internet!'),('c41da11875328dea57f88ee198f9f7819f535b6ae672f627e4e5f79f2b7c63fe','jemoermoer','2323','Leeg',NULL,'wejo'),('d6c71c4471bd9c36b56aa9b63e54f0e452f2e10eb29e7d01bad80b89956b766a','Justsomebody','65.432.1.xxx','Leeg',NULL,'Tekst van het bericht'),('d6c71c4471bd9c36b56aa9b63e54f0e479188f5d22d9f5e7a20bc1e053245f54',NULL,'65.432.1.xxx','Tekst van het bericht',NULL,'Tekst van het bericht'),('e15bd765efcf652d4dac45741792280a7fcd4d2535fac49da67b2115c85334a4','Thsomas','65.432.1.xxx','Leeg',NULL,'Teksfcesdcvscacast van het bericht'),('e2d4257514dc7671d3321209d0c83f7f52f2e10eb29e7d01bad80b89956b766a','Justsomebody2','65.432.1.xxx','Leeg',NULL,'Tekst van het bericht'),('e6958e9fe19be5239698530a5a45b4cb4fc462e4a38b1ef860b237ff0659773d',NULL,'23.2323.xx.xx','Leeg',NULL,'KOMT VECHTEN G'),('ef6e65efc188e7dffd7335b646a85a2126cae7718c32180a7a0f8e19d6d40a59',NULL,'213.322.322.xxx','leuk',NULL,'leuk'),('efffc53cd9c0640226f0f66d9c5535f46141ba778e106295983fccd9384a7d3a','thesedlife','144.12.2.xxx','Leeg',NULL,'Ik voel me onzeker, help me afvallen please.'),('f2b8139131e85264c1d1aca08685f110640ba2370c69f1242beace90276cc804','Anthony2','34.34.34','Leeg',NULL,'Haccdwqssseqcewqqcelpme'),('sss','Pinopilatuspas','yeet','Het internet is een grote plek vol enge mensen. Pas op met wat je post!','facebook','Mentaal instabiel');
/*!40000 ALTER TABLE `ContactPersoon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Log`
--

DROP TABLE IF EXISTS `Log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Log` (
  `Medewerker` varchar(255) NOT NULL,
  `Info` varchar(255) NOT NULL,
  `LogTime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`Medewerker`,`Info`,`LogTime`),
  CONSTRAINT `Log_fk0` FOREIGN KEY (`Medewerker`) REFERENCES `Medewerker` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Log`
--

LOCK TABLES `Log` WRITE;
/*!40000 ALTER TABLE `Log` DISABLE KEYS */;
/*!40000 ALTER TABLE `Log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medewerker`
--

DROP TABLE IF EXISTS `Medewerker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Medewerker` (
  `Email` varchar(50) NOT NULL,
  `UserPassword` varchar(50) NOT NULL,
  `Usertype` varchar(50) NOT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medewerker`
--

LOCK TABLES `Medewerker` WRITE;
/*!40000 ALTER TABLE `Medewerker` DISABLE KEYS */;
INSERT INTO `Medewerker` VALUES ('k.wakkermanm@mederwerker.ckm.nl','ttt','default'),('m.kraft@mederwerker.ckm.nl','meerblokjesismeerbeter','admin'),('m.supermedewerker@ckm.nl','@123fortnightchtmaster@','admin'),('w.de.pino@mederwerker.ckm.nl','kwerkoverwerk','default');
/*!40000 ALTER TABLE `Medewerker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MessageTemplate`
--

DROP TABLE IF EXISTS `MessageTemplate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MessageTemplate` (
  `MessageID` varchar(255) NOT NULL,
  `Message` varchar(255) NOT NULL,
  `Info` varchar(255) NOT NULL,
  PRIMARY KEY (`MessageID`),
  UNIQUE KEY `MessageID` (`MessageID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MessageTemplate`
--

LOCK TABLES `MessageTemplate` WRITE;
/*!40000 ALTER TABLE `MessageTemplate` DISABLE KEYS */;
INSERT INTO `MessageTemplate` VALUES ('0','Wejo G flex niet zo hard dit is niet normaal. Als je zo hard dept en fortnightcht speelt ben je sws een probleem','Geschreven door Jemoeder, bedoel voor doelgroep 8-12 jaar'),('1','Hoi! Lees dit goed. Wees er van bewust dat je in rieel gevaar kan zijn, door de dingen die je post. Neem alsjeblieft contact met ons op.','Geschreven door Isabel, bedoel voor doelgroep 12-25 jaar'),('2','Kijk uit met wat je op internet zet!','Geschreven door Jan, bedoel voor doelgroep 12-40 jaar'),('3','Het internet is een grote plek vol enge mensen. Pas op met wat je post!','Geschreven door Henk, doelgroep: 25-35');
/*!40000 ALTER TABLE `MessageTemplate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Platform`
--

DROP TABLE IF EXISTS `Platform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Platform` (
  `PlatformName` varchar(50) NOT NULL,
  PRIMARY KEY (`PlatformName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Platform`
--

LOCK TABLES `Platform` WRITE;
/*!40000 ALTER TABLE `Platform` DISABLE KEYS */;
INSERT INTO `Platform` VALUES ('assas'),('bookface'),('bookie'),('facebook'),('facebook, meida'),('facesmoel'),('insta'),('kik '),('snapchat'),('snaspchat'),('sss'),('whatsapp'),('whatsapp,snapchat'),('whatsapp,snapchat, kik'),('whatssssapp,snapchat');
/*!40000 ALTER TABLE `Platform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `yeet`
--

DROP TABLE IF EXISTS `yeet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `yeet` (
  `piet` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yeet`
--

LOCK TABLES `yeet` WRITE;
/*!40000 ALTER TABLE `yeet` DISABLE KEYS */;
/*!40000 ALTER TABLE `yeet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-22  5:22:29
