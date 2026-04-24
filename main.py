import hashlib
import uvicorn
from datetime import datetime
from pathlib import Path
from lxml import etree
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# --- Configuración de Entorno ---
# Montamos la carpeta de estáticos para las fotos de las camisetas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Creamos la carpeta para las facturas si no existe
Path("facturas_generadas").mkdir(exist_ok=True)

# Base de datos simulada de la Selección
PRODUCTOS = {
    "1": {"nombre": "Camiseta Local 2026", "precio": 349900, "imagen": "local.png"},
    "2": {"nombre": "Camiseta Visitante", "precio": 349900, "imagen": "visitante.png"}
}

def generar_xml_dian(datos):
    """Genera el XML con estándar UBL 2.1 exigido por la DIAN."""
    NS_MAP = {
        None: "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2",
        "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
    }
    root = etree.Element("Invoice", nsmap=NS_MAP)
    
    # Nodo de Identificación de Factura
    cbc_id = etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}ID")
    cbc_id.text = datos['numero']
    
    # Nodo CUFE (Código Único de Factura Electrónica)
    cbc_uuid = etree.SubElement(root, "{urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2}UUID", schemeName="CUFE-SHA384")
    cbc_uuid.text = datos['cufe']
    
    # Guardado físico del XML
    xml_string = etree.tostring(root, pretty_print=True, encoding="UTF-8", xml_declaration=True)
    ruta_archivo = f"facturas_generadas/{datos['numero']}.xml"
    with open(ruta_archivo, "wb") as f:
        f.write(xml_string)
        
    return xml_string.decode("utf-8")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"productos": PRODUCTOS}
    )

@app.post("/comprar")
async def comprar(request: Request, producto_id: str = Form(...)):
    prod = PRODUCTOS[producto_id]
    num = f"FCF-{datetime.now().strftime('%H%M%S')}"
    
    # Cálculo de CUFE
    cadena_semilla = f"{num}{prod['precio']}COL2026"
    cufe = hashlib.sha384(cadena_semilla.encode()).hexdigest()
    
    xml_content = generar_xml_dian({"numero": num, "cufe": cufe, "precio": prod['precio']})
    
    # CORRECCIÓN AQUÍ: Usar argumentos nombrados
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "productos": PRODUCTOS,
            "resultado": {
                "num": num, 
                "cufe": cufe, 
                "xml": xml_content,
                "prod_nombre": prod['nombre']
            }
        }
    )

# --- BLOQUE DE EJECUCIÓN ---
if __name__ == "__main__":
    # Arranca el servidor en el puerto 8000 con recarga automática
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)