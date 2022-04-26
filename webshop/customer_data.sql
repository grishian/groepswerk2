-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server versie:                10.6.5-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Versie:              11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumpen data van tabel webshop.t_customer: ~2 rows (ongeveer)
DELETE FROM `t_customer`;
/*!40000 ALTER TABLE `t_customer` DISABLE KEYS */;
INSERT INTO `t_customer` (`PK_ID`, `F_CREATEON`, `F_UPDATEDON`, `F_NAME`, `F_COUNTRY`, `F_CITY`, `F_STREET`, `F_NR_EXTRA`, `F_ZIP`, `F_PHONE_NR`, `F_MAIL`, `F_WHISLIST_id`) VALUES
	(1, '2022-03-22 21:33:29', '2022-03-22 21:35:16', 'Bob', NULL, NULL, NULL, NULL, NULL, '09999999', 'grishian1@hotmail.com', NULL),
	(2, '2022-03-23 13:06:39', '2022-03-23 13:06:39', 'grishian', NULL, NULL, NULL, NULL, NULL, '08888888', 'grigri2@hotmail.odm', NULL),
	(3, '2022-03-22 21:33:29', '2022-03-22 21:35:16', 'dirk', NULL, NULL, NULL, NULL, NULL,, '09999999', 'grishian3@hotmail.com', NULL),
	(4, '2022-03-23 13:06:39', '2022-03-23 13:06:39', 'jan', NULL, NULL, NULL, NULL, NULL, '08888888', 'grigri4@hotmail.odm', NULL),
	(5, '2022-03-22 21:33:29', '2022-03-22 21:35:16', 'fien', NULL, NULL, NULL, NULL, NULL, '09999999', 'grishian5@hotmail.com', NULL),
	(6, '2022-03-23 13:06:39', '2022-03-23 13:06:39', 'diter', NULL, NULL, NULL, NULL, NULL, '08888888', 'grigri6@hotmail.odm', NULL);
/*!40000 ALTER TABLE `t_customer` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
