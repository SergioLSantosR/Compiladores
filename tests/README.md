# Casos de prueba

Ejecutar desde la raíz del repositorio:

```bash
python -m src.pipeline tests/test_valido.ml          # código 0
python -m src.pipeline tests/test_error_lexico.ml    # código 1
python -m src.pipeline tests/test_error_sintactico.ml
python -m src.pipeline tests/test_error_semantico.ml # código 2
```

O en PowerShell: `.\tests\run_tests.ps1`
