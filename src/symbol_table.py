# src/symbol_table.py


class Simbolo:
    """Representa una variable registrada en la tabla de símbolos."""

    __slots__ = ("nombre", "tipo", "linea", "columna")

    def __init__(self, nombre: str, tipo: str, linea: int = 0, columna: int = 0):
        self.nombre = nombre
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def __repr__(self):
        return f"Simbolo({self.nombre!r}, {self.tipo!r}, L{self.linea}:C{self.columna})"


class SimboloFuncion:
    """Representa una función registrada en la tabla de símbolos."""

    __slots__ = ("nombre", "tipo_retorno", "parametros", "linea", "columna")

    def __init__(
        self,
        nombre: str,
        tipo_retorno: str,
        parametros: list[tuple[str, str]],
        linea: int = 0,
        columna: int = 0,
    ):
        self.nombre = nombre
        self.tipo_retorno = tipo_retorno
        self.parametros = parametros    # [(nombre, tipo), ...]
        self.linea = linea
        self.columna = columna

    def __repr__(self):
        return (
            f"SimboloFuncion({self.nombre!r}, ret={self.tipo_retorno!r}, "
            f"params={self.parametros!r}, L{self.linea}:C{self.columna})"
        )


class TablaSimbolos:
    """
    Tabla de símbolos basada en una Pila de Tablas Hash (Stack of Hash Tables).

    - Índice 0 de la pila es el ámbito global.
    - Cada entrar_ambito() agrega un nuevo dict al tope (ámbito local).
    - Cada salir_ambito() elimina el dict del tope.
    - Las funciones se registran siempre en el ámbito global (índice 0).
    """

    def __init__(self):
        self._ambitos: list[dict[str, Simbolo]] = [{}]   # ámbito global
        self._funciones: dict[str, SimboloFuncion] = {}

    # ------------------------------------------------------------------ #
    #  Manejo de ámbitos (scopes)
    # ------------------------------------------------------------------ #

    def entrar_ambito(self) -> None:
        """Crea un nuevo ámbito local (al entrar a función, ciclo o bloque)."""
        self._ambitos.append({})

    def salir_ambito(self) -> None:
        """Elimina el ámbito local del tope (al salir del bloque).
        Nunca elimina el ámbito global."""
        if len(self._ambitos) > 1:
            self._ambitos.pop()

    @property
    def profundidad(self) -> int:
        """Profundidad actual de la pila de ámbitos (1 = solo global)."""
        return len(self._ambitos)

    @property
    def ambito_actual(self) -> dict[str, Simbolo]:
        """Referencia al ámbito del tope de la pila."""
        return self._ambitos[-1]

    # ------------------------------------------------------------------ #
    #  Variables
    # ------------------------------------------------------------------ #

    def declarar(
        self, nombre: str, tipo: str, linea: int = 0, columna: int = 0
    ) -> Simbolo | None:
        """
        Declara una variable en el ámbito actual (tope de la pila).

        Retorna el Simbolo creado si la declaración fue exitosa.
        Retorna None si ya existe una variable con ese nombre en el
        **mismo** ámbito (redeclaración).
        """
        if nombre in self._ambitos[-1]:
            return None
        sim = Simbolo(nombre, tipo, linea, columna)
        self._ambitos[-1][nombre] = sim
        return sim

    def buscar(self, nombre: str) -> Simbolo | None:
        """
        Busca una variable desde el ámbito más interno hacia el global.
        Retorna el Simbolo si lo encuentra, o None si no existe en
        ningún ámbito (variable no declarada).
        Soporta shadowing: la primera coincidencia (tope → base) gana.
        """
        for ambito in reversed(self._ambitos):
            if nombre in ambito:
                return ambito[nombre]
        return None

    def buscar_ambito_actual(self, nombre: str) -> Simbolo | None:
        """Busca una variable solamente en el ámbito actual (tope)."""
        return self._ambitos[-1].get(nombre)

    # ------------------------------------------------------------------ #
    #  Funciones
    # ------------------------------------------------------------------ #

    def declarar_funcion(
        self,
        nombre: str,
        tipo_retorno: str,
        parametros: list[tuple[str, str]],
        linea: int = 0,
        columna: int = 0,
    ) -> SimboloFuncion | None:
        """
        Registra una función en el ámbito global.

        Retorna el SimboloFuncion creado, o None si ya existe una
        función con ese nombre (redeclaración de función).
        """
        if nombre in self._funciones:
            return None
        func = SimboloFuncion(nombre, tipo_retorno, parametros, linea, columna)
        self._funciones[nombre] = func
        return func

    def buscar_funcion(self, nombre: str) -> SimboloFuncion | None:
        """Busca una función por nombre. Retorna None si no existe."""
        return self._funciones.get(nombre)

    # ------------------------------------------------------------------ #
    #  Utilidades de depuración
    # ------------------------------------------------------------------ #

    def __repr__(self) -> str:
        lineas = [f"TablaSimbolos (profundidad={self.profundidad})"]
        for i, ambito in enumerate(self._ambitos):
            etiqueta = "GLOBAL" if i == 0 else f"LOCAL-{i}"
            lineas.append(f"  [{etiqueta}] {ambito}")
        if self._funciones:
            lineas.append(f"  [FUNCIONES] {self._funciones}")
        return "\n".join(lineas)
