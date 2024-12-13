from flask import Flask, request

main= Flask(__name__)

@main.route('/')
def home():
    return "Welcome to the Flask Calculator! Use /calculate?num1=value1&num2=value2&operation=add/subtract/multiply/divide."


@main.route('/calculate', methods =['GET'])
def calculate():
    # result= None
    # if request.method=='POST':
        
    num1 = request.args.get('num1', type=float)
    num2= request.args.get('num2',type=float)
    operation= request.args.get('operation', type= str)
    
    result= "N/A"
        
        
    if operation== 'add':
        result= num1+num2
    elif operation== 'subtract':
        result= num1-num2
    elif operation== 'multiply':
        result= num1*num2
    elif operation== 'divide':
        if num2!=0:
            result= num1/num2
        else:
            result="undefined"
        
    return f"result={result}"


if __name__=='__main__':
    main.run(debug=True)