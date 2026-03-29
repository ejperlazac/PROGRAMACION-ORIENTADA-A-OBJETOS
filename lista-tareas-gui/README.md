# Aplicación GUI de Lista de Tareas

## Descripción

La presente aplicación ha sido desarrollada en Python utilizando la biblioteca Tkinter, con el propósito de gestionar una lista de tareas mediante una interfaz gráfica de usuario. El sistema permite al usuario añadir nuevas tareas, marcarlas como completadas y eliminarlas, integrando el manejo de eventos como elemento central de interacción.

---

## Objetivo

Desarrollar una aplicación GUI que permita gestionar tareas de manera interactiva, aplicando los conceptos fundamentales del manejo de eventos, tales como eventos de teclado y eventos de mouse, dentro del entorno de programación en Python.

---

## Funcionalidades

- Ingreso de nuevas tareas mediante un campo de texto.
- Adición de tareas a través de un botón o mediante la tecla Enter.
- Visualización de tareas en una lista.
- Marcado de tareas como completadas con cambio visual.
- Eliminación de tareas seleccionadas.
- Implementación de eventos adicionales como doble clic para mejorar la interacción.

---

## Tecnologías utilizadas

- Lenguaje de programación Python  
- Biblioteca Tkinter  
- Sistema de control de versiones Git  
- Plataforma GitHub  

---

## Manejo de eventos

La aplicación implementa el manejo de eventos como base de su funcionamiento. Se han incorporado eventos de teclado, permitiendo añadir tareas mediante la tecla Enter, así como eventos de mouse a través de los botones de la interfaz. Asimismo, se ha implementado un evento adicional de doble clic sobre los elementos de la lista para marcar tareas como completadas, evidenciando la capacidad de respuesta dinámica de la aplicación ante las acciones del usuario.

---

## Lógica de la aplicación

Las tareas se almacenan en una estructura de datos tipo lista, donde cada elemento contiene información sobre el texto de la tarea y su estado. Cuando una tarea es marcada como completada, su representación visual cambia para reflejar dicho estado. Al eliminar una tarea, esta es removida tanto de la interfaz gráfica como de la estructura de almacenamiento interno.

---

## Ejecución

Para ejecutar la aplicación, se debe utilizar el siguiente comando en la terminal:

```bash
py app.py

Autor:
Evelin Perlaza