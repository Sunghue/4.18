class ArrayStack :
    def __init__( self, capacity ):	        # 생성자 정의
        self.capacity = capacity		    # 용량(고정)
        self.array = [None]*self.capacity	# 요소들을 저장할 배열
        self.top = -1			            # 스택 상단의 인덱스

    # 코드 1.2b: 스택 클래스의 연산들
    def isEmpty( self ) :
       return self.top == -1

    def isFull( self ) :
       return self.top == self.capacity-1

    def push( self, item ):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else: pass              # overflow 예외는 처리하지 않았음

    def pop( self ):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass              # underflow 예외는 처리하지 않았음

    def peek( self ):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass              # underflow 예외는 처리하지 않았음

    def __str__(self ) :
        return str(self.array[0:self.top+1][::-1])

    def size( self ) : return self.top+1

def checkBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch=='{' or ch=='[' or ch=='(' :
            stack.push(ch)
        elif ch=='}' or ch==']' or ch==')' :
            if stack.isEmpty() :
                print("조건 2 위반")
                print(ch)
                return False
            else :
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    print("조건 3 위반")
                    print(ch)
                    return False
    
    if stack.isEmpty()==False:
        print("조건 1 위반")
        print(stack)
    else:
        print(0)
    


filename = "괄호검사.py"
with open(filename , "r") as infile :
    str = infile.read()
    print("소스파일", filename, " ---> ", checkBrackets(str))


