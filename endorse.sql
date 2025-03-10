-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 01, 2024 at 02:08 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `endorse`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_reg`
--

CREATE TABLE `admin_reg` (
  `id` int(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_reg`
--

INSERT INTO `admin_reg` (`id`, `name`, `email`, `password`) VALUES
(1, 'Nisha', 'nishait2111@gmail.com', 'nisha123');

-- --------------------------------------------------------

--
-- Table structure for table `business_reg`
--

CREATE TABLE `business_reg` (
  `id` int(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `address` varchar(50) NOT NULL,
  `pincode` varchar(10) NOT NULL,
  `photo` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `business_reg`
--

INSERT INTO `business_reg` (`id`, `name`, `email`, `password`, `gender`, `mobile`, `address`, `pincode`, `photo`, `status`) VALUES
(1, 'Nisha', 'nishait2111@gmail.com', 'Niish31', 'female', '6383207813', 'salem', '636306', 'bike.jpg', 'true'),
(2, 'Moni', 'moni143@gmail.com', 'MooniSx', 'female', '1234567890', 'Banglore', '684367', 'books.jpg', 'true'),
(3, 'krish', 'krish13@gmail.com', 'krish', 'male', '2147483647', 'Salem', '636408', 'carrom.jpg', 'false'),
(5, 'Nishanthini', 'ssnishanthini2002@gmail.com', 'nisha123', 'female', '9443696863', 'Salem', '636004', 'apple.jpg', 'false');

-- --------------------------------------------------------

--
-- Table structure for table `business_sell`
--

CREATE TABLE `business_sell` (
  `id` int(11) NOT NULL,
  `category` varchar(50) NOT NULL,
  `brand` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `price` varchar(20) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `sellid` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `business_sell`
--

INSERT INTO `business_sell` (`id`, `category`, `brand`, `title`, `description`, `price`, `photo`, `sellid`) VALUES
(1, 'mobile', 'oppo', 'Oppo A38', '4GB RAM, 128GB Storage | 5000 mAh Battery', '9,999', 'oppo.jpg', '1'),
(2, 'home appliances', 'air conditionar', 'Bluestar AC', '1.5 Ton 3 Star Wi-Fi Inverter Smart Split AC', '36,950', 'air.png', '1'),
(3, 'mobile', 'redmi', 'Redmi 11 Prime 5G', 'Thunder Black, 4GB RAM, 64GB Storage', '11,299', 'redmi12.jpg', '3'),
(4, 'mobile', 'redmi', 'Redmi 11 Prime', 'Thunder Black, 4GB RAM, 64GB Storage', '11,299', 'redmi12.jpg', '3'),
(7, 'home appliances', 'washing machine', 'washing machine', 'good quality', '11,299', 'washing-machine.png', '1'),
(8, 'mobile', 'samsung', 'Samsung Galaxy', '4GB, 64GB ', '22,999', 'samsung.jpg', '1'),
(9, 'mobile', 'vivo', 'Vivo V27', 'Good Quality 5G Mobile', '18,699', 'vivo.jpg', '2'),
(10, 'mobile', 'iphone', 'iphone 6S', '4.7 inch HD Display 4GB, 128GB', '39,999', 'iphone6s.jpg', '2'),
(11, 'electronics', 'laptop', 'Dell Laptop', 'Core i5 8GB RAM | 264GB ROM', '35,739', 'lap.jpg', '2'),
(12, 'electronics', 'tv', 'Samsung TV', '40 inch Smart TV', '22,699', 'tv.jpg', '2'),
(13, 'electronics', 'camera', 'GoCam', 'Ultra HD Screen', '40,299', 'cam.jpg', '3'),
(14, 'home appliances', 'refridgerator', 'LG Refridgerator', 'Single Door 3 Star Refridgerator', '18,599', 'fridge.png', '3');

-- --------------------------------------------------------

--
-- Table structure for table `my_orders`
--

CREATE TABLE `my_orders` (
  `id` int(20) NOT NULL,
  `uid` int(20) NOT NULL,
  `image` varchar(500) NOT NULL,
  `payment` varchar(50) NOT NULL,
  `title` varchar(500) NOT NULL,
  `description` varchar(500) NOT NULL,
  `price` varchar(50) NOT NULL,
  `sellid` int(20) NOT NULL,
  `uname` varchar(20) NOT NULL,
  `uphone` varchar(10) NOT NULL,
  `uemail` varchar(25) NOT NULL,
  `uaddress` varchar(50) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `my_orders`
--

INSERT INTO `my_orders` (`id`, `uid`, `image`, `payment`, `title`, `description`, `price`, `sellid`, `uname`, `uphone`, `uemail`, `uaddress`, `status`) VALUES
(1, 1, 'None', 'cash', 'Redmi 12', '5G Mobile 8GB RAM | 128GB ROM', '10,217', 0, 'Nisha', '6383207813', 'nishait2111@gmail.com', 'Salem', 'ordered'),
(2, 1, 'lap.jpg', 'cash', 'Dell Laptop', 'Core i5 8GB RAM | 264GB ROM', '35,739', 2, 'Nisha', '6383207813', 'nishait2111@gmail.com', 'Salem', 'ordered'),
(3, 1, 'iphone6s.jpg', 'Card', 'iphone 6S', '4.7 inch HD Display 4GB, 128GB', '39,999', 2, 'Nisha', '6383207813', 'nishait2111@gmail.com', 'Salem', 'Order Accepted'),
(4, 2, 'air.png', 'cash', 'Bluestar AC', '1.5 Ton 3 Star Wi-Fi Inverter Smart Split AC', '36,950', 1, 'Moni', '1234567890', 'moni143@gmail.com', 'Erode', 'Order Accepted'),
(5, 2, 'fridge.png', 'cash', 'LG Refridgerator', 'Single Door 3 Star Refridgerator', '18,599', 3, 'Moni', '1234567890', 'moni143@gmail.com', 'Erode', 'ordered'),
(6, 6, 'washing-machine.png', 'cash', 'washing machine', 'good quality', '11,299', 1, 'Kaushalya', '2147483647', 'kowsikowsi@gmail.com', 'kotagiri', 'ordered'),
(7, 6, 'vivo.jpg', 'upi', 'Vivo V27', 'Good Quality 5G Mobile', '18,699', 2, 'Kaushalya', '2147483647', 'kowsikowsi@gmail.com', 'kotagiri', 'Order Accepted');

-- --------------------------------------------------------

--
-- Table structure for table `sell_product`
--

CREATE TABLE `sell_product` (
  `id` int(20) NOT NULL,
  `category` varchar(50) NOT NULL,
  `brand` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `price` int(20) NOT NULL,
  `photo` varchar(20) NOT NULL,
  `sellid` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sell_product`
--

INSERT INTO `sell_product` (`id`, `category`, `brand`, `title`, `description`, `price`, `photo`, `sellid`) VALUES
(1, 'refridgerator', '', 'ljihugyftdrse', ';kojihugyftre', 6457, 'book.jpg', 0),
(2, 'samsung', '', 'Samsung Galaxy S24', '128 GB RAM  8GB ROM \r\nGood Quality\r\n  ', 12, 'samsung.jpg', 0),
(3, 'samsung', '', 'Samsung Galaxy S24', '128 GB RAM  8GB ROM \r\nGood Quality\r\n  ', 12, 'samsung.jpg', 0),
(4, 'washing machine', '', 'washing machine', 'gheixjdkfghjkl', 30000, 'washing-machine.png', 0),
(5, 'washing machine', '', 'washing', 'fghjkl;', 20000, 'washing-machine.png', 1),
(6, 'camera', '', 'cfgvhbj', 'sedrfgh', 6, 'bike.jpg', 0),
(7, 'washing machine', '', ',njbhvg', 'kjgf', 8564635, 'air.png', 0),
(8, 'washing machine', '', ', jbhvgcf', 'kojihyut', 42442, 'books.jpg', 0),
(9, 'laptop', '', 'dxfcgvhbj', 'zxcfvgbhjn', 5155, 'bike.jpg', 1);

-- --------------------------------------------------------

--
-- Table structure for table `userreg`
--

CREATE TABLE `userreg` (
  `id` int(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `address` varchar(100) NOT NULL,
  `pincode` int(10) NOT NULL,
  `photo` varchar(30) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userreg`
--

INSERT INTO `userreg` (`id`, `name`, `email`, `password`, `gender`, `mobile`, `address`, `pincode`, `photo`, `status`) VALUES
(1, 'Nisha', 'nishait2111@gmail.com', 'nisha', 'female', '6383207813', 'Salem', 636306, 'toy.jpg', 'false'),
(2, 'Moni', 'moni143@gmail.com', 'Mooni74', 'female', '1234567890', 'Erode', 636401, 'back.jpg', 'true'),
(3, 'NISHANTHINI S S', 'ssnishanthini2002@gmail.com', 'nisha123', 'female', '2147483647', 'salem', 636306, 'bike.jpg', 'false'),
(4, 'krish', 'krish13@gmail.com', 'krish13', 'male', '2147483647', 'Banglore', 636401, 'book.jpg', 'false'),
(5, 'Kaushalya', 'kowsi@gmail.com', 'kowsi', 'female', '2147483647', 'Ooty', 684367, 'ac.jpg', 'false'),
(6, 'Kaushalya', 'kowsikowsi@gmail.com', 'Kaows9o', 'female', '2147483647', 'kotagiri', 643217, 'tv.jpg', 'true'),
(7, 'Madhu', 'madhu27@gmail.com', 'madhhu', 'female', '9487990863', 'Trichengode', 634824, 'sam_fridge.jpg', 'false');

-- --------------------------------------------------------

--
-- Table structure for table `user_sell`
--

CREATE TABLE `user_sell` (
  `id` int(20) NOT NULL,
  `category` varchar(50) NOT NULL,
  `brand` varchar(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `price` varchar(50) NOT NULL,
  `photo` varchar(50) NOT NULL,
  `sellid` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_sell`
--

INSERT INTO `user_sell` (`id`, `category`, `brand`, `title`, `description`, `price`, `photo`, `sellid`) VALUES
(1, 'mobile', 'redmi', 'Redmi 12', '5G Mobile 8GB RAM | 128GB ROM', '10,217', 'redmi.jpg', '1'),
(2, 'mobile', 'samsung', 'Samsung Galaxy S24 Ultra', '128GB\r\n5G Mobile\r\nGood Quality', '12,217', 'samsung.jpg', '1'),
(3, 'mobile', 'oppo', 'Oppo A59', '6GB | 128GB \r\n', '11,000', 'oppo.jpg', '1'),
(4, 'mobile', 'vivo', 'Vivo V27', 'Good Quality\r\n5G Mobile', '10,250', 'vivo.jpg', '1'),
(5, 'mobile', 'iphone', 'Apple iPhone 6s', '4.7 inch HD Display\n2GB, 128GB', '10,517', 'iphone6s.jpg', '1'),
(6, 'electronics', 'laptop', 'Dell Laptop', 'Core i5\n8GB RAM | 264GB ROM\n', '20,000', 'lap.jpg', '1'),
(7, 'electronics', 'tv', 'Samsung TV', '40 inch Smart TV', '16,500', 'tv.jpg', '1'),
(8, 'electronics', 'camera', 'GoCam', 'Ultra HD Screen', '4,000', 'cam.jpg', '1'),
(9, 'home appliances', 'washing machine', 'LG Washing Machine', 'Front Load\r\nFully Automatic', '15,500', 'washing-machine.png', '1'),
(10, 'home appliances', 'refridgerator', 'LG Refridgerator', 'Single Door\r\n3 Star Refridgerator', '15,500', 'fridge.png', '1'),
(11, 'home appliances', 'air conditionar', 'Blue Star Inverter AC', '1.5 Ton', '22,500', 'air.png', '1'),
(12, 'kids', 'tricycle', 'Tricycle', 'Good Quality', '800', 'tricycle.jpg', '1'),
(13, 'kids', 'toy vehicles', 'Toy Car', 'Good Quality', '1500', 'toy vehicle.jpg', '1'),
(14, 'kids', 'soft toys', 'Panda Toy', 'Big size', '500', 'softtoy.jpg', '1'),
(15, 'kids', 'games puzzle', 'Chess Board', 'New Product', '250', 'chess.jpg', '1'),
(16, 'sports', 'cricket', 'Cricket kit', 'Good Condition', '2500', 'cricket.jpg', '1'),
(17, 'sports', 'batmiton', 'Batmiton Racket', 'New', '480', 'batmiton.jpg', '1'),
(18, 'sports', 'football', 'Football Shoes', 'Good Condition', '550', 'football.jpg', '1'),
(19, 'books', 'biography', 'Wings of Fire', 'Book for Sale', '200', 'book.jpg', '1'),
(20, 'books', 'fantasy', 'Harry Potter', 'Book for Sale', '250', 'fantasy.jpg', '1'),
(21, 'books', 'hystorical fiction', 'Rajaraja Chozhan', 'Book for Sale', '120', 'history.jpg', '1'),
(23, 'mobile', 'redmi', 'Redmi 11 Prime', 'Thunder Black, 4GB, 64GB', '11,299', 'redmi12.jpg', '3'),
(24, 'home appliances', 'refridgerator', 'Samsung Refrigerator', '256 L Convertible Freezer Double Door', '22,790', 'sam_fridge.jpg', '3'),
(25, 'mobile', 'refridgerator', 'Refridgerator', 'Good Quality', '11,299', 'fridge.png', 'None'),
(26, 'kids', 'soft toys', 'Panda Toy', 'Good quality and Big size ', '550', 'softtoy.jpg', '3'),
(29, 'mobile', 'iphone', 'IPhone', 'new mobile', '20000', 'apple.jpg', '%s'),
(30, 'kids', 'games puzzle', 'Carrom Board 32 inch', 'with coin, sticker & boric powder', '1225', 'carrom.jpg', '1'),
(31, 'mobile', 'samsung', 'Samsung', '128GB 5G Mobile Good Quality', '22,500', 'samsung.jpg', '1'),
(32, 'mobile', 'vivo', 'Vivo V27', 'Good Quality 5G Mobile', '15,599', 'vivo.jpg', '2'),
(33, 'mobile', 'iphone', 'Iphone', 'HD Display 4GB, 128GB', '35,000', 'iphone6s.jpg', '2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_reg`
--
ALTER TABLE `admin_reg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `business_reg`
--
ALTER TABLE `business_reg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `business_sell`
--
ALTER TABLE `business_sell`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `my_orders`
--
ALTER TABLE `my_orders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sell_product`
--
ALTER TABLE `sell_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userreg`
--
ALTER TABLE `userreg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_sell`
--
ALTER TABLE `user_sell`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_reg`
--
ALTER TABLE `admin_reg`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `business_reg`
--
ALTER TABLE `business_reg`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `business_sell`
--
ALTER TABLE `business_sell`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `my_orders`
--
ALTER TABLE `my_orders`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `sell_product`
--
ALTER TABLE `sell_product`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `userreg`
--
ALTER TABLE `userreg`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user_sell`
--
ALTER TABLE `user_sell`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
