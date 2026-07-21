import re
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove duplicate html2canvas
content = content.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>\n    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>', '<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>')

# 2. Set default view to profesores
content = content.replace("const vistaActual = ref('crear');", "const vistaActual = ref('profesores');")

# 3. Add Guide Bubble
guide_html = """
        <!-- Guía de uso rápida -->
        <div class="bg-blue-50 dark:bg-blue-900/30 border-l-4 border-[#B1CEFA] p-4 mb-6 rounded-r-lg shadow-sm">
            <h3 class="font-bold text-lg mb-2 text-[#000000] dark:text-white">Guía Rápida de Uso:</h3>
            <ol class="list-decimal list-inside space-y-1 text-sm text-gray-700 dark:text-gray-300">
                <li><span class="font-bold text-black dark:text-white">Profesores:</span> Registra a los docentes y ponles calificación.</li>
                <li><span class="font-bold text-black dark:text-white">Materias:</span> Crea tus materias asignando los profesores previamente registrados y definiendo sus horarios.</li>
                <li><span class="font-bold text-black dark:text-white">Resultados:</span> Presiona "Generar" (dentro de Materias) y aquí verás tus opciones viables de horarios sin empalmes.</li>
                <li><span class="font-bold text-black dark:text-white">Exportar:</span> Podrás descargar el horario en PNG o PDF desde la sección de Resultados.</li>
            </ol>
        </div>
"""
# Insert guide after <main class="...">
content = content.replace('<main class="max-w-6xl mx-auto p-6 mt-4 flex-grow w-full">', '<main class="max-w-6xl mx-auto p-6 mt-4 flex-grow w-full">\n' + guide_html)

# 4. Remove specific emojis
emojis_to_remove = ['🧑‍🏫', '📚', '🗓️', '📖', '☀️', '🌙', '⭐', '⚠️', '✅', '⚡', '🖼️', '📄', '👁️']
for emoji in emojis_to_remove:
    content = content.replace(emoji, '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modificaciones aplicadas.")
