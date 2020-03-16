class callcenteroperation:
    def __init__(self, responder , manager , director):
        self.call = None
        self.responder = responder
        self.manager  = manager
        self.director = director

    def dispatchcall(self ):
        if self.responder:
            print("Hello I handled it")
        elif self.manager:
            print("Manager handled it ")
        else:
            print("Director handled it")

if __name__ == '__main__':
    a = callcenteroperation(None, None, "yes")
    a.dispatchcall( )
