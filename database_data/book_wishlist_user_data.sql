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

-- Dumpen data van tabel webshop.t_book: ~9 rows (ongeveer)
DELETE FROM `t_book`;
/*!40000 ALTER TABLE `t_book` DISABLE KEYS */;
INSERT INTO `t_book` (`F_TYPE`, `F_TITLE`, `F_AUTHOR`, `F_ISBN`, `F_GENRE`, `F_PRICE`, `F_LANGUAGE`, `F_SERIES`, `F_SIZE`, `F_SYNOPSIS`, `F_COVER`) VALUES
	('e-book', 'Een e-book verhaal', 'Grishian Gracida', '01001000100', 'horror', '10,00', 'NL', NULL, '100', 'Een verhaal over een e-book.', 'https://wikiimg.tojsiabtv.com/wikipedia/commons/thumb/0/00/Amazon_Kindle_3.JPG/1200px-Amazon_Kindle_3.JPG'),
	('fysical', 'The Shining', 'Stephen King', '9780385121675', 'horror', '16,99', 'EN', 'NO', '125', 'Scott Carey blijft gewicht verliezen zonder dat zijn uiterlijk verandert, en zo gebeuren er wel meer vreemde dingen. In het plaatsje Castle Rock belandt hij midden in een escalerende ruzie met zijn lesbische buren. Een van hen is vriendelijk, de andere cold as ice. De vrouwen willen een restaurant openen maar de inwoners willen niets weten van een lesbisch koppel. Als Scott inziet met wat voor vooroordelen zij, en hijzelf, te maken hebben, besluit hij te helpen. Onverwachte verbonden, de jaarlijkse hardloopwedstrijd en Scotts mysterieuze aandoening brengen het beste in mensen naar boven. ', 'https://cdn.standaardboekhandel.be/product/9789044354966/front-medium-790144740.jpg'),
	('fysical', 'Piep zei de muis', ' M.J. Arlidge', '9789022595657', 'fiction', '11,00', 'NL', ' Helen Grace', '384', 'Helen Grace is de heldin van de populaire thrillerreeks van M.J. Arlidge.\r\n\r\nZe is een geharde rechercheur die motor rijdt en zich het liefst alleen door het leven slaat, maar wordt achtervolgd door persoonlijke demonen die haar af en toe zelfs in een depressie dreigen te storten. Toch is zij onmisbaar in de strijd tegen psychopaten die Southampton blijven teisteren en onschuldige slachtoffers maken, op gruwelijke wijze… ', 'https://cdn.standaardboekhandel.be/product/9789022595657/front-medium-2456385135.jpg'),
	('fysical', 'De vlucht uit Falaise', 'John Flanagan', '9789025772741', 'fiction', '16,99', 'NL', 'De Grijze Jager', '254', '‘De Grijze Jager 16 – De vlucht uit Falaise’ is deel 16 in de populaire serie van John Flanagan. In het vervolg op de spannende cliffhanger van deel 15 ‘De vermiste prins’ lees je hoe het verder gaat met Maddie en Will. Will en Maddie zijn gevangenen van de machtsbeluste baron Lassigny, die ook de prins die zij hadden willen bevrijden, heeft ontvoerd. Kunnen ze ontsnappen, en hun missie voltooien door de prins veilig thuis te krijgen? De situatie lijkt almaar slechter te worden. De baron speelt een vuil spelletje en de prins berust in zijn lot. Alle hoop op ontsnapping lijkt verloren, maar dan krijgen ze hulp uit onverwachte hoek. Het blijkt maar weer eens dat Grijze Jagers nog niet zo makkelijk opgeven, hoe onmogelijk de missie ook lijkt. ', 'https://cdn.standaardboekhandel.be/product/9789025772741/front-medium-4094174220.jpg'),
	('fysical', 'De gunst', 'Nicci French', '9789026357688', 'fiction', '22,99', 'NL', NULL, '412', 'De gunst is de nieuwe ijzersterke thriller van Nicci French. Jude is een succesvol arts en is gelukkig met haar verloofde Nat. Vanuit het niets duikt haar eerste liefde, Liam, op in het ziekenhuis waar ze werkt. Ze hebben elkaar niet meer gezien sinds hun relatie op dramatische wijze eindigde, jaren eerder. Liam vraagt haar om een bijzondere gunst: zou ze hem dat weekend — alsjeblieft? — willen ontmoeten in een cottage in Norfolk? Weifelend stemt ze toe, en ze verzwijgt haar tripje voor Nat. Maar Liam komt niet opdagen. Even later krijgt ze een telefoontje van de politie dat haar leven totaal op zijn kop zet. Ze probeert erachter te komen wat er precies is gebeurd, maar wordt daardoor steeds verder Liams wereld ingezogen. Zijn familie en vrienden lijken allemaal iets voor haar te verzwijgen. Ze moet dan ook alles op alles zetten om zich staande te houden — en het er levend van af te brengen.', 'https://cdn.standaardboekhandel.be/product/9789026357688/front-medium-1756524833.jpg'),
	('fysical', 'Naar het paradijs', 'Hanya Yanagihara', '9789046828960', 'fiction', '24,99', 'NL', 'none', '672', 'In 1893 maakt New York deel uit van de Vrije Staten, waar mensen ogenschijnlijk mogen liefhebben wie ze willen. David verzet zich tegen de door zijn rijke familie gearrangeerde verloving met een geschikte kandidaat; hij voelt zich meer aangetrokken tot een charismatische maar arme muziekleraar.\r\nIn het door de aidsepidemie geteisterde Manhattan van 1993 woont de jonge Hawaïaanse David samen met zijn veel oudere, rijkere partner, voor wie hij zijn moeilijke jeugd en het lot van zijn vader verzwijgt.\r\nIn 2093 probeert Charlie zich staande te houden in het totalitaire New York zonder de bescherming van haar grootvader, een gerenommeerd wetenschapper. Ze ontmoet David, die zegt haar te kunnen redden - maar kan zij hem vertrouwen?\r\n\r\nDeze drie delen vormen samen een weergaloos epos over familie, verlies en de zoektocht naar liefde. Wat niet alleen de personages, maar ook de verschillende versies van Amerika met elkaar verbindt, is de worsteling met de eigenschappen die ons menselijk maken: angst, liefde, schaamte, afhankelijkheid, eenzaamheid en bovenal het pijnlijke verlangen om degenen van wie we houden te beschermen.', 'https://cdn.standaardboekhandel.be/product/9789046828960/front-medium-1037726691.jpg'),
	('fysical', ' Autorijden van A tot Z : theorie & praktijk ', 'Flor Koninckx, Joe Di Dio', '9789068471564', 'non-fiction', '32,95', 'NL', 'none', '420', '...', 'https://cdn.standaardboekhandel.be/product/9789068471564/front-medium-3213470637.jpg'),
	('fysical', 'Jacht', 'Toni Coppers, Annick Lambert', '9789463937320', 'fiction', '22,99', 'NL', 'Lies Meerhout', '336', '‘s Nachts is de haven van Antwerpen het terrein van de ‘uithalers’, kleine garnalen die voor de drugskartels het vuile werk opknappen en rondsjouwen met sporttassen vol cocaïne. Wanneer een man vrijkomt uit de gevangenis en er aan het hoofd van een maffiafamilie een machtswissel optreedt, worden gewone mensen meegezogen in een draaikolk van wraak en geweld. Of zijn die gewone mensen toch niet zo gewoon? Commissaris Liese Meerhout en hoofdinspecteur Michel Masson ontdekken de gruwel van de drugslogica en moeten vechten om overeind te blijven en hun dierbaren te redden. Toni Coppers staat bekend om zijn ingenieuze en spannende plots. Hij schrijft over mensen van vlees en bloed, die tot leven komen dankzij de uitgewerkte psychologische karaktertekeningen. Net die combinatie van spanning en menselijke diepgang maakt een Coppers lezen zo verslavend. Coppers is zonder twijfel Vlaanderens meest bekroonde misdaadauteur. ', 'https://cdn.standaardboekhandel.be/product/9789463937320/front-medium-2805555821.jpg'),
	('fysical', 'Shelf love', 'Noor Murad, Yotam Ottolengi', '9789464040883', 'free time', '24,99', 'NL', 'Ottolengi test kitchen', '256', 'Van bestsellerauteur Yotam Ottolenghi en zijn superteam van chef-koks is dit Ottolenghi unplugged: onweerstaanbare recepten voor flexibele, doordeweekse gerechten - met alle geheimen om het meeste uit je voorraadkast, koelkast en vriezer te halen. Dit is de OTK-manier om iedere dag heerlijk en stressvrij te eten. In Shelf love neemt Ottolenghi de ingrediënten als uitgangspunt, en bouwt daar de recepten omheen. Heb je nog een blik tomaten achter in de kast staan? Maak dan Geblakerde aubergine met tomaat en tahin. Een verdwaalde courgette in je koelkast? Smul van Gegrilde courgettes met warme yoghurt en saffraanboter! Voor de eerste keer verwelkomt het Ottolenghi Test Kitchen-team ons in hun creatieve ruimte. Hun gerechten bevatten alle smaak en originaliteit die we van Ottolenghi verwachten, maar bieden meer flexibiliteit om ze eigen te maken, met behulp van wat we al in onze keukenkasten kunnen vinden.', 'https://cdn.standaardboekhandel.be/product/9789464040883/front-medium-4106892365.jpg');
/*!40000 ALTER TABLE `t_book` ENABLE KEYS */;

-- Dumpen data van tabel webshop.t_wishlist: ~4 rows (ongeveer)
DELETE FROM `t_wishlist`;
/*!40000 ALTER TABLE `t_wishlist` DISABLE KEYS */;
INSERT INTO `t_wishlist` (`F_ID`, `F_USER_ID`, `F_BOOK_ID`) VALUES
	(14, 1, '9780385121675'),
	(16, 1, '9789026357688'),
	(17, 1, '9789463937320');
/*!40000 ALTER TABLE `t_wishlist` ENABLE KEYS */;

-- Dumpen data van tabel webshop.user: ~8 rows (ongeveer)
DELETE FROM `user`;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `email`, `username`, `password`, `active`, `profile`) VALUES
	(1, 'bob@hotmail.com', 'Bob', 'pbkdf2:sha256:260000$8hEwxSXvyNCh4aBG$ff595e2d0c63dab1d2b551adb30e9a3280914e4c71b2b05cbd16b91d26ca946f', 1, 0),
	(2, 'tim@hotmail.com', 'Tim', 'pbkdf2:sha256:260000$FzwhXkv0mQIp58O7$2b5cea9f54bc65c9ae96b929d37f3a3b24aafb838f530b0ee4a284c6def99653', 1, 1),
	(3, 'dirk@hotmail.com', 'Dirk', 'pbkdf2:sha256:260000$nvxJFXjlkjF4iSBP$e00192240b491edb22986fca5d5729b6115c59c024507785c49d9069569eab99', 1, 1),
	(4, 'wim@hotmail.com', 'Wim', 'pbkdf2:sha256:260000$ohW8U3BK8Jdm5Fon$98f098675f6ae1b79679a99f72f58a6f7f760decaeaadf0c470880d21251a6ed', 1, 0),
	(5, 'daan@hotmail.com', 'Daan', 'pbkdf2:sha256:260000$RsUnBrtgiDEDS3vf$89501061b9a69964e37a3edbc67bb066ec1e7308b6f3e02033b95b1b2f438dee', 1, 1),
	(6, 'nikitavanderaa@gmail.com', 'Skadi', 'pbkdf2:sha256:260000$Avs6FPGoTCzp5NPI$06555b23ce231e3c0d2f2fabf58735b8a8eace179bd0ff61de1c9090a98a21b5', 1, 1),
	(7, 'runy@hotmail.com', 'runy', 'pbkdf2:sha256:260000$h4l4TbETSs0obYjt$0df68dd70c45117c8b055cc0c4678b3f6f7d068a1d2ba54bf27a736da43d237a', 1, 1),
	(8, 'robvc2@gmail.com', 'morectus', 'pbkdf2:sha256:260000$QJJzvZeRvvOAttEa$c572968b2ee6abad398f03cad50850899e7503f39c52a33ee9219c5442e850af', 1, 1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
