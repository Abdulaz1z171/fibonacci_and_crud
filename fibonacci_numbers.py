#  Fibonacci sonlarini iterator orqali topish
class FibonacciSequence:
    
    def __init__(self,stop):
        self.prev = 0           # Fibonacci da gi 0-qiymati va oldingi son
        self.current = 1        # Fibonaccida hozirgi qiymat
        self.stop = stop        # Fibonaccida tuxtash nuqtasi yani stop = 6 da fibonaccining (f6) qiymatigacha boradi 
        self.count = 0          # siklni tuxtatish kerak buladi
    
    def __iter__(self):
        return self
    

    def __next__(self):
        if self.count < self.stop: 
            next_number = self.prev + self.current # Fibonaccida keyingi raqamni topishda oldingi va xozirgi raqamlar yigindisi orqali topiladi
            self.current = self.prev          # xar bitta next qiganimizda bizni xozirgi qiymatimiz oldingiga uzgarsin 
            self.prev = next_number           # oldingi qiymatimiz esa keyingi raqamga uzgaarsin
            self.count += 1                   # xar bir next qilganda count bitta ga oshsin va stopga tenglahsganda xatolik bersin
            return self.prev
        
        else:
            raise StopIteration
            
        
        
my_f = FibonacciSequence(7)
while True:    
    try:
        print(next(my_f))
    except StopIteration :
        break
    