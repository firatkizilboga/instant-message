class Package:
    def __init__(self,name,request,text) -> None:
        self.name = name
        self.request = request
        self.text = text
        self.recievers = [name]
    def to_json(self):
        return "{"+ f"'name':'{self.name}','request':'{self.request}','text':'{self.text}'" +"}"
    def read_json(json):
        dict_form = eval(json)
        name = dict_form["name"]
        request = dict_form["request"]
        text = dict_form["text"]
        return Package(name,request,text)


class Client:
    def __init__(self) -> None:
        pass