class Cola_doble(object):

    def __init__(self,datos = None,long = 1):
        self.__data = [None for i in range(long + 2)]
        self.__data[long + 1] = 0
        self.__data[long] = 0
        if datos == None:
            return
        elif len(data) > long:
            return(False)
        else:
            for index in range(len(datos)):
                self.__data[index] = datos[index]
                self.__data[long + 1] += 1
        
    def isEmpty(self):
        long = len(self.__data[:-2])
        if self.__data[long + 1] == 0:
            return(True)
        return(False)

    def isFull(self):
        long = len(self.__data[:-2])
        if self.__data[long + 1] == long:
            return(True)
        return(False)

    def right_enqueue(self,value):
        long = len(self.__data[:-2])
        if not self.isFull():
            first = self.__data[long]
            elements = self.__data[long + 1]
            pos = ((first + elements) % long)
            self.__data[pos] = value
            self.__data[long + 1] += 1
        return(False)

    def left_enqueue(self,value):
        long = len(self.__data[:-2])
        if not self.isFull():
            first = self.__data[long]
            pos = ((first - 1) % long)
            self.__data[pos] = value
            self.__data[long + 1] += 1
            self.__data[long] = (first - 1) % long
        return(False)
    
    def left_dequeue(self):
        long = len(self.__data[:-2])
        self.__data[long + 1]
        if not self.isEmpty():
            first = self.__data[long]
            value = self.__data[first]
            self.__data[first] = None
            self.__data[long + 1] -= 1
            first = (first + 1) % long
            self.__data[long] = first
            return(value)
        return(False)

    def right_dequeue(self):
        if not self.isEmpty():
            long = len(self.__data[:-2])
            first = self.__data[long]
            elements = self.__data[long + 1]
            pos = ((first + elements - 1) % long)
            value = self.__data[pos]
            self.__data[long + 1] -= 1
            self.__data[pos] = None
            return(value)
        return(False)
    
    def __len__(self):
        long = len(self.__data[:-2])
        return(self.__data[long + 1])

    def __str__(self):
        long = len(self.__data[:-2])
        elements = self.__data[long + 1]
        first = self.__data[long]
        if first + elements <= long:
            pos = first + elements
            text = str(self.__data[first:pos])
        else:
            pos = (first + elements) % long
            text1 = str(self.__data[first:-2])
            text2 = str(self.__data[:pos])
            text = text1[:-1] + ", " + text2[1:]
        return(text)

a= Cola_doble(long = 20)

for i in range(20):
    a.left_enqueue(i)
    print(a)
for i in range(20):
    a.right_dequeue()
    print(a)
for i in range(20):
    a.right_enqueue(i)
    print(a)
for i in range(20):
    a.left_dequeue()
    print(a)
