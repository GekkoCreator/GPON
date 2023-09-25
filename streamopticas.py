# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:04:47 2023

@author: jfern
"""
import streamlit as st
import folium
from streamlit_folium import folium_static
from folium import plugins
import pandas as pd
from PIL import Image
import webbrowser




#----------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Red GPON: Características y Funcionamiento")


st.markdown("La Red GPON (Gigabit Passive Optical Network) es una tecnología de acceso de banda ancha que utiliza una infraestructura de fibra óptica para proporcionar servicios de alta velocidad a los usuarios finales. Esta tecnología ofrece numerosas ventajas y características que la hacen popular en redes de telecomunicaciones y acceso a internet.", unsafe_allow_html=True)

st.header("Características de la Red GPON")
st.markdown("""
- **Velocidades de hasta 2.5 Gbps**: GPON puede proporcionar velocidades de descarga de hasta 2.5 Gbps y velocidades de carga de hasta 1.25 Gbps.
- **Distancias de alcance**: Puede proporcionar servicios a distancias de hasta 20 kilómetros desde el equipo central hasta el usuario final.
- **Multiplexación por división de longitud de onda (WDM)**: GPON utiliza WDM para transmitir datos en diferentes longitudes de onda, lo que permite la multiplexación de datos.
- **División por tiempo**: Permite la multiplexación de múltiples usuarios en una sola fibra óptica utilizando divisiones de tiempo.
- **Fiabilidad y seguridad**: GPON es altamente confiable y seguro debido a la naturaleza de la fibra óptica y los protocolos de seguridad implementados.
""")

st.subheader("Topología Anillo")
texto_largo4 = """
Una red GPON (Gigabit Passive Optical Network) con topología de anillo es un tipo de arquitectura de red óptica que utiliza un diseño en forma de anillo para conectar múltiples ubicaciones o usuarios finales. Esta topología ofrece ciertas ventajas, como redundancia y confiabilidad, aunque también presenta desafíos específicos. 
Es importante destacar que la implementación exacta de una red GPON de anillo puede variar según los requisitos específicos de la red y las necesidades del proveedor de servicios. También es fundamental tener en cuenta factores como la planificación de la ruta de la fibra, la redundancia y la gestión de fallos para garantizar un rendimiento óptimo y la confiabilidad de la red.


La topología de anillo ha sido seleccionada como la arquitectura principal para la construcción de la red GPON (Gigabit Passive Optical Network). Esta elección se basa en sus ventajas clave, como la redundancia que garantiza una alta confiabilidad y la capacidad de mantener la conectividad en caso de fallas.
"""
st.markdown(texto_largo4)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#MAPA

def main():
    st.title("Puntos que conectara la Red")
    
    latitude1 = 7.137724039532561
    longitude1 = -73.12797716888309
    latitude2 = 7.065926713308867
    longitude2 = -73.09532957534736
    latitude3 = 7.023291075347385
    longitude3 = -73.05922810222823
    latitude4 = 7.008361499851373
    longitude4 = -73.05137483334907
    
    m = folium.Map(location=[latitude1, longitude1], zoom_start=12)
    
    locations = [
        [latitude1, longitude1],
        [latitude2, longitude2],
        [latitude3, longitude3],
        [latitude4, longitude4],
        [latitude1, longitude1]
    ]
    
    
    folium.PolyLine(locations=locations, color='blue').add_to(m)
    
    popup_text1 = "SEDE BUCARAMANGA  (ONT: Huawei HG8245Q2)(Splitter: Skylynn-SCFCSTMULC(1x8))"
    folium.Marker(location=[latitude1, longitude1], popup=popup_text1).add_to(m)
    popup_text2 = "SEDE FLORIDABLANCA  (OLT: Huawei MA5608T-24)(ONT: Huawei HG8245Q2)(Splitter: Skylynn-SCFCSTMULC(1x8))"
    folium.Marker(location=[latitude2, longitude2], popup=popup_text2).add_to(m)
    popup_text3 = "SEDE PIEDECUESTA  (ONT: Huawei HG8245Q2)(Splitter: Skylynn-SCFCSTMULC(1x8))"
    folium.Marker(location=[latitude3, longitude3], popup=popup_text3).add_to(m)
    popup_text4 = "SEDE LIMONAL  (ONT: Huawei HG8245Q2)(Splitter: Skylynn-SCFCSTMULC(1x8))"
    folium.Marker(location=[latitude4, longitude4], popup=popup_text4).add_to(m)
    


    folium_static(m)
if __name__ == "__main__":
    main()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

tab1, tab2, tab3 = st.tabs(["OLT (Huawei MA5608T-24)", "ONT(Huawei HG8245Q2)", "Splitter(Skylynn-SCFCSTMULC(1x8))"])

with tab1:
    
   st.header("Huawei MA5608T-24")
   

   imagen_url1 = "https://sc01.alicdn.com/kf/H7dcfbee642ae477da308158e4478831fu.png" 
   st.image(imagen_url1, caption=' Huawei MA5608T-24', use_column_width=True)
   st.write(" Este modelo ofrece una capacidad más limitada en comparación con las OLT de mayor tamaño, pero es adecuado para despliegues en redes más pequeñas o en lugares donde se requiere un menor número de conexiones.")
   st.subheader("Información sobre el MA5608T-24")
   texto_largo1 = """
   - **24 puertos:** Como su nombre indica, esta OLT tiene 24 puertos, lo que significa que puede servir hasta 24 clientes u ubicaciones finales en la red GPON.

   - **Capacidad de Escalabilidad:** Aunque tiene un número limitado de puertos, el MA5608T-24 es escalable y puede expandirse con el tiempo para agregar más puertos o capacidades a medida que crece la red.

   - **Interfaces de Conexión:** Proporciona interfaces para conexiones GPON y Ethernet para conectar clientes y otros dispositivos en la red.

   - **Gestión Avanzada:** Ofrece herramientas avanzadas de gestión y administración para facilitar la configuración, supervisión y mantenimiento de la red.

   - **Compatibilidad con Servicios de Banda Ancha:** Puede ofrecer servicios de banda ancha de alta velocidad, incluyendo Internet, voz y video a los clientes conectados.

   - **Alta Disponibilidad:** Está diseñado para proporcionar alta disponibilidad y confiabilidad en la red.


   """



   st.markdown(texto_largo1)
   def main():
       st.title("Datasheet y Caracteristicas")


       if st.button("Ir a la pagina"):
     
           url1 = "https://www.alibaba.com/product-detail/New-And-Original-Huawei-Smartax-Ma5608t_1600860738533.html?spm=a2700.7735675.0.0.387e5nSt5nStIt&s=p"
        
      
           webbrowser.open(url1)

   if __name__ == "__main__":
       main()

   
   

with tab2:
    
   st.header("Huawei HG8245Q2")
   imagen_url2 = "https://www.batna24.com/img2/1000/327329_3.webp?20989284173" 
   st.image(imagen_url2, caption='Huawei HG8245Q2', use_column_width=True)
   st.write("El Huawei HG8245Q2 es una unidad Optical Network Unit (ONU) que forma parte de la familia Huawei EchoLife. Es una ONU que se utiliza en redes de fibra óptica pasiva (GPON) para proporcionar conectividad de banda ancha y servicios de telecomunicaciones a usuarios residenciales y pequeñas empresas. ")
   st.subheader("Información sobre el Huawei HG8245Q2")
   texto_largo2 = """
   - **Conectividad de Fibra Óptica GPON:** El HG8245Q2 se conecta a la red de fibra óptica GPON, lo que permite a los usuarios acceder a servicios de alta velocidad, como Internet de banda ancha, telefonía IP (VoIP) y servicios de video.

   - **Puertos Ethernet:** Suele estar equipado con múltiples puertos Ethernet que permiten conectar dispositivos como computadoras, enrutadores, teléfonos IP y otros dispositivos a través de cables Ethernet.

   - **Wi-Fi Integrado:** Muchos modelos del HG8245Q2 incluyen capacidades de Wi-Fi integrado, lo que permite a los usuarios conectarse de forma inalámbrica a la red.

   - **Compatibilidad con IPv6:** Es compatible con IPv6, lo que facilita la transición a la próxima generación de protocolo de Internet.

   - **QoS (Quality of Service):** Ofrece funciones de QoS para garantizar un rendimiento óptimo de los servicios, especialmente en aplicaciones sensibles a la latencia como VoIP y streaming de video.

   - **Administración Remota:** Puede ser gestionado y configurado de forma remota por parte del proveedor de servicios, lo que facilita las tareas de mantenimiento y solución de problemas.

   - **Diseño Compacto:** Tiene un diseño compacto y se puede instalar fácilmente en hogares y pequeñas oficinas.

   """
   
   st.markdown(texto_largo2)
   
   datasheet2 = 'https://www.batna24.com/es/p/huawei-hg8245q2-ont-rmmnl'
   
   st.subheader("Datasheet y Caracteristicas")
   
   if st.button('Ir a la Página 2'):
       
       st.markdown(f'[Huawei HG8245Q2]({datasheet2})')
   
   

with tab3:
    
   st.header("Skylynn-SCFCSTMULC(1x8)")
   imagen_url3 = "https://sc02.alicdn.com/kf/HTB16647iborBKNjSZFjq6A_SpXa1/232962086/HTB16647iborBKNjSZFjq6A_SpXa1.jpg" 
   st.image(imagen_url3, caption='Skylynn-SCFCSTMULC(1x8)', use_column_width=True)
   st.write(" Los divisores PLC (circuito plano de onda de luz) son divisores monomodo con una relación de división uniforme de una fibra de entrada a múltiples fibras de salida. ")
   st.subheader("Información sobre el Skylynn-SCFCSTMULC(1x8)")
   
   texto_largo3 = """
   - **Conectividad:** Cuenta con una entrada óptica (1 puerto de entrada) y ocho salidas ópticas (8 puertos de salida) para conectar a los clientes.

   - **Diseño Compacto:** Tiene un diseño compacto y es adecuado para su instalación en gabinetes de distribución de fibra óptica en edificios o centrales de acceso.

   - **Compatibilidad:** Este splitter es compatible con las normas GPON y se utiliza comúnmente en despliegues de redes de acceso de fibra óptica para proporcionar servicios de banda ancha a múltiples suscriptores.
   """
   
   st.markdown(texto_largo3)
   
   datasheet3 = 'https://www.alibaba.com/product-detail/Ftth-Gpon-1x2-1x8-1x4-1x16_62039925713.html?spm=a2700.7735675.0.0.6c18f4n1f4n1AL&s=p'
   
   st.subheader("Datasheet y Caracteristicas")
   
   if st.button('Ir a la Página 3'):
       
       st.markdown(f'[Skylynn-SCFCSTMULC(1x8)]({datasheet3})')
   
   
   
   



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Tabla de equipos necesarios 



# Crear un DataFrame de ejemplo con 7 columnas y 5 filas
data = pd.DataFrame({
    "Equipo": ["OLT", "ONT", "Splitter"],
    "Marca": ["Huawei", "Huawei", "Skylynn"],
    "Modelo": ["MA5608T-24", "HG8245Q2 ", "SCFCSTMULC(1x8)"],
    "Cantidad": ["1", "4", "4"],
    

    "Precio x Unid": ["US$ 1,098.00 ", "US$ 63,90", "US$ 2,50"]
})

# Título de la página
st.title("Tabla de Equipos necesarios")

# Crear una tabla en Streamlit para mostrar y editar los datos
table = st.table(data)
# Fin de la página

