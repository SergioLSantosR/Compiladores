# Git — ramas por funcionalidad

## Convención

- `main`: integración estable.  
- `feature/<nombre>`: una funcionalidad o entrega (ej. `feature/pipeline-ast`, `feature/casos-prueba`).  
- **No modificar** la configuración de ramas `pipeline` ↔ `test` en remoto si el equipo ya la usa para CI.

## Flujo recomendado

```bash
git checkout main
git pull
git checkout -b feature/mi-cambio
# commits descriptivos en inglés o español, imperativo:
# feat: añadir SemanticVisitor con ámbitos
# fix: corregir mensaje de error léxico
git push -u origin feature/mi-cambio
# PR / merge a main
```

## Commits descriptivos (ejemplos)

- `feat(grammar): while, func y return`  
- `feat(pipeline): fases léxico a intérprete`  
- `test: casos válido, léxico, sintáctico y semántico`  
- `docs: informe pipeline y diagrama mermaid`
