class tnProduct:
    #Identificador de URL	Nombre	Categorías	Nombre de propiedad 1	Valor de propiedad 1	Nombre de propiedad 2	Valor de propiedad 2	Nombre de propiedad 3	Valor de propiedad 3
    # Precio	Precio promocional	Peso (kg)	Alto (cm)	Ancho (cm)	Profundidad (cm)	Stock	SKU	Código de barras	Mostrar en tienda	Envío sin cargo
    # Descripción	Tags	Título para SEO	Descripción para SEO	Marca	Producto Físico	MPN (Número de pieza del fabricante)	Sexo	Rango de edad

    __urlName = None
    __name = None
    __category = None
    __property1 = None
    __property1Value = None
    __property2 = None
    __property2Value = None
    __property3 = None
    __property3Value = None
    __price = None
    __pricePromo = None
    __weight = None
    __height = None
    __width = None
    __depth = None
    __stock = None
    __sku = None
    __barcode = None
    __showInShop = None
    __freeShipping = None
    __description = None
    __tags = None
    __seoTitle = None
    __seoDescription = None
    __brand = None
    __physical = None
    __mpn = None
    __sex = None
    __ageRange = None

    #'Identificador de URL', 'Nombre', 'Categorías', 'Precio', 'Precio promocional', 'Peso (kg)', 'Stock', 'SKU', 'Código de barras', 'Mostrar en tienda', 'Envío sin cargo', 'Descripción', 'Tags', 'Título para SEO', 'Descripción para SEO', 'Marca', 'Producto Físico', 'MPN (Número de pieza del fabricante)', 'Sexo', 'Rango de edad'
    def __init__(self, urlName, name, category, price, pricePromo, weight, height, width, depth, stock, sku, barcode, showInShop, freeShipping, description, tags, seoTitle, seoDescription, brand, physical, mpn, sex, ageRange):
        self.__urlName = urlName
        self.__name = name
        self.__category = category
        self.__property1 = ''
        self.__property1Value = ''
        self.__property2 = ''
        self.__property2Value = ''
        self.__property3 = ''
        self.__property3Value = ''
        self.__price = price
        self.__pricePromo = pricePromo
        self.__weight = weight
        self.__height = height
        self.__width = width
        self.__depth = depth
        self.__stock = stock
        self.__sku = sku
        self.__barcode = barcode
        self.__showInShop = showInShop
        self.__freeShipping = freeShipping
        self.__description =  description
        self.__tags = tags
        self.__seoTitle = seoTitle
        self.__seoDescription = seoDescription
        self.__brand = brand
        self.__physical = physical
        self.__mpn = mpn
        self.__sex = sex
        self.__ageRange = ageRange
    


    # Getters

    def getBarcode(self):
        return self.__barcode
    
    def getName(self):
        return self.__name
    
    def getStock(self):
        return self.__stock

    def setStock(self, newStock):
        self.__stock = newStock
    
    def setDescription(self):
        self.__description = """
            <p><span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">Somos MAXSER. Empresa Sanjuanina dedicada a la venta y reparaci&oacute;n de equipos inform&aacute;ticos, m&aacute;s de 15 a&ntilde;os nos avalan en nuestra trayectoria, contando con personal especializado en cada sector nos centramos en brindar siempre el MAXimo SERvicio a nuestros clientes.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- Contamos con amplia variedad de marcas y modelos.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- Realizamos env&iacute;o a todo el pa&iacute;s.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- Disponemos de factura A.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- Precios acorde a lo que necesites.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- La mejor atenci&oacute;n.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">- El mejor asesoramiento.</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">HORARIOS DE ATENCI&Oacute;N:</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">* LUNES A VIERNES DE 09 A 21HS</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">* S&Aacute;BADOS DE 10 A 14HS</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">******* B&uacute;scanos y conoce m&aacute;s de nosotros en nuestras redes. *******</span><br />
            <span style="color: rgb(102, 102, 102); font-family: &quot;Proxima Nova&quot;, -apple-system, &quot;Helvetica Neue&quot;, Helvetica, Roboto, Arial, sans-serif; font-size: 20px;">Consultar disponibilidad de stock, colores disponible y demas detalles por cada producto.</span></p>
        """

    def getPrice(self):
        return self.__price
    
    def setPrice(self, newPrice):
        self.__price = newPrice

    def setPromotionalPrice(self, newPrice):
        self.__promotionalPrice = newPrice
    
    def getData(self):
         return (
            self.__urlName,
            self.__name,
            self.__category,
            self.__property1,
            self.__property1Value,
            self.__property2,
            self.__property2Value,
            self.__property3,
            self.__property3Value,
            self.__price,
            self.__pricePromo,
            self.__weight,
            self.__height,
            self.__width,
            self.__depth,
            self.__stock,
            self.__sku,
            self.__barcode,
            self.__showInShop,
            self.__freeShipping,
            self.__description,
            self.__tags,
            self.__seoTitle,
            self.__seoDescription,
            self.__brand,
            self.__physical,
            self.__mpn,
            self.__sex,
            self.__ageRange
        )