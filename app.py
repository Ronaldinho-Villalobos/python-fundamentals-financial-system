# =====================================================
# PROYECTO PYTHON FUNDAMENTALS
# Sistema de Gestión Financiera Interactivo
# Autor: Ronaldinho Agricio Villalobos Torres
# =====================================================

import streamlit as st
import pandas as pd

# =====================================================
# CONFIGURACIÓN GENERAL
# =====================================================

st.set_page_config(
    page_title="Proyecto Python Fundamentals",
    page_icon="💻",
    layout="wide"
)

# =====================================================
# 🎨 Poniendo color oscuros
# =====================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #f1f5f9;
    font-family: 'Segoe UI', sans-serif;
}

h1 { color: #38bdf8; }
h2, h3 { color: #60a5fa; }

label, .stMarkdown, .stText {
    color: #e2e8f0 !important;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #0f172a);
}

section[data-testid="stSidebar"] * {
    color: #f1f5f9 !important;
}

.stButton > button {
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1rem;
    font-weight: 600;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1d4ed8, #2563eb);
    transform: scale(1.05);
}

.tarjeta {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📌 Navegación del Proyecto")

pagina = st.sidebar.selectbox(
    "Selecciona una sección",
    ["🏠 Inicio", "1️⃣ Ejercicio 1", "2️⃣ Ejercicio 2", "3️⃣ Ejercicio 3", "4️⃣ Ejercicio 4"]
)

# =====================================================
# 🏠 Pantalla principal
# =====================================================

if pagina == "🏠 Inicio":

    st.title("💻 Proyecto Python Fundamentals")
    st.markdown("---")

    st.image(
        "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c",
        use_container_width=True
    )

    st.markdown("## 📚 Módulos del Proyecto")

    st.markdown("""
    <div class="tarjeta">
    📘 <b>Variables y Condicionales</b><br>
    📘 <b>Listas y Diccionarios</b><br>
    📘 <b>Funciones y Programación Funcional</b><br>
    📘 <b>Programación Orientada a Objetos (POO)</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 👋 Bienvenido a la Aplicación")

    st.markdown("""
    Esta aplicación fue desarrollada por **Ronaldinho Agricio Villalobos Torres**.

    Curso: **Python Fundamentals – 2026**

    Proyecto enfocado en un **Sistema de Gestión Financiera Interactivo**, 
    donde se aplican conceptos fundamentales de Python.

    Herramientas utilizadas:
    - 🐍 Python
    - 🚀 Streamlit
    - 📊 Pandas

    ---
    """)

    st.markdown("## 📋 Lista de Ejercicios")

    st.markdown("""
    1️⃣ **Ejercicio 1:** Variables y Condicionales  
    2️⃣ **Ejercicio 2:** Listas y Diccionarios  
    3️⃣ **Ejercicio 3:** Programación Funcional (map y lambda)  
    4️⃣ **Ejercicio 4:** Programación Orientada a Objetos (POO)  
    """)

    st.success("Selecciona una opción en el menú lateral para explorar cada ejercicio.")

# =====================================================
# 📘 EJERCICIO 1
# =====================================================

elif pagina == "1️⃣ Ejercicio 1":

    st.header("📘 Evaluación de Presupuesto")

    presupuesto = st.number_input("💰 Presupuesto mensual (S/)", min_value=0.0)
    gasto = st.number_input("💸 Gasto mensual (S/)", min_value=0.0)

    if st.button("Evaluar presupuesto"):
        if gasto > presupuesto:
            st.error(f"❌ Excediste el presupuesto en S/{gasto - presupuesto:,.2f}")
        elif gasto == presupuesto:
            st.warning("⚠️ Estás en el límite del presupuesto.")
        else:
            st.success(f"✅ Ahorraste S/{presupuesto - gasto:,.2f}")

# =====================================================
# 📘 EJERCICIO 2
# =====================================================

elif pagina == "2️⃣ Ejercicio 2":

    st.header("📘 Registro de Actividades")

    if "lista_actividades" not in st.session_state:
        st.session_state.lista_actividades = []

    nombre = st.text_input("📌 Nombre actividad:")
    tipo = st.selectbox("Categoría:", ["💰 Ingreso", "💸 Gasto", "🏦 Ahorro", "📈 Inversión"])
    presupuesto = st.number_input("Presupuesto (S/)", min_value=0.0)
    gasto = st.number_input("Gasto Real (S/)", min_value=0.0)

    if st.button("➕ Agregar"):
        if nombre:
            st.session_state.lista_actividades.append({
                "nombre": nombre,
                "tipo": tipo,
                "presupuesto": presupuesto,
                "gasto": gasto
            })
            st.success("Actividad agregada correctamente")
            st.rerun()

    if st.session_state.lista_actividades:
        df = pd.DataFrame(st.session_state.lista_actividades)
        df["diferencia"] = df["presupuesto"] - df["gasto"]
        st.dataframe(df)

# =====================================================
# 📘 EJERCICIO 3
# =====================================================

elif pagina == "3️⃣ Ejercicio 3":

    st.header("📘 Programación Funcional")
    st.subheader("📊 Sistema de Retorno de Inversión")

    if 'registro_inversiones' not in st.session_state:
        st.session_state.registro_inversiones = []

    def calcular_retorno(monto, tasa, meses):
        return monto * tasa * meses

    nombre = st.text_input("Nombre de la inversión:")

    col1, col2, col3 = st.columns(3)

    with col1:
        monto = st.number_input("Monto invertido (S/):", min_value=0.0, value=10000.0)

    with col2:
        tasa = st.number_input("Tasa (%):", min_value=0.0, max_value=100.0, value=5.0) / 100

    with col3:
        meses = st.number_input("Meses:", min_value=1, max_value=60, value=12)

    if st.button("➕ Agregar inversión"):
        if nombre:
            st.session_state.registro_inversiones.append({
                "nombre": nombre,
                "monto": monto,
                "tasa": tasa,
                "meses": meses
            })
            st.success("Inversión agregada")
            st.rerun()

    if st.session_state.registro_inversiones:

        resultados = list(map(
            lambda inv: {
                "nombre": inv["nombre"],
                "monto": inv["monto"],
                "retorno": calcular_retorno(inv["monto"], inv["tasa"], inv["meses"])
            },
            st.session_state.registro_inversiones
        ))

        for r in resultados:
            st.write(f"**{r['nombre']}** → Inversión: S/{r['monto']:,.0f} | Retorno: S/{r['retorno']:,.0f}")

# =====================================================
# 📘 EJERCICIO 4
# =====================================================

elif pagina == "4️⃣ Ejercicio 4":

    st.header("📘 Programación Orientada a Objetos")

    class Actividad:

        def __init__(self, nombre, tipo, presupuesto, gasto):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto = gasto

        def esta_en_presupuesto(self):
            return self.gasto <= self.presupuesto

        def mostrar_info(self):
            diferencia = self.presupuesto - self.gasto
            estado = "✅ En presupuesto" if self.esta_en_presupuesto() else "❌ Fuera del presupuesto"
            return f"""
            ### {self.nombre}
            Tipo: {self.tipo}
            Presupuesto: S/{self.presupuesto:,.2f}
            Gasto: S/{self.gasto:,.2f}
            Diferencia: S/{diferencia:,.2f}
            {estado}
            """

    if 'objetos' not in st.session_state:
        st.session_state.objetos = []

    nombre = st.text_input("Nombre actividad:")
    tipo = st.selectbox("Tipo:", ["Ingreso", "Gasto", "Ahorro", "Inversión"])
    presupuesto = st.number_input("Presupuesto (S/)", 0.0)
    gasto = st.number_input("Gasto Real (S/)", 0.0)

    if st.button("Crear objeto"):
        if nombre:
            st.session_state.objetos.append(
                Actividad(nombre, tipo, presupuesto, gasto)
            )
            st.rerun()

    for i, obj in enumerate(st.session_state.objetos):
        st.markdown(obj.mostrar_info())
        if st.button("❌ Eliminar", key=f"del_{i}"):
            st.session_state.objetos.pop(i)
            st.rerun()
