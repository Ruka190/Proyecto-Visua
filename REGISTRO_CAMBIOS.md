# Registro de Cambios — Proyecto Visua

Documento de control para llevar constancia de **todas** las acciones realizadas sobre el
proyecto (entorno, herramientas, código, repositorio). Cada sesión de trabajo añade una
entrada nueva aquí antes de hacer commit.

**Formato de entrada:** fecha (AAAA-MM-DD) · tipo (Entorno / Código / Repo / Configuración)
· descripción de lo hecho · resultado/estado.

---

## 2026-10-08

### Entorno — Descarga inicial del repositorio
- **Tipo:** Entorno / Repo
- **Acción:** Se descargó el repositorio `Ruka190/Proyecto-Visua` por primera vez.
  Como `gh` y `git` aún no estaban instalados, se descargó el ZIP de la rama `main`
  y se descomprimió en `Proyecto-Visua-main/`.
- **Resultado:** Contenido disponible localmente (proyecto Django: `manage.py`,
  `Beyond_Date/`, app `inicio/`).

### Entorno — Dependencias Python del proyecto
- **Tipo:** Entorno
- **Acción:** Creado entorno virtual en `../.venv` (fuera de la carpeta del repo, no
  se commitea). Instalado `requirements.txt`: Django 6.1.2, asgiref 3.12.1,
  sqlparse 0.6.0, tzdata 2026.5 (Python 3.13.2).
- **Resultado:** `manage.py migrate` aplicado sin errores (admin, auth, contenttypes,
  sessions) y `manage.py check` → 0 problemas.

### Entorno — Primer arranque del servidor
- **Tipo:** Entorno
- **Acción:** Ejecutado `manage.py runserver` en `Proyecto-Visua-main/`.
- **Resultado:** HTTP 200 en http://127.0.0.1:8000/. Servidor detenido luego para
  migrar a la carpeta clonada con Git.

### Entorno — Instalación de herramientas de desarrollo
- **Tipo:** Entorno
- **Acción:**
  - Instalado **Git 2.55.0.5** vía winget.
  - **Visual Studio Code** ya estaba instalado (versión portátil 1.113.0 en
    `Escritorio\VSCode-win32-x64-1.113.0`); se añadió su `bin/` al PATH del usuario
    para usar la CLI `code`.
  - Extensiones VS Code: `ms-python.python` (ya instalada),
    `batisteo.vscode-django` v1.15.0, `ms-python.black-formatter` v2026.6.0.
- **Resultado:** `git` y `code` disponibles desde la terminal.

### Configuración — Identidad y credenciales Git
- **Tipo:** Repo / Configuración
- **Acción:** Configuración global de Git:
  - `user.name = Ruka190`
  - `user.email = l.ellenat@udd.cl`
  - `credential.helper = manager` (Git Credential Manager → login con navegador)
  - `init.defaultBranch = main`
- **Resultado:** Commits firmados con la identidad correcta; autenticación de push
  lista (primera vez pedirá autorizar GitHub en el navegador).

### Repo — Reemplazo de carpeta ZIP por clone real
- **Tipo:** Repo
- **Acción:** Clonado `https://github.com/Ruka190/Proyecto-Visua.git` en
  `Proyecto-Visua/` (con historial completo) y eliminada la carpeta temporal
  `Proyecto-Visua-main/` (copia ZIP sin historial). Migraciones re-ejecutadas en la
  nueva carpeta.
- **Resultado:** `main` sincronizada con `origin/main` (HEAD `62d4e4d`),
  `manage.py check` → 0 problemas, servidor arrancado desde la nueva carpeta.

### Configuración — Archivos de soporte para VS Code y este registro
- **Tipo:** Configuración / Código
- **Acción:** Creados:
  - `.vscode/settings.json` — intérprete del venv y `DJANGO_SETTINGS_MODULE` para
    la extensión de Django.
  - `REGISTRO_CAMBIOS.md` — este documento.
- **Resultado:** VS Code abre el proyecto con el entorno correcto preseleccionado.

### Repo — Intento de push a `origin` (fallido) y cambio a repo provisional
- **Tipo:** Repo
- **Acción:**
  - Primer push a `origin` (`Ruka190/Proyecto-Visua`) → **error 403**: las credenciales
    guardadas en el equipo pertenecían a otra cuenta (`pepe2390`).
  - Se eliminó la credencial obsoleta de `github.com` y se repitió el push para
    autenticar con la cuenta **Ruka190** (login con navegador vía Git Credential Manager).
  - A petición del usuario, se creó el remote **`provisional`** apuntando a
    `https://github.com/Ruka190/blahblahblah.git` (repo nuevo, vacío) para trabajar
    sin arriesgar el repositorio original.
  - Primer push al repo provisional devolvió también 403 (credencial aún refrescándose);
    un reintento inmediato funcionó.
- **Resultado:** `main` publicada en el repo provisional
  (`provisional/main` → commit `6ab24aa` "Agrega registro de cambios y configuracion
  de VS Code"), tracking configurado con `-u provisional main`.
  **`origin` (Proyecto-Visua) NO recibió ningún push** — sigue intacto.

### Configuración — Estado actual de remotes
- **Tipo:** Repo / Configuración
- **Acción:** `git remote -v` queda así:
  - `origin` → `https://github.com/Ruka190/Proyecto-Visua.git` (repo original, solo lectura por ahora)
  - `provisional` → `https://github.com/Ruka190/blahblahblah.git` (destino de push actual)
- **Resultado:** Todo push se envía a `provisional` hasta que el usuario indique lo contrario.

---

## Pendiente / notas
- **Push a `origin` bloqueado (403):** el usuario Ruka190 no tiene permiso de escritura
  confirmado sobre `Proyecto-Visua` desde esta máquina. Verificar: (1) que la cuenta
  Ruka190 sea dueña o collaboradora del repo original, (2) el token/permisos de la
  sesión de GitHub. Hasta entonces, todos los pushes van a `provisional`.
- El repo `blahblahblah` es **provisional**: cuando el problema de permisos con
  `origin` se resuelva, migrar (push a origin) y opcionalmente eliminar el remote.
- Próximas entradas: cada cambio de código, migración nueva, dependencia añadida
  o decisión de diseño se registra aquí antes del commit correspondiente.
