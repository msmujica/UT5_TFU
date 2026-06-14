CREATE DATABASE IF NOT EXISTS ut5_tfu_db;

USE ut5_tfu_db;

-- =========================
-- PERSONA
-- Clase base
-- =========================

CREATE TABLE IF NOT EXISTS persona (
    id_persona INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL
);

-- =========================
-- EMPLEADO
-- Hereda de Persona
-- =========================

CREATE TABLE IF NOT EXISTS empleado (
    id_persona INT PRIMARY KEY,
    cargo VARCHAR(100),

    CONSTRAINT fk_empleado_persona
        FOREIGN KEY (id_persona)
        REFERENCES persona(id_persona)
        ON DELETE CASCADE
);

-- =========================
-- DUEÑO
-- Hereda de Persona
-- =========================

CREATE TABLE IF NOT EXISTS duenio (
    id_persona INT PRIMARY KEY,

    CONSTRAINT fk_duenio_persona
        FOREIGN KEY (id_persona)
        REFERENCES persona(id_persona)
        ON DELETE CASCADE
);

-- =========================
-- PRODUCTO
-- =========================

CREATE TABLE IF NOT EXISTS producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    precio DECIMAL(10,2) NOT NULL,
    activo BOOLEAN NOT NULL DEFAULT TRUE
);

-- =========================
-- PEDIDO
-- =========================

CREATE TABLE IF NOT EXISTS pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,

    celular_cliente VARCHAR(30) NOT NULL,

    fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    estado ENUM(
        'PENDIENTE',
        'EN_PREPARACION',
        'LISTO',
        'ENTREGADO',
        'CANCELADO'
    ) NOT NULL DEFAULT 'PENDIENTE',

    total DECIMAL(10,2) NOT NULL DEFAULT 0,

    id_empleado INT,

    CONSTRAINT fk_pedido_empleado
        FOREIGN KEY (id_empleado)
        REFERENCES empleado(id_persona)
);

-- =========================
-- DETALLE PEDIDO
-- =========================

CREATE TABLE IF NOT EXISTS detalle_pedido (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,

    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,

    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_detalle_pedido
        FOREIGN KEY (id_pedido)
        REFERENCES pedido(id_pedido)
        ON DELETE CASCADE,

    CONSTRAINT fk_detalle_producto
        FOREIGN KEY (id_producto)
        REFERENCES producto(id_producto)
);

-- =========================
-- PAGO
-- =========================

CREATE TABLE IF NOT EXISTS pago (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,

    id_pedido INT NOT NULL,

    medio_pago ENUM(
        'EFECTIVO',
        'TARJETA',
        'TRANSFERENCIA',
        'MERCADO_PAGO'
    ) NOT NULL,

    estado_pago ENUM(
        'PENDIENTE',
        'APROBADO',
        'RECHAZADO'
    ) NOT NULL DEFAULT 'PENDIENTE',

    monto DECIMAL(10,2) NOT NULL,
    fecha_hora DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_pago_pedido
        FOREIGN KEY (id_pedido)
        REFERENCES pedido(id_pedido)
        ON DELETE CASCADE
);


-- =========================
-- INSERT DATA
-- =========================
INSERT INTO persona (
    id_persona,
    nombre,
    apellido,
    email,
    contrasena
)
VALUES
(1, 'Carlos', 'Gomez', 'empleado@test.com', '1234'),
(2, 'Martin', 'Mujica', 'duenio@test.com', '1234');

INSERT INTO empleado (
    id_persona,
    cargo
)
VALUES
(1, 'Empleado de mostrador');

INSERT INTO duenio (
    id_persona
)
VALUES
(2);

INSERT INTO producto (
    id_producto,
    nombre,
    descripcion,
    precio,
    activo
)
VALUES
(1, 'Hamburguesa clásica', 'Hamburguesa con queso', 250.00, TRUE),
(2, 'Papas fritas', 'Porción de papas fritas', 120.00, TRUE),
(3, 'Refresco', 'Bebida fría', 90.00, TRUE);

INSERT INTO pedido (
    id_pedido,
    celular_cliente,
    estado,
    total,
    id_empleado
)
VALUES
(1, '099123456', 'PENDIENTE', 370.00, 1);

INSERT INTO detalle_pedido (
    id_detalle,
    id_pedido,
    id_producto,
    cantidad,
    precio_unitario,
    subtotal
)
VALUES
(1, 1, 1, 1, 250.00, 250.00),
(2, 1, 2, 1, 120.00, 120.00);

INSERT INTO pago (
    id_pago,
    id_pedido,
    medio_pago,
    estado_pago,
    monto
)
VALUES
(1, 1, 'EFECTIVO', 'APROBADO', 370.00);