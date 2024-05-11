class zero:
    def __init__(self,secret,meeting,time):
        self.secret = secret
        self.meeting = meeting
        self.time = time

a,b,c = map(str,input().split())
zero1 = zero(a,b,c)
print(f"secret code : {zero1.secret}")
print(f"meeting point : {zero1.meeting}")
print(f"time : {zero1.time}")