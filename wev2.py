from nicegui import ui
from datetime import datetime

# Configuración inicial
ui.colors(primary='#4F46E5')  # Color principal (índigo)
ui.query('body').classes('bg-gray-800 text-white')  # Fondo oscuro + texto blanco

# Header con logo y título
with ui.header().classes('bg-indigo-50 justify-between items-center'):
    with ui.row().classes('items-center gap-4'):
        ui.icon('person_add', size='lg', color='primary')
        ui.label('Registro de Usuarios').classes('text-2xl font-bold text-primary')
    ui.button('ℹ️ Info', on_click=lambda: ui.notify('App v1.0 - Creada con NiceGUI'))

# Formulario principal
with ui.card().classes('w-full max-w-md mx-auto my-8 p-6 shadow-lg rounded-lg'):
    # Sección 1: Datos personales
    ui.label('📝 Datos Personales').classes('text-xl font-semibold mb-4 text-primary')
    
    nombre = ui.input('Nombre completo', placeholder='Ej: Juan Pérez').classes('w-full mb-4')
    
    with ui.row().classes('w-full gap-4'):
        edad = ui.number('Edad', placeholder='18', min=12, max=120, format='%.0f').classes('flex-1')
        genero = ui.select(['Masculino', 'Femenino', 'Otro'], label='Género').classes('flex-1')
    
    # Sección 2: Contacto
    ui.label('📱 Contacto').classes('text-xl font-semibold mt-6 mb-4 text-primary')
    email = ui.input('Email', placeholder='tucorreo@ejemplo.com').classes('w-full mb-4')
    
    # Sección 3: Intereses (checkboxes)
    ui.label('🎯 Intereses').classes('text-xl font-semibold mt-6 mb-4 text-primary')
    intereses = ui.checkbox(['Tecnología', 'Deportes', 'Arte', 'Ciencia'], value=['Tecnología']).classes('w-full')

    # Botón de enviar con validación
    def enviar_formulario():
        if not nombre.value:
            ui.notify('⚠️ Falta el nombre', type='negative')
            return
        if not (12 <= int(edad.value if edad.value else 0) <= 120):
            ui.notify('⚠️ Edad debe ser entre 12 y 120', type='warning')
            return
            
        registro = {
            'nombre': nombre.value,
            'edad': int(edad.value),
            'genero': genero.value,
            'email': email.value,
            'intereses': intereses.value,
            'fecha': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
        
        resultado.set_text(f'''
        ✅ Registro exitoso!
        ──────────────────
        👤 Nombre: {registro['nombre']}
        🎂 Edad: {registro['edad']} años
        🚻 Género: {registro['genero']}
        📧 Email: {registro['email']}
        ❤️ Intereses: {', '.join(registro['intereses'])}
        📅 Fecha: {registro['fecha']}
        ''')
        ui.notify('📄 Formulario enviado correctamente!')

    ui.button('📤 Enviar Formulario', on_click=enviar_formulario).classes('w-full mt-6 h-12 bg-primary text-white hover:bg-indigo-700')

# Resultados (se muestra después de enviar)
resultado = ui.label().classes('w-full max-w-md mx-auto mt-4 p-4 bg-indigo-50 rounded-lg whitespace-pre-wrap')

# Footer
with ui.footer().classes('bg-gray-100 p-4 text-center text-gray-600'):
    ui.label('© 2023 Mi App - Todos los derechos reservados')

# Ejecutar la app
ui.run(title='App de Registro',port = 8081,  reload=True)