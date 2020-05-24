import grpc

from proto import todo_pb2
from proto import todo_pb2_grpc

class Client:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = todo_pb2_grpc.TodoServiceStub(self.channel)

    def print_list(self):
        resp = self.stub.GetToDoList(todo_pb2.Empty())    
        for item in resp:
            if not item.is_done:
                print("{}, {} \n".format(item.id, item.text))
        self.print_completed_list()

    def print_completed_list(self):
        resp = self.stub.GetToDoList(todo_pb2.Empty())    
        first = True
        for item in resp:
            #print(item.is_done)
            #print(type(item.is_done)) 
            if item.is_done:
                if first:
                        print("------Completed-------")
                        first = False
                print("{}, {} \n".format(item.id, item.text))


    def add_todo(self):
        t = input("Enter todo : ")
        x = todo_pb2.Txt(text = t)  
        Client().stub.AddToDo(x)
        return 

    def done_todo(self):
        i = int(input("Enter the id of todo which u wanna mark as done : "))
        y = todo_pb2.Id(id = i)
        self.stub.DoneToDO(y)

    def delete_todo(self):
        i = int(input("Enter the id of todo which u wanna delete : "))
        y = todo_pb2.Id(id = i)
        self.stub.DeleteToDO(y)                         

# x = todo_pb2.Txt(text = "a")
# Client().stub.AddToDo(x)
# Client().stub.AddToDo(x)

# y = todo_pb2.Id(id = 2)
# response = Client().stub.DoneToDO(y)

# response = Client().stub.DeleteToDO(y)

# response = Client().stub.GetToDoList(todo_pb2.Empty())    

# for item in response:
#     print(item)

if __name__ == "__main__" :
    c = Client()
    while True:
        c.print_list()
        choice = int(input("Available options : 1, Add 2, Done 3, Delete 4, End : "))

        if choice == 1:
            c.add_todo()

        if choice == 2:
            c.done_todo()

        if choice == 3:
            c.delete_todo()    

        if choice == 4:
            break    