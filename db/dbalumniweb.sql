-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 02, 2021 at 04:02 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dbalumniweb`
--

-- --------------------------------------------------------

--
-- Table structure for table `tblalumni`
--

CREATE TABLE IF NOT EXISTS `tblalumni` (
  `alumniid` varchar(50) NOT NULL,
  `alumniname` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` bigint(11) NOT NULL,
  `qual` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `recruited` varchar(10) NOT NULL,
  `company` varchar(50) NOT NULL,
  `designation` varchar(50) NOT NULL,
  PRIMARY KEY (`alumniid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblalumni`
--

INSERT INTO `tblalumni` (`alumniid`, `alumniname`, `gender`, `dob`, `address`, `phone`, `qual`, `image`, `email`, `recruited`, `company`, `designation`) VALUES
('1', 'Vishnu', 'Male', '1993-10-12', 'Aluva', 2147483647, '+2', 'images/ad1.jpg', 'vishnu@gmail.com', '', '', ''),
('2', 'Albert', 'Male', '1993-10-01', 'sfgbstfr', 2147483647, 'BSC', 'images/te1.jpg', 'albert@gmail.com', '', '', ''),
('3', 'thasni ', 'Female', '1999-01-28', 'afssfg', 9446974606, 'ghkhjl', 'images/g4.jpg', 'thachu@gmail.com', '', '', ''),
('4', 'Shilpa', 'Female', '2020-02-08', 'sdgrt', 9651023478, 'MCA', '/media/l4_K3823o0.jpg', 'shilpa@gmail.com', '', '', ''),
('5', 'Jeena', 'Female', '2020-02-05', 'awefrer', 9512364780, 'MCA', '/media/tp2_Aav0obK.jpg', 'jeena@gmail.com', '', '', ''),
('ALMN1', 'Aadhithyan', 'Male', '1991-05-08', 'nvhgv', 7356777874, 'BTech', '/media/t2.jpg', 'aadhithyan@gmail.com', 'Yes', '', ''),
('ALMN15', 'Mridul', 'Male', '1992-08-24', 'jhbhu', 7356777874, 'BTech', '/media/t1.jpg', 'mridul@gmail.com', 'No', '', ''),
('ALMN21', 'Tom', 'Male', '0000-00-00', 'ijnh', 9574861230, 'BTech', '/media/t2_DWnYHWZ.jpg', 'tom@gmail.com', 'Yes', 'Infosys', 'Senior Engineer'),
('ALMN25', 'vyshnavi', 'Female', '2020-10-27', 'sdfgh', 7356777874, 'gvbh', '/media/bridal-mehndi-designs5.jpg', 'vyshnavi@gmail.com', 'Yes', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `tblbatchdetails`
--

CREATE TABLE IF NOT EXISTS `tblbatchdetails` (
  `name` varchar(50) NOT NULL,
  `yop` int(11) NOT NULL,
  `regno` varchar(50) NOT NULL,
  `alumniid` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tblbatchdetails`
--

INSERT INTO `tblbatchdetails` (`name`, `yop`, `regno`, `alumniid`, `contact`) VALUES
('Aadhithyan', 2012, '401526', 'ALMN1', '7356777874'),
('Abhijith', 2012, '401527', 'ALMN2', '7356777874'),
('Anandhu', 2012, '401528', 'ALMN3', '7356777874'),
('Anju', 2012, '401529', 'ALMN4', '7356777874'),
('Anna', 2012, '401530', 'ALMN5', '7356777874'),
('Arjun', 2012, '401531', 'ALMN6', '7356777874'),
('Athul', 2012, '401532', 'ALMN7', '7356777874'),
('Ben', 2012, '401533', 'ALMN8', '7356777874'),
('Edwin', 2012, '401534', 'ALMN9', '7356777874'),
('Elsa', 2012, '401535', 'ALMN10', '7356777874'),
('Kannan', 2012, '401536', 'ALMN11', '7356777874'),
('Manju', 2012, '401537', 'ALMN12', '7356777874'),
('Martin', 2012, '401538', 'ALMN13', '7356777874'),
('Meghna', 2012, '401539', 'ALMN14', '7356777874'),
('Mridul', 2012, '401540', 'ALMN15', '7356777874'),
('Rahul', 2012, '401541', 'ALMN16', '7356777874'),
('Sabu', 2012, '401542', 'ALMN17', '7356777874'),
('Shilpa', 2012, '401543', 'ALMN18', '7356777874'),
('Sijo', 2012, '401544', 'ALMN19', '7356777874'),
('Sujith', 2012, '401545', 'ALMN20', '7356777874'),
('Tom', 2012, '401546', 'ALMN21', '7356777874'),
('Vishnu', 2012, '401547', 'ALMN22', '7356777874'),
('Zac', 2012, '401548', 'ALMN23', '7356777874'),
('Zen', 2012, '401549', 'ALMN24', '7356777874'),
('vyshnavi', 2011, '301532', 'ALMN25', '7356777874');

-- --------------------------------------------------------

--
-- Table structure for table `tblevent`
--

CREATE TABLE IF NOT EXISTS `tblevent` (
  `eventid` int(11) NOT NULL AUTO_INCREMENT,
  `eventname` varchar(50) NOT NULL,
  `eventdate` date NOT NULL,
  `eventtime` varchar(50) NOT NULL,
  `eventvenue` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `adultrate` varchar(50) NOT NULL,
  `otherrate` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`eventid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `tblevent`
--

INSERT INTO `tblevent` (`eventid`, `eventname`, `eventdate`, `eventtime`, `eventvenue`, `description`, `adultrate`, `otherrate`, `status`) VALUES
(1, 'Grand alumni event 2019', '2019-10-23', '3 pm', 'Aluva Auditorium', 'gvargfr', '', '', '0'),
(2, 'Grand alumni fest', '2019-10-02', '10 am', 'MA Auditorium', 'gvargfr', '', '', '0'),
(3, 'Fest', '2019-10-16', '10 am', 'College Auditorium', 'qwe', '', '', '0'),
(4, 'qwerty', '0000-00-00', '10:00', 'drgedf', 'fedewd', '150', '50', '0'),
(5, 'Grand Alumni meet 2020', '0000-00-00', '16:00', 'Grand Hyatt', 'kjersvn', '250', '250', '1'),
(6, 'Campzotica', '2020-12-05', '10:00', 'auditorium', 'bgvfbnjhbg', '500', '750', '1'),
(7, 'New year meet', '2021-01-03', '11:00', 'Grand Hyatt', 'uhnbhu', '250', '150', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tblimage`
--

CREATE TABLE IF NOT EXISTS `tblimage` (
  `imageid` int(11) NOT NULL AUTO_INCREMENT,
  `eventid` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`imageid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `tblimage`
--

INSERT INTO `tblimage` (`imageid`, `eventid`, `image`, `description`) VALUES
(1, 1, 'images/b2.jpg', 'sdrgerg'),
(2, 1, 'images/f5.jpg', 'erhgreth'),
(3, 0, 'images/alpin-natur-filzmoos.jpg', 'gwerfew'),
(4, 0, 'images/Australien-Fraser-Island-blaue-Stunde-Natur.jpg', 'grerg'),
(5, 0, 'images/3.jpg', 'wtewrt'),
(6, 4, '/media/abstract-backgrounds-soap-bubble-oil-bubbles-textures-pack_jjjncKH.jpg', 'khg');

-- --------------------------------------------------------

--
-- Table structure for table `tbllogin`
--

CREATE TABLE IF NOT EXISTS `tbllogin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `utype` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbllogin`
--

INSERT INTO `tbllogin` (`username`, `password`, `utype`, `status`) VALUES
('admin@gmail.com', 'admin', 'admin', '1'),
('vishnu@gmail.com', 'vishnu', 'alumni', '1'),
('sakthi@gmail.com', 'sakthi@gmail.com', 'emanager', '1'),
('albert@gmail.com', 'albert', 'alumni', '1'),
('ertruy@gmail.com', 'qwerty', 'emanager', '1'),
('thachu@gmail.com', 'qwerty', 'alumni', '1'),
('shilpa@gmail.com', 'shilpa@123', 'alumni', '1'),
('jeena@gmail.com', 'jeena@123', 'alumni', '1'),
('ragu@gmail.com', 'ragu@123', 'eventmanager', '1'),
('ALMN1', '7356777874', 'alumni', '1'),
('ALMN2', '7356777874', 'alumni', 'inactive'),
('ALMN3', '7356777874', 'alumni', 'inactive'),
('ALMN4', '7356777874', 'alumni', 'inactive'),
('ALMN5', '7356777874', 'alumni', 'inactive'),
('ALMN6', '7356777874', 'alumni', 'inactive'),
('ALMN7', '7356777874', 'alumni', 'inactive'),
('ALMN8', '7356777874', 'alumni', 'inactive'),
('ALMN9', '7356777874', 'alumni', 'inactive'),
('ALMN10', '7356777874', 'alumni', 'inactive'),
('ALMN11', '7356777874', 'alumni', 'inactive'),
('ALMN12', '7356777874', 'alumni', 'inactive'),
('ALMN13', '7356777874', 'alumni', 'inactive'),
('ALMN14', '7356777874', 'alumni', 'inactive'),
('ALMN15', '7356777874', 'alumni', '0'),
('ALMN16', '7356777874', 'alumni', 'inactive'),
('ALMN17', '7356777874', 'alumni', 'inactive'),
('ALMN18', '7356777874', 'alumni', 'inactive'),
('ALMN19', '7356777874', 'alumni', 'inactive'),
('ALMN20', '7356777874', 'alumni', 'inactive'),
('ALMN21', '7356777874', 'alumni', '1'),
('ALMN22', '7356777874', 'alumni', 'inactive'),
('ALMN23', '7356777874', 'alumni', 'inactive'),
('ALMN24', '7356777874', 'alumni', 'inactive'),
('ALMN25', '7356777874', 'alumni', '1');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_eventregistration`
--

CREATE TABLE IF NOT EXISTS `tbl_eventregistration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `eventid` int(50) NOT NULL,
  `aemail` varchar(50) NOT NULL,
  `ar` varchar(50) NOT NULL,
  `otr` varchar(50) NOT NULL,
  `totalprice` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `tbl_eventregistration`
--

INSERT INTO `tbl_eventregistration` (`id`, `eventid`, `aemail`, `ar`, `otr`, `totalprice`, `status`) VALUES
(1, 6, 'ALMN25', '2', '1', '1750', 'registered'),
(3, 7, 'ALMN21', '2', '2', '800', 'registered'),
(4, 7, 'ALMN21', '2', '2', '800', 'registered');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_payment`
--

CREATE TABLE IF NOT EXISTS `tbl_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `regid` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `cnumber` varchar(50) NOT NULL,
  `exdate` varchar(50) NOT NULL,
  `cvv` varchar(50) NOT NULL,
  `totalprice` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `tbl_payment`
--

INSERT INTO `tbl_payment` (`id`, `regid`, `name`, `cnumber`, `exdate`, `cvv`, `totalprice`, `status`) VALUES
(1, 1, 'gvbh', '8788 8888 8888 8888', '0011-11-28', '111', '1750', 'paid'),
(2, 4, 'Tom', '1234 5687 9892 5645', '12/2022', '123', '800', 'paid');
