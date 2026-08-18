# Career Lab

Career Lab es un entorno personal de aprendizaje técnico y desarrollo profesional.

Su objetivo es construir conocimientos de ingeniería de software de forma progresiva, práctica e iterativa, evitando roadmaps excesivamente grandes y aprendizaje basado únicamente en cursos o tecnologías.

El laboratorio utiliza proyectos pequeños como hilo conductor para entender cómo funcionan los sistemas de software de extremo a extremo.

---

## Objetivo profesional

Evolucionar progresivamente desde Software Developer hacia perfiles con mayor capacidad de diseño y responsabilidad técnica.

La dirección profesional a largo plazo está relacionada con:

- Software Engineering
- Arquitectura de software y soluciones
- Backend
- Python
- Inteligencia Artificial aplicada a sistemas software

El objetivo a largo plazo sirve como orientación, no como roadmap detallado.

Solo se diseña en profundidad el siguiente nivel de aprendizaje.

---

## Filosofía

### 1. Aprender desde problemas reales

El aprendizaje parte de preguntas concretas:

- ¿Qué ocurre cuando hago una petición?
- ¿Dónde está ejecutándose esta aplicación?
- ¿Cómo se configura?
- ¿Dónde persisten sus datos?
- ¿Cómo sé si está funcionando correctamente?
- ¿Qué ocurre cuando falla?
- ¿Cómo llega una nueva versión a producción?

Cuando aparece un concepto que no entiendo, bajo una capa, estudio ese concepto y vuelvo al problema original.

### 2. Fundamentos antes que herramientas

Las herramientas cambian. Los conceptos permanecen durante más tiempo.

Por eso el objetivo no es aprender Docker, Azure, FastAPI o cualquier tecnología concreta como fin en sí mismo.

El objetivo es comprender conceptos como:

- procesos
- HTTP
- redes
- persistencia
- configuración
- observabilidad
- despliegue
- resiliencia
- diseño de software

Las tecnologías se utilizan como herramientas para practicar estos conceptos.

### 3. Progresión iterativa

El desarrollo se organiza mediante niveles.

```text
Nivel global
    |
    +-- Subnivel
    |     +-- Microobjetivo
    |     +-- Microobjetivo
    |     +-- Microobjetivo
    |
    +-- Checkpoint
```

Solo se define detalladamente el nivel actual.

Cuando se completa:

1. se revisan las evidencias;
2. se identifican nuevas lagunas;
3. se diseña el siguiente nivel.

### 4. Evidencia antes que consumo

Completar un curso, leer un libro o ver un vídeo no significa haber adquirido una competencia.

El progreso debe demostrarse mediante evidencias:

- explicar un concepto con palabras propias;
- aplicarlo;
- diagnosticar un problema;
- justificar una decisión;
- demostrarlo en el proyecto.

Los recursos son herramientas de aprendizaje, no objetivos.

---

## Uso de Inteligencia Artificial

La IA forma parte del entorno como mentor e instructor.

Por defecto, no debe actuar como desarrollador.

Las reglas completas están definidas en `AGENTS.md`.

---

## Estado actual

El nivel activo está definido en `CURRENT_LEVEL.md`.

El progreso y las evidencias se registran en `PROGRESS.md`.

---

## Estructura

```text
career-lab/
+-- app/             Proyecto práctico
+-- context/         Contexto personal reutilizable
+-- docs/            Conocimiento consolidado
+-- evals/           Evaluaciones y checkpoints
+-- prompts/         Prompts reutilizables
+-- scripts/         Automatizaciones
+-- specs/           Especificaciones de ejercicios/proyectos
+-- AGENTS.md        Reglas para agentes de IA
+-- CURRENT_LEVEL.md Nivel activo
+-- PROGRESS.md      Bitácora de aprendizaje
+-- README.md
```

---

## Flujo de trabajo

1. Leer `CURRENT_LEVEL.md`.
2. Identificar el microobjetivo activo.
3. Trabajar sobre el proyecto de `/app`.
4. Usar la IA como mentor, no como implementador.
5. Investigar únicamente los conceptos necesarios para resolver la duda actual.
6. Generar una evidencia de aprendizaje.
7. Registrar el progreso relevante en `PROGRESS.md`.
8. Continuar con el siguiente microobjetivo.
9. Al terminar el subnivel, realizar el checkpoint correspondiente.
10. Diseñar el siguiente tramo únicamente después de revisar el anterior.

---

## Uso de recursos

Los recursos de aprendizaje se seleccionan en función de una necesidad concreta.

Prioridad recomendada:

1. documentación oficial;
2. documentación técnica primaria;
3. laboratorios o ejercicios pequeños;
4. capítulos concretos de libros;
5. artículos técnicos;
6. vídeos, podcasts o divulgación complementaria.

No se busca acumular recursos.

Como norma general, cada microobjetivo debería tener:

- 1 recurso principal;
- 1 recurso opcional.

Si el recurso no ayuda a responder una pregunta del nivel actual, probablemente no sea necesario todavía.

---

## Principios de alcance

Para evitar parálisis por análisis:

- no se diseña el roadmap completo a varios años;
- no se estudian tecnologías sin una necesidad concreta;
- no se añaden objetivos futuros al nivel actual;
- no se amplía el proyecto innecesariamente;
- no se confunde complejidad técnica con progreso.

El siguiente escalón debe ser siempre suficientemente pequeño como para poder trabajarlo y evaluarlo.

---

## Criterio de progreso

Cada microobjetivo sigue tres dimensiones:

### Entender

Puedo explicar qué ocurre y por qué.

### Aplicar

Puedo utilizar el concepto de forma independiente.

### Diagnosticar

Puedo investigar qué ocurre cuando algo no funciona como esperaba.

Un objetivo no se considera completado simplemente por haber consumido contenido formativo.

---

## Rol del proyecto práctico

El proyecto de `/app` actúa como laboratorio.

Su función no es convertirse en un producto grande o comercial.

Debe permanecer lo suficientemente pequeño como para permitir experimentar con:

- comportamiento de una aplicación;
- ejecución;
- configuración;
- persistencia;
- integración;
- observabilidad;
- errores;
- despliegue;
- decisiones de diseño.

Cada nueva funcionalidad debería existir porque permite estudiar un concepto, no porque haga el proyecto más impresionante.

---

## Evolución del entorno

Career Lab también puede evolucionar progresivamente como entorno de trabajo AI-first.

En el futuro podrá incorporar, si existe una necesidad real:

- contexto estructurado;
- prompts versionados;
- especificaciones;
- evaluaciones;
- automatizaciones;
- herramientas para agentes;
- trazabilidad;
- validaciones;
- flujos de trabajo asistidos por IA.

Estas capacidades no forman parte del objetivo actual.

Se introducirán únicamente cuando aporten valor al proceso de aprendizaje.

---

## Principio principal

> No intentar aprender todo lo necesario para llegar al objetivo final.
>
> Aprender únicamente lo necesario para subir el siguiente escalón.
