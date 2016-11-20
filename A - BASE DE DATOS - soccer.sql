-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-11-2016 a las 00:44:07
-- Versión del servidor: 10.1.8-MariaDB
-- Versión de PHP: 5.6.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `soccer`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

CREATE TABLE `equipos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `lema` varchar(100) NOT NULL,
  `siglas` varchar(3) NOT NULL,
  `clasificacion` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `equipos`
--

INSERT INTO `equipos` (`id`, `nombre`, `lema`, `siglas`, `clasificacion`) VALUES
(0, 'Invitado\n', '', 'INV', 0),
(26, 'Costa Rica', 'La Tricolor', 'CRC', 18),
(27, 'Argentina', 'Albiceleste', 'ARG', 1),
(28, 'Brasil', 'Verdeamarelos', 'BRA', 3),
(29, 'Estados Unidos', 'The Stars and Stripes', 'USA', 24);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fechas`
--

CREATE TABLE `fechas` (
  `id_fecha` int(11) NOT NULL,
  `fecha` varchar(50) NOT NULL,
  `equipo1` varchar(100) NOT NULL,
  `id_equipo1` int(11) NOT NULL,
  `equipo2` varchar(100) NOT NULL,
  `id_equipo2` int(11) NOT NULL,
  `hora_lugar` varchar(100) NOT NULL DEFAULT '15:00 pm, San Jose, Costa Rica',
  `gol_equipo1` int(50) NOT NULL,
  `gol_equipo2` int(50) NOT NULL,
  `anotadores1` varchar(500) NOT NULL,
  `anotadores2` varchar(500) NOT NULL,
  `estado` int(11) NOT NULL DEFAULT '0',
  `gano` int(3) NOT NULL DEFAULT '0',
  `perdio` int(3) NOT NULL DEFAULT '0',
  `empato` int(3) NOT NULL DEFAULT '0',
  `gol_gano` int(50) NOT NULL DEFAULT '0',
  `gol_perdio` int(50) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `fechas`
--

INSERT INTO `fechas` (`id_fecha`, `fecha`, `equipo1`, `id_equipo1`, `equipo2`, `id_equipo2`, `hora_lugar`, `gol_equipo1`, `gol_equipo2`, `anotadores1`, `anotadores2`, `estado`, `gano`, `perdio`, `empato`, `gol_gano`, `gol_perdio`) VALUES
(154, '1', 'Costa Rica', 26, 'Argentina', 27, '15:00 pm, San Jose, Costa Rica', 1, 4, '<li>Keylor Navas</li>', '<li>Lionel Messi</li><li>Lionel Messi</li><li>Lionel Messi</li><li>Lionel Messi</li>', 1, 27, 26, 0, 4, -4),
(155, '1', 'Brasil', 28, 'Estados Unidos', 29, '15:00 pm, San Jose, Costa Rica', 0, 0, '', '', 0, 0, 0, 0, 0, 0),
(156, '2', 'Costa Rica', 26, 'Estados Unidos', 29, '15:00 pm, San Jose, Costa Rica', 0, 0, '', '', 0, 0, 0, 0, 0, 0),
(157, '2', 'Argentina', 27, 'Brasil', 28, '15:00 pm, San Jose, Costa Rica', 0, 0, '', '', 0, 0, 0, 0, 0, 0),
(158, '3', 'Costa Rica', 26, 'Brasil', 28, '15:00 pm, San Jose, Costa Rica', 0, 0, '', '', 0, 0, 0, 0, 0, 0),
(159, '3', 'Estados Unidos', 29, 'Argentina', 27, '15:00 pm, San Jose, Costa Rica', 0, 0, '', '', 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `general`
--

CREATE TABLE `general` (
  `nombre_torneo` varchar(500) NOT NULL,
  `equipos_participan` int(100) NOT NULL,
  `equipos_clasifican` int(100) NOT NULL,
  `puntos_p_ganado` int(100) NOT NULL,
  `puntos_p_empatado` int(100) NOT NULL,
  `fecha` int(3) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `general`
--

INSERT INTO `general` (`nombre_torneo`, `equipos_participan`, `equipos_clasifican`, `puntos_p_ganado`, `puntos_p_empatado`, `fecha`) VALUES
('TORNEO DE INVIERO', 0, 5, 5, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `goles`
--

CREATE TABLE `goles` (
  `id_gol` int(11) NOT NULL,
  `id_jugador` int(11) NOT NULL,
  `id_juego` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `goles`
--

INSERT INTO `goles` (`id_gol`, `id_jugador`, `id_juego`) VALUES
(26, 9, 154),
(27, 23, 154),
(28, 23, 154),
(29, 23, 154),
(30, 23, 154);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugadores`
--

CREATE TABLE `jugadores` (
  `id_jugador` int(11) NOT NULL,
  `nombre_jugador` varchar(100) NOT NULL,
  `id_equipo` int(11) NOT NULL,
  `posicion` varchar(100) NOT NULL,
  `numero` int(100) NOT NULL,
  `foto` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `jugadores`
--

INSERT INTO `jugadores` (`id_jugador`, `nombre_jugador`, `id_equipo`, `posicion`, `numero`, `foto`) VALUES
(9, 'Keylor Navas', 26, 'Portero', 1, 'RealM-Shahter15_(9).jpg'),
(10, 'Johnny Acosta', 26, 'Defensa', 2, 'images.jpg'),
(11, 'Francisco Calvo', 26, 'Defensa', 3, 'Francisco_Calvo_August_2016.jpg'),
(12, 'Celso Borges', 26, 'Mediocampista', 5, 'avatar.jpg'),
(13, 'Bryan Ruiz', 26, 'Mediocampista', 10, 'images (1).jpg'),
(14, 'Joel Campbell', 26, 'Mediocampista', 12, 'Joel+Campbell+Costa+Rica+v+Greece+Round+16+NAra_CB6Oqfl.jpg'),
(15, 'Johan Venegas', 26, 'Delantero', 11, 'Johan-Venegas-futbolista-Paulo-Wanchoe_LNCIMA20150611_0117_27.jpg'),
(16, 'Marcos Ure&ntilde;a', 26, 'Delantero', 21, '3pXPQ5jz.jpg'),
(17, 'Sergio Romero', 27, 'Portero', 20, 'Germany_and_Argentina_face_off_in_the_final_of_the_World_Cup_2014_-2014-07-13_(31).jpg'),
(18, '&Aacute;ngel Di Mar&iacute;a', 27, 'Mediocampista', 11, 'PSG-Shakhter15_(2).jpg'),
(19, 'Javier Mascherano', 27, 'Mediocampista', 14, 'Mascherano_casagob.jpg'),
(20, 'Gabriel Mercado', 27, 'Defensa', 24, 'Gabriel_Mercado.jpg'),
(21, 'Facundo Roncaglia', 27, 'Defensa', 32, 'Facundo+Roncaglia+Ecuador+v+Argentina+tH4D5uBOI8hl.jpg'),
(22, 'Lucas Biglia', 27, 'Mediocampista', 6, 'l.jpg'),
(23, 'Lionel Messi', 27, 'Delantero', 10, '2015_UEFA_Super_Cup_64_crop.jpg'),
(24, '&Aacute;ngel Correa', 27, 'Delantero', 11, 'Angel_Correa_U20_World_Cup_crop.jpg'),
(25, 'Alisson Becker', 28, 'Portero', 19, 'Internacional-2015_(2).jpg'),
(26, 'Dani Alves', 28, 'Defensa', 23, '220px-Dani_Alves_17527.jpg'),
(27, 'Joao Miranda', 28, 'Defensa', 3, 'Miranda_v_Real_Madrid_2013.jpg'),
(28, 'Carlos Casemiro', 28, 'Mediocampista', 14, 'Shahter-Reak_M_2015_(16).jpg'),
(29, 'Renato Augusto', 28, 'Mediocampista', 8, 'Renato_Augusto_-_Rio_2016.jpg'),
(30, 'Douglas Costa', 28, 'Delantero', 11, 'Douglas_Costa1.jpg'),
(31, 'Gabriel Jesus', 28, 'Delantero', 33, 'a.jpg'),
(32, 'Neymar', 28, 'Delantero', 10, 'ECUADOR_vs_BRASIL_(29392285815)_(cropped).jpg'),
(33, 'Brad Guzan', 29, 'Portero', 1, 'Brad_Guzan_vs_Belgium_1.jpg'),
(34, 'DeAndre Yedlin', 29, 'Defensa', 24, 'DeAndre_Yedlin_training_2014_Brazil_(cropped).jpg'),
(35, 'Steve Birnbaum', 29, 'Defensa', 3, 'Steve_Birnbaum_DC_United.JPG'),
(36, 'Michael Bradley', 29, 'Mediocampista', 4, 'Austria_vs._USA_2013-11-19_(079).jpg'),
(37, 'Darlington Nagbe', 29, 'Mediocampista', 6, 'Portl-RSL_(10).jpg'),
(38, 'Bobby Wood', 29, 'Delantero', 7, 'Bobby_Wood_1860_2011_2.JPG'),
(39, 'Clint Dempsey', 29, 'Delantero', 2, 'Clint_Dempsey.jpg'),
(40, 'Gyasi Zardes', 29, 'Delantero', 11, 'Gyasi_Zardes_2.jpg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `siglas` (`siglas`),
  ADD UNIQUE KEY `clasificacion` (`clasificacion`);

--
-- Indices de la tabla `fechas`
--
ALTER TABLE `fechas`
  ADD PRIMARY KEY (`id_fecha`);

--
-- Indices de la tabla `general`
--
ALTER TABLE `general`
  ADD PRIMARY KEY (`nombre_torneo`);

--
-- Indices de la tabla `goles`
--
ALTER TABLE `goles`
  ADD PRIMARY KEY (`id_gol`);

--
-- Indices de la tabla `jugadores`
--
ALTER TABLE `jugadores`
  ADD PRIMARY KEY (`id_jugador`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipos`
--
ALTER TABLE `equipos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
--
-- AUTO_INCREMENT de la tabla `fechas`
--
ALTER TABLE `fechas`
  MODIFY `id_fecha` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=160;
--
-- AUTO_INCREMENT de la tabla `goles`
--
ALTER TABLE `goles`
  MODIFY `id_gol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT de la tabla `jugadores`
--
ALTER TABLE `jugadores`
  MODIFY `id_jugador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
