-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 21, 2026 at 01:56 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

CREATE DATABASE IF NOT EXISTS `smestaj`;
USE `smestaj`;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `smestaj`
--

-- --------------------------------------------------------

--
-- Table structure for table `drzava`
--

CREATE TABLE `drzava` (
  `drzavaID` int(11) NOT NULL,
  `drzava` text NOT NULL,
  `kontinent` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `drzava`
--

INSERT INTO `drzava` (`drzavaID`, `drzava`, `kontinent`) VALUES
(1, 'Austrija', 'Evropa'),
(2, 'Japan', 'Azija'),
(3, 'Egipat', 'Afrika'),
(4, 'Srbija', 'Evropa');

-- --------------------------------------------------------

--
-- Table structure for table `grad`
--

CREATE TABLE `grad` (
  `gradID` int(11) NOT NULL,
  `naziv_grada` text NOT NULL,
  `drzavaID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `grad`
--

INSERT INTO `grad` (`gradID`, `naziv_grada`, `drzavaID`) VALUES
(1, 'Tokio', 2),
(2, 'Beč', 1),
(3, 'Grac', 1),
(4, 'Beograd', 4);

-- --------------------------------------------------------

--
-- Table structure for table `hotel`
--

CREATE TABLE `hotel` (
  `hotelID` int(11) NOT NULL,
  `naziv` text NOT NULL,
  `gradID` int(11) NOT NULL,
  `adresa` text NOT NULL,
  `zvezdice` int(11) NOT NULL,
  `ljubimci` tinyint(1) NOT NULL,
  `vrsta_smestaja` text NOT NULL,
  `obrok` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hotel`
--

INSERT INTO `hotel` (`hotelID`, `naziv`, `gradID`, `adresa`, `zvezdice`, `ljubimci`, `vrsta_smestaja`, `obrok`) VALUES
(1, 'Paradise', 2, 'Franca Ferdinanda 5', 4, 0, 'hotel', 'polu-pansion'),
(2, 'Sakura', 1, 'General Kasukabe, Shibuya', 5, 0, 'hotel', 'pun pansion'),
(3, 'Mozart', 3, 'Wolfgang Amadeus Mozart 25', 3, 1, 'apartmani', 'samostalni obroci'),
(4, 'Jugoslavija', 4, 'Bulevar Vuka Karadžića 20', 4, 0, 'Hotel', 'polu-pansion');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `drzava`
--
ALTER TABLE `drzava`
  ADD PRIMARY KEY (`drzavaID`);

--
-- Indexes for table `grad`
--
ALTER TABLE `grad`
  ADD PRIMARY KEY (`gradID`),
  ADD KEY `drzavaID` (`drzavaID`);

--
-- Indexes for table `hotel`
--
ALTER TABLE `hotel`
  ADD PRIMARY KEY (`hotelID`),
  ADD KEY `gradID` (`gradID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `drzava`
--
ALTER TABLE `drzava`
  MODIFY `drzavaID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `grad`
--
ALTER TABLE `grad`
  MODIFY `gradID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `hotel`
--
ALTER TABLE `hotel`
  MODIFY `hotelID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `grad`
--
ALTER TABLE `grad`
  ADD CONSTRAINT `grad_ibfk_1` FOREIGN KEY (`drzavaID`) REFERENCES `drzava` (`drzavaID`);

--
-- Constraints for table `hotel`
--
ALTER TABLE `hotel`
  ADD CONSTRAINT `hotel_ibfk_1` FOREIGN KEY (`gradID`) REFERENCES `grad` (`gradID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
