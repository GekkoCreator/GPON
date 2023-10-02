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
st.title("Construcción de una red de fibra optica GPON")

st.title("------------------------------------------------")

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

imagen_url1 = "https://www.fibraopticahoy.com/blog/imagenes/2017/04/Anillo_MM.jpg" 
st.image(imagen_url1, caption=' Topología Anillo', use_column_width=True)

st.title("Limitaciones de la topología anillo")
 
texto_largo9 = """
   - **Escalabilidad Limitada:** En una topología de anillo, cada OLT (Terminal Óptico de Línea) debe estar conectada a la siguiente OLT en el anillo. Esto puede limitar la escalabilidad de la red, ya que agregar más OLTs implica una expansión compleja y costosa del anillo.

   - **Redundancia Limitada:** Aunque la topología de anillo puede ofrecer cierta redundancia, si una sección del anillo se daña o falla, toda la red puede quedar interrumpida hasta que se resuelva el problema.

   - **Mayor Latencia:** Las señales deben viajar por todo el anillo antes de llegar a su destino, lo que puede aumentar la latencia en comparación con otras topologías más directas, como la estrella.

  - **Costos de Implementación y Mantenimiento:** La construcción y el mantenimiento de una red de anillo GPON pueden ser más costosos y complejos debido a la necesidad de gestionar y mantener la topología en anillo, especialmente en términos de gestión de la señalización.
 """
st.markdown(texto_largo9)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#MAPA

def main():
    st.title("Puntos que conectará la Red")
    
    texto_largo8 = """
      Se crea un mapa interactivo utilizando la biblioteca Folium en una aplicación de Streamlit. El mapa muestra múltiples ubicaciones geográficas y utiliza marcadores de diferentes colores  que hacen referencia a la posicion como estan ubicados los equiposde la red GPON, las ubicaciones de cada universidad y círculos con radios específicos para resaltar áreas de cobertura. Además, agrega marcadores con descripciones emergentes (pop-ups) para cada equipo y sede.
    """
    st.markdown(texto_largo8)
    
    latitude1 = 7.136832447973945
    longitude1 = -73.12828388014697
    latitude2 = 7.065926713308867
    longitude2 = -73.09532957534736
    latitude3 = 7.023291075347385
    longitude3 = -73.05922810222823
    latitude4 = 7.008361499851373
    longitude4 = -73.05137483334907
    latitude5 = 7.065768178806944
    longitude5 = -73.09491425726685
    latitude6 = 7.136711647331867
    longitude6 = -73.12855171666415
    latitude7 = 7.136400608347979
    longitude7 = -73.12819220149491
    latitude8 = 7.1369307914687425
    longitude8 = -73.1286510221131
    latitude9 = 7.136366852691973
    longitude9 = -73.12830395129089
    latitude10 = 7.066081599455114
    longitude10 = -73.09550632569302
    latitude11 = 7.06516167069749
    longitude11= -73.095368697213
    latitude12= 7.065183871923638
    longitude12= -73.09529708831347
    latitude13 = 7.022437971271721
    longitude13 = -73.05915537159005
    latitude14= 7.022608537439764
    longitude14= -73.05937735149331
    latitude15= 7.022580109749435
    longitude15= -73.05944179727169
    latitude16 = 7.008055612412627
    longitude16 = -73.05148281866464
    latitude17 = 7.0077043037856575
    longitude17 = -73.05136645058937
    latitude18 = 7.007783709183413
    longitude18 = -73.0511822011369
    
    m = folium.Map(location=[latitude1, longitude1], zoom_start=12)
    
    locations = [
        [latitude1, longitude1],
        [latitude2, longitude2],
        [latitude3, longitude3],
        [latitude4, longitude4],
        [latitude1, longitude1]
    ]
    
    folium.PolyLine(locations=locations, color='blue').add_to(m)
    

    radius = 60
    folium.Circle(
        location=[latitude1, longitude1],
        radius=radius,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.2,
        popup="Área Cobertura 1"
    ).add_to(m)
    
    radius = 150  
    folium.Circle(
        location=[latitude5, longitude5],
        radius=radius,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.2,
        popup="Área Cobertura 2"
    ).add_to(m)
    
    radius = 100  # Radio en metros
    folium.Circle(
        location=[latitude3, longitude3],
        radius=radius,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.2,
        popup="Área Cobertura 3"
    ).add_to(m)
    
    radius = 80
    folium.Circle(
        location=[latitude4, longitude4],
        radius=radius,
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.2,
        popup="Área Cobertura 4"
    ).add_to(m)
    
    
    popup_text1 = "SEDE BUCARAMANGA"
    folium.Marker(location=[latitude1, longitude1], popup=popup_text1, icon = folium.Icon(color ='green')).add_to(m)
    popup_text2 = "SEDE FLORIDABLANCA"
    folium.Marker(location=[latitude2, longitude2], popup=popup_text2, icon = folium.Icon(color ='green')).add_to(m)
    popup_text3 = "SEDE PIEDECUESTA"
    folium.Marker(location=[latitude3, longitude3], popup=popup_text3, icon = folium.Icon(color ='green')).add_to(m)
    popup_text4 = "SEDE LIMONAL"
    folium.Marker(location=[latitude4, longitude4], popup=popup_text4, icon = folium.Icon(color ='green')).add_to(m)
    
    marker1 = folium.Marker(
        location=[latitude6, longitude6],  # Coordenadas del punto
        popup=folium.Popup("OLT (Huawei MA5608T-24)")  # Texto del pop-up
    ).add_to(m)
    
    marker2 = folium.Marker(
        location=[latitude7, longitude7],  # Coordenadas del punto
        popup=folium.Popup(" Pirmer Splitter(Skylynn-SCFCSTMULC(1x8)")  # Texto del pop-up
    ).add_to(m)
    
    marker3 = folium.Marker(
        location=[latitude8, longitude8],  # Coordenadas del punto
        popup=folium.Popup("Primer ONT(Huawei HG8245Q2)")  # Texto del pop-up
    ).add_to(m)
    
    marker4 = folium.Marker(
        location=[latitude9, longitude9],  # Coordenadas del punto
        popup=folium.Popup("Caja NAP / DAGA-NID-2000-E")  # Texto del pop-up
    ).add_to(m)
    
    marker5 = folium.Marker(
        location=[latitude10, longitude10],  # Coordenadas del punto
        popup=folium.Popup(" Segundo ONT(Huawei HG8245Q2)")  # Texto del pop-up
    ).add_to(m)
    
    marker5 = folium.Marker(
        location=[latitude11, longitude11],  # Coordenadas del punto
        popup=folium.Popup("Segunda Caja NAP / DAGA-NID-2000-E")  # Texto del pop-up
    ).add_to(m)
    
    marker6 = folium.Marker(
        location=[latitude12, longitude12],  # Coordenadas del punto
        popup=folium.Popup(" Segunda Splitter(Skylynn-SCFCSTMULC(1x8)")  # Texto del pop-up
    ).add_to(m)
    
    marker7 = folium.Marker(
        location=[latitude13, longitude13],  # Coordenadas del punto
        popup=folium.Popup(" Tercera ONT(Huawei HG8245Q2)")  # Texto del pop-up
    ).add_to(m)
    
    
    marker8 = folium.Marker(
        location=[latitude14, longitude14],  # Coordenadas del punto
        popup=folium.Popup(" Tercer Caja NAP / DAGA-NID-2000-E")  # Texto del pop-up
    ).add_to(m)
    
    marker9 = folium.Marker(
        location=[latitude15, longitude15],  # Coordenadas del punto
        popup=folium.Popup(" Tercer Splitter(Skylynn-SCFCSTMULC(1x8)")  # Texto del pop-up
    ).add_to(m)
    
    marker10 = folium.Marker(
        location=[latitude16, longitude16],  # Coordenadas del punto
        popup=folium.Popup(" Cuarta ONT(Huawei HG8245Q2)")  # Texto del pop-up
    ).add_to(m)
    
    marker11 = folium.Marker(
        location=[latitude17, longitude17],  # Coordenadas del punto
        popup=folium.Popup(" Cuarta Caja NAP / DAGA-NID-2000-E")  # Texto del pop-up
    ).add_to(m)
    
    marker12 = folium.Marker(
        location=[latitude18, longitude18],  # Coordenadas del punto
        popup=folium.Popup(" Cuarta Splitter(Skylynn-SCFCSTMULC(1x8)")  # Texto del pop-up
    ).add_to(m)
    
    
    
    folium_static(m)
    
     
 

if __name__ == "__main__":
    main()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(["OLT (Huawei MA5608T-24)", "ONT(Huawei HG8245Q2)", "Splitter(Skylynn-SCFCSTMULC(1x8))", "Caja NAP / DAGA-NID-2000-E"])

with tab1:
    
   st.header("Huawei MA5608T-24")
   

   imagen_url1 = "https://sc01.alicdn.com/kf/H7dcfbee642ae477da308158e4478831fu.png" 
   st.image(imagen_url1, caption=' Huawei MA5608T-24', use_column_width=True)
   st.write(" Este modelo ofrece una capacidad más limitada en comparación con las OLT de mayor tamaño, pero es adecuado para despliegues en redes más pequeñas o en lugares donde se requiere un menor número de conexiones.")
   st.subheader("Información sobre el MA5608T-24 (CARACTERISTICAS)")
   texto_largo1 = """
   - **24 puertos:** Como su nombre indica, esta OLT tiene 24 puertos, lo que significa que puede servir hasta 24 clientes u ubicaciones finales en la red GPON.

   - **Capacidad de Escalabilidad:** Aunque tiene un número limitado de puertos, el MA5608T-24 es escalable y puede expandirse con el tiempo para agregar más puertos o capacidades a medida que crece la red.

   - **Interfaces de Conexión:** Proporciona interfaces para conexiones GPON y Ethernet para conectar clientes y otros dispositivos en la red.

   - **Gestión Avanzada:** Ofrece herramientas avanzadas de gestión y administración para facilitar la configuración, supervisión y mantenimiento de la red.

   - **Compatibilidad con Servicios de Banda Ancha:** Puede ofrecer servicios de banda ancha de alta velocidad, incluyendo Internet, voz y video a los clientes conectados.

   - **Alta Disponibilidad:** Está diseñado para proporcionar alta disponibilidad y confiabilidad en la red.


   """



   st.markdown(texto_largo1)
   datasheet1 = 'https://www.alibaba.com/product-detail/New-And-Original-Huawei-Smartax-Ma5608t_1600860738533.html?spm=a2700.7735675.0.0.387e5nSt5nStIt&s=p'
   
   st.subheader("Datasheet y Caracteristicas")
   
   if st.button('Ir a la Página 1'):
       
       st.markdown(f'[Huawei MA5608T-24]({datasheet1})')

   
   

with tab2:
    
   st.header("Huawei HG8245Q2")
   imagen_url2 = "https://www.batna24.com/img2/1000/327329_3.webp?20989284173" 
   st.image(imagen_url2, caption='Huawei HG8245Q2', use_column_width=True)
   st.write("El Huawei HG8245Q2 es una unidad Optical Network Unit (ONU) que forma parte de la familia Huawei EchoLife. Es una ONU que se utiliza en redes de fibra óptica pasiva (GPON) para proporcionar conectividad de banda ancha y servicios de telecomunicaciones a usuarios residenciales y pequeñas empresas. ")
   st.subheader("Información sobre el Huawei HG8245Q2 (CARACTERISTICAS)")
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
   st.subheader("Información sobre el Skylynn-SCFCSTMULC(1x8) (CARACTERISTICAS)")
   
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

with tab4:
    st.header("DAGA-NID-2000-E")
    imagen_url4 = "https://cdnx.jumpseller.com/e-daga/image/16712081/M-FNAP-A-BP-16T-SCAPC-HC.jpg?1651093191" 
    st.image(imagen_url4, caption='DAGA-NID-2000-E', use_column_width=True)
    st.write(" Una caja NAP es un dispositivo utilizado en redes de telecomunicaciones, especialmente en redes de acceso de fibra óptica, para proporcionar conectividad a los usuarios finales y gestionar la distribución de señales de datos, voz y video.")
    st.subheader("Información sobre DAGA-NID-2000-E (CARACTERISTICAS)")
    
    texto_largo4 = """
    - **Conexiones de Fibra Óptica:** Las cajas NAP suelen contar con múltiples puertos o conexiones para la entrada y salida de fibras ópticas. Estos puertos permiten la conexión de cables de fibra óptica desde la red de proveedores de servicios hasta la caja NAP y desde allí hacia los dispositivos finales, como ONTs (Optical Network Terminals).

    - **Distribución de Señal:** Las cajas NAP se utilizan para distribuir la señal óptica desde la red principal hacia los usuarios finales. Pueden contar con divisiones internas (splitters) que dividen la señal en múltiples canales para servir a varios usuarios.

    - **Protección:** Para garantizar la integridad de la red, las cajas NAP suelen estar diseñadas para resistir condiciones ambientales adversas, como la humedad y las temperaturas extremas. También pueden incluir mecanismos de seguridad para evitar el acceso no autorizado.
    """
    
    st.markdown(texto_largo4)
    
    datasheet4 = 'https://www.daga-store.com/caja-nap-poste-ip65-8-puertos-sc'
    
    st.subheader("Datasheet y Caracteristicas")
    
    if st.button('Ir a la Página 5'):
        
        st.markdown(f'[DAGA-NID-2000-E]({datasheet4})')
   
   
   
   



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Tabla de equipos necesarios 
st.title("Tabla de Equipos necesarios")
 
texto_largo9 = """
  En la siguiente tabla, se presentan los modelos, marcas, cantidades y precios de los equipos para la red de fibra óptica GPON. Es importante destacar que esta tabla se centra en proporcionar información esencial sobre los equipos y su costo total. Para obtener detalles más específicos y características técnicas de cada equipo, puedes consultar las visualizaciones correspondientes en las secciones individuales del contenedor
 """
st.markdown(texto_largo9)


# Crear un DataFrame de ejemplo con 7 columnas y 5 filas
data = pd.DataFrame({
    "Equipo": ["OLT", "ONT", "Splitter", "Caja Nap", "TOTAL"],
    "Marca": ["Huawei", "Huawei", "Skylynn", "DAGA", "-"],
    "Modelo": ["MA5608T-24", "HG8245Q2 ", "SCFCSTMULC(1x8)", "NID-2000-E","-"],
    "Cantidad": ["1", "4", "4", "4","13"],
    

    "Precio x Unid": ["US$ 1,098.00 ", "US$ 63,90", "US$ 2,50","US$ 31,88", "US$ 99,378"], 
    "Precio Total": ["US$ 1,098.00 ", "US$ 255,6", "US$ 10","US$ 127,52", "US$ 394.218"]
})

# Título de la página


# Crear una tabla en Streamlit para mostrar y editar los datos
table = st.table(data)
# Fin de la página

