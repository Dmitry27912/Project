class Handler:
    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if hasattr(self, '_next_handler'):
            return self._next_handler.handle(request)

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("Handler A handled request A")
            return True
        else:
            return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("Handler B handled request B")
            return True
        else:
            return super().handle(request)

