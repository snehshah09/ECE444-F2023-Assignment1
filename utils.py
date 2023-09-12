class Utils:
    @staticmethod
    def reversed(number):
        reverse_num = 0
        negative_flag = False

        if number < 0:
            negative_flag = True
            number = abs(number)

        while number > 0:
            reverse_num = reverse_num * 10 + (number % 10)
            number = number // 10

        if negative_flag:
            reverse_num = -reverse_num

        return reverse_num

    @staticmethod
    def formatter(number):
        binary = bin(number)[2:] 
        octal = oct(number)[2:]   
        return {
            "binary": binary,
            "octal": octal
        }
