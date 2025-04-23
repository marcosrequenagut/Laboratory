API REST para Gestión de Proyectos.
Este proyecto implementa una API REST utilizando FastAPI para gestionar proyectos, permitiendo la creación de proyectos, registro de tiempo y eliminación de proyectos. Los proyectos se almacenan en una base de datos SQLite.

Descripción
La API permite realizar las siguientes acciones sobre los proyectos:

1.- Crear un proyecto: Si el proyecto no existe, se crea un nuevo proyecto con un tiempo inicial de 0.
2.- Obtener todos los proyectos: Muestra todos los proyectos y su tiempo asociado.
3.- Registrar tiempo: Permite agregar tiempo a un proyecto existente.
4.- Eliminar un proyecto: Borra un proyecto de la base de datos.
5.- Snapshot: (Futuro) Funcionalidad para crear un snapshot de un proyecto.

Los proyectos están representados por su nombre y un tiempo asociado (en minutos).
