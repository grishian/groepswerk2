-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.6.4-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping data for table webshop.t_book: ~2 rows (approximately)
/*!40000 ALTER TABLE `t_book` DISABLE KEYS */;
INSERT INTO `t_book` (`PK_ID`, `F_CREATEON`, `F_UPDATEDON`, `F_TYPE`, `F_TITLE`, `F_AUTHOR`, `F_ISBN`, `F_GENRE`, `F_PRICE`, `F_LANGUAGE`, `F_SERIES`, `F_SIZE`) VALUES
	(2, '2022-03-23 13:06:08', '2022-03-23 13:06:08', 'ebook', 'Fallen', 'Lauren Kate', '100', 'Fantasy', '12', 'English', 'Fallen', '258'),
	(3, '2022-03-23 13:07:41', '2022-03-23 13:07:41', 'audiobook', 'Lavender Hill', 'Stephen Fry', '101', 'Novel', '8', 'Dutch', 'Calm', '45'),
	(4, '2022-03-23 13:06:08', '2022-03-23 13:06:08', 'ebook', 'Teardrop', 'Lauren Kate', '102', 'Fantasy', '14', 'English', 'Fallen', '311'),
	(5, '2022-03-23 13:06:08', '2022-03-23 13:06:08', 'audiobook', 'Encanto', 'Lin Manuel Miranda', '103', 'Kids', '9', 'Spanish', 'Disney', '120'),
	(6, '2022-03-23 13:06:08', '2022-03-23 13:06:08', 'physicalbook', 'A court of thorns and roses', 'Sarah J Maas', '104', 'Romance', '12', 'English', 'Court', '354'),
	(7, '2022-03-23 13:06:08', '2022-03-23 13:06:08', 'physicalbook', 'The Lord of the rings', 'Tolkien', '105', 'Sci-fi', '17', 'English', 'LOTR', '387');
/*!40000 ALTER TABLE `t_book` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
