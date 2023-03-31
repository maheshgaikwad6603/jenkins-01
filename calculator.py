

class DemoController:

    def addtion(self,num1,num2):
        if type(num1)==int and type(num2)==int:
            if num1<0 or num2>0:
                raise Exception("only postitive number required......")
            else:
                result = num2 + num1
                return result

        else:
            raise Exception("invalid param")

