-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema comida_italiana
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema comida_italiana
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `comida_italiana` DEFAULT CHARACTER SET utf8 ;
USE `comida_italiana` ;

-- -----------------------------------------------------
-- Table `comida_italiana`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `comida_italiana`.`clientes` (
  `id_cliente` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(100) NULL,
  `gender` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE INDEX `id_cliente_UNIQUE` (`id_cliente` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `comida_italiana`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `comida_italiana`.`productos` (
  `id_producto` VARCHAR(45) NOT NULL,
  `nombre_producto` VARCHAR(100) NULL,
  `categoría` VARCHAR(45) NULL,
  `precio` FLOAT NULL,
  `origen` VARCHAR(45) NULL,
  `descripción` MEDIUMTEXT NULL,
  PRIMARY KEY (`id_producto`),
  UNIQUE INDEX `id_producto_UNIQUE` (`id_producto` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `comida_italiana`.`ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `comida_italiana`.`ventas` (
  `id_venta` INT NOT NULL,
  `id_cliente` INT NOT NULL,
  `id_producto` VARCHAR(45) NOT NULL,
  `fecha_venta` DATETIME NULL,
  `cantidad` INT NULL,
  `total` FLOAT NULL,
  PRIMARY KEY (`id_ventas`),
  INDEX `fk_ventas_clientes1_idx` (`id_cliente` ASC) VISIBLE,
  INDEX `fk_ventas_productos1_idx` (`id_producto` ASC) VISIBLE,
  CONSTRAINT `fk_ventas_clientes1`
    FOREIGN KEY (`id_cliente`)
    REFERENCES `comida_italiana`.`clientes` (`id_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ventas_productos1`
    FOREIGN KEY (`id_producto`)
    REFERENCES `comida_italiana`.`productos` (`id_producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
