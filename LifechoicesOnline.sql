-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 23, 2021 at 02:15 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `LifechoicesOnline`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `full_name` varchar(60) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone number` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `full_name`, `username`, `password`, `email`, `phone number`) VALUES
(3333, 'Holy Life', 'holy', '1234', 'holyl@gmail.com', '0843066302'),
(6666, 'Lee Hope', 'leeh', '1234', 'leeh@gmail.com', '0843066302');

-- --------------------------------------------------------

--
-- Table structure for table `sign_register`
--

CREATE TABLE `sign_register` (
  `username` varchar(50) NOT NULL,
  `sign_in` varchar(10) NOT NULL,
  `sign_out` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sign_register`
--

INSERT INTO `sign_register` (`username`, `sign_in`, `sign_out`) VALUES
('liamh', '16:18:17', '16:21:43'),
('liamh', '10:56:41', '10:56:56');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `full_name` varchar(60) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_number` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`full_name`, `username`, `password`, `email`, `phone_number`) VALUES
('', '', '', '', ''),
('Alex Sassmon', 'Alexs', '1234', 'alexs@gmail.com', '0843066302'),
('asd', 'asd', '1234', 'asd', '1234'),
('Cameron Sassmon', 'camerons', '1234', 'camerons@gmail.com', '\r\n0843066302'),
('Ethan Loba', 'ethanl', '1234', 'ethanloba@gmail.com', '	\r\n0843066302'),
('Kyle Poena', 'kylep', '1234', 'kylep@gmail.com', '	\r\n0843066302'),
('Liam Horne', 'liamh', '1234', 'liamh@gmail.com', '0843066302');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
