import grpc
from concurrent import futures
import time

from proto import todo_pb2_grpc
from proto import todo_pb2

from proto.todo_pb2 import ToDo, List, Empty

class ToDoService(todo_pb2_grpc.TodoServiceServicer):
    def __init__(self):
        self.TODO_LIST = []
    
    def AddToDo(self, request, context):
        #print(request.text) 
        l = len(self.TODO_LIST)
        i = (self.TODO_LIST[l-1].id)+1 if l>0 else 1
        #print(l+1)
        t = ToDo(id = i, text = request.text, is_done = False )
        self.TODO_LIST.append(t)
        #print(self.TODO_LIST)
        return Empty()

    def DoneToDO(self, request, context):
        i = request.id
        for t in self.TODO_LIST:
            if t.id == i:
                t.is_done = True
        #self.TODO_LIST[i-1].is_done = True
        #print(self.TODO_LIST)
        return Empty()
 

    def DeleteToDO(self, request, context ):
        i = request.id
        for idx, t in enumerate(self.TODO_LIST):
            if t.id == i:
                req_idx = idx 
        req_idx += 1        
        self.TODO_LIST = self.TODO_LIST[:req_idx-1] + self.TODO_LIST[req_idx:]        
        #print(self.TODO_LIST)
        return Empty()

    def GetToDoList(self, request, context):
        for x in self.TODO_LIST:
            yield x
        

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

todo_pb2_grpc.add_TodoServiceServicer_to_server(ToDoService() , server)

print("Starting server. Listening to port 50051")
server.add_insecure_port('[::]:50051')
server.start()

try:
	while True:
		time.sleep(86400)
except KeyboardInterrupt:
	server.stop(0)		

